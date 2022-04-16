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
    
    :param user_id: Identifier of the user to be called
    :type user_id: :class:`int`
    
    :param protocol: The call protocols supported by the application
    :type protocol: :class:`CallProtocol`
    
    :param is_video: Pass true to create a video call
    :type is_video: :class:`bool`
    
    """

    ID: str = Field("createCall", alias="@type")
    user_id: int
    protocol: CallProtocol
    is_video: bool

    @staticmethod
    def read(q: dict) -> CreateCall:
        return CreateCall.construct(**q)
