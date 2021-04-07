# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CanTransferOwnershipResult(BaseObject):
    """
    Represents result of checking whether the current session can be used to transfer a chat ownership to another user
    
    """

    ID: str = Field("canTransferOwnershipResult", alias="@type")


class CanTransferOwnershipResultOk(CanTransferOwnershipResult):
    """
    The session can be used
    
    """

    ID: str = Field("canTransferOwnershipResultOk", alias="@type")

    @staticmethod
    def read(q: dict) -> CanTransferOwnershipResultOk:
        return CanTransferOwnershipResultOk.construct(**q)


class CanTransferOwnershipResultPasswordNeeded(CanTransferOwnershipResult):
    """
    The 2-step verification needs to be enabled first
    
    """

    ID: str = Field("canTransferOwnershipResultPasswordNeeded", alias="@type")

    @staticmethod
    def read(q: dict) -> CanTransferOwnershipResultPasswordNeeded:
        return CanTransferOwnershipResultPasswordNeeded.construct(**q)


class CanTransferOwnershipResultPasswordTooFresh(CanTransferOwnershipResult):
    """
    The 2-step verification was enabled recently, user needs to wait
    
    Params:
        retry_after (:class:`int`)
            Time left before the session can be used to transfer ownership of a chat, in seconds
        
    """

    ID: str = Field("canTransferOwnershipResultPasswordTooFresh", alias="@type")
    retry_after: int

    @staticmethod
    def read(q: dict) -> CanTransferOwnershipResultPasswordTooFresh:
        return CanTransferOwnershipResultPasswordTooFresh.construct(**q)


class CanTransferOwnershipResultSessionTooFresh(CanTransferOwnershipResult):
    """
    The session was created recently, user needs to wait
    
    Params:
        retry_after (:class:`int`)
            Time left before the session can be used to transfer ownership of a chat, in seconds
        
    """

    ID: str = Field("canTransferOwnershipResultSessionTooFresh", alias="@type")
    retry_after: int

    @staticmethod
    def read(q: dict) -> CanTransferOwnershipResultSessionTooFresh:
        return CanTransferOwnershipResultSessionTooFresh.construct(**q)
