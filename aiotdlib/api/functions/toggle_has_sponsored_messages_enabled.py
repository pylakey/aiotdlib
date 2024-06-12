# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleHasSponsoredMessagesEnabled(BaseObject):
    """
    Toggles whether the current user has sponsored messages enabled. The setting has no effect for users without Telegram Premium for which sponsored messages are always enabled

    :param has_sponsored_messages_enabled: Pass true to enable sponsored messages for the current user; false to disable them
    :type has_sponsored_messages_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleHasSponsoredMessagesEnabled"] = Field(
        "toggleHasSponsoredMessagesEnabled", validation_alias="@type", alias="@type"
    )
    has_sponsored_messages_enabled: Bool = False
