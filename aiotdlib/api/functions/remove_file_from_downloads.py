# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveFileFromDownloads(BaseObject):
    """
    Removes a file from the file download list
    
    :param file_id: Identifier of the downloaded file
    :type file_id: :class:`int`
    
    :param delete_from_cache: Pass true to delete the file from the TDLib file cache
    :type delete_from_cache: :class:`bool`
    
    """

    ID: str = Field("removeFileFromDownloads", alias="@type")
    file_id: int
    delete_from_cache: bool

    @staticmethod
    def read(q: dict) -> RemoveFileFromDownloads:
        return RemoveFileFromDownloads.construct(**q)
