import socket

class Newtwork:
    def __init__(self):
        self.clinet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.122.1"
        self.port = 2012
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def gotpos(self):
        return self.pos

    def connect(self):
        try:
            self.clinet.connect(self.addr)
            return self.clinet.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.clinet.send(str.encode(data))
            return self.clinet.recv(2048).decode()
        except socket .error as e:
            print(e)

n = Newtwork()

print(n.send("hello"))
print(n.send("working"))
