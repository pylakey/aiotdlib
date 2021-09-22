# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RemoveContacts(BaseObject):
    """
    Removes users from the contact list
    
    :param user_ids: Identifiers of users to be deleted
    :type user_ids: :class:`list[int]`
    
    """

    ID: str = Field("removeContacts", alias="@type")
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> RemoveContacts:
        return RemoveContacts.construct(**q)
