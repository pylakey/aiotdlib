# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetActiveLiveLocationMessages(BaseObject):
    """
    Returns all active live locations that should be updated by the application. The list is persistent across application restarts only if the message database is used
    
    """

    ID: str = Field("getActiveLiveLocationMessages", alias="@type")

    @staticmethod
    def read(q: dict) -> GetActiveLiveLocationMessages:
        return GetActiveLiveLocationMessages.construct(**q)
