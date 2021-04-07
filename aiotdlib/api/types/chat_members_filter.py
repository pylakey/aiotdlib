# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatMembersFilter(BaseObject):
    """
    Specifies the kind of chat members to return in searchChatMembers
    
    """

    ID: str = Field("chatMembersFilter", alias="@type")


class ChatMembersFilterAdministrators(ChatMembersFilter):
    """
    Returns the owner and administrators
    
    """

    ID: str = Field("chatMembersFilterAdministrators", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMembersFilterAdministrators:
        return ChatMembersFilterAdministrators.construct(**q)


class ChatMembersFilterBanned(ChatMembersFilter):
    """
    Returns users banned from the chat; can be used only by administrators in a supergroup or in a channel
    
    """

    ID: str = Field("chatMembersFilterBanned", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMembersFilterBanned:
        return ChatMembersFilterBanned.construct(**q)


class ChatMembersFilterBots(ChatMembersFilter):
    """
    Returns bot members of the chat
    
    """

    ID: str = Field("chatMembersFilterBots", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMembersFilterBots:
        return ChatMembersFilterBots.construct(**q)


class ChatMembersFilterContacts(ChatMembersFilter):
    """
    Returns contacts of the user
    
    """

    ID: str = Field("chatMembersFilterContacts", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMembersFilterContacts:
        return ChatMembersFilterContacts.construct(**q)


class ChatMembersFilterMembers(ChatMembersFilter):
    """
    Returns all chat members, including restricted chat members
    
    """

    ID: str = Field("chatMembersFilterMembers", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMembersFilterMembers:
        return ChatMembersFilterMembers.construct(**q)


class ChatMembersFilterMention(ChatMembersFilter):
    """
    Returns users which can be mentioned in the chat
    
    Params:
        message_thread_id (:class:`int`)
            If non-zero, the identifier of the current message thread
        
    """

    ID: str = Field("chatMembersFilterMention", alias="@type")
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> ChatMembersFilterMention:
        return ChatMembersFilterMention.construct(**q)


class ChatMembersFilterRestricted(ChatMembersFilter):
    """
    Returns users under certain restrictions in the chat; can be used only by administrators in a supergroup
    
    """

    ID: str = Field("chatMembersFilterRestricted", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatMembersFilterRestricted:
        return ChatMembersFilterRestricted.construct(**q)
