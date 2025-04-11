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
    MessageSender,
)


class SetPinnedGifts(BaseObject):
    """
    Changes the list of pinned gifts on the current user's or the channel's profile page; requires can_post_messages administrator right in the channel chat

    :param owner_id: Identifier of the user or the channel chat that received the gifts
    :type owner_id: :class:`MessageSender`
    :param received_gift_ids: New list of pinned gifts. All gifts must be upgraded and saved on the profile page first. There can be up to getOption("pinned_gift_count_max") pinned gifts
    :type received_gift_ids: :class:`Vector[String]`
    """

    ID: typing.Literal["setPinnedGifts"] = Field("setPinnedGifts", validation_alias="@type", alias="@type")
    owner_id: MessageSender
    received_gift_ids: Vector[String]
