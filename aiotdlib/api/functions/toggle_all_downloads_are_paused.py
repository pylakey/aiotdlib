# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleAllDownloadsArePaused(BaseObject):
    """
    Changes pause state of all files in the file download list
    
    :param are_paused: Pass true to pause all downloads; pass false to unpause them
    :type are_paused: :class:`bool`
    
    """

    ID: str = Field("toggleAllDownloadsArePaused", alias="@type")
    are_paused: bool

    @staticmethod
    def read(q: dict) -> ToggleAllDownloadsArePaused:
        return ToggleAllDownloadsArePaused.construct(**q)
