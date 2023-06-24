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


class CreateChatFolder(BaseObject):
    """
    Creates new chat folder. Returns information about the created chat folder. There can be up to getOption("chat_folder_count_max") chat folders, but the limit can be increased with Telegram Premium

    :param folder: The new chat folder
    :type folder: :class:`ChatFolder`
    """

    ID: typing.Literal["createChatFolder"] = "createChatFolder"
    folder: ChatFolder
