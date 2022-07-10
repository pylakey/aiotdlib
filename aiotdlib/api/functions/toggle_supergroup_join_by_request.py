# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupJoinByRequest(BaseObject):
    """
    Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can_restrict_members administrator right
    
    :param supergroup_id: Identifier of the channel
    :type supergroup_id: :class:`int`
    
    :param join_by_request: New value of join_by_request
    :type join_by_request: :class:`bool`
    
    """

    ID: str = Field("toggleSupergroupJoinByRequest", alias="@type")
    supergroup_id: int
    join_by_request: bool

    @staticmethod
    def read(q: dict) -> ToggleSupergroupJoinByRequest:
        return ToggleSupergroupJoinByRequest.construct(**q)
