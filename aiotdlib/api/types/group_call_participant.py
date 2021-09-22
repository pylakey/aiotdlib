# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .group_call_participant_video_info import GroupCallParticipantVideoInfo
from .message_sender import MessageSender
from ..base_object import BaseObject


class GroupCallParticipant(BaseObject):
    """
    Represents a group call participant
    
    :param participant_id: Identifier of the group call participant
    :type participant_id: :class:`MessageSender`
    
    :param audio_source_id: User's audio channel synchronization source identifier
    :type audio_source_id: :class:`int`
    
    :param screen_sharing_audio_source_id: User's screen sharing audio channel synchronization source identifier
    :type screen_sharing_audio_source_id: :class:`int`
    
    :param video_info: Information about user's video channel; may be null if there is no active video, defaults to None
    :type video_info: :class:`GroupCallParticipantVideoInfo`, optional
    
    :param screen_sharing_video_info: Information about user's screen sharing video channel; may be null if there is no active screen sharing video, defaults to None
    :type screen_sharing_video_info: :class:`GroupCallParticipantVideoInfo`, optional
    
    :param bio: The participant user's bio or the participant chat's description
    :type bio: :class:`str`
    
    :param is_current_user: True, if the participant is the current user
    :type is_current_user: :class:`bool`
    
    :param is_speaking: True, if the participant is speaking as set by setGroupCallParticipantIsSpeaking
    :type is_speaking: :class:`bool`
    
    :param is_hand_raised: True, if the participant hand is raised
    :type is_hand_raised: :class:`bool`
    
    :param can_be_muted_for_all_users: True, if the current user can mute the participant for all other group call participants
    :type can_be_muted_for_all_users: :class:`bool`
    
    :param can_be_unmuted_for_all_users: True, if the current user can allow the participant to unmute themselves or unmute the participant (if the participant is the current user)
    :type can_be_unmuted_for_all_users: :class:`bool`
    
    :param can_be_muted_for_current_user: True, if the current user can mute the participant only for self
    :type can_be_muted_for_current_user: :class:`bool`
    
    :param can_be_unmuted_for_current_user: True, if the current user can unmute the participant for self
    :type can_be_unmuted_for_current_user: :class:`bool`
    
    :param is_muted_for_all_users: True, if the participant is muted for all users
    :type is_muted_for_all_users: :class:`bool`
    
    :param is_muted_for_current_user: True, if the participant is muted for the current user
    :type is_muted_for_current_user: :class:`bool`
    
    :param can_unmute_self: True, if the participant is muted for all users, but can unmute themselves
    :type can_unmute_self: :class:`bool`
    
    :param volume_level: Participant's volume level; 1-20000 in hundreds of percents
    :type volume_level: :class:`int`
    
    :param order: User's order in the group call participant list. Orders must be compared lexicographically. The bigger is order, the higher is user in the list. If order is empty, the user must be removed from the participant list
    :type order: :class:`str`
    
    """

    ID: str = Field("groupCallParticipant", alias="@type")
    participant_id: MessageSender
    audio_source_id: int
    screen_sharing_audio_source_id: int
    video_info: typing.Optional[GroupCallParticipantVideoInfo] = None
    screen_sharing_video_info: typing.Optional[GroupCallParticipantVideoInfo] = None
    bio: str
    is_current_user: bool
    is_speaking: bool
    is_hand_raised: bool
    can_be_muted_for_all_users: bool
    can_be_unmuted_for_all_users: bool
    can_be_muted_for_current_user: bool
    can_be_unmuted_for_current_user: bool
    is_muted_for_all_users: bool
    is_muted_for_current_user: bool
    can_unmute_self: bool
    volume_level: int
    order: str

    @staticmethod
    def read(q: dict) -> GroupCallParticipant:
        return GroupCallParticipant.construct(**q)
