# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DisableAllSupergroupUsernames(BaseObject):
    """
    Disables all active non-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["disableAllSupergroupUsernames"] = "disableAllSupergroupUsernames"
    supergroup_id: Int53
