# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddChatFolderByInviteLink(BaseObject):
    """
    Adds a chat folder by an invite link

    :param invite_link: Invite link for the chat folder
    :type invite_link: :class:`String`
    :param chat_ids: Identifiers of the chats added to the chat folder. The chats are automatically joined if they aren't joined yet
    :type chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["addChatFolderByInviteLink"] = "addChatFolderByInviteLink"
    invite_link: String
    chat_ids: Vector[Int53]
