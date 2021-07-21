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
    
    Params:
        participant_id (:class:`MessageSender`)
            Identifier of the group call participant
        
        audio_source_id (:class:`int`)
            User's audio channel synchronization source identifier
        
        screen_sharing_audio_source_id (:class:`int`)
            User's screen sharing audio channel synchronization source identifier
        
        video_info (:class:`GroupCallParticipantVideoInfo`)
            Information about user's video channel; may be null if there is no active video
        
        screen_sharing_video_info (:class:`GroupCallParticipantVideoInfo`)
            Information about user's screen sharing video channel; may be null if there is no active screen sharing video
        
        bio (:class:`str`)
            The participant user's bio or the participant chat's description
        
        is_current_user (:class:`bool`)
            True, if the participant is the current user
        
        is_speaking (:class:`bool`)
            True, if the participant is speaking as set by setGroupCallParticipantIsSpeaking
        
        is_hand_raised (:class:`bool`)
            True, if the participant hand is raised
        
        can_be_muted_for_all_users (:class:`bool`)
            True, if the current user can mute the participant for all other group call participants
        
        can_be_unmuted_for_all_users (:class:`bool`)
            True, if the current user can allow the participant to unmute themselves or unmute the participant (if the participant is the current user)
        
        can_be_muted_for_current_user (:class:`bool`)
            True, if the current user can mute the participant only for self
        
        can_be_unmuted_for_current_user (:class:`bool`)
            True, if the current user can unmute the participant for self
        
        is_muted_for_all_users (:class:`bool`)
            True, if the participant is muted for all users
        
        is_muted_for_current_user (:class:`bool`)
            True, if the participant is muted for the current user
        
        can_unmute_self (:class:`bool`)
            True, if the participant is muted for all users, but can unmute themselves
        
        volume_level (:class:`int`)
            Participant's volume level; 1-20000 in hundreds of percents
        
        order (:class:`str`)
            User's order in the group call participant list. Orders must be compared lexicographically. The bigger is order, the higher is user in the list. If order is empty, the user must be removed from the participant list
        
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
