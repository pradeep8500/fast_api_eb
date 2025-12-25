"""
FastAPI application entry point.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello World"}
