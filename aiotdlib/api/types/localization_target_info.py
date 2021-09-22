# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .language_pack_info import LanguagePackInfo
from ..base_object import BaseObject


class LocalizationTargetInfo(BaseObject):
    """
    Contains information about the current localization target
    
    :param language_packs: List of available language packs for this application
    :type language_packs: :class:`list[LanguagePackInfo]`
    
    """

    ID: str = Field("localizationTargetInfo", alias="@type")
    language_packs: list[LanguagePackInfo]

    @staticmethod
    def read(q: dict) -> LocalizationTargetInfo:
        return LocalizationTargetInfo.construct(**q)
