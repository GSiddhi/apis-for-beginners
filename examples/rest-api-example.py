"""
REST API Example – Python

This file demonstrates how a Python application interacts with a REST API.
It shows a complete flow of creating, fetching, updating, and deleting
a resource using HTTP requests.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def create_post():
    # POST returns JSON with a new id
    payload = {
        "title": "My first API post",
        "body": "Learning how to use REST APIs with Python",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    return response.json()["id"]


def get_post(post_id):
    # GET returns JSON data
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    return response.json()


def update_post(post_id):
    # PUT may not return a response body, so we use status code
    payload = {
        "title": "Updated API post title"
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    return response.status_code


def delete_post(post_id):
    # DELETE usually returns only a status code
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    return response.status_code


def main():
    post_id = create_post()
    print("Post created:", post_id)

    post = get_post(post_id)
    print("Fetched post:", post)

    update_status = update_post(post_id)
    print("Update status code:", update_status)

    delete_status = delete_post(post_id)
    print("Delete status code:", delete_status)


if __name__ == "__main__":
    main()
