# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetReadDatePrivacySettings(BaseObject):
    """
    Returns privacy settings for message read date
    """

    ID: typing.Literal["getReadDatePrivacySettings"] = Field(
        "getReadDatePrivacySettings", validation_alias="@type", alias="@type"
    )
