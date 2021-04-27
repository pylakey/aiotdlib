# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class InviteGroupCallParticipants(BaseObject):
    """
    Invites users to an active group call. Sends a service message of type messageInviteToGroupCall for voice chats
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        user_ids (:obj:`list[int]`)
            User identifiers. At most 10 users can be invited simultaneously
        
    """

    ID: str = Field("inviteGroupCallParticipants", alias="@type")
    group_call_id: int
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> InviteGroupCallParticipants:
        return InviteGroupCallParticipants.construct(**q)
