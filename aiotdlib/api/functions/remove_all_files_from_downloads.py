# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveAllFilesFromDownloads(BaseObject):
    """
    Removes all files from the file download list
    
    :param only_active: Pass true to remove only active downloads, including paused
    :type only_active: :class:`bool`
    
    :param only_completed: Pass true to remove only completed downloads
    :type only_completed: :class:`bool`
    
    :param delete_from_cache: Pass true to delete the file from the TDLib file cache
    :type delete_from_cache: :class:`bool`
    
    """

    ID: str = Field("removeAllFilesFromDownloads", alias="@type")
    only_active: bool
    only_completed: bool
    delete_from_cache: bool

    @staticmethod
    def read(q: dict) -> RemoveAllFilesFromDownloads:
        return RemoveAllFilesFromDownloads.construct(**q)
