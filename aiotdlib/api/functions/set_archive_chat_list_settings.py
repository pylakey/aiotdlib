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
    ArchiveChatListSettings,
)


class SetArchiveChatListSettings(BaseObject):
    """
    Changes settings for automatic moving of chats to and from the Archive chat lists

    :param settings: New settings
    :type settings: :class:`ArchiveChatListSettings`
    """

    ID: typing.Literal["setArchiveChatListSettings"] = "setArchiveChatListSettings"
    settings: ArchiveChatListSettings
