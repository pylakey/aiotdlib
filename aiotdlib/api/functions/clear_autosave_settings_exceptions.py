# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearAutosaveSettingsExceptions(BaseObject):
    """
    Clears the list of all autosave settings exceptions. The method is guaranteed to work only after at least one call to getAutosaveSettings
    """

    ID: typing.Literal["clearAutosaveSettingsExceptions"] = "clearAutosaveSettingsExceptions"
