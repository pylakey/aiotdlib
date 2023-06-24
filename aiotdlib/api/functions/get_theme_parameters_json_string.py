# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    ThemeParameters,
)


class GetThemeParametersJsonString(BaseObject):
    """
    Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously

    :param theme: Theme parameters to convert to JSON
    :type theme: :class:`ThemeParameters`
    """

    ID: typing.Literal["getThemeParametersJsonString"] = "getThemeParametersJsonString"
    theme: ThemeParameters
