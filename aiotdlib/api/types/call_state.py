# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .call_discard_reason import CallDiscardReason
from .call_protocol import CallProtocol
from .call_server import CallServer
from .error import Error
from ..base_object import BaseObject


class CallState(BaseObject):
    """
    Describes the current call state
    
    """

    ID: str = Field("callState", alias="@type")


class CallStateDiscarded(CallState):
    """
    The call has ended successfully
    
    Params:
        reason (:class:`CallDiscardReason`)
            The reason, why the call has ended
        
        need_rating (:class:`bool`)
            True, if the call rating should be sent to the server
        
        need_debug_information (:class:`bool`)
            True, if the call debug information should be sent to the server
        
    """

    ID: str = Field("callStateDiscarded", alias="@type")
    reason: CallDiscardReason
    need_rating: bool
    need_debug_information: bool

    @staticmethod
    def read(q: dict) -> CallStateDiscarded:
        return CallStateDiscarded.construct(**q)


class CallStateError(CallState):
    """
    The call has ended with an error
    
    Params:
        error (:class:`Error`)
            Error. An error with the code 4005000 will be returned if an outgoing call is missed because of an expired timeout
        
    """

    ID: str = Field("callStateError", alias="@type")
    error: Error

    @staticmethod
    def read(q: dict) -> CallStateError:
        return CallStateError.construct(**q)


class CallStateExchangingKeys(CallState):
    """
    The call has been answered and encryption keys are being exchanged
    
    """

    ID: str = Field("callStateExchangingKeys", alias="@type")

    @staticmethod
    def read(q: dict) -> CallStateExchangingKeys:
        return CallStateExchangingKeys.construct(**q)


class CallStateHangingUp(CallState):
    """
    The call is hanging up after discardCall has been called
    
    """

    ID: str = Field("callStateHangingUp", alias="@type")

    @staticmethod
    def read(q: dict) -> CallStateHangingUp:
        return CallStateHangingUp.construct(**q)


class CallStatePending(CallState):
    """
    The call is pending, waiting to be accepted by a user
    
    Params:
        is_created (:class:`bool`)
            True, if the call has already been created by the server
        
        is_received (:class:`bool`)
            True, if the call has already been received by the other party
        
    """

    ID: str = Field("callStatePending", alias="@type")
    is_created: bool
    is_received: bool

    @staticmethod
    def read(q: dict) -> CallStatePending:
        return CallStatePending.construct(**q)


class CallStateReady(CallState):
    """
    The call is ready to use
    
    Params:
        protocol (:class:`CallProtocol`)
            Call protocols supported by the peer
        
        servers (:obj:`list[CallServer]`)
            List of available call servers
        
        config (:class:`str`)
            A JSON-encoded call config
        
        encryption_key (:class:`str`)
            Call encryption key
        
        emojis (:obj:`list[str]`)
            Encryption key emojis fingerprint
        
        allow_p2p (:class:`bool`)
            True, if peer-to-peer connection is allowed by users privacy settings
        
    """

    ID: str = Field("callStateReady", alias="@type")
    protocol: CallProtocol
    servers: list[CallServer]
    config: str
    encryption_key: str
    emojis: list[str]
    allow_p2p: bool

    @staticmethod
    def read(q: dict) -> CallStateReady:
        return CallStateReady.construct(**q)
