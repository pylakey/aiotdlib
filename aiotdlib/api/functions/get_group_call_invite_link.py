# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetGroupCallInviteLink(BaseObject):
    """
    Returns invite link to a voice chat in a public chat
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param can_self_unmute: Pass true if the invite_link should contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag
    :type can_self_unmute: :class:`bool`
    
    """

    ID: str = Field("getGroupCallInviteLink", alias="@type")
    group_call_id: int
    can_self_unmute: bool

    @staticmethod
    def read(q: dict) -> GetGroupCallInviteLink:
        return GetGroupCallInviteLink.construct(**q)
