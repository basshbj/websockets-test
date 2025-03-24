import websockets
import asyncio

# Create WebSocket Client
async def ws_client():
  print("[LOG] WebSocket Client Started")
  ws_backend_server_endpoint = "ws://127.0.0.1:8000/ws"

  # Connect to WebSocket server
  async with websockets.connect(ws_backend_server_endpoint) as ws_client:
    print("[LOG] Connected to WebSocket Server")
    
    try:
      while True:
        # Send value to server
        text = input("Enter a value: ")

        if text == "exit":
          await ws_client.close(1000, "Close connection")

        await ws_client.send(text)

        # Receive value from server
        new_text = await ws_client.recv()
        print(f"[LOG] WS Response: {new_text}")
    except websockets.exceptions.ConnectionClosedError:
      print("[ERROR] Connection Closed")


if __name__ == "__main__":
  asyncio.run(ws_client())