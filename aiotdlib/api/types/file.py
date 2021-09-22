# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .local_file import LocalFile
from .remote_file import RemoteFile
from ..base_object import BaseObject


class File(BaseObject):
    """
    Represents a file
    
    :param id: Unique file identifier
    :type id: :class:`int`
    
    :param size: File size, in bytes; 0 if unknown
    :type size: :class:`int`
    
    :param expected_size: Approximate file size in bytes in case the exact file size is unknown. Can be used to show download/upload progress
    :type expected_size: :class:`int`
    
    :param local: Information about the local copy of the file
    :type local: :class:`LocalFile`
    
    :param remote: Information about the remote copy of the file
    :type remote: :class:`RemoteFile`
    
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
