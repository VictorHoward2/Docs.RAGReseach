import re


def chunk_text(text, chunk_size=300, overlap=0):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def chunk_by_heading(text):
    # Tách theo heading markdown ##
    parts = text.split('\n')

    chunks = []
    current_heading = None

    for part in parts:
        part = part.strip()
        if not part:
            continue

        if part.startswith("## "):
            current_heading = part
        else:
            if current_heading:
                chunks.append(current_heading + "\n" + part)
            else:
                chunks.append(part)

    return chunks
