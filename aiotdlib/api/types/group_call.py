# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .group_call_recent_speaker import GroupCallRecentSpeaker
from ..base_object import BaseObject


class GroupCall(BaseObject):
    """
    Describes a group call
    
    :param id: Group call identifier
    :type id: :class:`int`
    
    :param title: Group call title
    :type title: :class:`str`
    
    :param scheduled_start_date: Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 if it is already active or was ended
    :type scheduled_start_date: :class:`int`
    
    :param enabled_start_notification: True, if the group call is scheduled and the current user will receive a notification when the group call will start
    :type enabled_start_notification: :class:`bool`
    
    :param is_active: True, if the call is active
    :type is_active: :class:`bool`
    
    :param is_joined: True, if the call is joined
    :type is_joined: :class:`bool`
    
    :param need_rejoin: True, if user was kicked from the call because of network loss and the call needs to be rejoined
    :type need_rejoin: :class:`bool`
    
    :param can_be_managed: True, if the current user can manage the group call
    :type can_be_managed: :class:`bool`
    
    :param participant_count: Number of participants in the group call
    :type participant_count: :class:`int`
    
    :param loaded_all_participants: True, if all group call participants are loaded
    :type loaded_all_participants: :class:`bool`
    
    :param recent_speakers: Recently speaking users in the group call
    :type recent_speakers: :class:`list[GroupCallRecentSpeaker]`
    
    :param is_my_video_enabled: True, if the current user's video is enabled
    :type is_my_video_enabled: :class:`bool`
    
    :param is_my_video_paused: True, if the current user's video is paused
    :type is_my_video_paused: :class:`bool`
    
    :param can_enable_video: True, if the current user can broadcast video or share screen
    :type can_enable_video: :class:`bool`
    
    :param mute_new_participants: True, if only group call administrators can unmute new participants
    :type mute_new_participants: :class:`bool`
    
    :param can_change_mute_new_participants: True, if the current user can enable or disable mute_new_participants setting
    :type can_change_mute_new_participants: :class:`bool`
    
    :param record_duration: Duration of the ongoing group call recording, in seconds; 0 if none. An updateGroupCall update is not triggered when value of this field changes, but the same recording goes on
    :type record_duration: :class:`int`
    
    :param is_video_recorded: True, if a video file is being recorded for the call
    :type is_video_recorded: :class:`bool`
    
    :param duration: Call duration, in seconds; for ended calls only
    :type duration: :class:`int`
    
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
    is_video_recorded: bool
    duration: int

    @staticmethod
    def read(q: dict) -> GroupCall:
        return GroupCall.construct(**q)
