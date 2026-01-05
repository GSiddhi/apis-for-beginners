# REST API Example – User Profile Management

This example demonstrates how a real application uses **REST APIs**
to manage user profile data using ***Python***.

Imagine a simple application where users can:
- view their profile
- create an account
- update their information
- delete their account

Each of these actions is handled using a REST API.

---

## Example Overview

The application communicates with a server that stores user data.
The server exposes REST API endpoints for different actions.

The client (app or website) never directly accesses the database.
All communication happens through REST APIs.

---

## API Endpoints Used

For this scenario, assume the server provides the following endpoints:

- `GET /users/1` → fetch user details  
- `POST /users` → create a new user  
- `PUT /users/1` → update user details  
- `DELETE /users/1` → delete a user  

Each endpoint performs one clear action.

---

## Fetching User Profile (GET)

When the app needs to display a user’s profile, it sends a GET request.

```python
import requests

response = requests.get("https://api.myapp.com/users/1")
```

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


## Creating a New User (POST)

When a user signs up, the app sends user details to the server.

```python
data = {
  "name": "Siddhi",
  "email": "siddhi@example.com"
}

response = requests.post("https://api.myapp.com/users", json=data)
```
The server creates a new user record.

### Example Response
