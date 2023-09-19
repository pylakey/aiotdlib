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
    ChatFolder,
)


class GetChatFolderChatCount(BaseObject):
    """
    Returns approximate number of chats in a being created chat folder. Main and archive chat lists must be fully preloaded for this function to work correctly

    :param folder: The new chat folder
    :type folder: :class:`ChatFolder`
    """

    ID: typing.Literal["getChatFolderChatCount"] = "getChatFolderChatCount"
    folder: ChatFolder
