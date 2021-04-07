# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputPassportElementError


class SetPassportElementErrors(BaseObject):
    """
    Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        errors (:obj:`list[InputPassportElementError]`)
            The errors
        
    """

    ID: str = Field("setPassportElementErrors", alias="@type")
    user_id: int
    errors: list[InputPassportElementError]

    @staticmethod
    def read(q: dict) -> SetPassportElementErrors:
        return SetPassportElementErrors.construct(**q)
