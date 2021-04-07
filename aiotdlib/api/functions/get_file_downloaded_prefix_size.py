# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetFileDownloadedPrefixSize(BaseObject):
    """
    Returns file downloaded prefix size from a given offset
    
    Params:
        file_id (:class:`int`)
            Identifier of the file
        
        offset (:class:`int`)
            Offset from which downloaded prefix size should be calculated
        
    """

    ID: str = Field("getFileDownloadedPrefixSize", alias="@type")
    file_id: int
    offset: int

    @staticmethod
    def read(q: dict) -> GetFileDownloadedPrefixSize:
        return GetFileDownloadedPrefixSize.construct(**q)
