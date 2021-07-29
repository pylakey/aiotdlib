# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSuggestedFileName(BaseObject):
    """
    Returns suggested name for saving a file in a given directory
    
    Params:
        file_id (:class:`int`)
            Identifier of the file
        
        directory (:class:`str`)
            Directory in which the file is supposed to be saved
        
    """

    ID: str = Field("getSuggestedFileName", alias="@type")
    file_id: int
    directory: str

    @staticmethod
    def read(q: dict) -> GetSuggestedFileName:
        return GetSuggestedFileName.construct(**q)
