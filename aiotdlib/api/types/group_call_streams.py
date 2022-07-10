# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .group_call_stream import GroupCallStream
from ..base_object import BaseObject


class GroupCallStreams(BaseObject):
    """
    Represents a list of group call streams
    
    :param streams: A list of group call streams
    :type streams: :class:`list[GroupCallStream]`
    
    """

    ID: str = Field("groupCallStreams", alias="@type")
    streams: list[GroupCallStream]

    @staticmethod
    def read(q: dict) -> GroupCallStreams:
        return GroupCallStreams.construct(**q)
