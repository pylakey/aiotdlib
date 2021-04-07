# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .statistical_graph import StatisticalGraph
from ..base_object import BaseObject


class MessageStatistics(BaseObject):
    """
    A detailed statistics about a message
    
    Params:
        message_interaction_graph (:class:`StatisticalGraph`)
            A graph containing number of message views and shares
        
    """

    ID: str = Field("messageStatistics", alias="@type")
    message_interaction_graph: StatisticalGraph

    @staticmethod
    def read(q: dict) -> MessageStatistics:
        return MessageStatistics.construct(**q)
