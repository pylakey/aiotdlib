# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    
    :param sticker: The animated sticker with the dice animation
    :type sticker: :class:`Sticker`
    
    """

    ID: str = Field("diceStickersRegular", alias="@type")
    sticker: Sticker

    @staticmethod
    def read(q: dict) -> DiceStickersRegular:
        return DiceStickersRegular.construct(**q)


class DiceStickersSlotMachine(DiceStickers):
    """
    Animated stickers to be combined into a slot machine
    
    :param background: The animated sticker with the slot machine background. The background animation must start playing after all reel animations finish
    :type background: :class:`Sticker`
    
    :param lever: The animated sticker with the lever animation. The lever animation must play once in the initial dice state
    :type lever: :class:`Sticker`
    
    :param left_reel: The animated sticker with the left reel
    :type left_reel: :class:`Sticker`
    
    :param center_reel: The animated sticker with the center reel
    :type center_reel: :class:`Sticker`
    
    :param right_reel: The animated sticker with the right reel
    :type right_reel: :class:`Sticker`
    
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
