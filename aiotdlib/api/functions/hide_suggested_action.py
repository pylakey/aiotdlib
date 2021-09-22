# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import SuggestedAction
from ..base_object import BaseObject


class HideSuggestedAction(BaseObject):
    """
    Hides a suggested action
    
    :param action: Suggested action to hide
    :type action: :class:`SuggestedAction`
    
    """

    ID: str = Field("hideSuggestedAction", alias="@type")
    action: SuggestedAction

    @staticmethod
    def read(q: dict) -> HideSuggestedAction:
        return HideSuggestedAction.construct(**q)
