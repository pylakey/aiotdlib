# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .file_type import FileType
from ..base_object import BaseObject


class StorageStatisticsByFileType(BaseObject):
    """
    Contains the storage usage statistics for a specific file type
    
    Params:
        file_type (:class:`FileType`)
            File type
        
        size (:class:`int`)
            Total size of the files
        
        count (:class:`int`)
            Total number of files
        
    """

    ID: str = Field("storageStatisticsByFileType", alias="@type")
    file_type: FileType
    size: int
    count: int

    @staticmethod
    def read(q: dict) -> StorageStatisticsByFileType:
        return StorageStatisticsByFileType.construct(**q)
