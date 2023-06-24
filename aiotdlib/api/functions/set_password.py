# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetPassword(BaseObject):
    """
    Changes the 2-step verification password for the current user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed

    :param old_password: Previous 2-step verification password of the user
    :type old_password: :class:`String`
    :param new_password: New 2-step verification password of the user; may be empty to remove the password
    :type new_password: :class:`String`
    :param new_hint: New password hint; may be empty
    :type new_hint: :class:`String`
    :param set_recovery_email_address: Pass true to change also the recovery email address
    :type set_recovery_email_address: :class:`Bool`
    :param new_recovery_email_address: New recovery email address; may be empty
    :type new_recovery_email_address: :class:`String`
    """

    ID: typing.Literal["setPassword"] = "setPassword"
    old_password: String
    new_password: String = ""
    new_hint: String = ""
    set_recovery_email_address: Bool = False
    new_recovery_email_address: String = ""
