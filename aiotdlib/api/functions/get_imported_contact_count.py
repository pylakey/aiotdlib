# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetImportedContactCount(BaseObject):
    """
    Returns the total number of imported contacts
    """

    ID: typing.Literal["getImportedContactCount"] = "getImportedContactCount"
