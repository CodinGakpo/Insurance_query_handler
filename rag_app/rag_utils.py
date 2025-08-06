# # rag_app/rag_utils.py

# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # Load embedding model
# embedder = SentenceTransformer('all-MiniLM-L6-v2')

# # Sample corpus
# documents = [
#     "Django is a high-level Python Web framework.",
#     "RAG is a technique that combines retrieval and generation.",
#     "FAISS is a library for efficient similarity search."
# ]

# # Embed the corpus
# corpus_embeddings = embedder.encode(documents, convert_to_numpy=True)

# # Build FAISS index
# dimension = corpus_embeddings.shape[1]
# index = faiss.IndexFlatL2(dimension)
# index.add(corpus_embeddings)

# def retrieve(query, top_k=2):
#     query_embedding = embedder.encode([query], convert_to_numpy=True)
#     distances, indices = index.search(query_embedding, top_k)
#     results = [documents[i] for i in indices[0]]
#     return results
