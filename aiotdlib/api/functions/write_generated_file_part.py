# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class WriteGeneratedFilePart(BaseObject):
    """
    Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file
    
    Params:
        generation_id (:class:`int`)
            The identifier of the generation process
        
        offset (:class:`int`)
            The offset from which to write the data to the file
        
        data (:class:`str`)
            The data to write
        
    """

    ID: str = Field("writeGeneratedFilePart", alias="@type")
    generation_id: int
    offset: int
    data: str

    @staticmethod
    def read(q: dict) -> WriteGeneratedFilePart:
        return WriteGeneratedFilePart.construct(**q)
