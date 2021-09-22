# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class PushReceiverId(BaseObject):
    """
    Contains a globally unique push receiver identifier, which can be used to identify which account has received a push notification
    
    :param id: The globally unique identifier of push notification subscription
    :type id: :class:`int`
    
    """

    ID: str = Field("pushReceiverId", alias="@type")
    id: int

    @staticmethod
    def read(q: dict) -> PushReceiverId:
        return PushReceiverId.construct(**q)
