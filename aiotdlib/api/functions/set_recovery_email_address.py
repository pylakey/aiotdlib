# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetRecoveryEmailAddress(BaseObject):
    """
    Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed. If new_recovery_email_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation

    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    :param new_recovery_email_address: New recovery email address
    :type new_recovery_email_address: :class:`String`
    """

    ID: typing.Literal["setRecoveryEmailAddress"] = "setRecoveryEmailAddress"
    password: String
    new_recovery_email_address: String
