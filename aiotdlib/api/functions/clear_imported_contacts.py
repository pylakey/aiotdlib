# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearImportedContacts(BaseObject):
    """
    Clears all imported contacts, contact list remains unchanged
    """

    ID: typing.Literal["clearImportedContacts"] = "clearImportedContacts"
