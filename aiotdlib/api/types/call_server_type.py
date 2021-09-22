# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CallServerType(BaseObject):
    """
    Describes the type of a call server
    
    """

    ID: str = Field("callServerType", alias="@type")


class CallServerTypeTelegramReflector(CallServerType):
    """
    A Telegram call reflector
    
    :param peer_tag: A peer tag to be used with the reflector
    :type peer_tag: :class:`str`
    
    """

    ID: str = Field("callServerTypeTelegramReflector", alias="@type")
    peer_tag: str

    @staticmethod
    def read(q: dict) -> CallServerTypeTelegramReflector:
        return CallServerTypeTelegramReflector.construct(**q)


class CallServerTypeWebrtc(CallServerType):
    """
    A WebRTC server
    
    :param username: Username to be used for authentication
    :type username: :class:`str`
    
    :param password: Authentication password
    :type password: :class:`str`
    
    :param supports_turn: True, if the server supports TURN
    :type supports_turn: :class:`bool`
    
    :param supports_stun: True, if the server supports STUN
    :type supports_stun: :class:`bool`
    
    """

    ID: str = Field("callServerTypeWebrtc", alias="@type")
    username: str
    password: str
    supports_turn: bool
    supports_stun: bool

    @staticmethod
    def read(q: dict) -> CallServerTypeWebrtc:
        return CallServerTypeWebrtc.construct(**q)
