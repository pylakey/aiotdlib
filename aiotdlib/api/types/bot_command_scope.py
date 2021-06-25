# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class BotCommandScope(BaseObject):
    """
    Represents the scope to which bot commands are relevant
    
    """

    ID: str = Field("botCommandScope", alias="@type")


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """
    A scope covering all group and supergroup chat administrators
    
    """

    ID: str = Field("botCommandScopeAllChatAdministrators", alias="@type")

    @staticmethod
    def read(q: dict) -> BotCommandScopeAllChatAdministrators:
        return BotCommandScopeAllChatAdministrators.construct(**q)


class BotCommandScopeAllGroupChats(BotCommandScope):
    """
    A scope covering all group and supergroup chats
    
    """

    ID: str = Field("botCommandScopeAllGroupChats", alias="@type")

    @staticmethod
    def read(q: dict) -> BotCommandScopeAllGroupChats:
        return BotCommandScopeAllGroupChats.construct(**q)


class BotCommandScopeAllPrivateChats(BotCommandScope):
    """
    A scope covering all private chats
    
    """

    ID: str = Field("botCommandScopeAllPrivateChats", alias="@type")

    @staticmethod
    def read(q: dict) -> BotCommandScopeAllPrivateChats:
        return BotCommandScopeAllPrivateChats.construct(**q)


class BotCommandScopeChat(BotCommandScope):
    """
    A scope covering all members of a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("botCommandScopeChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> BotCommandScopeChat:
        return BotCommandScopeChat.construct(**q)


class BotCommandScopeChatAdministrators(BotCommandScope):
    """
    A scope covering all administrators of a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("botCommandScopeChatAdministrators", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> BotCommandScopeChatAdministrators:
        return BotCommandScopeChatAdministrators.construct(**q)


class BotCommandScopeChatMember(BotCommandScope):
    """
    A scope covering a member of a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        user_id (:class:`int`)
            User identifier
        
    """

    ID: str = Field("botCommandScopeChatMember", alias="@type")
    chat_id: int
    user_id: int

    @staticmethod
    def read(q: dict) -> BotCommandScopeChatMember:
        return BotCommandScopeChatMember.construct(**q)


class BotCommandScopeDefault(BotCommandScope):
    """
    A scope covering all users
    
    """

    ID: str = Field("botCommandScopeDefault", alias="@type")

    @staticmethod
    def read(q: dict) -> BotCommandScopeDefault:
        return BotCommandScopeDefault.construct(**q)
