# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetBotUpdatesStatus(BaseObject):
    """
    Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only
    
    :param pending_update_count: The number of pending updates
    :type pending_update_count: :class:`int`
    
    :param error_message: The last error message
    :type error_message: :class:`str`
    
    """

    ID: str = Field("setBotUpdatesStatus", alias="@type")
    pending_update_count: int
    error_message: str

    @staticmethod
    def read(q: dict) -> SetBotUpdatesStatus:
        return SetBotUpdatesStatus.construct(**q)
