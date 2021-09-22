# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ReportSupergroupSpam(BaseObject):
    """
    Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup
    
    :param supergroup_id: Supergroup identifier
    :type supergroup_id: :class:`int`
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param message_ids: Identifiers of messages sent in the supergroup by the user. This list must be non-empty
    :type message_ids: :class:`list[int]`
    
    """

    ID: str = Field("reportSupergroupSpam", alias="@type")
    supergroup_id: int
    user_id: int
    message_ids: list[int]

    @staticmethod
    def read(q: dict) -> ReportSupergroupSpam:
        return ReportSupergroupSpam.construct(**q)
