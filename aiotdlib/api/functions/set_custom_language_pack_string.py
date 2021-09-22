# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import LanguagePackString
from ..base_object import BaseObject


class SetCustomLanguagePackString(BaseObject):
    """
    Adds, edits or deletes a string in a custom local language pack. Can be called before authorization
    
    :param language_pack_id: Identifier of a previously added custom local language pack in the current localization target
    :type language_pack_id: :class:`str`
    
    :param new_string: New language pack string
    :type new_string: :class:`LanguagePackString`
    
    """

    ID: str = Field("setCustomLanguagePackString", alias="@type")
    language_pack_id: str
    new_string: LanguagePackString

    @staticmethod
    def read(q: dict) -> SetCustomLanguagePackString:
        return SetCustomLanguagePackString.construct(**q)
