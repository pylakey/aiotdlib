# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckAuthenticationBotToken(BaseObject):
    """
    Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in
    
    Params:
        token (:class:`str`)
            The bot token
        
    """

    ID: str = Field("checkAuthenticationBotToken", alias="@type")
    token: str

    @staticmethod
    def read(q: dict) -> CheckAuthenticationBotToken:
        return CheckAuthenticationBotToken.construct(**q)
