# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import CallProtocol


class CreateCall(BaseObject):
    """
    Creates a new call
    
    Params:
        user_id (:class:`int`)
            Identifier of the user to be called
        
        protocol (:class:`CallProtocol`)
            Description of the call protocols supported by the application
        
        is_video (:class:`bool`)
            True, if a video call needs to be created
        
    """

    ID: str = Field("createCall", alias="@type")
    user_id: int
    protocol: CallProtocol
    is_video: bool

    @staticmethod
    def read(q: dict) -> CreateCall:
        return CreateCall.construct(**q)
