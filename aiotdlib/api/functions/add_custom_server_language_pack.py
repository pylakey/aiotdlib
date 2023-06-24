# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddCustomServerLanguagePack(BaseObject):
    """
    Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization

    :param language_pack_id: Identifier of a language pack to be added
    :type language_pack_id: :class:`String`
    """

    ID: typing.Literal["addCustomServerLanguagePack"] = "addCustomServerLanguagePack"
    language_pack_id: String
