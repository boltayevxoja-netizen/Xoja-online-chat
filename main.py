import os
import json
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Internetda ishlashi uchun CORS sozlamasi
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

active_connections = {}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    active_connections[client_id] = websocket
    try:
        while True:
            data = await websocket.receive_text()
            message = json.dumps({"sender": client_id, "text": data})
            for connection in active_connections.values():
                await connection.send_text(message)
    except:
        del active_connections[client_id]

if __name__ == "__main__":
    # Render yoki boshqa hostinglar uchun portni aniqlash
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)