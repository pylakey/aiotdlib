# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class StartGroupCallRecording(BaseObject):
    """
    Starts recording of an active group call. Requires groupCall.can_be_managed group call flag

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param title: Group call recording title; 0-64 characters
    :type title: :class:`String`
    :param record_video: Pass true to record a video file instead of an audio file
    :type record_video: :class:`Bool`
    :param use_portrait_orientation: Pass true to use portrait orientation for video instead of landscape one
    :type use_portrait_orientation: :class:`Bool`
    """

    ID: typing.Literal["startGroupCallRecording"] = "startGroupCallRecording"
    group_call_id: Int32
    title: String = Field("", max_length=64)
    record_video: Bool = False
    use_portrait_orientation: Bool = False
