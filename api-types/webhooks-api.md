*Think about getting a delivery notification.*

*You don’t keep opening the app again and again to check if your package has arrived. Instead, the app notifies you automatically when there is an update.*

*This is how Webhooks work.*
*They notify your application when something happens.*
*Let’s study **Webhooks API** in detail.*



# Webhooks API

- Webhooks are event-driven APIs.
- They automatically send data when an event occurs.
- They remove the need to repeatedly ask the server for updates.

---

## What are Webhooks?

Webhooks are a way for one system to **send real-time data to another system** when a specific event happens.

Instead of the client requesting data again and again, the server **pushes the data automatically**.

Webhooks are often called **“reverse APIs”** because the server initiates the communication.

---

<br>

Webhooks work using **HTTP POST requests**.

## How Webhooks Work

1. The client provides a callback URL.
2. An event occurs on the server.
3. The server sends an HTTP POST request to the callback URL.
4. The client receives and processes the data.

This happens automatically without polling.

---

## Example Webhook Payload

When an event occurs, the server sends data to the client using an HTTP POST request.

The data sent by a webhook is usually in **JSON format**.

Example payload:
```json
{
  "event": "order_created",
  "order_id": 1234,
  "amount": 2499,
  "status": "confirmed"
}
```

---

## Example Callback URL

A callback URL is usually a public endpoint on the client’s system.

Example:
https://myapp.com/webhooks/order-status


In this example:
- `myapp.com` is the client application
- `/webhooks/order-status` is the endpoint created to receive webhook events

When an event occurs, the server sends a POST request with event data to this URL.

---



## Where Webhooks APIs Are Commonly Used

Webhooks are commonly used in:
- payment systems
- e-commerce platforms
- CI/CD pipelines
- messaging and notification systems

Examples include:
- payment confirmation notifications
- order status updates
- code push events

---
## Key Characteristics of Webhooks APIs

Webhooks have certain characteristics that make them useful for real-time systems.

### Event-Driven
- Webhooks are triggered by events
- Data is sent only when something happens


### Real-Time Updates
- Information is delivered instantly
- No delays caused by repeated requests


### Efficient Communication
- Reduces unnecessary network calls
- Saves server and client resources


### One-Way Communication
- Data flows from server to client
- The client does not request the data

---

## Limitations of Webhooks APIs

While Webhooks are efficient, they also have limitations.

### Delivery Failures
- If the receiving server is down, the webhook may fail.
Retry mechanisms must be implemented.


### Security Concerns
-Webhook endpoints must be secured.
Otherwise, they can be exposed to unauthorized requests.

### No Response Control
- Webhooks are one-way.
- The sender does not wait for complex responses from the receiver.

---

## Summary

Webhooks allow servers to notify applications automatically when events occur.
They provide real-time updates without the need for repeated requests.
This makes Webhooks ideal for event-driven and notification-based systems.

