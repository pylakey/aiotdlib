# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class MessageLink(BaseObject):
    """
    Contains an HTTPS link to a message in a supergroup or channel
    
    Params:
        link (:class:`str`)
            Message link
        
        is_public (:class:`bool`)
            True, if the link will work for non-members of the chat
        
    """

    ID: str = Field("messageLink", alias="@type")
    link: str
    is_public: bool

    @staticmethod
    def read(q: dict) -> MessageLink:
        return MessageLink.construct(**q)
