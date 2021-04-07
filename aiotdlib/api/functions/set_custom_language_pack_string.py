# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import LanguagePackString


class SetCustomLanguagePackString(BaseObject):
    """
    Adds, edits or deletes a string in a custom local language pack. Can be called before authorization
    
    Params:
        language_pack_id (:class:`str`)
            Identifier of a previously added custom local language pack in the current localization target
        
        new_string (:class:`LanguagePackString`)
            New language pack string
        
    """

    ID: str = Field("setCustomLanguagePackString", alias="@type")
    language_pack_id: str
    new_string: LanguagePackString

    @staticmethod
    def read(q: dict) -> SetCustomLanguagePackString:
        return SetCustomLanguagePackString.construct(**q)
