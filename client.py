import socket

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNCT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.sent("SENT" + FILE)
client.connect(ADDR)
client.close()

