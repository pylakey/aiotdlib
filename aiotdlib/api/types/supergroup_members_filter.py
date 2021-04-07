# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SupergroupMembersFilter(BaseObject):
    """
    Specifies the kind of chat members to return in getSupergroupMembers
    
    """

    ID: str = Field("supergroupMembersFilter", alias="@type")


class SupergroupMembersFilterAdministrators(SupergroupMembersFilter):
    """
    Returns the owner and administrators
    
    """

    ID: str = Field("supergroupMembersFilterAdministrators", alias="@type")

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterAdministrators:
        return SupergroupMembersFilterAdministrators.construct(**q)


class SupergroupMembersFilterBanned(SupergroupMembersFilter):
    """
    Returns users banned from the supergroup or channel; can be used only by administrators
    
    Params:
        query (:class:`str`)
            Query to search for
        
    """

    ID: str = Field("supergroupMembersFilterBanned", alias="@type")
    query: str

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterBanned:
        return SupergroupMembersFilterBanned.construct(**q)


class SupergroupMembersFilterBots(SupergroupMembersFilter):
    """
    Returns bot members of the supergroup or channel
    
    """

    ID: str = Field("supergroupMembersFilterBots", alias="@type")

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterBots:
        return SupergroupMembersFilterBots.construct(**q)


class SupergroupMembersFilterContacts(SupergroupMembersFilter):
    """
    Returns contacts of the user, which are members of the supergroup or channel
    
    Params:
        query (:class:`str`)
            Query to search for
        
    """

    ID: str = Field("supergroupMembersFilterContacts", alias="@type")
    query: str

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterContacts:
        return SupergroupMembersFilterContacts.construct(**q)


class SupergroupMembersFilterMention(SupergroupMembersFilter):
    """
    Returns users which can be mentioned in the supergroup
    
    Params:
        query (:class:`str`)
            Query to search for
        
        message_thread_id (:class:`int`)
            If non-zero, the identifier of the current message thread
        
    """

    ID: str = Field("supergroupMembersFilterMention", alias="@type")
    query: str
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterMention:
        return SupergroupMembersFilterMention.construct(**q)


class SupergroupMembersFilterRecent(SupergroupMembersFilter):
    """
    Returns recently active users in reverse chronological order
    
    """

    ID: str = Field("supergroupMembersFilterRecent", alias="@type")

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterRecent:
        return SupergroupMembersFilterRecent.construct(**q)


class SupergroupMembersFilterRestricted(SupergroupMembersFilter):
    """
    Returns restricted supergroup members; can be used only by administrators
    
    Params:
        query (:class:`str`)
            Query to search for
        
    """

    ID: str = Field("supergroupMembersFilterRestricted", alias="@type")
    query: str

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterRestricted:
        return SupergroupMembersFilterRestricted.construct(**q)


class SupergroupMembersFilterSearch(SupergroupMembersFilter):
    """
    Used to search for supergroup or channel members via a (string) query
    
    Params:
        query (:class:`str`)
            Query to search for
        
    """

    ID: str = Field("supergroupMembersFilterSearch", alias="@type")
    query: str

    @staticmethod
    def read(q: dict) -> SupergroupMembersFilterSearch:
        return SupergroupMembersFilterSearch.construct(**q)
