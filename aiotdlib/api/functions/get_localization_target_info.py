# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetLocalizationTargetInfo(BaseObject):
    """
    Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization

    :param only_local: Pass true to get only locally available information without sending network requests
    :type only_local: :class:`Bool`
    """

    ID: typing.Literal["getLocalizationTargetInfo"] = "getLocalizationTargetInfo"
    only_local: Bool = False
