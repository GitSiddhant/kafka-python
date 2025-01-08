import socket  # noqa: F401


def create_message(correlationId):
    idByte = correlationId.to_bytes(4, byteorder="big")
    return len(idByte).to_bytes(4, byteorder="big") + idByte

def handle_client(client):
    s = client.recv(1024)
    correlationId = int.from_bytes(s[8:12], byteorder="big")   
    client.sendall(create_message(correlationId))
    client.close()

def main():
    print("Logs from your program will appear here!")
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    print("Server is listening on port 9092")
    while True:
        client, addr = server.accept()
        handle_client(client)

    
    



if __name__ == "__main__":
    main()
