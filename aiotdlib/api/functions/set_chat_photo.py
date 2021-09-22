# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputChatPhoto
from ..base_object import BaseObject


class SetChatPhoto(BaseObject):
    """
    Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param photo: New chat photo. Pass null to delete the chat photo
    :type photo: :class:`InputChatPhoto`
    
    """

    ID: str = Field("setChatPhoto", alias="@type")
    chat_id: int
    photo: InputChatPhoto

    @staticmethod
    def read(q: dict) -> SetChatPhoto:
        return SetChatPhoto.construct(**q)
