import faiss
import pickle
import numpy as np
from embedder import get_embedding

index = faiss.read_index('index/faiss.index')
with open('index/documents.pkl', 'rb') as f:
    documents = pickle.load(f)

def search(query, top_k = 3):
    query_embedding = get_embedding(query)
    query_embedding = np.array([query_embedding])

    distance, indices = index.search(query_embedding, top_k)

    results = []
    for i, idx in enumerate(indices[0]):
        results.append({'text' : documents[idx],
                        'distance' : distance[0][i]
                        })
        
    return results