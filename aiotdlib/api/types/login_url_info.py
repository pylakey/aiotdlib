# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LoginUrlInfo(BaseObject):
    """
    Contains information about an inline button of type inlineKeyboardButtonTypeLoginUrl
    
    """

    ID: str = Field("loginUrlInfo", alias="@type")


class LoginUrlInfoOpen(LoginUrlInfo):
    """
    An HTTP url needs to be open
    
    Params:
        url (:class:`str`)
            The URL to open
        
        skip_confirm (:class:`bool`)
            True, if there is no need to show an ordinary open URL confirm
        
    """

    ID: str = Field("loginUrlInfoOpen", alias="@type")
    url: str
    skip_confirm: bool

    @staticmethod
    def read(q: dict) -> LoginUrlInfoOpen:
        return LoginUrlInfoOpen.construct(**q)


class LoginUrlInfoRequestConfirmation(LoginUrlInfo):
    """
    An authorization confirmation dialog needs to be shown to the user
    
    Params:
        url (:class:`str`)
            An HTTP URL to be opened
        
        domain (:class:`str`)
            A domain of the URL
        
        bot_user_id (:class:`int`)
            User identifier of a bot linked with the website
        
        request_write_access (:class:`bool`)
            True, if the user needs to be requested to give the permission to the bot to send them messages
        
    """

    ID: str = Field("loginUrlInfoRequestConfirmation", alias="@type")
    url: str
    domain: str
    bot_user_id: int
    request_write_access: bool

    @staticmethod
    def read(q: dict) -> LoginUrlInfoRequestConfirmation:
        return LoginUrlInfoRequestConfirmation.construct(**q)
