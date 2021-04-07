# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LanguagePackInfo(BaseObject):
    """
    Contains information about a language pack
    
    Params:
        id (:class:`str`)
            Unique language pack identifier
        
        base_language_pack_id (:class:`str`)
            Identifier of a base language pack; may be empty. If a string is missed in the language pack, then it should be fetched from base language pack. Unsupported in custom language packs
        
        name (:class:`str`)
            Language name
        
        native_name (:class:`str`)
            Name of the language in that language
        
        plural_code (:class:`str`)
            A language code to be used to apply plural forms. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info
        
        is_official (:class:`bool`)
            True, if the language pack is official
        
        is_rtl (:class:`bool`)
            True, if the language pack strings are RTL
        
        is_beta (:class:`bool`)
            True, if the language pack is a beta language pack
        
        is_installed (:class:`bool`)
            True, if the language pack is installed by the current user
        
        total_string_count (:class:`int`)
            Total number of non-deleted strings from the language pack
        
        translated_string_count (:class:`int`)
            Total number of translated strings from the language pack
        
        local_string_count (:class:`int`)
            Total number of non-deleted strings from the language pack available locally
        
        translation_url (:class:`str`)
            Link to language translation interface; empty for custom local language packs
        
    """

    ID: str = Field("languagePackInfo", alias="@type")
    id: str
    base_language_pack_id: str
    name: str
    native_name: str
    plural_code: str
    is_official: bool
    is_rtl: bool
    is_beta: bool
    is_installed: bool
    total_string_count: int
    translated_string_count: int
    local_string_count: int
    translation_url: str

    @staticmethod
    def read(q: dict) -> LanguagePackInfo:
        return LanguagePackInfo.construct(**q)
