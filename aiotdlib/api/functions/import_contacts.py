# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Contact


class ImportContacts(BaseObject):
    """
    Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored
    
    Params:
        contacts (:obj:`list[Contact]`)
            The list of contacts to import or edit; contacts' vCard are ignored and are not imported
        
    """

    ID: str = Field("importContacts", alias="@type")
    contacts: list[Contact]

    @staticmethod
    def read(q: dict) -> ImportContacts:
        return ImportContacts.construct(**q)
