import asyncio
import logging
import time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

logging.basicConfig(
  level=logging.INFO, 
  format="%(asctime)s - %(levelname)s - %(message)s"
)
#logger = logging.getLogger(__name__)
logger = logging.getLogger("uvicorn")

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()

  try:
    while True:
      data = await websocket.receive_text()
      logger.info(f"Received data: {data}")

      data_new = data.upper()

      time.sleep(2)
      logger.info("Awaited 2 seconds")
      logger.info(f"Data to be sent: {data_new}")

      await websocket.send_text(f"Transformed: {data_new}")
  except WebSocketDisconnect:
    print("Client disconnected")