# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetLanguagePackInfo(BaseObject):
    """
    Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization
    
    :param language_pack_id: Language pack identifier
    :type language_pack_id: :class:`str`
    
    """

    ID: str = Field("getLanguagePackInfo", alias="@type")
    language_pack_id: str

    @staticmethod
    def read(q: dict) -> GetLanguagePackInfo:
        return GetLanguagePackInfo.construct(**q)
