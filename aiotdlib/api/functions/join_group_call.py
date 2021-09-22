# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import MessageSender
from ..base_object import BaseObject


class JoinGroupCall(BaseObject):
    """
    Joins an active group call. Returns join response payload for tgcalls
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param participant_id: Identifier of a group call participant, which will be used to join the call; voice chats only
    :type participant_id: :class:`MessageSender`
    
    :param audio_source_id: Caller audio channel synchronization source identifier; received from tgcalls
    :type audio_source_id: :class:`int`
    
    :param payload: Group call join payload; received from tgcalls
    :type payload: :class:`str`
    
    :param is_muted: True, if the user's microphone is muted
    :type is_muted: :class:`bool`
    
    :param is_my_video_enabled: True, if the user's video is enabled
    :type is_my_video_enabled: :class:`bool`
    
    :param invite_hash: If non-empty, invite hash to be used to join the group call without being muted by administrators
    :type invite_hash: :class:`str`
    
    """

    ID: str = Field("joinGroupCall", alias="@type")
    group_call_id: int
    participant_id: MessageSender
    audio_source_id: int
    payload: str
    is_muted: bool
    is_my_video_enabled: bool
    invite_hash: str

    @staticmethod
    def read(q: dict) -> JoinGroupCall:
        return JoinGroupCall.construct(**q)
