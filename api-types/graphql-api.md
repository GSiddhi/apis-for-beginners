*Think about choosing notification settings.*

*You decide whether you want email notifications, SMS alerts, or app notifications.*
*You don’t receive all notifications by default.*

*GraphQL works in a similar way.*
*The client selects exactly what information it wants to receive.*


# GraphQL API

- GraphQL API is a modern way of building APIs.
- It allows clients to request exactly the data they need.
- It was created to solve data-fetching problems in REST APIs.

---

## What is a GraphQL API?

GraphQL stands for **Graph Query Language**.

It is a query language for APIs and a runtime for executing those queries.

A GraphQL API allows the client to **decide what data it wants**, instead of the server deciding the response structure.

---

<br>

Unlike REST, GraphQL usually works with **a single endpoint**.

## How GraphQL Works

In GraphQL:
- the client sends a query describing the required data
- the server processes the query
- the server returns only the requested data

This makes communication efficient and flexible.

---

## Why GraphQL Was Needed

REST APIs often return fixed responses.

This can cause:
- receiving more data than needed
- making multiple requests to collect related data

GraphQL was designed to solve these problems by giving control to the client.

---

## GraphQL Query Structure

A GraphQL request is written as a **query** that specifies the exact fields required.

Example:
```graphql
{
  user {
    id
    name
    email
  }
}
```
This query asks only for the user’s id, name, and email — nothing extra.
