# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import Error
from ..base_object import BaseObject


class FinishFileGeneration(BaseObject):
    """
    Finishes the file generation
    
    :param generation_id: The identifier of the generation process
    :type generation_id: :class:`int`
    
    :param error: If set, means that file generation has failed and should be terminated
    :type error: :class:`Error`
    
    """

    ID: str = Field("finishFileGeneration", alias="@type")
    generation_id: int
    error: Error

    @staticmethod
    def read(q: dict) -> FinishFileGeneration:
        return FinishFileGeneration.construct(**q)
