# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject
from ..types import Location, ReplyMarkup


class EditInlineMessageLiveLocation(BaseObject):
    """
    Edits the content of a live location in an inline message sent via a bot; for bots only
    
    Params:
        inline_message_id (:class:`str`)
            Inline message identifier
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup
        
        location (:class:`Location`)
            New location content of the message; may be null. Pass null to stop sharing the live location
        
        heading (:class:`int`)
            The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        
        proximity_alert_radius (:class:`int`)
            The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        
    """

    ID: str = Field("editInlineMessageLiveLocation", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup
    location: typing.Optional[Location] = None
    heading: int
    proximity_alert_radius: int

    @staticmethod
    def read(q: dict) -> EditInlineMessageLiveLocation:
        return EditInlineMessageLiveLocation.construct(**q)
