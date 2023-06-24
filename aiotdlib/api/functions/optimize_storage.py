# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    FileType,
)


class OptimizeStorage(BaseObject):
    """
    Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted

    :param size: Limit on the total size of files after deletion, in bytes. Pass -1 to use the default limit
    :type size: :class:`Int53`
    :param ttl: Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit
    :type ttl: :class:`Int32`
    :param count: Limit on the total number of files after deletion. Pass -1 to use the default limit
    :type count: :class:`Int32`
    :param immunity_delay: The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value
    :type immunity_delay: :class:`Int32`
    :param file_types: If non-empty, only files with the given types are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
    :type file_types: :class:`Vector[FileType]`
    :param chat_ids: If non-empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)
    :type chat_ids: :class:`Vector[Int53]`
    :param exclude_chat_ids: If non-empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)
    :type exclude_chat_ids: :class:`Vector[Int53]`
    :param chat_limit: Same as in getStorageStatistics. Affects only returned statistics
    :type chat_limit: :class:`Int32`
    :param return_deleted_file_statistics: Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics
    :type return_deleted_file_statistics: :class:`Bool`
    """

    ID: typing.Literal["optimizeStorage"] = "optimizeStorage"
    size: Int53
    ttl: Int32
    count: Int32
    immunity_delay: Int32
    file_types: Vector[FileType]
    chat_ids: Vector[Int53]
    exclude_chat_ids: Vector[Int53]
    chat_limit: Int32
    return_deleted_file_statistics: Bool = False
