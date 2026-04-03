import faiss
import pickle
import pandas as pd
import numpy as np
from embedder import get_embedding 

df = pd.read_csv("data/documents.csv")
texts = df["text"].tolist()

embeddings = [get_embedding(text) for text in texts]
embeddings = np.array(embeddings)
dimension = embeddings.shape[1]

print(dimension)

index = faiss.IndexFlatL2(dimension)
index.add(embeddings) # type: ignore

faiss.write_index(index, 'index/faiss.index')
with open('index/documents.pkl', 'wb') as f:
    pickle.dump(texts, f)

print("Index built and saved successfully!")