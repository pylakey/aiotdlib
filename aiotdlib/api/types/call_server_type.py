# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        peer_tag (:class:`str`)
            A peer tag to be used with the reflector
        
    """

    ID: str = Field("callServerTypeTelegramReflector", alias="@type")
    peer_tag: str

    @staticmethod
    def read(q: dict) -> CallServerTypeTelegramReflector:
        return CallServerTypeTelegramReflector.construct(**q)


class CallServerTypeWebrtc(CallServerType):
    """
    A WebRTC server
    
    Params:
        username (:class:`str`)
            Username to be used for authentication
        
        password (:class:`str`)
            Authentication password
        
        supports_turn (:class:`bool`)
            True, if the server supports TURN
        
        supports_stun (:class:`bool`)
            True, if the server supports STUN
        
    """

    ID: str = Field("callServerTypeWebrtc", alias="@type")
    username: str
    password: str
    supports_turn: bool
    supports_stun: bool

    @staticmethod
    def read(q: dict) -> CallServerTypeWebrtc:
        return CallServerTypeWebrtc.construct(**q)
