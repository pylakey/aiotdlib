# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleSupergroupIsForum(BaseObject):
    """
    Toggles whether the supergroup is a forum; requires owner privileges in the supergroup. Discussion supergroups can't be converted to forums

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param is_forum: New value of is_forum
    :type is_forum: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupIsForum"] = "toggleSupergroupIsForum"
    supergroup_id: Int53
    is_forum: Bool
