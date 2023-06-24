# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DiscardCall(BaseObject):
    """
    Discards a call

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    :param duration: The call duration, in seconds
    :type duration: :class:`Int32`
    :param connection_id: Identifier of the connection used during the call
    :type connection_id: :class:`Int64`
    :param is_disconnected: Pass true if the user was disconnected
    :type is_disconnected: :class:`Bool`
    :param is_video: Pass true if the call was a video call
    :type is_video: :class:`Bool`
    """

    ID: typing.Literal["discardCall"] = "discardCall"
    call_id: Int32
    duration: Int32
    connection_id: Int64
    is_disconnected: Bool = False
    is_video: Bool = False
