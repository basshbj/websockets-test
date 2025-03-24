import websockets
import asyncio
from openai import AsyncAzureOpenAI

WS_API_ENDPOINT = "ws://localhost:8765"

# Create WebSocket Server
async def ws_backend_server(ws_backend):

  print("[WS_BACKEND][LOG] WebSocket Server Started")

  try:
    async with websockets.connect(WS_API_ENDPOINT) as ws_api:
      while True:
        # Receive value from client
        text = await ws_backend.recv()

        print(f"[WS_BACKEND][LOG] Client input: {text}")

        # Send to the API WebSocket Server  
        print("[WS_BACKEND][LOG] Connected to API WebSocket")
        await ws_api.send(text)

        ws_api_response = await ws_api.recv()
        print(f"[WS_BACKEND][LOG] API WS Response: {ws_api_response}")

        await ws_backend.send(ws_api_response)
  except websockets.exceptions.ConnectionClosedError as e1:
    print("[WS_BACKEND][ERROR] Connection Closed")
  finally:
    await ws_backend.close()


# Main Methood
async def main():
  async with websockets.serve(ws_backend_server, "localhost", 9999):
    await asyncio.Future()  # run forever

  
if __name__ == "__main__":
  asyncio.run(main())
