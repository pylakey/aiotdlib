# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AcceptTermsOfService(BaseObject):
    """
    Accepts Telegram terms of services

    :param terms_of_service_id: Terms of service identifier
    :type terms_of_service_id: :class:`String`
    """

    ID: typing.Literal["acceptTermsOfService"] = "acceptTermsOfService"
    terms_of_service_id: String
