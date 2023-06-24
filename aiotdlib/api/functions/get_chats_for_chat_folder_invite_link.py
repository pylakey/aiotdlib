# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatsForChatFolderInviteLink(BaseObject):
    """
    Returns identifiers of chats from a chat folder, suitable for adding to a chat folder invite link

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    """

    ID: typing.Literal["getChatsForChatFolderInviteLink"] = "getChatsForChatFolderInviteLink"
    chat_folder_id: Int32
