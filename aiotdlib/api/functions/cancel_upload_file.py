# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CancelUploadFile(BaseObject):
    """
    Stops the uploading of a file. Supported only for files uploaded by using uploadFile. For other files the behavior is undefined
    
    Params:
        file_id (:class:`int`)
            Identifier of the file to stop uploading
        
    """

    ID: str = Field("cancelUploadFile", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> CancelUploadFile:
        return CancelUploadFile.construct(**q)
