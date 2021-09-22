# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file_type import FileType
from ..base_object import BaseObject


class StorageStatisticsByFileType(BaseObject):
    """
    Contains the storage usage statistics for a specific file type
    
    :param file_type: File type
    :type file_type: :class:`FileType`
    
    :param size: Total size of the files, in bytes
    :type size: :class:`int`
    
    :param count: Total number of files
    :type count: :class:`int`
    
    """

    ID: str = Field("storageStatisticsByFileType", alias="@type")
    file_type: FileType
    size: int
    count: int

    @staticmethod
    def read(q: dict) -> StorageStatisticsByFileType:
        return StorageStatisticsByFileType.construct(**q)
