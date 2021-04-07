# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import SuggestedAction


class HideSuggestedAction(BaseObject):
    """
    Hides a suggested action
    
    Params:
        action (:class:`SuggestedAction`)
            Suggested action to hide
        
    """

    ID: str = Field("hideSuggestedAction", alias="@type")
    action: SuggestedAction

    @staticmethod
    def read(q: dict) -> HideSuggestedAction:
        return HideSuggestedAction.construct(**q)
