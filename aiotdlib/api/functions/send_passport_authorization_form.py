# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PassportElementType


class SendPassportAuthorizationForm(BaseObject):
    """
    Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused
    
    Params:
        autorization_form_id (:class:`int`)
            Authorization form identifier
        
        types (:obj:`list[PassportElementType]`)
            Types of Telegram Passport elements chosen by user to complete the authorization form
        
    """

    ID: str = Field("sendPassportAuthorizationForm", alias="@type")
    autorization_form_id: int
    types: list[PassportElementType]

    @staticmethod
    def read(q: dict) -> SendPassportAuthorizationForm:
        return SendPassportAuthorizationForm.construct(**q)
