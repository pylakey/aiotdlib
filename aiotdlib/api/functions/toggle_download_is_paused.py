# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleDownloadIsPaused(BaseObject):
    """
    Changes pause state of a file in the file download list
    
    :param file_id: Identifier of the downloaded file
    :type file_id: :class:`int`
    
    :param is_paused: Pass true if the download is paused
    :type is_paused: :class:`bool`
    
    """

    ID: str = Field("toggleDownloadIsPaused", alias="@type")
    file_id: int
    is_paused: bool

    @staticmethod
    def read(q: dict) -> ToggleDownloadIsPaused:
        return ToggleDownloadIsPaused.construct(**q)
