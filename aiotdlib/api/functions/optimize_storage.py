# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import FileType
from ..base_object import BaseObject


class OptimizeStorage(BaseObject):
    """
    Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted
    
    :param size: Limit on the total size of files after deletion, in bytes. Pass -1 to use the default limit
    :type size: :class:`int`
    
    :param ttl: Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit
    :type ttl: :class:`int`
    
    :param count: Limit on the total count of files after deletion. Pass -1 to use the default limit
    :type count: :class:`int`
    
    :param immunity_delay: The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value
    :type immunity_delay: :class:`int`
    
    :param file_types: If not empty, only files with the given type(s) are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
    :type file_types: :class:`list[FileType]`
    
    :param chat_ids: If not empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)
    :type chat_ids: :class:`list[int]`
    
    :param exclude_chat_ids: If not empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)
    :type exclude_chat_ids: :class:`list[int]`
    
    :param return_deleted_file_statistics: Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics
    :type return_deleted_file_statistics: :class:`bool`
    
    :param chat_limit: Same as in getStorageStatistics. Affects only returned statistics
    :type chat_limit: :class:`int`
    
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
