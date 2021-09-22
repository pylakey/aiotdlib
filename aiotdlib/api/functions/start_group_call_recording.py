# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class StartGroupCallRecording(BaseObject):
    """
    Starts recording of an active group call. Requires groupCall.can_be_managed group call flag
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param title: Group call recording title; 0-64 characters, defaults to None
    :type title: :class:`str`, optional
    
    :param record_video: Pass true to record a video file instead of an audio file
    :type record_video: :class:`bool`
    
    :param use_portrait_orientation: Pass true to use portrait orientation for video instead of landscape one
    :type use_portrait_orientation: :class:`bool`
    
    """

    ID: str = Field("startGroupCallRecording", alias="@type")
    group_call_id: int
    title: typing.Optional[str] = Field(None, max_length=64)
    record_video: bool
    use_portrait_orientation: bool

    @staticmethod
    def read(q: dict) -> StartGroupCallRecording:
        return StartGroupCallRecording.construct(**q)
