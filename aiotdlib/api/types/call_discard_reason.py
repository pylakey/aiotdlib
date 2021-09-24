# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CallDiscardReason(BaseObject):
    """
    Describes the reason why a call was discarded
    
    """

    ID: str = Field("callDiscardReason", alias="@type")


class CallDiscardReasonDeclined(CallDiscardReason):
    """
    The call was ended before the conversation started. It was declined by the other party
    
    """

    ID: str = Field("callDiscardReasonDeclined", alias="@type")

    @staticmethod
    def read(q: dict) -> CallDiscardReasonDeclined:
        return CallDiscardReasonDeclined.construct(**q)


class CallDiscardReasonDisconnected(CallDiscardReason):
    """
    The call was ended during the conversation because the users were disconnected
    
    """

    ID: str = Field("callDiscardReasonDisconnected", alias="@type")

    @staticmethod
    def read(q: dict) -> CallDiscardReasonDisconnected:
        return CallDiscardReasonDisconnected.construct(**q)


class CallDiscardReasonEmpty(CallDiscardReason):
    """
    The call wasn't discarded, or the reason is unknown
    
    """

    ID: str = Field("callDiscardReasonEmpty", alias="@type")

    @staticmethod
    def read(q: dict) -> CallDiscardReasonEmpty:
        return CallDiscardReasonEmpty.construct(**q)


class CallDiscardReasonHungUp(CallDiscardReason):
    """
    The call was ended because one of the parties hung up
    
    """

    ID: str = Field("callDiscardReasonHungUp", alias="@type")

    @staticmethod
    def read(q: dict) -> CallDiscardReasonHungUp:
        return CallDiscardReasonHungUp.construct(**q)


class CallDiscardReasonMissed(CallDiscardReason):
    """
    The call was ended before the conversation started. It was canceled by the caller or missed by the other party
    
    """

    ID: str = Field("callDiscardReasonMissed", alias="@type")

    @staticmethod
    def read(q: dict) -> CallDiscardReasonMissed:
        return CallDiscardReasonMissed.construct(**q)
