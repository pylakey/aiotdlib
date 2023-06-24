# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetCountries(BaseObject):
    """
    Returns information about existing countries. Can be called before authorization
    """

    ID: typing.Literal["getCountries"] = "getCountries"
