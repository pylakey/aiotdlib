# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .downloaded_file_counts import DownloadedFileCounts
from .file_download import FileDownload
from ..base_object import BaseObject


class FoundFileDownloads(BaseObject):
    """
    Contains a list of downloaded files, found by a search
    
    :param total_counts: Total number of suitable files, ignoring offset
    :type total_counts: :class:`DownloadedFileCounts`
    
    :param files: The list of files
    :type files: :class:`list[FileDownload]`
    
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`str`
    
    """

    ID: str = Field("foundFileDownloads", alias="@type")
    total_counts: DownloadedFileCounts
    files: list[FileDownload]
    next_offset: str

    @staticmethod
    def read(q: dict) -> FoundFileDownloads:
        return FoundFileDownloads.construct(**q)
