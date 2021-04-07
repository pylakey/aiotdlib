# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetChatClientData(BaseObject):
    """
    Changes application-specific data associated with a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        client_data (:class:`str`)
            New value of client_data
        
    """

    ID: str = Field("setChatClientData", alias="@type")
    chat_id: int
    client_data: str

    @staticmethod
    def read(q: dict) -> SetChatClientData:
        return SetChatClientData.construct(**q)
