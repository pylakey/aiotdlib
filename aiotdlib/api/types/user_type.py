# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class UserType(BaseObject):
    """
    Represents the type of a user. The following types are possible: regular users, deleted users and bots
    
    """

    ID: str = Field("userType", alias="@type")


class UserTypeBot(UserType):
    """
    A bot (see https://core.telegram.org/bots)
    
    :param can_join_groups: True, if the bot can be invited to basic group and supergroup chats
    :type can_join_groups: :class:`bool`
    
    :param can_read_all_group_messages: True, if the bot can read all messages in basic group or supergroup chats and not just those addressed to the bot. In private and channel chats a bot can always read all messages
    :type can_read_all_group_messages: :class:`bool`
    
    :param is_inline: True, if the bot supports inline queries
    :type is_inline: :class:`bool`
    
    :param inline_query_placeholder: Placeholder for inline queries (displayed on the application input field)
    :type inline_query_placeholder: :class:`str`
    
    :param need_location: True, if the location of the user should be sent with every inline query to this bot
    :type need_location: :class:`bool`
    
    """

    ID: str = Field("userTypeBot", alias="@type")
    can_join_groups: bool
    can_read_all_group_messages: bool
    is_inline: bool
    inline_query_placeholder: str
    need_location: bool

    @staticmethod
    def read(q: dict) -> UserTypeBot:
        return UserTypeBot.construct(**q)


class UserTypeDeleted(UserType):
    """
    A deleted user or deleted bot. No information on the user besides the user identifier is available. It is not possible to perform any active actions on this type of user
    
    """

    ID: str = Field("userTypeDeleted", alias="@type")

    @staticmethod
    def read(q: dict) -> UserTypeDeleted:
        return UserTypeDeleted.construct(**q)


class UserTypeRegular(UserType):
    """
    A regular user
    
    """

    ID: str = Field("userTypeRegular", alias="@type")

    @staticmethod
    def read(q: dict) -> UserTypeRegular:
        return UserTypeRegular.construct(**q)


class UserTypeUnknown(UserType):
    """
    No information on the user besides the user identifier is available, yet this user has not been deleted. This object is extremely rare and must be handled like a deleted user. It is not possible to perform any actions on users of this type
    
    """

    ID: str = Field("userTypeUnknown", alias="@type")

    @staticmethod
    def read(q: dict) -> UserTypeUnknown:
        return UserTypeUnknown.construct(**q)
