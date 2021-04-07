# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .passport_required_element import PassportRequiredElement
from ..base_object import BaseObject


class PassportAuthorizationForm(BaseObject):
    """
    Contains information about a Telegram Passport authorization form that was requested
    
    Params:
        id (:class:`int`)
            Unique identifier of the authorization form
        
        required_elements (:obj:`list[PassportRequiredElement]`)
            Information about the Telegram Passport elements that must be provided to complete the form
        
        privacy_policy_url (:class:`str`)
            URL for the privacy policy of the service; may be empty
        
    """

    ID: str = Field("passportAuthorizationForm", alias="@type")
    id: int
    required_elements: list[PassportRequiredElement]
    privacy_policy_url: str

    @staticmethod
    def read(q: dict) -> PassportAuthorizationForm:
        return PassportAuthorizationForm.construct(**q)
