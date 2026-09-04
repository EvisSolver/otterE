class Shadowsocks_Server:
    def __init__(self, address, port, method, password):
        self.address = address
        self.port = port

        self.method = method
        self.password = password

    def to_dict(self):
        return {
            "address": self.address,
            "port": self.port,

            "method": self.method,
            "password": self.password
        }