# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ViewSponsoredMessage(BaseObject):
    """
    Informs TDLib that a sponsored message was viewed by the user
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`str`)
            The identifier of the sponsored message being viewed
        
    """

    ID: str = Field("viewSponsoredMessage", alias="@type")
    chat_id: int
    message_id: str

    @staticmethod
    def read(q: dict) -> ViewSponsoredMessage:
        return ViewSponsoredMessage.construct(**q)
