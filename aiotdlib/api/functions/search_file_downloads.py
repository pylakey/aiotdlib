# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchFileDownloads(BaseObject):
    """
    Searches for files in the file download list or recently downloaded files from the list
    
    :param query: Query to search for; may be empty to return all downloaded files
    :type query: :class:`str`
    
    :param only_active: Pass true to search only for active downloads, including paused
    :type only_active: :class:`bool`
    
    :param only_completed: Pass true to search only for completed downloads
    :type only_completed: :class:`bool`
    
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`str`
    
    :param limit: The maximum number of files to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchFileDownloads", alias="@type")
    query: str
    only_active: bool
    only_completed: bool
    offset: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchFileDownloads:
        return SearchFileDownloads.construct(**q)
