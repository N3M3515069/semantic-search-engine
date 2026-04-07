# Semantic Search Engine

A semantic search engine that finds relevant documents based on **meaning**, not just keywords.

## How it works
- Documents are converted into vector embeddings using a pre-trained Sentence Transformer model
- Embeddings are stored in a FAISS index for fast similarity search
- User queries are embedded and compared against stored documents using L2 distance
- Top matching documents are returned ranked by similarity

## Tech Stack
- Python
- Sentence Transformers (all-MiniLM-L6-v2)
- FAISS (Facebook AI Similarity Search)
- NumPy & Pandas
- Streamlit

## Project Structure
semantic-search-engine/
├── app.py          # Streamlit UI
├── embedder.py     # Text to embedding conversion
├── indexer.py      # Builds and saves FAISS index
├── search.py       # Search logic
├── data/
│   └── documents.csv
├── index/
│   ├── faiss.index
│   └── documents.pkl
└── requirements.txt

## Setup & Run
```bash
pip install -r requirements.txt
python indexer.py
streamlit run app.py
``` 
