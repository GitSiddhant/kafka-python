import socket  # noqa: F401


def create_message(correlationId):
    
    return len("0").to_bytes(4, byteorder="big") + correlationId
def handle_client(client):
    s = client.recv(1024)
    correlationId = s[16:24]
    
    client.sendall(create_message(correlationId))
    client.close()
def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    print("Server is listening on port 9092")
    while True:
        client, addr = server.accept()
        handle_client(client)

    
    



if __name__ == "__main__":
    main()
