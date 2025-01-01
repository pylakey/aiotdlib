
from aiotdlib import Client


async def test_me(client: Client) -> None:
    my_info = await client.api.get_me()
    assert my_info is not None
    assert my_info.id is not None


async def test_chats(client: Client) -> None:
    chats = await client.get_main_list_chats(limit=1)
    assert len(chats) == 1
