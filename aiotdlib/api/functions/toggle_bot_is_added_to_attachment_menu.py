# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleBotIsAddedToAttachmentMenu(BaseObject):
    """
    Adds or removes a bot to attachment menu. Bot can be added to attachment menu, only if userTypeBot.can_be_added_to_attachment_menu == true
    
    :param bot_user_id: Bot's user identifier
    :type bot_user_id: :class:`int`
    
    :param is_added: Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu
    :type is_added: :class:`bool`
    
    """

    ID: str = Field("toggleBotIsAddedToAttachmentMenu", alias="@type")
    bot_user_id: int
    is_added: bool

    @staticmethod
    def read(q: dict) -> ToggleBotIsAddedToAttachmentMenu:
        return ToggleBotIsAddedToAttachmentMenu.construct(**q)
