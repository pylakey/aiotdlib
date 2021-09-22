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


class ImportContacts(BaseObject):
    """
    Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored
    
    :param contacts: The list of contacts to import or edit; contacts' vCard are ignored and are not imported
    :type contacts: :class:`list[Contact]`
    
    """

    ID: str = Field("importContacts", alias="@type")
    contacts: list[Contact]

    @staticmethod
    def read(q: dict) -> ImportContacts:
        return ImportContacts.construct(**q)
