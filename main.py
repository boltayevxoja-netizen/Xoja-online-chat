from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
messages = []

@app.get("/")
async def get_index():
    return FileResponse("index.html")

@app.post("/send")
async def send_msg(request: Request):
    data = await request.json()
    msg = data.get("text")
    if msg:
        messages.append(msg)
    return {"status": "ok"}

@app.get("/messages")
async def get_msgs():
    return {"messages": messages}