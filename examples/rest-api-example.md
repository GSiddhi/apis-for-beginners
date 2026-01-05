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

```json
{
  "id": 2,
  "name": "Siddhi",
  "email": "siddhi@example.com"
}
```
The server assigns an ID and sends the created user data back.

## Updating User Details (PUT)

When a user edits their profile, the app updates existing data.

```python
updated_data = {
  "name": "Siddhi Gujarathi"
}

response = requests.put("https://api.myapp.com/users/1", json=updated_data)
```
### Example Response
```json
{
  "id": 1,
  "name": "Siddhi Gujarathi",
  "email": "siddhi@example.com"
}
```
The server updates the stored data and returns the updated profile.

## Deleting a User (DELETE)

When a user deletes their account, the app sends a DELETE request.

```python
response = requests.delete("https://api.myapp.com/users/1")
```

### Example Response

```json
{
  "message": "User deleted successfully"
}
```
The server removes the user and confirms the action.
