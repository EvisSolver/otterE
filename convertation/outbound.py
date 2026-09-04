class Outbound:
    def __init__(
            self,
            protocol, settings,
            tag = "proxy", stream = None
    ):
        self.protocol = protocol
        self.settings = settings
        self.tag = tag

        self.stream = stream

    def to_dict(self):
        dic_t = {
            "protocol": self.protocol,
            "settings": self.settings.to_dict(),
            "tag": self.tag
        }
        if self.stream:
            dic_t["streamSettings"] = self.stream.to_dict()

        return dic_t