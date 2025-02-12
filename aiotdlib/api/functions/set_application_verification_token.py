# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetApplicationVerificationToken(BaseObject):
    """
    Application or reCAPTCHA verification has been completed. Can be called before authorization

    :param verification_id: Unique identifier for the verification process as received from updateApplicationVerificationRequired or updateApplicationRecaptchaVerificationRequired
    :type verification_id: :class:`Int53`
    :param token: Play Integrity API token for the Android application, or secret from push notification for the iOS application for application verification, or reCAPTCHA token for reCAPTCHA verifications; pass an empty string to abort verification and receive error VERIFICATION_FAILED for the request
    :type token: :class:`String`
    """

    ID: typing.Literal["setApplicationVerificationToken"] = Field(
        "setApplicationVerificationToken", validation_alias="@type", alias="@type"
    )
    verification_id: Int53
    token: String
