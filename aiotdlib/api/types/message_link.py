# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class MessageLink(BaseObject):
    """
    Contains an HTTPS link to a message in a supergroup or channel
    
    :param link: Message link
    :type link: :class:`str`
    
    :param is_public: True, if the link will work for non-members of the chat
    :type is_public: :class:`bool`
    
    """

    ID: str = Field("messageLink", alias="@type")
    link: str
    is_public: bool

    @staticmethod
    def read(q: dict) -> MessageLink:
        return MessageLink.construct(**q)
