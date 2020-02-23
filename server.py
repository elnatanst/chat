import socket
import threading


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.sock.bind(("", 10000))
        self.sock.listen(1)

    def register(self, conn, data):
        name, time = data.split(":", 2)[1:]
        for n, _ in enumerate(self.connections):
            if self.connections[n]["conn"] == conn:
                self.connections[n]["name"] = name
                self.connections[n]["time"] = time
            print(self.connections[n])
            logger.info(f"register {name} on {time}")
            conn.send(f"welcome {name}".encode())

    def get_connection_by_name(self, name):
        for c in self.connections:
            if c["name"] == name:
                return c["conn"]

    def get_name_by_connection(self, conn):
        for c in self.connections:
            if c["conn"] == conn:
                return c["name"]

    def send_message(self, conn, data):
        recipients, msg, time = data.split(":", 3)[1:]
        for rec in recipients.split(","):
            for c in self.connections:
                if c["name"] == rec:
                    c["conn"].send(f"[{self.get_name_by_connection(conn)}]:{msg}:[{time}]".encode())
                    logger.info(f"send message: [{self.get_name_by_connection(conn)}]:{msg}:[{time}]")

    def handler(self, c, a):
        while True:
            data = c.recv(1024).decode()
            print(data)
            if "register:" in data:
                self.register(c, data)
            if "send:" in data:
                self.send_message(c, data)

    def get_connections_list(self):
        conn_list = []
        for con in self.connections:
            conn_list.append(con["conn"])
        return conn_list

    def run(self):
        while True:
            logger.info('start server')
            c, a = self.sock.accept()
            c.settimeout(60)
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append({"name": "", "conn": c})
            logger.info(f'accept connection {c}')
            print(c)


if __name__ == "__main__":
    server = Server()
    import logging

    logger = logging.getLogger('chat_application')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('chat.log')
    fh.setLevel(logging.INFO)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('creating an instance of auxiliary_module.Auxiliary')
    server.run()
