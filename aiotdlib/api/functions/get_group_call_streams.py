# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetGroupCallStreams(BaseObject):
    """
    Returns information about available group call streams
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    """

    ID: str = Field("getGroupCallStreams", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> GetGroupCallStreams:
        return GetGroupCallStreams.construct(**q)
