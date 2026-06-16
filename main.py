from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

# CSS, JS, Rasmlar uchun papka (agar "static" papkang bo'lsa)
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("index.html")

# Chat xabarlari uchun misol (buni o'z mantig'ing bilan to'ldir)
@app.post("/send")
async def send_message(msg: str):
    return {"status": "success", "message": msg}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)