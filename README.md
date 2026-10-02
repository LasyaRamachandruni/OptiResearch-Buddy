# 🤖 OptiResearch Buddy: Your AI Research Assistant

*Because manually searching through 50 PDFs at midnight is nobody's idea of fun.*

OptiResearch Buddy is a retrieval-augmented generation (RAG) system that lets you chat with your optical reinforcement learning papers. Built with LangChain, FAISS, and Google Gemini, it's like having a research assistant who's actually read all your papers (and remembers everything).

## What Does It Do?

Upload your research PDFs, ask questions in plain English, and get intelligent answers backed by actual content from your documents. All processing happens locally—your research stays private, and you get semantic search that understands context, not just keywords.

**Perfect for:**
- PhD students drowning in literature reviews
- Researchers prepping for presentations
- Anyone who needs to synthesize information across multiple papers
- Lab groups building a shared knowledge base

## Architecture Overview

This is a classic RAG pipeline with some nice touches:

- **PDF Ingestion**: PyPDF2 extracts text from your research papers
- **Text Chunking**: Documents are split into semantically meaningful chunks
- **Embedding Generation**: HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`) convert text to dense vectors
- **Vector Storage**: FAISS indexes embeddings for blazing-fast similarity search
- **Retrieval**: Top-k most relevant chunks are pulled based on query similarity
- **Generation**: Google Gemini 2.5 synthesizes answers grounded in retrieved context
- **Interface**: Streamlit provides a clean, interactive web UI

## Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key ([grab one here](https://makersuite.google.com/app/apikey))
- ~500MB disk space for model downloads on first run

### Installation

Clone and set up the project:

```bash
git clone https://github.com/your-username/opti-research-buddy.git
cd opti-research-buddy

# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then copy `.env.example` to `.env` and add your key.

### Configuration

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_actual_api_key_here
```

Pro tip: Never commit this file! Add `.env` to your `.gitignore`.

### Launch 🚀

```bash
streamlit run pdfresearch.py
```

The app will open at `http://localhost:8501`. Upload some PDFs and start asking questions!

## How to Use

1. **Upload Papers**: Drag and drop your PDFs (the app handles multiple files at once)
2. **Wait for Magic**: Text extraction and embedding generation takes 10-30 seconds per paper
3. **Ask Away**: Type questions like you're talking to a colleague who's read everything
4. **Get Answers**: Receive contextual responses with relevant information synthesized from your docs

### Example Queries

Try these to see what it can do:

```
"What optimization algorithms are mentioned across these papers?"

"Compare the experimental setups used for optical neural networks"

"Which papers discuss hardware constraints for real-time inference?"

"Summarize the main findings about photonic computing efficiency"

"What datasets were used in the RL experiments?"
```

## Technical Deep Dive

### Embedding Model

We use `all-MiniLM-L6-v2` because it:
- Generates 384-dimensional embeddings (smaller = faster)
- Has been fine-tuned on 1B+ sentence pairs
- Balances quality and speed beautifully
- Works well for technical/scientific text

### Vector Search

FAISS (Facebook AI Similarity Search) handles nearest-neighbor lookups:
- Uses IndexFlatL2 for exact search (perfect for <100k vectors)
- Cosine similarity via L2 normalization
- Sub-millisecond query times on CPU

### Chunking Strategy

Text is split into 1000-character chunks with 200-character overlap to:
- Preserve semantic coherence
- Avoid cutting off mid-sentence
- Ensure context isn't lost at chunk boundaries

### LLM Configuration

Gemini 2.5 is configured with:
- Temperature: 0.3 (mostly deterministic, slight creativity)
- Top-p: 0.95 (nucleus sampling for quality)
- Max tokens: 1024 (enough for detailed answers)

## Troubleshooting

**"Module not found" errors**: Double-check your virtual environment is activated

**Slow first run**: Sentence transformers downloads models (~100MB) on first use—this is normal

**Empty answers**: Your PDFs might be scanned images without text layers. Try OCR preprocessing first

**API rate limits**: Gemini free tier has quotas. Check the [official docs](https://ai.google.dev/pricing) for current limits

**FAISS installation issues on Windows**: Use `faiss-cpu` not `faiss`. If still broken, try `conda install -c pytorch faiss-cpu`

## Performance Notes

**Expected throughput:**
- PDF processing: ~5-10 pages/second
- Embedding generation: ~50 chunks/second
- Query latency: 100-300ms (excluding LLM inference)
- LLM response time: 1-3 seconds for typical answers

**Scaling considerations:**
- Works well up to ~100 papers (10k chunks)
- Beyond that, consider switching to approximate search (IVF indexes)
- Memory usage: ~50MB per 1000 chunks

## Future Enhancements

Some ideas I'm excited about:

- **Automatic arXiv ingestion**: Fetch papers by DOI or search query
- **Citation extraction**: Parse and link references automatically
- **Multi-modal support**: Analyze figures, tables, and equations
- **Chunk attribution**: Show exact source paragraphs for each answer
- **Persistent storage**: SQLite backend for session history
- **Comparative analysis**: Side-by-side paper comparisons
- **Export functionality**: Generate markdown summaries or LaTeX citations

## Contributing

Found a bug? Have a feature idea? PRs and issues are welcome! 

Some areas that could use love:
- Better PDF parsing (especially for two-column layouts)
- Support for more LLM providers (Anthropic, OpenAI, local models)
- UI improvements and mobile responsiveness
- Batch processing for large document collections

## Resources & References

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [FAISS GitHub](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [RAG Paper (Lewis et al. 2020)](https://arxiv.org/abs/2005.11401)

## License

MIT License - use it, fork it, improve it!

---

**Disclaimer**: This tool helps you work faster, but always verify important information against original sources. AI can be confidently wrong sometimes—treat answers as a starting point for deeper investigation, not gospel truth.

**Built with ❤️ for researchers who have better things to do than manually grep through PDFs.**
