# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import PassportElementType
from ..base_object import BaseObject


class SendPassportAuthorizationForm(BaseObject):
    """
    Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused
    
    :param autorization_form_id: Authorization form identifier
    :type autorization_form_id: :class:`int`
    
    :param types: Types of Telegram Passport elements chosen by user to complete the authorization form
    :type types: :class:`list[PassportElementType]`
    
    """

    ID: str = Field("sendPassportAuthorizationForm", alias="@type")
    autorization_form_id: int
    types: list[PassportElementType]

    @staticmethod
    def read(q: dict) -> SendPassportAuthorizationForm:
        return SendPassportAuthorizationForm.construct(**q)
