# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchUserByPhoneNumber(BaseObject):
    """
    Searches a user by their phone number. Returns a 404 error if the user can't be found

    :param phone_number: Phone number to search for
    :type phone_number: :class:`String`
    """

    ID: typing.Literal["searchUserByPhoneNumber"] = "searchUserByPhoneNumber"
    phone_number: String
