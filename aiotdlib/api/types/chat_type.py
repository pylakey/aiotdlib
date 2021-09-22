# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatType(BaseObject):
    """
    Describes the type of a chat
    
    """

    ID: str = Field("chatType", alias="@type")


class ChatTypeBasicGroup(ChatType):
    """
    A basic group (a chat with 0-200 other users)
    
    :param basic_group_id: Basic group identifier
    :type basic_group_id: :class:`int`
    
    """

    ID: str = Field("chatTypeBasicGroup", alias="@type")
    basic_group_id: int

    @staticmethod
    def read(q: dict) -> ChatTypeBasicGroup:
        return ChatTypeBasicGroup.construct(**q)


class ChatTypePrivate(ChatType):
    """
    An ordinary chat with a user
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    """

    ID: str = Field("chatTypePrivate", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> ChatTypePrivate:
        return ChatTypePrivate.construct(**q)


class ChatTypeSecret(ChatType):
    """
    A secret chat with a user
    
    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`int`
    
    :param user_id: User identifier of the secret chat peer
    :type user_id: :class:`int`
    
    """

    ID: str = Field("chatTypeSecret", alias="@type")
    secret_chat_id: int
    user_id: int

    @staticmethod
    def read(q: dict) -> ChatTypeSecret:
        return ChatTypeSecret.construct(**q)


class ChatTypeSupergroup(ChatType):
    """
    A supergroup or channel (with unlimited members)
    
    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`int`
    
    :param is_channel: True, if the supergroup is a channel
    :type is_channel: :class:`bool`
    
    """

    ID: str = Field("chatTypeSupergroup", alias="@type")
    supergroup_id: int
    is_channel: bool

    @staticmethod
    def read(q: dict) -> ChatTypeSupergroup:
        return ChatTypeSupergroup.construct(**q)
