import emoji


async def get_emoji(name: str, link: str, text: str) -> tuple[str, str, str]:
    emoji_list = emoji.emoji_list(text)

    if emoji_list:
        found_emoji = emoji_list[0]["emoji"]

        return found_emoji, name, link
    return "unknown symbol/emoji"