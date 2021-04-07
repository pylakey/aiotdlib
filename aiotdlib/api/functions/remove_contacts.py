# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RemoveContacts(BaseObject):
    """
    Removes users from the contact list
    
    Params:
        user_ids (:obj:`list[int]`)
            Identifiers of users to be deleted
        
    """

    ID: str = Field("removeContacts", alias="@type")
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> RemoveContacts:
        return RemoveContacts.construct(**q)
