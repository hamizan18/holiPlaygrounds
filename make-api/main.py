import json
from pathlib import Path

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware, # Atur izin CORS pada aplikasi FastAPI
    allow_origins=["http://127.0.0.1:5500"], # Mengizinkan frontend dari origin yang ditentukan
    allow_credentials=False, # Tidak mengizinkan request lintas origin membawa kredensial pake mekanisme ini
    allow_methods=["GET"], # Mengizinkan metode GET untuk kebutuhan saat ini
    allow_headers=["*"], # Mengizinkan berbagai header request
)

# Lokasi file berdasarkan folder main.py
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"
HTML_FILE = BASE_DIR / "index.html"

@app.get("/")
def home():
    return FileResponse(HTML_FILE)

@app.get("/games")
def getGames():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        games = json.load(file)
    
    return games

