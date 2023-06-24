# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckChatFolderInviteLink(BaseObject):
    """
    Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder

    :param invite_link: Invite link to be checked
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["checkChatFolderInviteLink"] = "checkChatFolderInviteLink"
    invite_link: String
