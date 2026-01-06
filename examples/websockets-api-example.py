"""
WebSocket Example – Python

This file demonstrates a simple WebSocket server and client.

In this example:
- the server listens for incoming WebSocket connections
- the client connects to the server
- messages are exchanged in real time
"""

import asyncio          # Used to run asynchronous code
import websockets       # WebSocket library for Python


async def websocket_server(websocket):
    """
    This function handles a single WebSocket connection on the server side.
    It runs every time a client connects to the server.
    """

    # Wait for a message sent by the client
    message = await websocket.recv()
    print("Server received:", message)

    # Send a response back to the client over the same open connection
    await websocket.send("Hello from server")


async def start_server():
    """
    Starts the WebSocket server and keeps it running.
    """

    # Create a WebSocket server listening on localhost at port 8765
    async with websockets.serve(websocket_server, "localhost", 8765):
        # Prevent the server from exiting
        await asyncio.Future()


async def websocket_client():
    """
    WebSocket client that connects to the server and exchanges messages.
    """

    # Connect to the WebSocket server using the ws:// protocol
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Send a message to the server
        await websocket.send("Hello from client")

        # Wait for the server's response
        response = await websocket.recv()
        print("Client received:", response)


async def main():
    """
    Runs the WebSocket server and client together for demonstration purposes.
    """

    # Start the server as a background task
    server_task = asyncio.create_task(start_server())

    # Give the server time to start before the client connects
    await asyncio.sleep(1)

    # Run the client
    await websocket_client()

    # Stop the server after the demonstration
    server_task.cancel()


if __name__ == "__main__":
    # Entry point of the program
    asyncio.run(main())

