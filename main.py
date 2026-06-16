from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

# Bosh sahifaga kirganda index.html ni ko'rsatadi
@app.get("/")
async def read_index():
    return FileResponse("index.html")

if __name__ == "__main__":
    # Render uchun portni avtomatik aniqlash
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)