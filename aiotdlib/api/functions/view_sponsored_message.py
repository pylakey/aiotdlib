# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ViewSponsoredMessage(BaseObject):
    """
    Informs TDLib that a sponsored message was viewed by the user
    
    :param chat_id: Identifier of the chat with the sponsored message
    :type chat_id: :class:`int`
    
    :param sponsored_message_id: The identifier of the sponsored message being viewed
    :type sponsored_message_id: :class:`int`
    
    """

    ID: str = Field("viewSponsoredMessage", alias="@type")
    chat_id: int
    sponsored_message_id: int

    @staticmethod
    def read(q: dict) -> ViewSponsoredMessage:
        return ViewSponsoredMessage.construct(**q)
