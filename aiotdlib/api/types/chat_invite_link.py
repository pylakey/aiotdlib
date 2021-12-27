# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatInviteLink(BaseObject):
    """
    Contains a chat invite link
    
    :param invite_link: Chat invite link
    :type invite_link: :class:`str`
    
    :param name: Name of the link
    :type name: :class:`str`
    
    :param creator_user_id: User identifier of an administrator created the link
    :type creator_user_id: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the link was created
    :type date: :class:`int`
    
    :param edit_date: Point in time (Unix timestamp) when the link was last edited; 0 if never or unknown
    :type edit_date: :class:`int`
    
    :param expiration_date: Point in time (Unix timestamp) when the link will expire; 0 if never
    :type expiration_date: :class:`int`
    
    :param member_limit: The maximum number of members, which can join the chat using the link simultaneously; 0 if not limited. Always 0 if the link requires approval
    :type member_limit: :class:`int`
    
    :param member_count: Number of chat members, which joined the chat using the link
    :type member_count: :class:`int`
    
    :param pending_join_request_count: Number of pending join requests created using this link
    :type pending_join_request_count: :class:`int`
    
    :param creates_join_request: True, if the link only creates join request. If true, total number of joining members will be unlimited
    :type creates_join_request: :class:`bool`
    
    :param is_primary: True, if the link is primary. Primary invite link can't have name, expiration date, or usage limit. There is exactly one primary invite link for each administrator with can_invite_users right at a given time
    :type is_primary: :class:`bool`
    
    :param is_revoked: True, if the link was revoked
    :type is_revoked: :class:`bool`
    
    """

    ID: str = Field("chatInviteLink", alias="@type")
    invite_link: str
    name: str
    creator_user_id: int
    date: int
    edit_date: int
    expiration_date: int
    member_limit: int
    member_count: int
    pending_join_request_count: int
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool

    @staticmethod
    def read(q: dict) -> ChatInviteLink:
        return ChatInviteLink.construct(**q)
