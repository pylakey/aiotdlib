# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EndGroupCallScreenSharing(BaseObject):
    """
    Ends screen sharing in a joined group call

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["endGroupCallScreenSharing"] = "endGroupCallScreenSharing"
    group_call_id: Int32
