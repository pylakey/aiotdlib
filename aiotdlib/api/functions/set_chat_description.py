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
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param param_description: New chat description; 0-255 characters, defaults to None
    :type param_description: :class:`str`, optional
    
    """

    ID: str = Field("setChatDescription", alias="@type")
    chat_id: int
    param_description: typing.Optional[str] = Field(None, max_length=255)

    @staticmethod
    def read(q: dict) -> SetChatDescription:
        return SetChatDescription.construct(**q)
