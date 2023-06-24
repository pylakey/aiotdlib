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
    Contact,
)


class ChangeImportedContacts(BaseObject):
    """
    Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts. Query result depends on the result of the previous query, so only one query is possible at the same time

    :param contacts: The new list of contacts, contact's vCard are ignored and are not imported
    :type contacts: :class:`Vector[Contact]`
    """

    ID: typing.Literal["changeImportedContacts"] = "changeImportedContacts"
    contacts: Vector[Contact]
