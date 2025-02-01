# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EditChatSubscriptionInviteLink(BaseObject):
    """
    Edits a subscription invite link for a channel chat. Requires can_invite_users right in the chat for own links and owner privileges for other links

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param invite_link: Invite link to be edited
    :type invite_link: :class:`String`
    :param name: Invite link name; 0-32 characters
    :type name: :class:`String`
    """

    ID: typing.Literal["editChatSubscriptionInviteLink"] = Field(
        "editChatSubscriptionInviteLink", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    invite_link: String
    name: String = Field("", max_length=32)
