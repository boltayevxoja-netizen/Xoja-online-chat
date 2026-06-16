from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

# Agar loyihangda css, js yoki rasmlar bo'lsa, 
# "static" nomli papka yaratib, quyidagini ochib qo'y:
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("index.html")

if __name__ == "__main__":
    # Render avtomatik port ajratadi, uni shu yerda qabul qilamiz
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)