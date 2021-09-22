# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    
    :param url: The URL to open
    :type url: :class:`str`
    
    :param skip_confirm: True, if there is no need to show an ordinary open URL confirm
    :type skip_confirm: :class:`bool`
    
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
    
    :param url: An HTTP URL to be opened
    :type url: :class:`str`
    
    :param domain: A domain of the URL
    :type domain: :class:`str`
    
    :param bot_user_id: User identifier of a bot linked with the website
    :type bot_user_id: :class:`int`
    
    :param request_write_access: True, if the user needs to be requested to give the permission to the bot to send them messages
    :type request_write_access: :class:`bool`
    
    """

    ID: str = Field("loginUrlInfoRequestConfirmation", alias="@type")
    url: str
    domain: str
    bot_user_id: int
    request_write_access: bool

    @staticmethod
    def read(q: dict) -> LoginUrlInfoRequestConfirmation:
        return LoginUrlInfoRequestConfirmation.construct(**q)
