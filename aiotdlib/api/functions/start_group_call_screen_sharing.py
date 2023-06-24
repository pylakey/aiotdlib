# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class StartGroupCallScreenSharing(BaseObject):
    """
    Starts screen sharing in a joined group call. Returns join response payload for tgcalls

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param audio_source_id: Screen sharing audio channel synchronization source identifier; received from tgcalls
    :type audio_source_id: :class:`Int32`
    :param payload: Group call join payload; received from tgcalls
    :type payload: :class:`String`
    """

    ID: typing.Literal["startGroupCallScreenSharing"] = "startGroupCallScreenSharing"
    group_call_id: Int32
    audio_source_id: Int32
    payload: String
