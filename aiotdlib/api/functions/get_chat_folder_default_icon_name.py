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


class GetChatFolderDefaultIconName(BaseObject):
    """
    Returns default icon name for a folder. Can be called synchronously

    :param folder: Chat folder
    :type folder: :class:`ChatFolder`
    """

    ID: typing.Literal["getChatFolderDefaultIconName"] = "getChatFolderDefaultIconName"
    folder: ChatFolder
