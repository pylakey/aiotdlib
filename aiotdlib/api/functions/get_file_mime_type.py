# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetFileMimeType(BaseObject):
    """
    Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously
    
    Params:
        file_name (:class:`str`)
            The name of the file or path to the file
        
    """

    ID: str = Field("getFileMimeType", alias="@type")
    file_name: str

    @staticmethod
    def read(q: dict) -> GetFileMimeType:
        return GetFileMimeType.construct(**q)
