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
    SuggestedAction,
)


class HideSuggestedAction(BaseObject):
    """
    Hides a suggested action

    :param action: Suggested action to hide
    :type action: :class:`SuggestedAction`
    """

    ID: typing.Literal["hideSuggestedAction"] = "hideSuggestedAction"
    action: SuggestedAction
