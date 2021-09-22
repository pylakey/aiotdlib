# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_member_status import ChatMemberStatus
from ..base_object import BaseObject


class BasicGroup(BaseObject):
    """
    Represents a basic group of 0-200 users (must be upgraded to a supergroup to accommodate more than 200 users)
    
    :param id: Group identifier
    :type id: :class:`int`
    
    :param member_count: Number of members in the group
    :type member_count: :class:`int`
    
    :param status: Status of the current user in the group
    :type status: :class:`ChatMemberStatus`
    
    :param is_active: True, if the group is active
    :type is_active: :class:`bool`
    
    :param upgraded_to_supergroup_id: Identifier of the supergroup to which this group was upgraded; 0 if none
    :type upgraded_to_supergroup_id: :class:`int`
    
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
