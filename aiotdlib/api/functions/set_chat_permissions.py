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
    ChatPermissions,
)


class SetChatPermissions(BaseObject):
    """
    Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param permissions: New non-administrator members permissions in the chat
    :type permissions: :class:`ChatPermissions`
    """

    ID: typing.Literal["setChatPermissions"] = "setChatPermissions"
    chat_id: Int53
    permissions: ChatPermissions
