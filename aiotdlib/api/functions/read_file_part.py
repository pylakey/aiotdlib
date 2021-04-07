# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReadFilePart(BaseObject):
    """
    Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file
    
    Params:
        file_id (:class:`int`)
            Identifier of the file. The file must be located in the TDLib file cache
        
        offset (:class:`int`)
            The offset from which to read the file
        
        count (:class:`int`)
            Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position
        
    """

    ID: str = Field("readFilePart", alias="@type")
    file_id: int
    offset: int
    count: int

    @staticmethod
    def read(q: dict) -> ReadFilePart:
        return ReadFilePart.construct(**q)
