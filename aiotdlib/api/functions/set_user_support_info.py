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
    FormattedText,
)


class SetUserSupportInfo(BaseObject):
    """
    Sets support information for the given user; for Telegram support only

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param message: New information message
    :type message: :class:`FormattedText`
    """

    ID: typing.Literal["setUserSupportInfo"] = "setUserSupportInfo"
    user_id: Int53
    message: FormattedText
