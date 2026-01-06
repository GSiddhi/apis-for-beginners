"""
gRPC API Example – Python

This file shows a basic example of how a Python client calls a gRPC service.

In this example:
- a gRPC channel is created to communicate with the server
- a client stub generated from a .proto file is used
- a request message is sent to the server
- a response message is received from the server
"""

import grpc

# These files are generated from a .proto file
# They contain message definitions and the client stub
import user_pb2
import user_pb2_grpc


def get_user(user_id):
    # Create a channel to the gRPC server
    # insecure_channel means the connection is not encrypted
    # This is commonly used for local development and learning
    channel = grpc.insecure_channel("localhost:50051")

    # Create a stub (client-side object)
    # The stub exposes remote gRPC methods as normal Python functions
    stub = user_pb2_grpc.UserServiceStub(channel)

    # Build the request message defined in the .proto file
    request = user_pb2.GetUserRequest(id=user_id)

    # Call the remote procedure as if it were a local method
    response = stub.GetUser(request)

    return response


def main():
    # Fetch user data from the gRPC service
    user = get_user(1)

    print("User ID:", user.id)
    print("Name:", user.name)
    print("Email:", user.email)


if __name__ == "__main__":
    main()

