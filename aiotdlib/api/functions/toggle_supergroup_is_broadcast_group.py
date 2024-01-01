# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleSupergroupIsBroadcastGroup(BaseObject):
    """
    Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["toggleSupergroupIsBroadcastGroup"] = Field(
        "toggleSupergroupIsBroadcastGroup", validation_alias="@type", alias="@type"
    )
    supergroup_id: Int53
