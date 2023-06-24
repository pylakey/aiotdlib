# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteSavedCredentials(BaseObject):
    """
    Deletes saved credentials for all payment provider bots
    """

    ID: typing.Literal["deleteSavedCredentials"] = "deleteSavedCredentials"
