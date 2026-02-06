import requests

def call_llm(prompt, model="llama3.1:8b"):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    return res.json()["response"]

def call_instruction_llm(system, prompt, model="llama3.1:8b"):
    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "system": system,
            "prompt": prompt,
            "stream": False
        }
    )
    return res.json()["response"]