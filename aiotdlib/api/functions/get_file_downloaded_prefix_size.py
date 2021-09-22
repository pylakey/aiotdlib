# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetFileDownloadedPrefixSize(BaseObject):
    """
    Returns file downloaded prefix size from a given offset, in bytes
    
    :param file_id: Identifier of the file
    :type file_id: :class:`int`
    
    :param offset: Offset from which downloaded prefix size should be calculated
    :type offset: :class:`int`
    
    """

    ID: str = Field("getFileDownloadedPrefixSize", alias="@type")
    file_id: int
    offset: int

    @staticmethod
    def read(q: dict) -> GetFileDownloadedPrefixSize:
        return GetFileDownloadedPrefixSize.construct(**q)
