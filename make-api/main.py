from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Halo dari Mijaenn!"}

@app.get("/raul")
def getRaul():
    return {
        "task": [
            {"id": 1, "name": "Belajar Python"},
            {"id": 2, "name": "Belajar dari rumah"},
        ]
    }