# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Contact


class ChangeImportedContacts(BaseObject):
    """
    Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts. Query result depends on the result of the previous query, so only one query is possible at the same time
    
    Params:
        contacts (:obj:`list[Contact]`)
            The new list of contacts, contact's vCard are ignored and are not imported
        
    """

    ID: str = Field("changeImportedContacts", alias="@type")
    contacts: list[Contact]

    @staticmethod
    def read(q: dict) -> ChangeImportedContacts:
        return ChangeImportedContacts.construct(**q)
