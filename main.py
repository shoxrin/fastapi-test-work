from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.websocket_route("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    number = 1
    while True:
        data = await websocket.receive_json()
        data['id'] = number
        number += 1
        print(data)
        await websocket.send_json(data)
