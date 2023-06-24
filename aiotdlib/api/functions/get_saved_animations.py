# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSavedAnimations(BaseObject):
    """
    Returns saved animations
    """

    ID: typing.Literal["getSavedAnimations"] = "getSavedAnimations"
