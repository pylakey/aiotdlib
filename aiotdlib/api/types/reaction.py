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


class Reaction(BaseObject):
    """
    Contains stickers which must be used for reaction animation rendering
    
    :param reaction: Text representation of the reaction
    :type reaction: :class:`str`
    
    :param title: Reaction title
    :type title: :class:`str`
    
    :param is_active: True, if the reaction can be added to new messages and enabled in chats
    :type is_active: :class:`bool`
    
    :param is_premium: True, if the reaction is available only for Premium users
    :type is_premium: :class:`bool`
    
    :param static_icon: Static icon for the reaction
    :type static_icon: :class:`Sticker`
    
    :param appear_animation: Appear animation for the reaction
    :type appear_animation: :class:`Sticker`
    
    :param select_animation: Select animation for the reaction
    :type select_animation: :class:`Sticker`
    
    :param activate_animation: Activate animation for the reaction
    :type activate_animation: :class:`Sticker`
    
    :param effect_animation: Effect animation for the reaction
    :type effect_animation: :class:`Sticker`
    
    :param around_animation: Around animation for the reaction; may be null, defaults to None
    :type around_animation: :class:`Sticker`, optional
    
    :param center_animation: Center animation for the reaction; may be null, defaults to None
    :type center_animation: :class:`Sticker`, optional
    
    """

    ID: str = Field("reaction", alias="@type")
    reaction: str
    title: str
    is_active: bool
    is_premium: bool
    static_icon: Sticker
    appear_animation: Sticker
    select_animation: Sticker
    activate_animation: Sticker
    effect_animation: Sticker
    around_animation: typing.Optional[Sticker] = None
    center_animation: typing.Optional[Sticker] = None

    @staticmethod
    def read(q: dict) -> Reaction:
        return Reaction.construct(**q)
