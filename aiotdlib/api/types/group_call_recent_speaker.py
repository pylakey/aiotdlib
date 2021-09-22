# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class GroupCallRecentSpeaker(BaseObject):
    """
    Describes a recently speaking participant in a group call
    
    :param participant_id: Group call participant identifier
    :type participant_id: :class:`MessageSender`
    
    :param is_speaking: True, is the user has spoken recently
    :type is_speaking: :class:`bool`
    
    """

    ID: str = Field("groupCallRecentSpeaker", alias="@type")
    participant_id: MessageSender
    is_speaking: bool

    @staticmethod
    def read(q: dict) -> GroupCallRecentSpeaker:
        return GroupCallRecentSpeaker.construct(**q)
