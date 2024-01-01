# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetForumTopicDefaultIcons(BaseObject):
    """
    Returns list of custom emojis, which can be used as forum topic icon by all users
    """

    ID: typing.Literal["getForumTopicDefaultIcons"] = Field(
        "getForumTopicDefaultIcons", validation_alias="@type", alias="@type"
    )
