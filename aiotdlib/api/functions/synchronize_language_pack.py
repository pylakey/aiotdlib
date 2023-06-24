# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SynchronizeLanguagePack(BaseObject):
    """
    Fetches the latest versions of all strings from a language pack in the current localization target from the server. This method doesn't need to be called explicitly for the current used/base language packs. Can be called before authorization

    :param language_pack_id: Language pack identifier
    :type language_pack_id: :class:`String`
    """

    ID: typing.Literal["synchronizeLanguagePack"] = "synchronizeLanguagePack"
    language_pack_id: String
