# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .call_state import CallState
from ..base_object import BaseObject


class Call(BaseObject):
    """
    Describes a call
    
    :param id: Call identifier, not persistent
    :type id: :class:`int`
    
    :param user_id: Peer user identifier
    :type user_id: :class:`int`
    
    :param is_outgoing: True, if the call is outgoing
    :type is_outgoing: :class:`bool`
    
    :param is_video: True, if the call is a video call
    :type is_video: :class:`bool`
    
    :param state: Call state
    :type state: :class:`CallState`
    
    """

    ID: str = Field("call", alias="@type")
    id: int
    user_id: int
    is_outgoing: bool
    is_video: bool
    state: CallState

    @staticmethod
    def read(q: dict) -> Call:
        return Call.construct(**q)
