# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Location
from ..types import ReplyMarkup


class EditInlineMessageLiveLocation(BaseObject):
    """
    Edits the content of a live location in an inline message sent via a bot; for bots only
    
    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`str`
    
    :param reply_markup: The new message reply markup; pass null if none
    :type reply_markup: :class:`ReplyMarkup`
    
    :param location: New location content of the message; pass null to stop sharing the live location
    :type location: :class:`Location`
    
    :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
    :type heading: :class:`int`
    
    :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
    :type proximity_alert_radius: :class:`int`
    
    """

    ID: str = Field("editInlineMessageLiveLocation", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup
    location: Location
    heading: int
    proximity_alert_radius: int

    @staticmethod
    def read(q: dict) -> EditInlineMessageLiveLocation:
        return EditInlineMessageLiveLocation.construct(**q)
