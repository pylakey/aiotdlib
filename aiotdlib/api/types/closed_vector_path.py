# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .vector_path_command import VectorPathCommand
from ..base_object import BaseObject


class ClosedVectorPath(BaseObject):
    """
    Represents a closed vector path. The path begins at the end point of the last command
    
    Params:
        commands (:obj:`list[VectorPathCommand]`)
            List of vector path commands
        
    """

    ID: str = Field("closedVectorPath", alias="@type")
    commands: list[VectorPathCommand]

    @staticmethod
    def read(q: dict) -> ClosedVectorPath:
        return ClosedVectorPath.construct(**q)
