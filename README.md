OptiResearch Buddy: Chat with Your Research Papers
An interactive AI assistant for querying and synthesizing information from your optical reinforcement learning research papers. Upload PDFs, ask questions, and get intelligent answers grounded in your documents—all running locally on your machine.
Show Image
Show Image
What is This?
OptiResearch Buddy is a retrieval-augmented generation (RAG) application that lets you have conversations with your research papers. Instead of manually searching through dozens of PDFs, just ask questions in plain English and get answers backed by the actual content of your documents.
Perfect for researchers, PhD students, and anyone dealing with large amounts of technical literature who wants to:

Quickly find information across multiple papers
Prepare for qualifying exams or literature reviews
Synthesize insights from conference proceedings
Keep a searchable knowledge base of your field

Features

PDF Processing - Automatically extract and index text from research papers
Semantic Search - Find relevant information using meaning, not just keywords (powered by FAISS + HuggingFace embeddings)
Context-Aware Answers - Get responses from Google Gemini that cite your actual documents
Privacy First - Everything runs locally; your research stays on your machine
Clean Interface - Simple Streamlit web UI that anyone can use

Tech Stack

Frontend: Streamlit
LLM: Google Gemini 2.5
Vector Store: FAISS
Embeddings: HuggingFace Sentence Transformers
PDF Processing: PyPDF2
Framework: LangChain (v0.2+)

Installation
Prerequisites

Python 3.8 or higher
Google Gemini API key (get one here)

Setup

Clone the repository:

bashgit clone https://github.com/your-username/opti-research-buddy.git
cd opti-research-buddy

Create a virtual environment:

bashpython -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

Install dependencies:

bashpip install -r requirements.txt
Or install packages individually:
bashpip install streamlit PyPDF2 langchain langchain-community langchain-google-genai sentence-transformers python-dotenv faiss-cpu

Configure your API key:

Create a .env file in the project root:
GOOGLE_API_KEY=your_google_gemini_api_key_here
Usage
Start the application:
bashstreamlit run pdfresearch.py
Your browser should automatically open to http://localhost:8501. From there:

Upload PDFs - Drag and drop your research papers into the upload area
Wait for Processing - The app will extract text and build a searchable index
Ask Questions - Type your question in natural language
Get Answers - Receive contextual answers based on your documents

Example Questions

"What are the main approaches to optical hardware for reinforcement learning?"
"Does any paper mention real-time inference capabilities?"
"Compare the experimental setups used across these papers"
"What datasets were used in the studies?"

Use Cases

Literature Reviews - Quickly synthesize information from dozens of papers
Exam Prep - Quiz yourself on key concepts from your reading list
Research Groups - Create a shared knowledge base for your lab
Thesis Writing - Find supporting evidence and citations efficiently
Conference Deep Dives - Process entire proceedings and extract insights

Future Enhancements
Some ideas for extending this project:

Live Paper Fetching - Automatically pull the latest papers from arXiv or Google Scholar
Citation Tracking - Extract and display references from source documents
Multi-Format Support - Add support for DOCX, LaTeX, HTML, and plain text
Figure Analysis - Process images, graphs, and tables from papers
Source Highlighting - Show exact paragraphs where answers were found
Session History - Save your questions and answers across sessions
Topic Visualization - Generate embedding maps to visualize paper relationships

Known Limitations

Large PDFs (>100 pages) may take a while to process
Scanned PDFs without text layers won't work well
Quality depends on the clarity of the source documents
API rate limits apply (check Gemini documentation)

Resources

LangChain Documentation
Google Gemini API
HuggingFace Sentence Transformers
FAISS Documentation
Streamlit Docs

Contributing
Contributions are welcome! Whether it's bug fixes, new features, or documentation improvements, feel free to open an issue or submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Note: This tool is designed to help you work with your research papers more efficiently. Always verify important information against the original sources, and remember that AI-generated answers should be reviewed critically.
