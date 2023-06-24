# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendCallSignalingData(BaseObject):
    """
    Sends call signaling data

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    :param data: The data
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["sendCallSignalingData"] = "sendCallSignalingData"
    call_id: Int32
    data: Bytes
