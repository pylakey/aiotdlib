# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    AutosaveSettingsScope,
    ScopeAutosaveSettings,
)


class SetAutosaveSettings(BaseObject):
    """
    Sets autosave settings for the given scope. The method is guaranteed to work only after at least one call to getAutosaveSettings

    :param scope: Autosave settings scope
    :type scope: :class:`AutosaveSettingsScope`
    :param settings: New autosave settings for the scope; pass null to set autosave settings to default, defaults to None
    :type settings: :class:`ScopeAutosaveSettings`, optional
    """

    ID: typing.Literal["setAutosaveSettings"] = "setAutosaveSettings"
    scope: AutosaveSettingsScope
    settings: typing.Optional[ScopeAutosaveSettings] = None
