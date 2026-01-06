"""
Webhook Example – Python

This file shows a simple webhook receiver built using Flask.

In this example:
- a web server listens for incoming webhook events
- the server receives data sent by an external service
- the webhook payload is read and processed

This demonstrates how webhooks work on the receiving side.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    # Webhook data sent by the external service
    payload = request.json

    print("Webhook received:")
    print(payload)

    # Always respond with a 200 status to acknowledge receipt
    return jsonify({"status": "received"}), 200


def main():
    # Run the webhook server locally
    # The server listens for POST requests on /webhook
    app.run(port=5000)


if __name__ == "__main__":
    main()

