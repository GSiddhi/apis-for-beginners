*Think about watching live cricket scores or stock prices.*

*You don’t refresh the page every second to see updates. The score or price updates automatically as things change.*

*This is how WebSockets work.*
*They keep a connection open so the server can send updates instantly.*


# WebSockets API

- WebSockets enable real-time, two-way communication.
- They keep a persistent connection between client and server.
- They are commonly used in live and interactive applications.

---

## What is a WebSockets API?

WebSockets provide a way for a client and a server to **communicate continuously** over a single connection.

Unlike traditional HTTP requests, WebSockets:
- do not close the connection after a response
- allow both sides to send data at any time

This makes them ideal for real-time applications.

---

<br>

WebSockets start with an **HTTP handshake**.

## How WebSockets Work

1. The client sends an HTTP request asking to upgrade the connection.
2. The server agrees and upgrades the connection to WebSocket.
3. A persistent connection is established.
4. Data can now flow freely in both directions.

Once connected, there is no need to repeatedly send HTTP requests.

---

## WebSockets Communication Structure

WebSockets do not follow a request–response pattern.

After the connection is established:
- the client can send messages at any time
- the server can send messages at any time
- communication is continuous and bidirectional

Messages are exchanged as **frames** rather than traditional responses.

---

## Data Format in WebSockets

WebSockets can send:
- text data
- JSON data
- binary data

The format depends on how the application is designed.

Unlike REST APIs, there is no fixed response format.

---

## Where WebSockets APIs Are Commonly Used

WebSockets APIs are commonly used in:
- chat applications
- live notifications
- online multiplayer games
- real-time dashboards
- stock price updates

They are useful whenever instant updates are required.

---

## Key Characteristics of WebSockets APIs

WebSockets APIs have certain characteristics that make them suitable for real-time systems.

### Persistent Connection
- The connection stays open
- No need to reconnect for every message


### Two-Way Communication
- Both client and server can send data
- Messages are delivered instantly


### Low Latency
- No repeated request overhead
- Faster updates compared to polling


### Efficient for Real-Time Data
- Ideal for frequent updates
- Reduces unnecessary network traffic

---


## Limitations of WebSockets APIs

While WebSockets are powerful, they also have limitations.


### Connection Management
- Keeping many connections open can be resource-intensive.
- Servers must manage connections carefully.


### Scalability Challenges
- Handling large numbers of concurrent connections requires special infrastructure.


### Not Ideal for Simple Requests
- For simple request–response use cases, REST APIs are easier to implement.

---

## Summary

WebSockets provide a persistent, two-way communication channel between clients and servers.
They are ideal for real-time applications that require instant updates and continuous data exchange.

