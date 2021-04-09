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
    
    Params:
        first_name (:class:`str`)
            First name of the user written in English; 1-255 characters
        
        middle_name (:class:`str`)
            Middle name of the user written in English; 0-255 characters
        
        last_name (:class:`str`)
            Last name of the user written in English; 1-255 characters
        
        native_first_name (:class:`str`)
            Native first name of the user; 1-255 characters
        
        native_middle_name (:class:`str`)
            Native middle name of the user; 0-255 characters
        
        native_last_name (:class:`str`)
            Native last name of the user; 1-255 characters
        
        birthdate (:class:`Date`)
            Birthdate of the user
        
        gender (:class:`str`)
            Gender of the user, "male" or "female"
        
        country_code (:class:`str`)
            A two-letter ISO 3166-1 alpha-2 country code of the user's country
        
        residence_country_code (:class:`str`)
            A two-letter ISO 3166-1 alpha-2 country code of the user's residence country
        
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
