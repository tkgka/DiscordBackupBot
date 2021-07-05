import asyncio
# import re

import discord


async def get_text(client, message, timeout=30, check=None) -> str:
    """
    유저에게 text 데이터를 받아옵니다. 
    check 매개변수에 확인 함수를 사용해 정해진 형식에 맞는 입력만 받을 수 있습니다.
    """
    try:
        def __check(m):
            result = message.author.id == m.author.id and message.channel.id == m.channel.id

            if check is not None:
                return result and check(m)
            else:
                return result
                
        message = await client.wait_for(
            "message", check=__check, timeout=timeout
        )
        return message.content

    except asyncio.TimeoutError:
        return None


async def get_number(client, message, timeout=30) -> int:
    """
    유저에게 정수형 데이터를 받아옵니다. 
    """
    check = lambda t: t.isdigit()
    return int(await get_text(client, message, timeout=timeout, check=check))