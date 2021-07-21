# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .group_call_recent_speaker import GroupCallRecentSpeaker
from ..base_object import BaseObject


class GroupCall(BaseObject):
    """
    Describes a group call
    
    Params:
        id (:class:`int`)
            Group call identifier
        
        title (:class:`str`)
            Group call title
        
        scheduled_start_date (:class:`int`)
            Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 if it is already active or was ended
        
        enabled_start_notification (:class:`bool`)
            True, if the group call is scheduled and the current user will receive a notification when the group call will start
        
        is_active (:class:`bool`)
            True, if the call is active
        
        is_joined (:class:`bool`)
            True, if the call is joined
        
        need_rejoin (:class:`bool`)
            True, if user was kicked from the call because of network loss and the call needs to be rejoined
        
        can_be_managed (:class:`bool`)
            True, if the current user can manage the group call
        
        participant_count (:class:`int`)
            Number of participants in the group call
        
        loaded_all_participants (:class:`bool`)
            True, if all group call participants are loaded
        
        recent_speakers (:obj:`list[GroupCallRecentSpeaker]`)
            Recently speaking users in the group call
        
        is_my_video_enabled (:class:`bool`)
            True, if the current user's video is enabled
        
        is_my_video_paused (:class:`bool`)
            True, if the current user's video is paused
        
        can_enable_video (:class:`bool`)
            True, if the current user can broadcast video or share screen
        
        mute_new_participants (:class:`bool`)
            True, if only group call administrators can unmute new participants
        
        can_change_mute_new_participants (:class:`bool`)
            True, if the current user can enable or disable mute_new_participants setting
        
        record_duration (:class:`int`)
            Duration of the ongoing group call recording, in seconds; 0 if none. An updateGroupCall update is not triggered when value of this field changes, but the same recording goes on
        
        duration (:class:`int`)
            Call duration, in seconds; for ended calls only
        
    """

    ID: str = Field("groupCall", alias="@type")
    id: int
    title: str
    scheduled_start_date: int
    enabled_start_notification: bool
    is_active: bool
    is_joined: bool
    need_rejoin: bool
    can_be_managed: bool
    participant_count: int
    loaded_all_participants: bool
    recent_speakers: list[GroupCallRecentSpeaker]
    is_my_video_enabled: bool
    is_my_video_paused: bool
    can_enable_video: bool
    mute_new_participants: bool
    can_change_mute_new_participants: bool
    record_duration: int
    duration: int

    @staticmethod
    def read(q: dict) -> GroupCall:
        return GroupCall.construct(**q)
