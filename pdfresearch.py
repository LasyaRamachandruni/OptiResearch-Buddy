import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Use v0.2+ import if needed
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


load_dotenv()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=25000, chunk_overlap=2500)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    You are an advanced research assistant specialized in reinforcement learning and optics.
    When answering, use the provided context from uploaded research papers. 
    If the answer is not present in the provided context, reply: "No answer in the available literature."
    For questions about latest updates, summarize and reference the document's source if possible.
    Always be precise and cite research where applicable.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.2)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    print(response)
    st.write("Research Assistant Reply:", response["output_text"])

def main():
    st.set_page_config("Optical RL Research Assistant")
    st.header("Optical Reinforcement Learning Research Assistant 🧠🔬")
    st.info("Upload cutting-edge RL papers (PDFs) and ask deep research questions.")

    user_question = st.text_input("Ask your research question about Optical RL:")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Research Data Upload:")
        pdf_docs = st.file_uploader("Upload PDF files (latest RL research or reviews)", accept_multiple_files=True)
        if st.button("Process Papers"):
            with st.spinner("Extracting and indexing research..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Research indexed successfully.")

if __name__ == "__main__":
    main()
