# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class FileDownloadedPrefixSize(BaseObject):
    """
    Contains size of downloaded prefix of a file
    
    :param size: The prefix size, in bytes
    :type size: :class:`int`
    
    """

    ID: str = Field("fileDownloadedPrefixSize", alias="@type")
    size: int

    @staticmethod
    def read(q: dict) -> FileDownloadedPrefixSize:
        return FileDownloadedPrefixSize.construct(**q)
