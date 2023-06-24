# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPassportAuthorizationForm(BaseObject):
    """
    Returns a Telegram Passport authorization form for sharing data with a service

    :param bot_user_id: User identifier of the service's bot
    :type bot_user_id: :class:`Int53`
    :param scope: Telegram Passport element types requested by the service
    :type scope: :class:`String`
    :param public_key: Service's public key
    :type public_key: :class:`String`
    :param nonce: Unique request identifier provided by the service
    :type nonce: :class:`String`
    """

    ID: typing.Literal["getPassportAuthorizationForm"] = "getPassportAuthorizationForm"
    bot_user_id: Int53
    scope: String
    public_key: String
    nonce: String
