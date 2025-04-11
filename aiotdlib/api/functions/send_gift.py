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
    FormattedText,
    MessageSender,
)


class SendGift(BaseObject):
    """
    Sends a gift to another user or channel chat. May return an error with a message "STARGIFT_USAGE_LIMITED" if the gift was sold out

    :param gift_id: Identifier of the gift to send
    :type gift_id: :class:`Int64`
    :param owner_id: Identifier of the user or the channel chat that will receive the gift
    :type owner_id: :class:`MessageSender`
    :param text: Text to show along with the gift; 0-getOption("gift_text_length_max") characters. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities are allowed. Must be empty if the receiver enabled paid messages
    :type text: :class:`FormattedText`
    :param is_private: Pass true to show gift text and sender only to the gift receiver; otherwise, everyone will be able to see them
    :type is_private: :class:`Bool`
    :param pay_for_upgrade: Pass true to additionally pay for the gift upgrade and allow the receiver to upgrade it for free
    :type pay_for_upgrade: :class:`Bool`
    """

    ID: typing.Literal["sendGift"] = Field("sendGift", validation_alias="@type", alias="@type")
    gift_id: Int64
    owner_id: MessageSender
    text: FormattedText
    is_private: Bool = False
    pay_for_upgrade: Bool = False
