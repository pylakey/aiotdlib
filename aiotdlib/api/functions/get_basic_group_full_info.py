# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBasicGroupFullInfo(BaseObject):
    """
    Returns full information about a basic group by its identifier

    :param basic_group_id: Basic group identifier
    :type basic_group_id: :class:`Int53`
    """

    ID: typing.Literal["getBasicGroupFullInfo"] = "getBasicGroupFullInfo"
    basic_group_id: Int53
