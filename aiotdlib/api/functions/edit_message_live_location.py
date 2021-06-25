# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject
from ..types import Location
from ..types import ReplyMarkup


class EditMessageLiveLocation(BaseObject):
    """
    Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location. Returns the edited message after the edit is completed on the server side
    
    Params:
        chat_id (:class:`int`)
            The chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup; for bots only
        
        location (:class:`Location`)
            New location content of the message; may be null. Pass null to stop sharing the live location
        
        heading (:class:`int`)
            The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        
        proximity_alert_radius (:class:`int`)
            The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
        
    """

    ID: str = Field("editMessageLiveLocation", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup
    location: typing.Optional[Location] = None
    heading: int
    proximity_alert_radius: int

    @staticmethod
    def read(q: dict) -> EditMessageLiveLocation:
        return EditMessageLiveLocation.construct(**q)
