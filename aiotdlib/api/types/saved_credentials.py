# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SavedCredentials(BaseObject):
    """
    Contains information about saved card credentials
    
    Params:
        id (:class:`str`)
            Unique identifier of the saved credentials
        
        title (:class:`str`)
            Title of the saved credentials
        
    """

    ID: str = Field("savedCredentials", alias="@type")
    id: str
    title: str

    @staticmethod
    def read(q: dict) -> SavedCredentials:
        return SavedCredentials.construct(**q)
