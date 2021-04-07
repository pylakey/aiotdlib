# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UpgradeBasicGroupChatToSupergroupChat(BaseObject):
    """
    Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to upgrade
        
    """

    ID: str = Field("upgradeBasicGroupChatToSupergroupChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> UpgradeBasicGroupChatToSupergroupChat:
        return UpgradeBasicGroupChatToSupergroupChat.construct(**q)
