# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    Location,
    ReplyMarkup,
)


class EditInlineMessageLiveLocation(BaseObject):
    """
    Edits the content of a live location in an inline message sent via a bot; for bots only

    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`String`
    :param live_period: New time relative to the message send date, for which the location can be updated, in seconds. If 0x7FFFFFFF specified, then the location can be updated forever. Otherwise, must not exceed the current live_period by more than a day, and the live location expiration date must remain in the next 90 days. Pass 0 to keep the current live_period
    :type live_period: :class:`Int32`
    :param heading: The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
    :type heading: :class:`Int32`
    :param proximity_alert_radius: The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
    :type proximity_alert_radius: :class:`Int32`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    :param location: New location content of the message; pass null to stop sharing the live location, defaults to None
    :type location: :class:`Location`, optional
    """

    ID: typing.Literal["editInlineMessageLiveLocation"] = Field(
        "editInlineMessageLiveLocation", validation_alias="@type", alias="@type"
    )
    inline_message_id: String
    live_period: Int32 = 0
    heading: Int32 = 0
    proximity_alert_radius: Int32 = 0
    reply_markup: typing.Optional[ReplyMarkup] = None
    location: typing.Optional[Location] = None
