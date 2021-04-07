# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReportSupergroupSpam(BaseObject):
    """
    Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup
    
    Params:
        supergroup_id (:class:`int`)
            Supergroup identifier
        
        user_id (:class:`int`)
            User identifier
        
        message_ids (:obj:`list[int]`)
            Identifiers of messages sent in the supergroup by the user. This list must be non-empty
        
    """

    ID: str = Field("reportSupergroupSpam", alias="@type")
    supergroup_id: int
    user_id: int
    message_ids: list[int]

    @staticmethod
    def read(q: dict) -> ReportSupergroupSpam:
        return ReportSupergroupSpam.construct(**q)
