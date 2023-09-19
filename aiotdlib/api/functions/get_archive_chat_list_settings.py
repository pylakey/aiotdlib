# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetArchiveChatListSettings(BaseObject):
    """
    Returns settings for automatic moving of chats to and from the Archive chat lists
    """

    ID: typing.Literal["getArchiveChatListSettings"] = "getArchiveChatListSettings"
