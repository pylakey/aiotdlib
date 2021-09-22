# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .passport_element_type import PassportElementType
from ..base_object import BaseObject


class PassportSuitableElement(BaseObject):
    """
    Contains information about a Telegram Passport element that was requested by a service
    
    :param type_: Type of the element
    :type type_: :class:`PassportElementType`
    
    :param is_selfie_required: True, if a selfie is required with the identity document
    :type is_selfie_required: :class:`bool`
    
    :param is_translation_required: True, if a certified English translation is required with the document
    :type is_translation_required: :class:`bool`
    
    :param is_native_name_required: True, if personal details must include the user's name in the language of their country of residence
    :type is_native_name_required: :class:`bool`
    
    """

    ID: str = Field("passportSuitableElement", alias="@type")
    type_: PassportElementType = Field(..., alias='type')
    is_selfie_required: bool
    is_translation_required: bool
    is_native_name_required: bool

    @staticmethod
    def read(q: dict) -> PassportSuitableElement:
        return PassportSuitableElement.construct(**q)
