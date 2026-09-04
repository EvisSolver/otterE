from users import *
from servers import *


class VlessSettings:
    def __init__(
            self, 
            address, port, 
            id, encryption = "none", flow = None
    ):
        user = VlessUser(
            id,
            encryption,
            flow
        )
        
        self.vnext = [
            VnextServer(
                address, port, [user]
            )
        ]

    def to_dict(self):
        return {
            "vnext": [s.to_dict() for s in self.vnext],
        }

class VmessSettings:
    def __init__(
            self,
            address, port,
            id, alter_id = 0,
            security = "auto"
    ):
        user = VmessUser(id, alter_id, security)
        self.vnext = [
            VnextServer(
                address, port,
                [user]
            )
        ]

    def to_dict(self):
        return {
            "vnext": [s.to_dict() for s in self.vnext]
        }

class ShadowsocksSettings:
    def __init__(
            self,
            address, port,
            method, password
    ):
        self.servers = [
            Shadowsocks_Server(
                address, port,
                method, password
            )
        ]

    def to_dict(self):
        return {
            "servers": [s.to_dict() for s in self.servers]
        }

class TrojanSettings:
    def __init__(
            self,
            address, port,
            password
    ):
        self.servers = [
            Trojan_Server(
                address, port,
                password
            )
        ]

    def to_dict(self):
        return {
            "servers": [s.to_dict() for s in self.servers]
        }