# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupIsAllHistoryAvailable(BaseObject):
    """
    Toggles whether the message history of a supergroup is available to new members; requires can_change_info administrator right
    
    :param supergroup_id: The identifier of the supergroup
    :type supergroup_id: :class:`int`
    
    :param is_all_history_available: The new value of is_all_history_available
    :type is_all_history_available: :class:`bool`
    
    """

    ID: str = Field("toggleSupergroupIsAllHistoryAvailable", alias="@type")
    supergroup_id: int
    is_all_history_available: bool

    @staticmethod
    def read(q: dict) -> ToggleSupergroupIsAllHistoryAvailable:
        return ToggleSupergroupIsAllHistoryAvailable.construct(**q)
