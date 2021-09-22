# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatSource(BaseObject):
    """
    Describes a reason why an external chat is shown in a chat list
    
    """

    ID: str = Field("chatSource", alias="@type")


class ChatSourceMtprotoProxy(ChatSource):
    """
    The chat is sponsored by the user's MTProxy server
    
    """

    ID: str = Field("chatSourceMtprotoProxy", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatSourceMtprotoProxy:
        return ChatSourceMtprotoProxy.construct(**q)


class ChatSourcePublicServiceAnnouncement(ChatSource):
    """
    The chat contains a public service announcement
    
    :param type_: The type of the announcement
    :type type_: :class:`str`
    
    :param text: The text of the announcement
    :type text: :class:`str`
    
    """

    ID: str = Field("chatSourcePublicServiceAnnouncement", alias="@type")
    type_: str = Field(..., alias='type')
    text: str

    @staticmethod
    def read(q: dict) -> ChatSourcePublicServiceAnnouncement:
        return ChatSourcePublicServiceAnnouncement.construct(**q)
