# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    
    :param reason: The reason, why the call has ended
    :type reason: :class:`CallDiscardReason`
    
    :param need_rating: True, if the call rating should be sent to the server
    :type need_rating: :class:`bool`
    
    :param need_debug_information: True, if the call debug information should be sent to the server
    :type need_debug_information: :class:`bool`
    
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
    
    :param error: Error. An error with the code 4005000 will be returned if an outgoing call is missed because of an expired timeout
    :type error: :class:`Error`
    
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
    
    :param is_created: True, if the call has already been created by the server
    :type is_created: :class:`bool`
    
    :param is_received: True, if the call has already been received by the other party
    :type is_received: :class:`bool`
    
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
    
    :param protocol: Call protocols supported by the peer
    :type protocol: :class:`CallProtocol`
    
    :param servers: List of available call servers
    :type servers: :class:`list[CallServer]`
    
    :param config: A JSON-encoded call config
    :type config: :class:`str`
    
    :param encryption_key: Call encryption key
    :type encryption_key: :class:`str`
    
    :param emojis: Encryption key emojis fingerprint
    :type emojis: :class:`list[str]`
    
    :param allow_p2p: True, if peer-to-peer connection is allowed by users privacy settings
    :type allow_p2p: :class:`bool`
    
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
