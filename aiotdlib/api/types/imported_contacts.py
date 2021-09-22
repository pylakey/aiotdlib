# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ImportedContacts(BaseObject):
    """
    Represents the result of an ImportContacts request
    
    :param user_ids: User identifiers of the imported contacts in the same order as they were specified in the request; 0 if the contact is not yet a registered user
    :type user_ids: :class:`list[int]`
    
    :param importer_count: The number of users that imported the corresponding contact; 0 for already registered users or if unavailable
    :type importer_count: :class:`list[int]`
    
    """

    ID: str = Field("importedContacts", alias="@type")
    user_ids: list[int]
    importer_count: list[int]

    @staticmethod
    def read(q: dict) -> ImportedContacts:
        return ImportedContacts.construct(**q)
