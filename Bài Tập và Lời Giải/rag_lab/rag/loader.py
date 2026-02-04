import os

def load_documents(folder_path):
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt") or file.endswith(".md"):
            with open(os.path.join(folder_path, file), encoding="utf-8") as f:
                docs.append({
                    "text": f.read(),
                    "source": file
                })
    return docs
