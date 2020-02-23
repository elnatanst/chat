import socket
import sys
import threading
import time


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target=self.send_msg)
        iThread.daemon = True
        iThread.start()
        while True:
            data = self.sock.recv(1024)
            if data:
                print(data.decode())

    def send_msg(self):
        while True:
            inpt = input() + ":" + str(time.ctime())
            self.sock.send(bytes(inpt, "utf-8"))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        client = Client(sys.argv[1])
