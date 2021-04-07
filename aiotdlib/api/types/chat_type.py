# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatType(BaseObject):
    """
    Describes the type of a chat
    
    """

    ID: str = Field("chatType", alias="@type")


class ChatTypeBasicGroup(ChatType):
    """
    A basic group (i.e., a chat with 0-200 other users)
    
    Params:
        basic_group_id (:class:`int`)
            Basic group identifier
        
    """

    ID: str = Field("chatTypeBasicGroup", alias="@type")
    basic_group_id: int

    @staticmethod
    def read(q: dict) -> ChatTypeBasicGroup:
        return ChatTypeBasicGroup.construct(**q)


class ChatTypePrivate(ChatType):
    """
    An ordinary chat with a user
    
    Params:
        user_id (:class:`int`)
            User identifier
        
    """

    ID: str = Field("chatTypePrivate", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> ChatTypePrivate:
        return ChatTypePrivate.construct(**q)


class ChatTypeSecret(ChatType):
    """
    A secret chat with a user
    
    Params:
        secret_chat_id (:class:`int`)
            Secret chat identifier
        
        user_id (:class:`int`)
            User identifier of the secret chat peer
        
    """

    ID: str = Field("chatTypeSecret", alias="@type")
    secret_chat_id: int
    user_id: int

    @staticmethod
    def read(q: dict) -> ChatTypeSecret:
        return ChatTypeSecret.construct(**q)


class ChatTypeSupergroup(ChatType):
    """
    A supergroup (i.e. a chat with up to GetOption("supergroup_max_size") other users), or channel (with unlimited members)
    
    Params:
        supergroup_id (:class:`int`)
            Supergroup or channel identifier
        
        is_channel (:class:`bool`)
            True, if the supergroup is a channel
        
    """

    ID: str = Field("chatTypeSupergroup", alias="@type")
    supergroup_id: int
    is_channel: bool

    @staticmethod
    def read(q: dict) -> ChatTypeSupergroup:
        return ChatTypeSupergroup.construct(**q)
