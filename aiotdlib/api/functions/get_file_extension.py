# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetFileExtension(BaseObject):
    """
    Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously
    
    Params:
        mime_type (:class:`str`)
            The MIME type of the file
        
    """

    ID: str = Field("getFileExtension", alias="@type")
    mime_type: str

    @staticmethod
    def read(q: dict) -> GetFileExtension:
        return GetFileExtension.construct(**q)
