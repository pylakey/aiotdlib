# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetStatisticalGraph(BaseObject):
    """
    Loads an asynchronous or a zoomed in statistical graph
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param token: The token for graph loading
    :type token: :class:`str`
    
    :param x: X-value for zoomed in graph or 0 otherwise
    :type x: :class:`int`
    
    """

    ID: str = Field("getStatisticalGraph", alias="@type")
    chat_id: int
    token: str
    x: int

    @staticmethod
    def read(q: dict) -> GetStatisticalGraph:
        return GetStatisticalGraph.construct(**q)
