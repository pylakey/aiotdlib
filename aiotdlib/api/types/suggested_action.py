# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SuggestedAction(BaseObject):
    """
    Describes an action suggested to the current user
    
    """

    ID: str = Field("suggestedAction", alias="@type")


class SuggestedActionCheckPassword(SuggestedAction):
    """
    Suggests the user to check whether they still remember their 2-step verification password
    
    """

    ID: str = Field("suggestedActionCheckPassword", alias="@type")

    @staticmethod
    def read(q: dict) -> SuggestedActionCheckPassword:
        return SuggestedActionCheckPassword.construct(**q)


class SuggestedActionCheckPhoneNumber(SuggestedAction):
    """
    Suggests the user to check whether authorization phone number is correct and change the phone number if it is inaccessible
    
    """

    ID: str = Field("suggestedActionCheckPhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> SuggestedActionCheckPhoneNumber:
        return SuggestedActionCheckPhoneNumber.construct(**q)


class SuggestedActionConvertToBroadcastGroup(SuggestedAction):
    """
    Suggests the user to convert specified supergroup to a broadcast group
    
    :param supergroup_id: Supergroup identifier
    :type supergroup_id: :class:`int`
    
    """

    ID: str = Field("suggestedActionConvertToBroadcastGroup", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> SuggestedActionConvertToBroadcastGroup:
        return SuggestedActionConvertToBroadcastGroup.construct(**q)


class SuggestedActionEnableArchiveAndMuteNewChats(SuggestedAction):
    """
    Suggests the user to enable "archive_and_mute_new_chats_from_unknown_users" option
    
    """

    ID: str = Field("suggestedActionEnableArchiveAndMuteNewChats", alias="@type")

    @staticmethod
    def read(q: dict) -> SuggestedActionEnableArchiveAndMuteNewChats:
        return SuggestedActionEnableArchiveAndMuteNewChats.construct(**q)


class SuggestedActionSetPassword(SuggestedAction):
    """
    Suggests the user to set a 2-step verification password to be able to log in again
    
    :param authorization_delay: The number of days to pass between consecutive authorizations if the user declines to set password
    :type authorization_delay: :class:`int`
    
    """

    ID: str = Field("suggestedActionSetPassword", alias="@type")
    authorization_delay: int

    @staticmethod
    def read(q: dict) -> SuggestedActionSetPassword:
        return SuggestedActionSetPassword.construct(**q)


class SuggestedActionViewChecksHint(SuggestedAction):
    """
    Suggests the user to view a hint about the meaning of one and two check marks on sent messages
    
    """

    ID: str = Field("suggestedActionViewChecksHint", alias="@type")

    @staticmethod
    def read(q: dict) -> SuggestedActionViewChecksHint:
        return SuggestedActionViewChecksHint.construct(**q)
