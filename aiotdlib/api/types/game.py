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
    
    :param id: Game ID
    :type id: :class:`int`
    
    :param short_name: Game short name. To share a game use the URL https://t.me/{bot_username}?game={game_short_name}
    :type short_name: :class:`str`
    
    :param title: Game title
    :type title: :class:`str`
    
    :param text: Game text, usually containing scoreboards for a game
    :type text: :class:`FormattedText`
    
    :param param_description: Game description
    :type param_description: :class:`str`
    
    :param photo: Game photo
    :type photo: :class:`Photo`
    
    :param animation: Game animation; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    
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
