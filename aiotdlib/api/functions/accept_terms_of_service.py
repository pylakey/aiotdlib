# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AcceptTermsOfService(BaseObject):
    """
    Accepts Telegram terms of services
    
    Params:
        terms_of_service_id (:class:`str`)
            Terms of service identifier
        
    """

    ID: str = Field("acceptTermsOfService", alias="@type")
    terms_of_service_id: str

    @staticmethod
    def read(q: dict) -> AcceptTermsOfService:
        return AcceptTermsOfService.construct(**q)
