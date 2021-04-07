# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RevokeGroupCallInviteLink(BaseObject):
    """
    Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
    """

    ID: str = Field("revokeGroupCallInviteLink", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> RevokeGroupCallInviteLink:
        return RevokeGroupCallInviteLink.construct(**q)
