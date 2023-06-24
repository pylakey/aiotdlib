# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPhoneNumberInfoSync(BaseObject):
    """
    Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously

    :param language_code: A two-letter ISO 639-1 language code for country information localization
    :type language_code: :class:`String`
    :param phone_number_prefix: The phone number prefix
    :type phone_number_prefix: :class:`String`
    """

    ID: typing.Literal["getPhoneNumberInfoSync"] = "getPhoneNumberInfoSync"
    language_code: String
    phone_number_prefix: String
