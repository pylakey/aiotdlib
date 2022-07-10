# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchUserByPhoneNumber(BaseObject):
    """
    Searches a user by their phone number. Returns a 404 error if the user can't be found
    
    :param phone_number: Phone number to search for
    :type phone_number: :class:`str`
    
    """

    ID: str = Field("searchUserByPhoneNumber", alias="@type")
    phone_number: str

    @staticmethod
    def read(q: dict) -> SearchUserByPhoneNumber:
        return SearchUserByPhoneNumber.construct(**q)
