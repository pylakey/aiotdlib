# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .sticker import Sticker
from ..base_object import BaseObject


class DiceStickers(BaseObject):
    """
    Contains animated stickers which should be used for dice animation rendering
    
    """

    ID: str = Field("diceStickers", alias="@type")


class DiceStickersRegular(DiceStickers):
    """
    A regular animated sticker
    
    Params:
        sticker (:class:`Sticker`)
            The animated sticker with the dice animation
        
    """

    ID: str = Field("diceStickersRegular", alias="@type")
    sticker: Sticker

    @staticmethod
    def read(q: dict) -> DiceStickersRegular:
        return DiceStickersRegular.construct(**q)


class DiceStickersSlotMachine(DiceStickers):
    """
    Animated stickers to be combined into a slot machine
    
    Params:
        background (:class:`Sticker`)
            The animated sticker with the slot machine background. The background animation must start playing after all reel animations finish
        
        lever (:class:`Sticker`)
            The animated sticker with the lever animation. The lever animation must play once in the initial dice state
        
        left_reel (:class:`Sticker`)
            The animated sticker with the left reel
        
        center_reel (:class:`Sticker`)
            The animated sticker with the center reel
        
        right_reel (:class:`Sticker`)
            The animated sticker with the right reel
        
    """

    ID: str = Field("diceStickersSlotMachine", alias="@type")
    background: Sticker
    lever: Sticker
    left_reel: Sticker
    center_reel: Sticker
    right_reel: Sticker

    @staticmethod
    def read(q: dict) -> DiceStickersSlotMachine:
        return DiceStickersSlotMachine.construct(**q)
