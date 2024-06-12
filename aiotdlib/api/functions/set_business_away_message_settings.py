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
    BusinessAwayMessageSettings,
)


class SetBusinessAwayMessageSettings(BaseObject):
    """
    Changes the business away message settings of the current user. Requires Telegram Business subscription

    :param away_message_settings: The new settings for the away message of the business; pass null to disable the away message, defaults to None
    :type away_message_settings: :class:`BusinessAwayMessageSettings`, optional
    """

    ID: typing.Literal["setBusinessAwayMessageSettings"] = Field(
        "setBusinessAwayMessageSettings", validation_alias="@type", alias="@type"
    )
    away_message_settings: typing.Optional[BusinessAwayMessageSettings] = None
