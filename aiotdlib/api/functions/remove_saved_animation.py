# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class RemoveSavedAnimation(BaseObject):
    """
    Removes an animation from the list of saved animations
    
    Params:
        animation (:class:`InputFile`)
            Animation file to be removed
        
    """

    ID: str = Field("removeSavedAnimation", alias="@type")
    animation: InputFile

    @staticmethod
    def read(q: dict) -> RemoveSavedAnimation:
        return RemoveSavedAnimation.construct(**q)
