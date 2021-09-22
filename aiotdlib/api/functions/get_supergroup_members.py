# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import SupergroupMembersFilter
from ..base_object import BaseObject


class GetSupergroupMembers(BaseObject):
    """
    Returns information about members or banned users in a supergroup or channel. Can be used only if supergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters
    
    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`int`
    
    :param filter_: The type of users to return. By default, supergroupMembersFilterRecent
    :type filter_: :class:`SupergroupMembersFilter`
    
    :param offset: Number of users to skip
    :type offset: :class:`int`
    
    :param limit: The maximum number of users be returned; up to 200
    :type limit: :class:`int`
    
    """

    ID: str = Field("getSupergroupMembers", alias="@type")
    supergroup_id: int
    filter_: SupergroupMembersFilter = Field(..., alias='filter')
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetSupergroupMembers:
        return GetSupergroupMembers.construct(**q)
