# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SharePhoneNumber(BaseObject):
    """
    Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber
    
    :param user_id: Identifier of the user with whom to share the phone number. The user must be a mutual contact
    :type user_id: :class:`int`
    
    """

    ID: str = Field("sharePhoneNumber", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> SharePhoneNumber:
        return SharePhoneNumber.construct(**q)
