# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_member_status import ChatMemberStatus
from ..base_object import BaseObject


class Supergroup(BaseObject):
    """
    Represents a supergroup or channel with zero or more members (subscribers in the case of channels). From the point of view of the system, a channel is a special kind of a supergroup: only administrators can post and see the list of members, and posts from all administrators use the name and photo of the channel instead of individual names and profile photos. Unlike supergroups, channels can have an unlimited number of subscribers
    
    Params:
        id (:class:`int`)
            Supergroup or channel identifier
        
        username (:class:`str`)
            Username of the supergroup or channel; empty for private supergroups or channels
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the current user joined, or the point in time when the supergroup or channel was created, in case the user is not a member
        
        status (:class:`ChatMemberStatus`)
            Status of the current user in the supergroup or channel; custom title will be always empty
        
        member_count (:class:`int`)
            Number of members in the supergroup or channel; 0 if unknown. Currently it is guaranteed to be known only if the supergroup or channel was received through searchPublicChats, searchChatsNearby, getInactiveSupergroupChats, getSuitableDiscussionChats, getGroupsInCommon, or getUserPrivacySettingRules
        
        has_linked_chat (:class:`bool`)
            True, if the channel has a discussion group, or the supergroup is the designated discussion group for a channel
        
        has_location (:class:`bool`)
            True, if the supergroup is connected to a location, i.e. the supergroup is a location-based supergroup
        
        sign_messages (:class:`bool`)
            True, if messages sent to the channel should contain information about the sender. This field is only applicable to channels
        
        is_slow_mode_enabled (:class:`bool`)
            True, if the slow mode is enabled in the supergroup
        
        is_channel (:class:`bool`)
            True, if the supergroup is a channel
        
        is_broadcast_group (:class:`bool`)
            True, if the supergroup is a broadcast group, i.e. only administrators can send messages and there is no limit on number of members
        
        is_verified (:class:`bool`)
            True, if the supergroup or channel is verified
        
        restriction_reason (:class:`str`)
            If non-empty, contains a human-readable description of the reason why access to this supergroup or channel must be restricted
        
        is_scam (:class:`bool`)
            True, if many users reported this supergroup or channel as a scam
        
        is_fake (:class:`bool`)
            True, if many users reported this supergroup or channel as a fake account
        
    """

    ID: str = Field("supergroup", alias="@type")
    id: int
    username: str
    date: int
    status: ChatMemberStatus
    member_count: int
    has_linked_chat: bool
    has_location: bool
    sign_messages: bool
    is_slow_mode_enabled: bool
    is_channel: bool
    is_broadcast_group: bool
    is_verified: bool
    restriction_reason: str
    is_scam: bool
    is_fake: bool

    @staticmethod
    def read(q: dict) -> Supergroup:
        return Supergroup.construct(**q)
