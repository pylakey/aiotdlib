# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteSavedCredentials(BaseObject):
    """
    Deletes saved credentials for all payment provider bots
    
    """

    ID: str = Field("deleteSavedCredentials", alias="@type")

    @staticmethod
    def read(q: dict) -> DeleteSavedCredentials:
        return DeleteSavedCredentials.construct(**q)
