# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_member_status import ChatMemberStatus
from ..base_object import BaseObject


class BasicGroup(BaseObject):
    """
    Represents a basic group of 0-200 users (must be upgraded to a supergroup to accommodate more than 200 users)
    
    Params:
        id (:class:`int`)
            Group identifier
        
        member_count (:class:`int`)
            Number of members in the group
        
        status (:class:`ChatMemberStatus`)
            Status of the current user in the group
        
        is_active (:class:`bool`)
            True, if the group is active
        
        upgraded_to_supergroup_id (:class:`int`)
            Identifier of the supergroup to which this group was upgraded; 0 if none
        
    """

    ID: str = Field("basicGroup", alias="@type")
    id: int
    member_count: int
    status: ChatMemberStatus
    is_active: bool
    upgraded_to_supergroup_id: int

    @staticmethod
    def read(q: dict) -> BasicGroup:
        return BasicGroup.construct(**q)
