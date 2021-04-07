# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPassportAuthorizationFormAvailableElements(BaseObject):
    """
    Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form
    
    Params:
        autorization_form_id (:class:`int`)
            Authorization form identifier
        
        password (:class:`str`)
            Password of the current user
        
    """

    ID: str = Field("getPassportAuthorizationFormAvailableElements", alias="@type")
    autorization_form_id: int
    password: str

    @staticmethod
    def read(q: dict) -> GetPassportAuthorizationFormAvailableElements:
        return GetPassportAuthorizationFormAvailableElements.construct(**q)
