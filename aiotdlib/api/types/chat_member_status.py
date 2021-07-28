# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_permissions import ChatPermissions
from ..base_object import BaseObject


class ChatMemberStatus(BaseObject):
    """
    Provides information about the status of a member in a chat
    
    """

    ID: str = Field("chatMemberStatus", alias="@type")


class ChatMemberStatusAdministrator(ChatMemberStatus):
    """
    The user is a member of the chat and has some additional privileges. In basic groups, administrators can edit and delete messages sent by others, add new members, ban unprivileged members, and manage voice chats. In supergroups and channels, there are more detailed options for administrator privileges
    
    Params:
        custom_title (:class:`str`)
            A custom title of the administrator; 0-16 characters without emojis; applicable to supergroups only
        
        can_be_edited (:class:`bool`)
            True, if the current user can edit the administrator privileges for the called user
        
        can_manage_chat (:class:`bool`)
            True, if the administrator can get chat event log, get chat statistics, get message statistics in channels, get channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other privilege; applicable to supergroups and channels only
        
        can_change_info (:class:`bool`)
            True, if the administrator can change the chat title, photo, and other settings
        
        can_post_messages (:class:`bool`)
            True, if the administrator can create channel posts; applicable to channels only
        
        can_edit_messages (:class:`bool`)
            True, if the administrator can edit messages of other users and pin messages; applicable to channels only
        
        can_delete_messages (:class:`bool`)
            True, if the administrator can delete messages of other users
        
        can_invite_users (:class:`bool`)
            True, if the administrator can invite new users to the chat
        
        can_restrict_members (:class:`bool`)
            True, if the administrator can restrict, ban, or unban chat members; always true for channels
        
        can_pin_messages (:class:`bool`)
            True, if the administrator can pin messages; applicable to basic groups and supergroups only
        
        can_promote_members (:class:`bool`)
            True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that were directly or indirectly promoted by them
        
        can_manage_voice_chats (:class:`bool`)
            True, if the administrator can manage voice chats
        
        is_anonymous (:class:`bool`)
            True, if the administrator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only
        
    """

    ID: str = Field("chatMemberStatusAdministrator", alias="@type")
    custom_title: typing.Optional[str] = Field(None, max_length=16)
    can_be_edited: bool
    can_manage_chat: bool
    can_change_info: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_delete_messages: bool
    can_invite_users: bool
    can_restrict_members: bool
    can_pin_messages: bool
    can_promote_members: bool
    can_manage_voice_chats: bool
    is_anonymous: bool

    @staticmethod
    def read(q: dict) -> ChatMemberStatusAdministrator:
        return ChatMemberStatusAdministrator.construct(**q)


class ChatMemberStatusBanned(ChatMemberStatus):
    """
    The user or the chat was banned (and hence is not a member of the chat). Implies the user can't return to the chat, view messages, or be used as a participant identifier to join a voice chat of the chat
    
    Params:
        banned_until_date (:class:`int`)
            Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Always 0 in basic groups
        
    """

    ID: str = Field("chatMemberStatusBanned", alias="@type")
    banned_until_date: int

    @staticmethod
    def read(q: dict) -> ChatMemberStatusBanned:
        return ChatMemberStatusBanned.construct(**q)


class ChatMemberStatusCreator(ChatMemberStatus):
    """
    The user is the owner of the chat and has all the administrator privileges
    
    Params:
        custom_title (:class:`str`)
            A custom title of the owner; 0-16 characters without emojis; applicable to supergroups only
        
        is_anonymous (:class:`bool`)
            True, if the creator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only
        
        is_member (:class:`bool`)
            True, if the user is a member of the chat
        
    """

    ID: str = Field("chatMemberStatusCreator", alias="@type")
    custom_title: typing.Optional[str] = Field(None, max_length=16)
    is_anonymous: bool
    is_member: bool

    @staticmethod
    def read(q: dict) -> ChatMemberStatusCreator:
        return ChatMemberStatusCreator.construct(**q)


class ChatMemberStatusLeft(ChatMemberStatus):
    """
    The user or the chat is not a chat member
    
    """

    ID: str = Field("chatMemberStatusLeft", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMemberStatusLeft:
        return ChatMemberStatusLeft.construct(**q)


class ChatMemberStatusMember(ChatMemberStatus):
    """
    The user is a member of the chat, without any additional privileges or restrictions
    
    """

    ID: str = Field("chatMemberStatusMember", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMemberStatusMember:
        return ChatMemberStatusMember.construct(**q)


class ChatMemberStatusRestricted(ChatMemberStatus):
    """
    The user is under certain restrictions in the chat. Not supported in basic groups and channels
    
    Params:
        is_member (:class:`bool`)
            True, if the user is a member of the chat
        
        restricted_until_date (:class:`int`)
            Point in time (Unix timestamp) when restrictions will be lifted from the user; 0 if never. If the user is restricted for more than 366 days or for less than 30 seconds from the current time, the user is considered to be restricted forever
        
        permissions (:class:`ChatPermissions`)
            User permissions in the chat
        
    """

    ID: str = Field("chatMemberStatusRestricted", alias="@type")
    is_member: bool
    restricted_until_date: int
    permissions: ChatPermissions

    @staticmethod
    def read(q: dict) -> ChatMemberStatusRestricted:
        return ChatMemberStatusRestricted.construct(**q)
