# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DownloadedFileCounts(BaseObject):
    """
    Contains number of being downloaded and recently downloaded files found
    
    :param active_count: Number of active file downloads found, including paused
    :type active_count: :class:`int`
    
    :param paused_count: Number of paused file downloads found
    :type paused_count: :class:`int`
    
    :param completed_count: Number of completed file downloads found
    :type completed_count: :class:`int`
    
    """

    ID: str = Field("downloadedFileCounts", alias="@type")
    active_count: int
    paused_count: int
    completed_count: int

    @staticmethod
    def read(q: dict) -> DownloadedFileCounts:
        return DownloadedFileCounts.construct(**q)
