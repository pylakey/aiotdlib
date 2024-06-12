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
    ReadDatePrivacySettings,
)


class SetReadDatePrivacySettings(BaseObject):
    """
    Changes privacy settings for message read date

    :param settings: New settings
    :type settings: :class:`ReadDatePrivacySettings`
    """

    ID: typing.Literal["setReadDatePrivacySettings"] = Field(
        "setReadDatePrivacySettings", validation_alias="@type", alias="@type"
    )
    settings: ReadDatePrivacySettings
