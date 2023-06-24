# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputPassportElementError,
)


class SetPassportElementErrors(BaseObject):
    """
    Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param errors: The errors
    :type errors: :class:`Vector[InputPassportElementError]`
    """

    ID: typing.Literal["setPassportElementErrors"] = "setPassportElementErrors"
    user_id: Int53
    errors: Vector[InputPassportElementError]
