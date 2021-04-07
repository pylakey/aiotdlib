# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPassportAuthorizationForm(BaseObject):
    """
    Returns a Telegram Passport authorization form for sharing data with a service
    
    Params:
        bot_user_id (:class:`int`)
            User identifier of the service's bot
        
        scope (:class:`str`)
            Telegram Passport element types requested by the service
        
        public_key (:class:`str`)
            Service's public_key
        
        nonce (:class:`str`)
            Authorization form nonce provided by the service
        
    """

    ID: str = Field("getPassportAuthorizationForm", alias="@type")
    bot_user_id: int
    scope: str
    public_key: str
    nonce: str

    @staticmethod
    def read(q: dict) -> GetPassportAuthorizationForm:
        return GetPassportAuthorizationForm.construct(**q)
