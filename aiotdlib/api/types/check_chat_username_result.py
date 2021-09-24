# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckChatUsernameResult(BaseObject):
    """
    Represents result of checking whether a username can be set for a chat
    
    """

    ID: str = Field("checkChatUsernameResult", alias="@type")


class CheckChatUsernameResultOk(CheckChatUsernameResult):
    """
    The username can be set
    
    """

    ID: str = Field("checkChatUsernameResultOk", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckChatUsernameResultOk:
        return CheckChatUsernameResultOk.construct(**q)


class CheckChatUsernameResultPublicChatsTooMuch(CheckChatUsernameResult):
    """
    The user has too much chats with username, one of them should be made private first
    
    """

    ID: str = Field("checkChatUsernameResultPublicChatsTooMuch", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckChatUsernameResultPublicChatsTooMuch:
        return CheckChatUsernameResultPublicChatsTooMuch.construct(**q)


class CheckChatUsernameResultPublicGroupsUnavailable(CheckChatUsernameResult):
    """
    The user can't be a member of a public supergroup
    
    """

    ID: str = Field("checkChatUsernameResultPublicGroupsUnavailable", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckChatUsernameResultPublicGroupsUnavailable:
        return CheckChatUsernameResultPublicGroupsUnavailable.construct(**q)


class CheckChatUsernameResultUsernameInvalid(CheckChatUsernameResult):
    """
    The username is invalid
    
    """

    ID: str = Field("checkChatUsernameResultUsernameInvalid", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckChatUsernameResultUsernameInvalid:
        return CheckChatUsernameResultUsernameInvalid.construct(**q)


class CheckChatUsernameResultUsernameOccupied(CheckChatUsernameResult):
    """
    The username is occupied
    
    """

    ID: str = Field("checkChatUsernameResultUsernameOccupied", alias="@type")

    @staticmethod
    def read(q: dict) -> CheckChatUsernameResultUsernameOccupied:
        return CheckChatUsernameResultUsernameOccupied.construct(**q)
