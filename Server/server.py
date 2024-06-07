import socket
from  threading import Thread
IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
BUFFER_SIZE = 4096
clients = {}
import os

def handleClient(client,client_name):
    global clients
    global BUFFER_SIZE
    global SERVER

    # Sending welcome message
    banner1 = "Welcome, You are now connected to Server!\nClick on Refresh to see all available users.\nSelect the user and click on Connect to start chatting."
    client.send(banner1.encode())

    while True:
        try:
            BUFFER_SIZE=clients[client_name]["file_size"]
            chunk=client.recv(BUFFER_SIZE)
            message=chunk.decode().strip().lower()
            
        except:
            pass


def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        clientName=client.recv(4096).decode().lower()
        clients[clientName]={
            "client":client,
            "address":addr,
            "connectedWith":"",
            "fileName":""
        }
        print(f"Connection established with {clientName}:{addr}" )
        thread=Thread(target=handleClient,args=(client,clientName))
        thread.start()

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER


    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup_thread = Thread(target=setup)           #receiving multiple messages
setup_thread.start()

