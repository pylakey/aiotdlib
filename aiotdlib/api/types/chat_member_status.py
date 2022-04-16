# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_administrator_rights import ChatAdministratorRights
from .chat_permissions import ChatPermissions
from ..base_object import BaseObject


class ChatMemberStatus(BaseObject):
    """
    Provides information about the status of a member in a chat
    
    """

    ID: str = Field("chatMemberStatus", alias="@type")


class ChatMemberStatusAdministrator(ChatMemberStatus):
    """
    The user is a member of the chat and has some additional privileges. In basic groups, administrators can edit and delete messages sent by others, add new members, ban unprivileged members, and manage video chats. In supergroups and channels, there are more detailed options for administrator privileges
    
    :param custom_title: A custom title of the administrator; 0-16 characters without emojis; applicable to supergroups only, defaults to None
    :type custom_title: :class:`str`, optional
    
    :param can_be_edited: True, if the current user can edit the administrator privileges for the called user
    :type can_be_edited: :class:`bool`
    
    :param rights: Rights of the administrator
    :type rights: :class:`ChatAdministratorRights`
    
    """

    ID: str = Field("chatMemberStatusAdministrator", alias="@type")
    custom_title: typing.Optional[str] = Field(None, max_length=16)
    can_be_edited: bool
    rights: ChatAdministratorRights

    @staticmethod
    def read(q: dict) -> ChatMemberStatusAdministrator:
        return ChatMemberStatusAdministrator.construct(**q)


class ChatMemberStatusBanned(ChatMemberStatus):
    """
    The user or the chat was banned (and hence is not a member of the chat). Implies the user can't return to the chat, view messages, or be used as a participant identifier to join a video chat of the chat
    
    :param banned_until_date: Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Always 0 in basic groups
    :type banned_until_date: :class:`int`
    
    """

    ID: str = Field("chatMemberStatusBanned", alias="@type")
    banned_until_date: int

    @staticmethod
    def read(q: dict) -> ChatMemberStatusBanned:
        return ChatMemberStatusBanned.construct(**q)


class ChatMemberStatusCreator(ChatMemberStatus):
    """
    The user is the owner of the chat and has all the administrator privileges
    
    :param custom_title: A custom title of the owner; 0-16 characters without emojis; applicable to supergroups only, defaults to None
    :type custom_title: :class:`str`, optional
    
    :param is_anonymous: True, if the creator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only
    :type is_anonymous: :class:`bool`
    
    :param is_member: True, if the user is a member of the chat
    :type is_member: :class:`bool`
    
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
    
    :param is_member: True, if the user is a member of the chat
    :type is_member: :class:`bool`
    
    :param restricted_until_date: Point in time (Unix timestamp) when restrictions will be lifted from the user; 0 if never. If the user is restricted for more than 366 days or for less than 30 seconds from the current time, the user is considered to be restricted forever
    :type restricted_until_date: :class:`int`
    
    :param permissions: User permissions in the chat
    :type permissions: :class:`ChatPermissions`
    
    """

    ID: str = Field("chatMemberStatusRestricted", alias="@type")
    is_member: bool
    restricted_until_date: int
    permissions: ChatPermissions

    @staticmethod
    def read(q: dict) -> ChatMemberStatusRestricted:
        return ChatMemberStatusRestricted.construct(**q)
