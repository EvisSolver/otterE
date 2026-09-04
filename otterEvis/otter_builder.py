from convertation.outbound import Outbound
from convertation.stream import RealitySettings, StreamSettings
from otterEvis.converter import converter


def otter(json_dict):

    protocol, settings = converter(json_dict)
    stream = None

    stream_settings = json_dict.get("streamSettings", {})


    if stream_settings:
        reality = None
        reality_settings = stream_settings.get("realitySettings", {})

        if reality_settings:
            reality = RealitySettings(
                fingerprint = reality_settings.get("fingerprint", ""),
                public_key = reality_settings.get("publicKey", ""),

                server_name = reality_settings.get("serverName", ""),
                short_id = reality_settings.get("shortId", ""),
                spider_x = reality_settings.get("spiderX", "")
            )

        stream = StreamSettings(
            network = stream_settings.get("network", "tcp"),
            security = stream_settings.get("security", ""),
            reality = reality
        )

    return Outbound(protocol, settings, stream = stream)
