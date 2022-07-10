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
    
    :param id: Supergroup or channel identifier
    :type id: :class:`int`
    
    :param username: Username of the supergroup or channel; empty for private supergroups or channels
    :type username: :class:`str`
    
    :param date: Point in time (Unix timestamp) when the current user joined, or the point in time when the supergroup or channel was created, in case the user is not a member
    :type date: :class:`int`
    
    :param status: Status of the current user in the supergroup or channel; custom title will be always empty
    :type status: :class:`ChatMemberStatus`
    
    :param member_count: Number of members in the supergroup or channel; 0 if unknown. Currently, it is guaranteed to be known only if the supergroup or channel was received through searchPublicChats, searchChatsNearby, getInactiveSupergroupChats, getSuitableDiscussionChats, getGroupsInCommon, or getUserPrivacySettingRules
    :type member_count: :class:`int`
    
    :param has_linked_chat: True, if the channel has a discussion group, or the supergroup is the designated discussion group for a channel
    :type has_linked_chat: :class:`bool`
    
    :param has_location: True, if the supergroup is connected to a location, i.e. the supergroup is a location-based supergroup
    :type has_location: :class:`bool`
    
    :param sign_messages: True, if messages sent to the channel need to contain information about the sender. This field is only applicable to channels
    :type sign_messages: :class:`bool`
    
    :param join_to_send_messages: True, if users need to join the supergroup before they can send messages. Always true for channels and non-discussion supergroups
    :type join_to_send_messages: :class:`bool`
    
    :param join_by_request: True, if all users directly joining the supergroup need to be approved by supergroup administrators. Always false for channels and supergroups without username, location, or a linked chat
    :type join_by_request: :class:`bool`
    
    :param is_slow_mode_enabled: True, if the slow mode is enabled in the supergroup
    :type is_slow_mode_enabled: :class:`bool`
    
    :param is_channel: True, if the supergroup is a channel
    :type is_channel: :class:`bool`
    
    :param is_broadcast_group: True, if the supergroup is a broadcast group, i.e. only administrators can send messages and there is no limit on the number of members
    :type is_broadcast_group: :class:`bool`
    
    :param is_verified: True, if the supergroup or channel is verified
    :type is_verified: :class:`bool`
    
    :param restriction_reason: If non-empty, contains a human-readable description of the reason why access to this supergroup or channel must be restricted
    :type restriction_reason: :class:`str`
    
    :param is_scam: True, if many users reported this supergroup or channel as a scam
    :type is_scam: :class:`bool`
    
    :param is_fake: True, if many users reported this supergroup or channel as a fake account
    :type is_fake: :class:`bool`
    
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
    join_to_send_messages: bool
    join_by_request: bool
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
