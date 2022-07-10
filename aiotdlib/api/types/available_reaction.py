# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AvailableReaction(BaseObject):
    """
    Represents an available reaction
    
    :param reaction: Text representation of the reaction
    :type reaction: :class:`str`
    
    :param needs_premium: True, if Telegram Premium is needed to send the reaction
    :type needs_premium: :class:`bool`
    
    """

    ID: str = Field("availableReaction", alias="@type")
    reaction: str
    needs_premium: bool

    @staticmethod
    def read(q: dict) -> AvailableReaction:
        return AvailableReaction.construct(**q)
