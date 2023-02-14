from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory = 'src')

@app.get('/', response_class = HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    number = 1
    while True:
        data = await websocket.receive_json()
        data['id'] = number
        number += 1
        await websocket.send_json(data)
