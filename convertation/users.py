class VlessUser:
    def __init__(self, id, encryption = "none", flow = None):
        self.id = id
        self.encryption = encryption
        self.flow = flow

    def to_dict(self):
        dic_t = {
            "id": self.id,
            "encryption": self.encryption
        }
        if self.flow:
            dic_t["flow"] = self.flow
        return dic_t


class VmessUser:
    def __init__(self, id, alter_id = 0, security = "auto"):
        self.id = id
        self.alter_id = alter_id
        self.security = security

    def to_dict(self):
        return {
            "id": self.id,
            "alter_Id": self.alter_id,
            "security": self.security
        }


