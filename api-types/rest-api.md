# REST API

- REST API is the most commonly used type of API.
- It allows applications to communicate with servers over the internet.
- If you use apps or websites, you are already using REST APIs without knowing it. Let’s see how.

---

## What is a REST API?

REST stands for **Representational State Transfer**.

It is a standard way for applications to exchange data.

A REST API works like a **messenger between your application and the server**.

- Your application sends a request
- The API delivers the request to the server
- The server processes it
- The API sends the response back

<br>

### A Real-Life Example

Think about ordering food at a restaurant.

You don’t go into the kitchen and cook the food yourself.
Instead:
- You tell the waiter what you want
- The waiter takes your order to the kitchen
- The kitchen prepares the food
- The waiter brings the food back to you

In this situation:
- You are the application
- The kitchen is the server
- The waiter is the REST API

You don’t need to know how the food is cooked.
You just need to know how to place an order and receive the result.

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

## HTTP Methods in REST APIs

### 1. GET – Retrieve data

GET is used to **fetch data** from the server.

Example:
 GET https://api.myapp.com/users/1

This request asks the server to return details of the user with ID 1.

<br>

### 2. POST – Create data

POST is used to **send new data** to the server.

Example:
POST https://api.myapp.com/users

This request tells the server to create a new user.

<br>

### 3. PUT – Update data

PUT is used to **update existing data** on the server.

Example:
PUT https://api.myapp.com/users/1

This request tells the server to update details of the user with ID 1.

<br>

### 4. DELETE – Remove data

DELETE is used to **delete data** from the server.

Example:
DELETE https://api.myapp.com/users/1

This request tells the server to delete the user with ID 1.

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

## Key Characteristics of REST APIs

- Stateless: each request is independent
- Scalable: handles large numbers of users
- Platform independent: works across web, mobile, and other systems

---

## One-Line Summary

**REST API uses HTTP methods and URLs to perform actions on resources and exchange data over the internet.**
