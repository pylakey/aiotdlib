# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatAdministrator(BaseObject):
    """
    Contains information about a chat administrator
    
    Params:
        user_id (:class:`int`)
            User identifier of the administrator
        
        custom_title (:class:`str`)
            Custom title of the administrator
        
        is_owner (:class:`bool`)
            True, if the user is the owner of the chat
        
    """

    ID: str = Field("chatAdministrator", alias="@type")
    user_id: int
    custom_title: str
    is_owner: bool

    @staticmethod
    def read(q: dict) -> ChatAdministrator:
        return ChatAdministrator.construct(**q)
