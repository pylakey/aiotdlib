# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class OpenChat(BaseObject):
    """
    Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats)
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("openChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> OpenChat:
        return OpenChat.construct(**q)
