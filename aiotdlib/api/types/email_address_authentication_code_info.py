# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class EmailAddressAuthenticationCodeInfo(BaseObject):
    """
    Information about the email address authentication code that was sent
    
    Params:
        email_address_pattern (:class:`str`)
            Pattern of the email address to which an authentication code was sent
        
        length (:class:`int`)
            Length of the code; 0 if unknown
        
    """

    ID: str = Field("emailAddressAuthenticationCodeInfo", alias="@type")
    email_address_pattern: str
    length: int

    @staticmethod
    def read(q: dict) -> EmailAddressAuthenticationCodeInfo:
        return EmailAddressAuthenticationCodeInfo.construct(**q)
