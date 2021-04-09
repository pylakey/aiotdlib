# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .animation import Animation
from .formatted_text import FormattedText
from .photo import Photo
from ..base_object import BaseObject


class Game(BaseObject):
    """
    Describes a game
    
    Params:
        id (:class:`int`)
            Game ID
        
        short_name (:class:`str`)
            Game short name. To share a game use the URL https://t.me/{bot_username}?game={game_short_name}
        
        title (:class:`str`)
            Game title
        
        text (:class:`FormattedText`)
            Game text, usually containing scoreboards for a game
        
        param_description (:class:`str`)
            Game description
        
        photo (:class:`Photo`)
            Game photo
        
        animation (:class:`Animation`)
            Game animation; may be null
        
    """

    ID: str = Field("game", alias="@type")
    id: int
    short_name: str
    title: str
    text: FormattedText
    param_description: str
    photo: Photo
    animation: typing.Optional[Animation] = None

    @staticmethod
    def read(q: dict) -> Game:
        return Game.construct(**q)
