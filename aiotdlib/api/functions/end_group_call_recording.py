# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class EndGroupCallRecording(BaseObject):
    """
    Ends recording of an active group call. Requires groupCall.can_be_managed group call flag
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    """

    ID: str = Field("endGroupCallRecording", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> EndGroupCallRecording:
        return EndGroupCallRecording.construct(**q)
