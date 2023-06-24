# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetLanguagePackString(BaseObject):
    """
    Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously

    :param language_pack_database_path: Path to the language pack database in which strings are stored
    :type language_pack_database_path: :class:`String`
    :param localization_target: Localization target to which the language pack belongs
    :type localization_target: :class:`String`
    :param language_pack_id: Language pack identifier
    :type language_pack_id: :class:`String`
    :param key: Language pack key of the string to be returned
    :type key: :class:`String`
    """

    ID: typing.Literal["getLanguagePackString"] = "getLanguagePackString"
    language_pack_database_path: String
    localization_target: String
    language_pack_id: String
    key: String
