class Trojan_Server:
    def __init__(self, address, port, password):
        self.address = address
        self.port = port

        self.password = password

    def to_dict(self):
        return {
            "address": self.address,
            "port": self.port,
            
            "password": self.password
        }