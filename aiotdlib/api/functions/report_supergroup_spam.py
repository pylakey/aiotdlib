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
    Reports some messages from a message sender in a supergroup as spam; requires administrator rights in the supergroup
    
    :param supergroup_id: Supergroup identifier
    :type supergroup_id: :class:`int`
    
    :param message_ids: Identifiers of messages sent in the supergroup. All messages must be sent by the same sender. This list must be non-empty
    :type message_ids: :class:`list[int]`
    
    """

    ID: str = Field("reportSupergroupSpam", alias="@type")
    supergroup_id: int
    message_ids: list[int]

    @staticmethod
    def read(q: dict) -> ReportSupergroupSpam:
        return ReportSupergroupSpam.construct(**q)
