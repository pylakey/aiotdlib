# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatFolderInviteLinks(BaseObject):
    """
    Returns invite links created by the current user for a shareable chat folder

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    """

    ID: typing.Literal["getChatFolderInviteLinks"] = "getChatFolderInviteLinks"
    chat_folder_id: Int32
