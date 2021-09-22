# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputFile
from ..base_object import BaseObject


class RemoveSavedAnimation(BaseObject):
    """
    Removes an animation from the list of saved animations
    
    :param animation: Animation file to be removed
    :type animation: :class:`InputFile`
    
    """

    ID: str = Field("removeSavedAnimation", alias="@type")
    animation: InputFile

    @staticmethod
    def read(q: dict) -> RemoveSavedAnimation:
        return RemoveSavedAnimation.construct(**q)
