*Think about ordering food at a restaurant. You don’t go into the kitchen and cook the food yourself. Instead, you tell the waiter what you want. The waiter takes your order to the kitchen, the kitchen prepares the food, and the waiter brings it back to you. You don’t need to know how the food is cooked, you only need to know how to place the order and receive the result.*

*This is exactly how communication through a REST API works. The application is like the customer, the server is like the kitchen, and the REST API acts as the messenger between them. It takes requests from the application, delivers them to the server, and brings the response back.



# REST API

- REST API is the most commonly used type of API.
- It allows applications to communicate with servers over the internet.
- If you use apps or websites, you are already using REST APIs without knowing it. Let’s see how.

---

## What is a REST API?

REST stands for **Representational State Transfer**.

It is a standard way for applications to exchange data over the internet.

A REST API works like a **messenger between your application and the server**.

- Your application sends a request
- The API delivers the request to the server
- The server processes it
- The API sends the response back


---
<br>

REST APIs use **HTTP** to communicate between the client and the server.

## How REST Uses HTTP

In REST, communication is very simple and follows two ideas:

- The **URL tells *what* you are talking about**
- The **HTTP method tells *what you want to do***  

Think of it like giving instructions.

## URLs Point to Data

In REST APIs, the URL tells the server **which data you are talking about**.

Think of a URL as an address for data.

For example:
- `/users` refers to all users
- `/users/1` refers to one specific user
- `/products` refers to product data

So when a request is sent, the URL answers one simple question:

**“Which data does this request refer to?”**

<br>

## HTTP Methods in REST APIs

### 1. GET – Retrieve data

GET is used to **fetch data** from the server.

### Example: Fetching User Profile

When the app needs to display a user’s profile, it sends a GET request.

```python
import requests

response = requests.get("https://api.myapp.com/users/1")
```
This request asks the server to return details of the user with ID 1.
The server processes the request and returns user data.

### Example Response
```json
{
  "id": 1,
  "name": "Siddhi",
  "email": "siddhi@example.com"
}
```
The app reads this data and displays it to the user.

---

### 2. POST – Create data

POST is used to **send new data** to the server.

### Example: Creating a New User 

When a user signs up, the app sends user details to the server.
```python

data = {
  "name": "Siddhi",
  "email": "siddhi@example.com"
}

response = requests.post("https://api.myapp.com/users", json=data)
```

This request tells the server to create a new user.
The server creates a new user record.

### Example Response
```json
{
  "id": 2,
  "name": "Siddhi",
  "email": "siddhi@example.com"
}
```
The server assigns an ID and sends the created user data back.

---

### 3. PUT – Update data

PUT is used to **update existing data** on the server.

### Example: Updating User Details 

When a user edits their profile, the app updates existing data.
```python
updated_data = {
  "name": "Siddhi Gujarathi"
}

response = requests.put("https://api.myapp.com/users/1", json=updated_data)
```

This request tells the server to update details of the user with ID 1.

### Example Response
```json
{
  "id": 1,
  "name": "Siddhi Gujarathi",
  "email": "siddhi@example.com"
}
```
The server updates the stored data and returns the updated profile.

---

### 4. DELETE – Remove data

DELETE is used to **delete data** from the server.

### Example: Deleting a User

When a user deletes their account, the app sends a DELETE request.
```python
response = requests.delete("https://api.myapp.com/users/1")
```
This request tells the server to delete the user with ID 1.

### Example Response
```json
{
  "message": "User deleted successfully"
}
```
The server removes the user and confirms the action.

<br>

---


## REST API Response Format

After processing a request, the server sends back a response.

A response usually contains:
- a status code indicating success or failure
- data returned by the server

---

## JSON Response Format

Most REST APIs return data in **JSON (JavaScript Object Notation)** format.

Example:
```json
{
  "id": 1,
  "name": "Siddhi",
  "email": "siddhi@example.com"
}
```
This JSON object represents the user data returned by the API.

---

## Where REST APIs Are Commonly Used

REST APIs are widely used across many types of applications.

They are commonly used in:
- web applications
- mobile applications
- e-commerce platforms
- social media platforms
- public APIs such as weather, maps, and payments

REST APIs work well in situations where simplicity, scalability, and wide compatibility are important.

---

## Key Characteristics of REST APIs

REST APIs have a few key characteristics that make them simple and widely used.


### Stateless
- Each request sent to a REST API is independent.
- So if you send the same request twice, the server treats it as two separate requests.


### Scalable
- REST APIs are designed to handle growth.
- Because requests are independent, servers can handle many users at the same time


### Platform Independent
- REST APIs are not tied to any specific platform or language.
- The same REST API can be used by web applications, mobile apps, desktop apps and other services.


As long as the app can send HTTP requests, it can use a REST API.

<br>

---

## Limitations of REST APIs

While REST APIs are simple and widely used, they are not perfect for every situation.

### Overfetching and Underfetching
- receiving more data than needed (overfetching)
- making multiple requests to get all required data (underfetching)


### Multiple Requests for Related Data
For example:
- one request for user data
- another request for user posts
- another request for comments


### Not Strict Enough for Some Systems
Systems like:
- banking
- financial transactions
- government applications

often require stricter rules, guaranteed delivery, and stronger contracts.


### Performance Limitations in Large Systems

- For very large or real-time systems, REST may not be the fastest option.


---

## Summary

REST APIs make server communication easy and consistent.
They allow applications to request, send, and update data in a clear and organized way.
Because of this, REST APIs are used in most apps and websites today.
