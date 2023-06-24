# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRecommendedChatFolders(BaseObject):
    """
    Returns recommended chat folders for the current user
    """

    ID: typing.Literal["getRecommendedChatFolders"] = "getRecommendedChatFolders"
