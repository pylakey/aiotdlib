# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatStatisticsAdministratorActionsInfo(BaseObject):
    """
    Contains statistics about administrator actions done by a user
    
    Params:
        user_id (:class:`int`)
            Administrator user identifier
        
        deleted_message_count (:class:`int`)
            Number of messages deleted by the administrator
        
        banned_user_count (:class:`int`)
            Number of users banned by the administrator
        
        restricted_user_count (:class:`int`)
            Number of users restricted by the administrator
        
    """

    ID: str = Field("chatStatisticsAdministratorActionsInfo", alias="@type")
    user_id: int
    deleted_message_count: int
    banned_user_count: int
    restricted_user_count: int

    @staticmethod
    def read(q: dict) -> ChatStatisticsAdministratorActionsInfo:
        return ChatStatisticsAdministratorActionsInfo.construct(**q)
