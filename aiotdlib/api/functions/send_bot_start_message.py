# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SendBotStartMessage(BaseObject):
    """
    Invites a bot to a chat (if it is not yet a member) and sends it the /start command. Bots can't be invited to a private chat other than the chat with the bot. Bots can't be invited to channels (although they can be added as admins) and secret chats. Returns the sent message
    
    Params:
        bot_user_id (:class:`int`)
            Identifier of the bot
        
        chat_id (:class:`int`)
            Identifier of the target chat
        
        parameter (:class:`str`)
            A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)
        
    """

    ID: str = Field("sendBotStartMessage", alias="@type")
    bot_user_id: int
    chat_id: int
    parameter: str

    @staticmethod
    def read(q: dict) -> SendBotStartMessage:
        return SendBotStartMessage.construct(**q)
