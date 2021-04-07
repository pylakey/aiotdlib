# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetFileGenerationProgress(BaseObject):
    """
    Informs TDLib on a file generation progress
    
    Params:
        generation_id (:class:`int`)
            The identifier of the generation process
        
        expected_size (:class:`int`)
            Expected size of the generated file, in bytes; 0 if unknown
        
        local_prefix_size (:class:`int`)
            The number of bytes already generated
        
    """

    ID: str = Field("setFileGenerationProgress", alias="@type")
    generation_id: int
    expected_size: int
    local_prefix_size: int

    @staticmethod
    def read(q: dict) -> SetFileGenerationProgress:
        return SetFileGenerationProgress.construct(**q)
