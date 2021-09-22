# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class StartGroupCallScreenSharing(BaseObject):
    """
    Starts screen sharing in a joined group call. Returns join response payload for tgcalls
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param audio_source_id: Screen sharing audio channel synchronization source identifier; received from tgcalls
    :type audio_source_id: :class:`int`
    
    :param payload: Group call join payload; received from tgcalls
    :type payload: :class:`str`
    
    """

    ID: str = Field("startGroupCallScreenSharing", alias="@type")
    group_call_id: int
    audio_source_id: int
    payload: str

    @staticmethod
    def read(q: dict) -> StartGroupCallScreenSharing:
        return StartGroupCallScreenSharing.construct(**q)
