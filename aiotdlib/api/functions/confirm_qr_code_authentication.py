# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ConfirmQrCodeAuthentication(BaseObject):
    """
    Confirms QR code authentication on another device. Returns created session on success

    :param link: A link from a QR code. The link must be scanned by the in-app camera
    :type link: :class:`String`
    """

    ID: typing.Literal["confirmQrCodeAuthentication"] = "confirmQrCodeAuthentication"
    link: String
