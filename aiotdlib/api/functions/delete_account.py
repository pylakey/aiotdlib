# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteAccount(BaseObject):
    """
    Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword

    :param reason: The reason why the account was deleted; optional
    :type reason: :class:`String`
    :param password: The 2-step verification password of the current user. If not specified, account deletion can be canceled within one week
    :type password: :class:`String`
    """

    ID: typing.Literal["deleteAccount"] = "deleteAccount"
    reason: String
    password: String
