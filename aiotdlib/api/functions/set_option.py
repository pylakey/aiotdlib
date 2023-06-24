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
    OptionValue,
)


class SetOption(BaseObject):
    """
    Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization

    :param name: The name of the option
    :type name: :class:`String`
    :param value: The new value of the option; pass null to reset option value to a default value, defaults to None
    :type value: :class:`OptionValue`, optional
    """

    ID: typing.Literal["setOption"] = "setOption"
    name: String
    value: typing.Optional[OptionValue] = None
