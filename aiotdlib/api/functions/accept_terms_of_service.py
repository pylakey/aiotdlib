# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class AcceptTermsOfService(BaseObject):
    """
    Accepts Telegram terms of services
    
    :param terms_of_service_id: Terms of service identifier
    :type terms_of_service_id: :class:`str`
    
    """

    ID: str = Field("acceptTermsOfService", alias="@type")
    terms_of_service_id: str

    @staticmethod
    def read(q: dict) -> AcceptTermsOfService:
        return AcceptTermsOfService.construct(**q)
