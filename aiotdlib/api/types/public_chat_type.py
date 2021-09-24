# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PublicChatType(BaseObject):
    """
    Describes a type of public chats
    
    """

    ID: str = Field("publicChatType", alias="@type")


class PublicChatTypeHasUsername(PublicChatType):
    """
    The chat is public, because it has username
    
    """

    ID: str = Field("publicChatTypeHasUsername", alias="@type")

    @staticmethod
    def read(q: dict) -> PublicChatTypeHasUsername:
        return PublicChatTypeHasUsername.construct(**q)


class PublicChatTypeIsLocationBased(PublicChatType):
    """
    The chat is public, because it is a location-based supergroup
    
    """

    ID: str = Field("publicChatTypeIsLocationBased", alias="@type")

    @staticmethod
    def read(q: dict) -> PublicChatTypeIsLocationBased:
        return PublicChatTypeIsLocationBased.construct(**q)
