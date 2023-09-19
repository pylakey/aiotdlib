# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CanSendStory(BaseObject):
    """
    Checks whether the current user can send a story
    """

    ID: typing.Literal["canSendStory"] = "canSendStory"
