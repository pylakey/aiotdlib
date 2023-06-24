# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendAuthenticationFirebaseSms(BaseObject):
    """
    Sends Firebase Authentication SMS to the phone number of the user. Works only when the current authorization state is authorizationStateWaitCode and the server returned code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

    :param token: SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application
    :type token: :class:`String`
    """

    ID: typing.Literal["sendAuthenticationFirebaseSms"] = "sendAuthenticationFirebaseSms"
    token: String
