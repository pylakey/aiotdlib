# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ImportedContacts(BaseObject):
    """
    Represents the result of an ImportContacts request
    
    Params:
        user_ids (:obj:`list[int]`)
            User identifiers of the imported contacts in the same order as they were specified in the request; 0 if the contact is not yet a registered user
        
        importer_count (:obj:`list[int]`)
            The number of users that imported the corresponding contact; 0 for already registered users or if unavailable
        
    """

    ID: str = Field("importedContacts", alias="@type")
    user_ids: list[int]
    importer_count: list[int]

    @staticmethod
    def read(q: dict) -> ImportedContacts:
        return ImportedContacts.construct(**q)
