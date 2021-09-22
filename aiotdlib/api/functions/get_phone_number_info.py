# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetPhoneNumberInfo(BaseObject):
    """
    Returns information about a phone number by its prefix. Can be called before authorization
    
    :param phone_number_prefix: The phone number prefix
    :type phone_number_prefix: :class:`str`
    
    """

    ID: str = Field("getPhoneNumberInfo", alias="@type")
    phone_number_prefix: str

    @staticmethod
    def read(q: dict) -> GetPhoneNumberInfo:
        return GetPhoneNumberInfo.construct(**q)
