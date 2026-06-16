from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

@app.get("/")
async def get():
    return FileResponse("index.html")

# WebSocket qismi
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Xabarni barcha foydalanuvchilarga qaytarish
        await websocket.send_json({"text": data, "sender": client_id})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)