class VnextServer:
    """address(loc ip) + port + users[] - для vless и vmess"""
    def __init__(self, address, port, users):
        self.address = address
        self.port = port
        self.users = users

    def to_dict(self):
        return {
            "address": self.address,
            "port": self.port,
            "users": [user.to_dict() for user in self.users]
        }
