# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetGroupCallInviteLink(BaseObject):
    """
    Returns invite link to a voice chat in a public chat
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        can_self_unmute (:class:`bool`)
            Pass true if the invite_link should contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag
        
    """

    ID: str = Field("getGroupCallInviteLink", alias="@type")
    group_call_id: int
    can_self_unmute: bool

    @staticmethod
    def read(q: dict) -> GetGroupCallInviteLink:
        return GetGroupCallInviteLink.construct(**q)
