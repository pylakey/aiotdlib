# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetFileGenerationProgress(BaseObject):
    """
    Informs TDLib on a file generation progress
    
    :param generation_id: The identifier of the generation process
    :type generation_id: :class:`int`
    
    :param expected_size: Expected size of the generated file, in bytes; 0 if unknown
    :type expected_size: :class:`int`
    
    :param local_prefix_size: The number of bytes already generated
    :type local_prefix_size: :class:`int`
    
    """

    ID: str = Field("setFileGenerationProgress", alias="@type")
    generation_id: int
    expected_size: int
    local_prefix_size: int

    @staticmethod
    def read(q: dict) -> SetFileGenerationProgress:
        return SetFileGenerationProgress.construct(**q)
