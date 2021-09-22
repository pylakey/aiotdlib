# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DiscardCall(BaseObject):
    """
    Discards a call
    
    :param call_id: Call identifier
    :type call_id: :class:`int`
    
    :param is_disconnected: True, if the user was disconnected
    :type is_disconnected: :class:`bool`
    
    :param duration: The call duration, in seconds
    :type duration: :class:`int`
    
    :param is_video: True, if the call was a video call
    :type is_video: :class:`bool`
    
    :param connection_id: Identifier of the connection used during the call
    :type connection_id: :class:`int`
    
    """

    ID: str = Field("discardCall", alias="@type")
    call_id: int
    is_disconnected: bool
    duration: int
    is_video: bool
    connection_id: int

    @staticmethod
    def read(q: dict) -> DiscardCall:
        return DiscardCall.construct(**q)
