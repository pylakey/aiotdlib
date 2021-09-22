# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DisconnectWebsite(BaseObject):
    """
    Disconnects website from the current user's Telegram account
    
    :param website_id: Website identifier
    :type website_id: :class:`int`
    
    """

    ID: str = Field("disconnectWebsite", alias="@type")
    website_id: int

    @staticmethod
    def read(q: dict) -> DisconnectWebsite:
        return DisconnectWebsite.construct(**q)
