# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetContacts(BaseObject):
    """
    Returns all user contacts
    
    """

    ID: str = Field("getContacts", alias="@type")

    @staticmethod
    def read(q: dict) -> GetContacts:
        return GetContacts.construct(**q)
