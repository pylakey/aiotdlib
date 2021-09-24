# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ClearImportedContacts(BaseObject):
    """
    Clears all imported contacts, contact list remains unchanged
    
    """

    ID: str = Field("clearImportedContacts", alias="@type")

    @staticmethod
    def read(q: dict) -> ClearImportedContacts:
        return ClearImportedContacts.construct(**q)
