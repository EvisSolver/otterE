class RealitySettings:
    def __init__(
            self,
            fingerprint, public_key, server_name,
            short_id = "", spider_x = ""
    ):
        self.fingerprint = fingerprint

        self.public_key = public_key
        self.server_name = server_name

        self.short_id = short_id
        self.spider_x = spider_x

    def to_dict(self):
        dic_t = {
            "fingerprint": self.fingerprint,

            "publicKey": self.public_key,
            "serverName": self.server_name,
        }
        if self.short_id:
            dic_t["shortId"] = self.short_id
        if self.spider_x:
            dic_t["spiderX"] = self.spider_x

        return dic_t 
                

class StreamSettings:
    def __init__(self, network = "tcp", security = "", reality = None):
        self.network = network
        self.security = security

        self.reality_settings = reality

    def to_dict(self):
        dic_t = {
            "network": self.network,
            "security": self.security
        }
        if self.reality_settings:
            dic_t["realitySettings"] = self.reality_settings.to_dict()

        return dic_t