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
    ReactionType,
)


class SetSavedMessagesTagLabel(BaseObject):
    """
    Changes label of a Saved Messages tag; for Telegram Premium users only

    :param tag: The tag which label will be changed
    :type tag: :class:`ReactionType`
    :param label: New label for the tag; 0-12 characters
    :type label: :class:`String`
    """

    ID: typing.Literal["setSavedMessagesTagLabel"] = Field(
        "setSavedMessagesTagLabel", validation_alias="@type", alias="@type"
    )
    tag: ReactionType
    label: String = Field("", max_length=12)
