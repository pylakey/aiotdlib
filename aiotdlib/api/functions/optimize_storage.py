# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import FileType


class OptimizeStorage(BaseObject):
    """
    Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted
    
    Params:
        size (:class:`int`)
            Limit on the total size of files after deletion. Pass -1 to use the default limit
        
        ttl (:class:`int`)
            Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit
        
        count (:class:`int`)
            Limit on the total count of files after deletion. Pass -1 to use the default limit
        
        immunity_delay (:class:`int`)
            The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value
        
        file_types (:obj:`list[FileType]`)
            If not empty, only files with the given type(s) are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
        
        chat_ids (:obj:`list[int]`)
            If not empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)
        
        exclude_chat_ids (:obj:`list[int]`)
            If not empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)
        
        return_deleted_file_statistics (:class:`bool`)
            Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics
        
        chat_limit (:class:`int`)
            Same as in getStorageStatistics. Affects only returned statistics
        
    """

    ID: str = Field("optimizeStorage", alias="@type")
    size: int
    ttl: int
    count: int
    immunity_delay: int
    file_types: list[FileType]
    chat_ids: list[int]
    exclude_chat_ids: list[int]
    return_deleted_file_statistics: bool
    chat_limit: int

    @staticmethod
    def read(q: dict) -> OptimizeStorage:
        return OptimizeStorage.construct(**q)
