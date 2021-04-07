# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputChatPhoto


class SetChatPhoto(BaseObject):
    """
    Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        photo (:class:`InputChatPhoto`)
            New chat photo. Pass null to delete the chat photo
        
    """

    ID: str = Field("setChatPhoto", alias="@type")
    chat_id: int
    photo: InputChatPhoto

    @staticmethod
    def read(q: dict) -> SetChatPhoto:
        return SetChatPhoto.construct(**q)
