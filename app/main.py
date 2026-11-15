#Adapted from warestack/cc  class-7/lab/app/main.py

from fastapi import FastAPI

app = FastAPI(title="FastAPI for Piazza Assignment")

@app.get("/health")
def health():
    return {"status": "ok"}