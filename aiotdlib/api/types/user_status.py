# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UserStatus(BaseObject):
    """
    Describes the last time the user was online
    
    """

    ID: str = Field("userStatus", alias="@type")


class UserStatusEmpty(UserStatus):
    """
    The user status was never changed
    
    """

    ID: str = Field("userStatusEmpty", alias="@type")

    @staticmethod
    def read(q: dict) -> UserStatusEmpty:
        return UserStatusEmpty.construct(**q)


class UserStatusLastMonth(UserStatus):
    """
    The user is offline, but was online last month
    
    """

    ID: str = Field("userStatusLastMonth", alias="@type")

    @staticmethod
    def read(q: dict) -> UserStatusLastMonth:
        return UserStatusLastMonth.construct(**q)


class UserStatusLastWeek(UserStatus):
    """
    The user is offline, but was online last week
    
    """

    ID: str = Field("userStatusLastWeek", alias="@type")

    @staticmethod
    def read(q: dict) -> UserStatusLastWeek:
        return UserStatusLastWeek.construct(**q)


class UserStatusOffline(UserStatus):
    """
    The user is offline
    
    Params:
        was_online (:class:`int`)
            Point in time (Unix timestamp) when the user was last online
        
    """

    ID: str = Field("userStatusOffline", alias="@type")
    was_online: int

    @staticmethod
    def read(q: dict) -> UserStatusOffline:
        return UserStatusOffline.construct(**q)


class UserStatusOnline(UserStatus):
    """
    The user is online
    
    Params:
        expires (:class:`int`)
            Point in time (Unix timestamp) when the user's online status will expire
        
    """

    ID: str = Field("userStatusOnline", alias="@type")
    expires: int

    @staticmethod
    def read(q: dict) -> UserStatusOnline:
        return UserStatusOnline.construct(**q)


class UserStatusRecently(UserStatus):
    """
    The user was online recently
    
    """

    ID: str = Field("userStatusRecently", alias="@type")

    @staticmethod
    def read(q: dict) -> UserStatusRecently:
        return UserStatusRecently.construct(**q)
