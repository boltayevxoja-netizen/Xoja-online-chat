from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

# Xabarlarni xotirada saqlash uchun ro'yxat
messages = [] 

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/send")
async def send_message(msg: str):
    messages.append(msg)
    return {"status": "success", "message": msg}

@app.get("/get-messages")
async def get_messages():
    return {"messages": messages}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)