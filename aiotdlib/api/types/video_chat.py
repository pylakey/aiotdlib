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


class VideoChat(BaseObject):
    """
    Describes a video chat
    
    :param group_call_id: Group call identifier of an active video chat; 0 if none. Full information about the video chat can be received through the method getGroupCall
    :type group_call_id: :class:`int`
    
    :param has_participants: True, if the video chat has participants
    :type has_participants: :class:`bool`
    
    :param default_participant_id: Default group call participant identifier to join the video chat; may be null, defaults to None
    :type default_participant_id: :class:`MessageSender`, optional
    
    """

    ID: str = Field("videoChat", alias="@type")
    group_call_id: int
    has_participants: bool
    default_participant_id: typing.Optional[MessageSender] = None

    @staticmethod
    def read(q: dict) -> VideoChat:
        return VideoChat.construct(**q)
