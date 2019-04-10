import socket
import time

host, port = "127.0.0.1", 25001

x = 0
y = 0
z = 0

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((host, port))

	while True:
		x += 0.01
		y += 0.01
		z += 0.01 
		data = "(" + str(x) + "," + str(y) + "," + str(z) + ")" 
		sock.sendall(data.encode("utf-8"))
		data = sock.recv(1024).decode("utf-8")
		print(data)
		time.sleep(0.01)

finally:
	sock.close