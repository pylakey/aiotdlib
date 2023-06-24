# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EditChatFolderInviteLink(BaseObject):
    """
    Edits an invite link for a chat folder

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    :param invite_link: Invite link to be edited
    :type invite_link: :class:`String`
    :param chat_ids: New identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link editing
    :type chat_ids: :class:`Vector[Int53]`
    :param name: New name of the link; 0-32 characters
    :type name: :class:`String`
    """

    ID: typing.Literal["editChatFolderInviteLink"] = "editChatFolderInviteLink"
    chat_folder_id: Int32
    invite_link: String
    chat_ids: Vector[Int53]
    name: String = Field("", max_length=32)
