# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_position import MessagePosition
from ..base_object import BaseObject


class MessagePositions(BaseObject):
    """
    Contains a list of message positions
    
    :param total_count: Total number of messages found
    :type total_count: :class:`int`
    
    :param positions: List of message positions
    :type positions: :class:`list[MessagePosition]`
    
    """

    ID: str = Field("messagePositions", alias="@type")
    total_count: int
    positions: list[MessagePosition]

    @staticmethod
    def read(q: dict) -> MessagePositions:
        return MessagePositions.construct(**q)
