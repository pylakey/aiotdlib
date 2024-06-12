# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetNewChatPrivacySettings(BaseObject):
    """
    Returns privacy settings for new chat creation
    """

    ID: typing.Literal["getNewChatPrivacySettings"] = Field(
        "getNewChatPrivacySettings", validation_alias="@type", alias="@type"
    )
