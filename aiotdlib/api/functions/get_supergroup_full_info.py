# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSupergroupFullInfo(BaseObject):
    """
    Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute

    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["getSupergroupFullInfo"] = "getSupergroupFullInfo"
    supergroup_id: Int53
