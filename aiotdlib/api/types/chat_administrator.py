# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatAdministrator(BaseObject):
    """
    Contains information about a chat administrator
    
    :param user_id: User identifier of the administrator
    :type user_id: :class:`int`
    
    :param custom_title: Custom title of the administrator
    :type custom_title: :class:`str`
    
    :param is_owner: True, if the user is the owner of the chat
    :type is_owner: :class:`bool`
    
    """

    ID: str = Field("chatAdministrator", alias="@type")
    user_id: int
    custom_title: str
    is_owner: bool

    @staticmethod
    def read(q: dict) -> ChatAdministrator:
        return ChatAdministrator.construct(**q)
