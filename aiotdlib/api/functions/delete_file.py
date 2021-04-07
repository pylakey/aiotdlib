# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteFile(BaseObject):
    """
    Deletes a file from the TDLib file cache
    
    Params:
        file_id (:class:`int`)
            Identifier of the file to delete
        
    """

    ID: str = Field("deleteFile", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> DeleteFile:
        return DeleteFile.construct(**q)
