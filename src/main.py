import asyncio
from datetime import datetime
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: any, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def broadcast_time(self):
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await self.broadcast(f"Current time: {current_time}")
            await asyncio.sleep(1)

manager = ConnectionManager()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(manager.broadcast_time())

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try: 
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            for connection in manager.active_connections:
                if connection != websocket:
                    await manager.send_personal_message(f"Client #{client_id} says: {data}", connection)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} has left the chat")