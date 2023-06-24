# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStatisticalGraph(BaseObject):
    """
    Loads an asynchronous or a zoomed in statistical graph

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param token: The token for graph loading
    :type token: :class:`String`
    :param x: X-value for zoomed in graph or 0 otherwise
    :type x: :class:`Int53`
    """

    ID: typing.Literal["getStatisticalGraph"] = "getStatisticalGraph"
    chat_id: Int53
    token: String
    x: Int53
