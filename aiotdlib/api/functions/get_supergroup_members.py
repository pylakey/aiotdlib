# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import SupergroupMembersFilter


class GetSupergroupMembers(BaseObject):
    """
    Returns information about members or banned users in a supergroup or channel. Can be used only if SupergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the supergroup or channel
        
        filter_ (:class:`SupergroupMembersFilter`)
            The type of users to return. By default, supergroupMembersFilterRecent
        
        offset (:class:`int`)
            Number of users to skip
        
        limit (:class:`int`)
            The maximum number of users be returned; up to 200
        
    """

    ID: str = Field("getSupergroupMembers", alias="@type")
    supergroup_id: int
    filter_: SupergroupMembersFilter = Field(..., alias='filter')
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetSupergroupMembers:
        return GetSupergroupMembers.construct(**q)
