import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"

def embed_texts(texts, model="nomic-embed-text"):
    embeddings = []
    for t in texts:
        res = requests.post(
            OLLAMA_URL,
            json={"model": model, "prompt": t}
        )
        embeddings.append(res.json()["embedding"])
    return embeddings
