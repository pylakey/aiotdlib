# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputPassportElementError
from ..base_object import BaseObject


class SetPassportElementErrors(BaseObject):
    """
    Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param errors: The errors
    :type errors: :class:`list[InputPassportElementError]`
    
    """

    ID: str = Field("setPassportElementErrors", alias="@type")
    user_id: int
    errors: list[InputPassportElementError]

    @staticmethod
    def read(q: dict) -> SetPassportElementErrors:
        return SetPassportElementErrors.construct(**q)
