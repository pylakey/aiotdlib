# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReorderSupergroupActiveUsernames(BaseObject):
    """
    Changes order of active usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`Int53`
    :param usernames: The new order of active usernames. All currently active usernames must be specified
    :type usernames: :class:`Vector[String]`
    """

    ID: typing.Literal["reorderSupergroupActiveUsernames"] = "reorderSupergroupActiveUsernames"
    supergroup_id: Int53
    usernames: Vector[String]
