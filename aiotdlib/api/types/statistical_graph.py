# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class StatisticalGraph(BaseObject):
    """
    Describes a statistical graph
    
    """

    ID: str = Field("statisticalGraph", alias="@type")


class StatisticalGraphAsync(StatisticalGraph):
    """
    The graph data to be asynchronously loaded through getStatisticalGraph
    
    Params:
        token (:class:`str`)
            The token to use for data loading
        
    """

    ID: str = Field("statisticalGraphAsync", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> StatisticalGraphAsync:
        return StatisticalGraphAsync.construct(**q)


class StatisticalGraphData(StatisticalGraph):
    """
    A graph data
    
    Params:
        json_data (:class:`str`)
            Graph data in JSON format
        
        zoom_token (:class:`str`)
            If non-empty, a token which can be used to receive a zoomed in graph
        
    """

    ID: str = Field("statisticalGraphData", alias="@type")
    json_data: str
    zoom_token: str

    @staticmethod
    def read(q: dict) -> StatisticalGraphData:
        return StatisticalGraphData.construct(**q)


class StatisticalGraphError(StatisticalGraph):
    """
    An error message to be shown to the user instead of the graph
    
    Params:
        error_message (:class:`str`)
            The error message
        
    """

    ID: str = Field("statisticalGraphError", alias="@type")
    error_message: str

    @staticmethod
    def read(q: dict) -> StatisticalGraphError:
        return StatisticalGraphError.construct(**q)
