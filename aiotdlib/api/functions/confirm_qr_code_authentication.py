# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ConfirmQrCodeAuthentication(BaseObject):
    """
    Confirms QR code authentication on another device. Returns created session on success
    
    Params:
        link (:class:`str`)
            A link from a QR code. The link must be scanned by the in-app camera
        
    """

    ID: str = Field("confirmQrCodeAuthentication", alias="@type")
    link: str

    @staticmethod
    def read(q: dict) -> ConfirmQrCodeAuthentication:
        return ConfirmQrCodeAuthentication.construct(**q)
