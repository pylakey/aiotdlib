# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendPhoneNumberFirebaseSms(BaseObject):
    """
    Sends Firebase Authentication SMS to the specified phone number. Works only when received a code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

    :param token: Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application
    :type token: :class:`String`
    """

    ID: typing.Literal["sendPhoneNumberFirebaseSms"] = Field(
        "sendPhoneNumberFirebaseSms", validation_alias="@type", alias="@type"
    )
    token: String
