import emoji


async def get_emoji(name: str, link: str, text: str) -> tuple[str, str, str]:
    '''
        founding emoji in text: string
        if emoji_list = True(not empty) then we are creating found_emoji which = emoji_list
        we taking first element([0]) and taking ["emoji"] (the first emoji in list)

        Example:
            emoji_list = [
                {
                    "emoji": "🇫🇮"
                }
            ]
        so: found_emoji => emoji_list[0 list-index]["emoji" name of dict]
    '''

    emoji_list = emoji.emoji_list(text)

    if emoji_list:
        found_emoji = emoji_list[0]["emoji"]

        return found_emoji, name, link
    return "unknown symbol/emoji"