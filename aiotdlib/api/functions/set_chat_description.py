# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetChatDescription(BaseObject):
    """
    Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat
        
        param_description (:class:`str`)
            New chat description; 0-255 characters
        
    """

    ID: str = Field("setChatDescription", alias="@type")
    chat_id: int
    param_description: typing.Optional[str] = Field(None, max_length=255)

    @staticmethod
    def read(q: dict) -> SetChatDescription:
        return SetChatDescription.construct(**q)
