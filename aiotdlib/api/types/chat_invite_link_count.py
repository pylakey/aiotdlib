# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatInviteLinkCount(BaseObject):
    """
    Describes a chat administrator with a number of active and revoked chat invite links
    
    :param user_id: Administrator's user identifier
    :type user_id: :class:`int`
    
    :param invite_link_count: Number of active invite links
    :type invite_link_count: :class:`int`
    
    :param revoked_invite_link_count: Number of revoked invite links
    :type revoked_invite_link_count: :class:`int`
    
    """

    ID: str = Field("chatInviteLinkCount", alias="@type")
    user_id: int
    invite_link_count: int
    revoked_invite_link_count: int

    @staticmethod
    def read(q: dict) -> ChatInviteLinkCount:
        return ChatInviteLinkCount.construct(**q)
