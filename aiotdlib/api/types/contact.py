# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Contact(BaseObject):
    """
    Describes a user contact
    
    Params:
        phone_number (:class:`str`)
            Phone number of the user
        
        first_name (:class:`str`)
            First name of the user; 1-255 characters in length
        
        last_name (:class:`str`)
            Last name of the user
        
        vcard (:class:`str`)
            Additional data about the user in a form of vCard; 0-2048 bytes in length
        
        user_id (:class:`int`)
            Identifier of the user, if known; otherwise 0
        
    """

    ID: str = Field("contact", alias="@type")
    phone_number: str
    first_name: str = Field(..., min_length=1, max_length=255)
    last_name: str
    vcard: str
    user_id: int

    @staticmethod
    def read(q: dict) -> Contact:
        return Contact.construct(**q)
