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
    Suggests the user to check whether 2-step verification password is still remembered
    
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
    
    Params:
        supergroup_id (:class:`int`)
            Supergroup identifier
        
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


class SuggestedActionSeeTicksHint(SuggestedAction):
    """
    Suggests the user to see a hint about meaning of one and two ticks on sent message
    
    """

    ID: str = Field("suggestedActionSeeTicksHint", alias="@type")

    @staticmethod
    def read(q: dict) -> SuggestedActionSeeTicksHint:
        return SuggestedActionSeeTicksHint.construct(**q)
