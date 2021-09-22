# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    
    :param token: The token to use for data loading
    :type token: :class:`str`
    
    """

    ID: str = Field("statisticalGraphAsync", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> StatisticalGraphAsync:
        return StatisticalGraphAsync.construct(**q)


class StatisticalGraphData(StatisticalGraph):
    """
    A graph data
    
    :param json_data: Graph data in JSON format
    :type json_data: :class:`str`
    
    :param zoom_token: If non-empty, a token which can be used to receive a zoomed in graph
    :type zoom_token: :class:`str`
    
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
    
    :param error_message: The error message
    :type error_message: :class:`str`
    
    """

    ID: str = Field("statisticalGraphError", alias="@type")
    error_message: str

    @staticmethod
    def read(q: dict) -> StatisticalGraphError:
        return StatisticalGraphError.construct(**q)
