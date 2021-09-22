# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetPassportAuthorizationForm(BaseObject):
    """
    Returns a Telegram Passport authorization form for sharing data with a service
    
    :param bot_user_id: User identifier of the service's bot
    :type bot_user_id: :class:`int`
    
    :param scope: Telegram Passport element types requested by the service
    :type scope: :class:`str`
    
    :param public_key: Service's public key
    :type public_key: :class:`str`
    
    :param nonce: Unique request identifier provided by the service
    :type nonce: :class:`str`
    
    """

    ID: str = Field("getPassportAuthorizationForm", alias="@type")
    bot_user_id: int
    scope: str
    public_key: str
    nonce: str

    @staticmethod
    def read(q: dict) -> GetPassportAuthorizationForm:
        return GetPassportAuthorizationForm.construct(**q)
