"""
GraphQL API Example – Python

This file shows a simple example of calling a GraphQL API from Python.

In this example:
- we send a GraphQL query to a public GraphQL API
- we ask for details of a single country using its country code
- we receive only the fields requested in the query
- we print the returned data

This demonstrates how GraphQL queries are sent and how responses are handled.
"""

import requests

# Single GraphQL endpoint
GRAPHQL_URL = "https://countries.trevorblades.com/"


def fetch_country(code):
    # Define the GraphQL query and the fields we want
    query = """
    query GetCountry($code: ID!) {
        country(code: $code) {
            name
            capital
            currency
        }
    }
    """

    # Variables passed to the query
    variables = {
        "code": code
    }

    # Send the GraphQL request
    response = requests.post(
        GRAPHQL_URL,
        json={
            "query": query,
            "variables": variables
        }
    )

    return response.json()


def main():
    # Fetch country details for India
    result = fetch_country("IN")

    # Access the data returned by the GraphQL API
    country = result["data"]["country"]

    print("Country Name:", country["name"])
    print("Capital:", country["capital"])
    print("Currency:", country["currency"])


if __name__ == "__main__":
    main()

