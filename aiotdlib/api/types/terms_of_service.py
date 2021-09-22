# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .formatted_text import FormattedText
from ..base_object import BaseObject


class TermsOfService(BaseObject):
    """
    Contains Telegram terms of service
    
    :param text: Text of the terms of service
    :type text: :class:`FormattedText`
    
    :param min_user_age: The minimum age of a user to be able to accept the terms; 0 if any
    :type min_user_age: :class:`int`
    
    :param show_popup: True, if a blocking popup with terms of service must be shown to the user
    :type show_popup: :class:`bool`
    
    """

    ID: str = Field("termsOfService", alias="@type")
    text: FormattedText
    min_user_age: int
    show_popup: bool

    @staticmethod
    def read(q: dict) -> TermsOfService:
        return TermsOfService.construct(**q)
