# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PublicChatType


class GetCreatedPublicChats(BaseObject):
    """
    Returns a list of public chats of the specified type, owned by the user
    
    Params:
        type_ (:class:`PublicChatType`)
            Type of the public chats to return
        
    """

    ID: str = Field("getCreatedPublicChats", alias="@type")
    type_: PublicChatType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> GetCreatedPublicChats:
        return GetCreatedPublicChats.construct(**q)
