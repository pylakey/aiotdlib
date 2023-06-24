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


class EditChatFolder(BaseObject):
    """
    Edits existing chat folder. Returns information about the edited chat folder

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    :param folder: The edited chat folder
    :type folder: :class:`ChatFolder`
    """

    ID: typing.Literal["editChatFolder"] = "editChatFolder"
    chat_folder_id: Int32
    folder: ChatFolder
