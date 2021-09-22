# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class EmailAddressAuthenticationCodeInfo(BaseObject):
    """
    Information about the email address authentication code that was sent
    
    :param email_address_pattern: Pattern of the email address to which an authentication code was sent
    :type email_address_pattern: :class:`str`
    
    :param length: Length of the code; 0 if unknown
    :type length: :class:`int`
    
    """

    ID: str = Field("emailAddressAuthenticationCodeInfo", alias="@type")
    email_address_pattern: str
    length: int

    @staticmethod
    def read(q: dict) -> EmailAddressAuthenticationCodeInfo:
        return EmailAddressAuthenticationCodeInfo.construct(**q)
