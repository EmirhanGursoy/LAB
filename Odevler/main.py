import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1002))
server.listen()

client_socket, client_address = server.accept()

file = open('yeni_bayrak.jpeg', "wb")
image_chunk = client_socket.recv(2048)

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)
    
file.close()
client_socket.close()