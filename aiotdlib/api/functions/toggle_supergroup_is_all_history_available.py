# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleSupergroupIsAllHistoryAvailable(BaseObject):
    """
    Toggles whether the message history of a supergroup is available to new members; requires can_change_info administrator right

    :param supergroup_id: The identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param is_all_history_available: The new value of is_all_history_available
    :type is_all_history_available: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupIsAllHistoryAvailable"] = "toggleSupergroupIsAllHistoryAvailable"
    supergroup_id: Int53
    is_all_history_available: Bool
