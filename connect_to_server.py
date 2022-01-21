import socket
server_address = "192.168.100.8"
server_port = 44444
socket_para_conectar = server_address,server_port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(socket_para_conectar)
s.send("Hello".encode())

