# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class LanguagePackInfo(BaseObject):
    """
    Contains information about a language pack
    
    :param id: Unique language pack identifier
    :type id: :class:`str`
    
    :param base_language_pack_id: Identifier of a base language pack; may be empty. If a string is missed in the language pack, then it should be fetched from base language pack. Unsupported in custom language packs
    :type base_language_pack_id: :class:`str`
    
    :param name: Language name
    :type name: :class:`str`
    
    :param native_name: Name of the language in that language
    :type native_name: :class:`str`
    
    :param plural_code: A language code to be used to apply plural forms. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info
    :type plural_code: :class:`str`
    
    :param is_official: True, if the language pack is official
    :type is_official: :class:`bool`
    
    :param is_rtl: True, if the language pack strings are RTL
    :type is_rtl: :class:`bool`
    
    :param is_beta: True, if the language pack is a beta language pack
    :type is_beta: :class:`bool`
    
    :param is_installed: True, if the language pack is installed by the current user
    :type is_installed: :class:`bool`
    
    :param total_string_count: Total number of non-deleted strings from the language pack
    :type total_string_count: :class:`int`
    
    :param translated_string_count: Total number of translated strings from the language pack
    :type translated_string_count: :class:`int`
    
    :param local_string_count: Total number of non-deleted strings from the language pack available locally
    :type local_string_count: :class:`int`
    
    :param translation_url: Link to language translation interface; empty for custom local language packs
    :type translation_url: :class:`str`
    
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
