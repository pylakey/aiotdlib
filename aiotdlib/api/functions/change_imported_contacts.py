# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import Contact
from ..base_object import BaseObject


class ChangeImportedContacts(BaseObject):
    """
    Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts. Query result depends on the result of the previous query, so only one query is possible at the same time
    
    :param contacts: The new list of contacts, contact's vCard are ignored and are not imported
    :type contacts: :class:`list[Contact]`
    
    """

    ID: str = Field("changeImportedContacts", alias="@type")
    contacts: list[Contact]

    @staticmethod
    def read(q: dict) -> ChangeImportedContacts:
        return ChangeImportedContacts.construct(**q)
