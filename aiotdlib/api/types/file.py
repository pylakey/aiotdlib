# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .local_file import LocalFile
from .remote_file import RemoteFile
from ..base_object import BaseObject


class File(BaseObject):
    """
    Represents a file
    
    Params:
        id (:class:`int`)
            Unique file identifier
        
        size (:class:`int`)
            File size; 0 if unknown
        
        expected_size (:class:`int`)
            Expected file size in case the exact file size is unknown, but an approximate size is known. Can be used to show download/upload progress
        
        local (:class:`LocalFile`)
            Information about the local copy of the file
        
        remote (:class:`RemoteFile`)
            Information about the remote copy of the file
        
    """

    ID: str = Field("file", alias="@type")
    id: int
    size: int
    expected_size: int
    local: LocalFile
    remote: RemoteFile

    @staticmethod
    def read(q: dict) -> File:
        return File.construct(**q)
