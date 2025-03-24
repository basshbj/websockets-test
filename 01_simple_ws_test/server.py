import websockets
import asyncio

# Create WebSocket server
async def ws_server(websocket):
  print("[LOG] WebSocket Started")

  try:
    while True:
      # Receive value from client
      text = await websocket.recv()

      print(f"[LOG] Value from client: {text}")

      # Just convert the text to uppercase
      new_text = text.upper()

      await websocket.send(new_text)
  except websockets.exceptions.ConnectionClosedError as e1:
    print("[ERROR] Connection Closed")
  finally:
    await websocket.close()


async def main():
  async with websockets.serve(ws_server, "localhost", 8765):
    await asyncio.Future()  # run forever

if __name__ == "__main__":
  asyncio.run(main())
