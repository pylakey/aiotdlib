# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .formatted_text import FormattedText
from ..base_object import BaseObject


class TermsOfService(BaseObject):
    """
    Contains Telegram terms of service
    
    Params:
        text (:class:`FormattedText`)
            Text of the terms of service
        
        min_user_age (:class:`int`)
            The minimum age of a user to be able to accept the terms; 0 if any
        
        show_popup (:class:`bool`)
            True, if a blocking popup with terms of service must be shown to the user
        
    """

    ID: str = Field("termsOfService", alias="@type")
    text: FormattedText
    min_user_age: int
    show_popup: bool

    @staticmethod
    def read(q: dict) -> TermsOfService:
        return TermsOfService.construct(**q)
