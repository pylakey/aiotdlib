# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .date import Date
from ..base_object import BaseObject


class PersonalDetails(BaseObject):
    """
    Contains the user's personal details
    
    :param first_name: First name of the user written in English; 1-255 characters
    :type first_name: :class:`str`
    
    :param middle_name: Middle name of the user written in English; 0-255 characters, defaults to None
    :type middle_name: :class:`str`, optional
    
    :param last_name: Last name of the user written in English; 1-255 characters
    :type last_name: :class:`str`
    
    :param native_first_name: Native first name of the user; 1-255 characters
    :type native_first_name: :class:`str`
    
    :param native_middle_name: Native middle name of the user; 0-255 characters, defaults to None
    :type native_middle_name: :class:`str`, optional
    
    :param native_last_name: Native last name of the user; 1-255 characters
    :type native_last_name: :class:`str`
    
    :param birthdate: Birthdate of the user
    :type birthdate: :class:`Date`
    
    :param gender: Gender of the user, "male" or "female"
    :type gender: :class:`str`
    
    :param country_code: A two-letter ISO 3166-1 alpha-2 country code of the user's country
    :type country_code: :class:`str`
    
    :param residence_country_code: A two-letter ISO 3166-1 alpha-2 country code of the user's residence country
    :type residence_country_code: :class:`str`
    
    """

    ID: str = Field("personalDetails", alias="@type")
    first_name: str = Field(..., min_length=1, max_length=255)
    middle_name: typing.Optional[str] = Field(None, max_length=255)
    last_name: str = Field(..., min_length=1, max_length=255)
    native_first_name: str = Field(..., min_length=1, max_length=255)
    native_middle_name: typing.Optional[str] = Field(None, max_length=255)
    native_last_name: str = Field(..., min_length=1, max_length=255)
    birthdate: Date
    gender: str
    country_code: str
    residence_country_code: str

    @staticmethod
    def read(q: dict) -> PersonalDetails:
        return PersonalDetails.construct(**q)
