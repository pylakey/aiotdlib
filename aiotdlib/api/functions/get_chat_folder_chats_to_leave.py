# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatFolderChatsToLeave(BaseObject):
    """
    Returns identifiers of pinned or always included chats from a chat folder, which are suggested to be left when the chat folder is deleted

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    """

    ID: typing.Literal["getChatFolderChatsToLeave"] = "getChatFolderChatsToLeave"
    chat_folder_id: Int32
