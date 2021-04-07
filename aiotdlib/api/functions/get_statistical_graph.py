# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetStatisticalGraph(BaseObject):
    """
    Loads an asynchronous or a zoomed in statistical graph
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        token (:class:`str`)
            The token for graph loading
        
        x (:class:`int`)
            X-value for zoomed in graph or 0 otherwise
        
    """

    ID: str = Field("getStatisticalGraph", alias="@type")
    chat_id: int
    token: str
    x: int

    @staticmethod
    def read(q: dict) -> GetStatisticalGraph:
        return GetStatisticalGraph.construct(**q)
