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
    BusinessConnectedBot,
)


class SetBusinessConnectedBot(BaseObject):
    """
    Adds or changes business bot that is connected to the current user account

    :param bot: Connection settings for the bot
    :type bot: :class:`BusinessConnectedBot`
    """

    ID: typing.Literal["setBusinessConnectedBot"] = Field(
        "setBusinessConnectedBot", validation_alias="@type", alias="@type"
    )
    bot: BusinessConnectedBot
