# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class UpgradeBasicGroupChatToSupergroupChat(BaseObject):
    """
    Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group
    
    :param chat_id: Identifier of the chat to upgrade
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("upgradeBasicGroupChatToSupergroupChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> UpgradeBasicGroupChatToSupergroupChat:
        return UpgradeBasicGroupChatToSupergroupChat.construct(**q)
