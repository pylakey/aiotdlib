# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetFile(BaseObject):
    """
    Returns information about a file; this is an offline request
    
    Params:
        file_id (:class:`int`)
            Identifier of the file to get
        
    """

    ID: str = Field("getFile", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> GetFile:
        return GetFile.construct(**q)
