# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_administrator import ChatAdministrator
from ..base_object import BaseObject


class ChatAdministrators(BaseObject):
    """
    Represents a list of chat administrators
    
    Params:
        administrators (:obj:`list[ChatAdministrator]`)
            A list of chat administrators
        
    """

    ID: str = Field("chatAdministrators", alias="@type")
    administrators: list[ChatAdministrator]

    @staticmethod
    def read(q: dict) -> ChatAdministrators:
        return ChatAdministrators.construct(**q)
