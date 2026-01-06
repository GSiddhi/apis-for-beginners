*This file provides brief instructions on how to run the example files in this folder. Each section explains the basic steps required to  
execute a specific example.*


## GraphQL API Example

The GraphQL example shows how to send a query and receive structured
data from a GraphQL API.

### How to run

1. Install dependencies:
   pip install requests
2. Run the file:
   python graphql_api_example.py

---

## gRPC API Example

The gRPC example demonstrates how a client calls remote procedures
using generated stubs.

### How to run

This example requires:
- grpcio and grpcio-tools
- generated files from a .proto definition
- a running gRPC server

> This example is for learning structure and flow.

---

## REST API Example

The REST example shows how to create, fetch, update, and delete data
using HTTP requests in Python.

### How to run

1. Install dependencies:
   pip install requests
2. Run the file:
   python rest_api_example.py

---

## SOAP API Example

The SOAP example demonstrates how to send an XML-based SOAP request
from a Python client.

### How to run

1. Install dependencies:
   pip install requests
2. Run the file:
   python soap_api_example.py

> Note: Public SOAP demo services may be unavailable at times.

---

## Webhooks Example

The webhook example demonstrates how to receive data sent by an external
service using an HTTP POST request.

### How to run

1. Install dependencies:
   pip install flask

2. Run the webhook server:
   python webhook_example.py

3. In a separate terminal (Windows PowerShell), send a test webhook event:

   ```powershell
   Invoke-RestMethod -Uri http://127.0.0.1:5000/webhook `
     -Method POST `
     -ContentType "application/json" `
     -Body '{"event":"order_created","order_id":123}'

### What this command does

This command manually sends a webhook event to your local webhook server to verify that:

- the server is running  
- it can receive POST requests  
- it can read JSON data  
- it responds correctly  

In simple terms, you are pretending to be an external service and sending a webhook event to your application.

---

## WebRTC Example

The WebRTC example runs in a web browser, not from the terminal.

### How to run

1. Open the folder containing `webrtc_example.html` in VS Code  
2. Right-click the file and choose **Open with Live Server**  
   (or open the file directly in a browser)
3. Allow camera access when prompted

You should see your live camera feed in the browser.

---

## WebSocket Example

This example demonstrates real-time, two-way communication between
a WebSocket client and server using Python.

### How to run

1. Install dependencies:
   pip install websockets
2. Run the file:
   python websocket_example.py
