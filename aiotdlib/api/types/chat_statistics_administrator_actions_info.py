# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatStatisticsAdministratorActionsInfo(BaseObject):
    """
    Contains statistics about administrator actions done by a user
    
    :param user_id: Administrator user identifier
    :type user_id: :class:`int`
    
    :param deleted_message_count: Number of messages deleted by the administrator
    :type deleted_message_count: :class:`int`
    
    :param banned_user_count: Number of users banned by the administrator
    :type banned_user_count: :class:`int`
    
    :param restricted_user_count: Number of users restricted by the administrator
    :type restricted_user_count: :class:`int`
    
    """

    ID: str = Field("chatStatisticsAdministratorActionsInfo", alias="@type")
    user_id: int
    deleted_message_count: int
    banned_user_count: int
    restricted_user_count: int

    @staticmethod
    def read(q: dict) -> ChatStatisticsAdministratorActionsInfo:
        return ChatStatisticsAdministratorActionsInfo.construct(**q)
