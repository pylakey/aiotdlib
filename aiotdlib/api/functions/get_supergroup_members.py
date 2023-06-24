# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    SupergroupMembersFilter,
)


class GetSupergroupMembers(BaseObject):
    """
    Returns information about members or banned users in a supergroup or channel. Can be used only if supergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters

    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`Int53`
    :param offset: Number of users to skip
    :type offset: :class:`Int32`
    :param limit: The maximum number of users be returned; up to 200
    :type limit: :class:`Int32`
    :param filter_: The type of users to return; pass null to use supergroupMembersFilterRecent, defaults to None
    :type filter_: :class:`SupergroupMembersFilter`, optional
    """

    ID: typing.Literal["getSupergroupMembers"] = "getSupergroupMembers"
    supergroup_id: Int53
    offset: Int32
    limit: Int32
    filter_: typing.Optional[SupergroupMembersFilter] = Field(None, alias="filter")
