# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveContacts(BaseObject):
    """
    Removes users from the contact list

    :param user_ids: Identifiers of users to be deleted
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["removeContacts"] = "removeContacts"
    user_ids: Vector[Int53]
