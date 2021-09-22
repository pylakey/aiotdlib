# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Contact(BaseObject):
    """
    Describes a user contact
    
    :param phone_number: Phone number of the user
    :type phone_number: :class:`str`
    
    :param first_name: First name of the user; 1-255 characters in length
    :type first_name: :class:`str`
    
    :param last_name: Last name of the user
    :type last_name: :class:`str`
    
    :param vcard: Additional data about the user in a form of vCard; 0-2048 bytes in length
    :type vcard: :class:`str`
    
    :param user_id: Identifier of the user, if known; otherwise 0
    :type user_id: :class:`int`
    
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
