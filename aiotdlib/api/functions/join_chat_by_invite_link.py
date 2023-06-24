# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class JoinChatByInviteLink(BaseObject):
    """
    Uses an invite link to add the current user to the chat if possible. May return an error with a message "INVITE_REQUEST_SENT" if only a join request was created

    :param invite_link: Invite link to use
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["joinChatByInviteLink"] = "joinChatByInviteLink"
    invite_link: String
