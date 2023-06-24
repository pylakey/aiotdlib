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
    CallProtocol,
)


class CreateCall(BaseObject):
    """
    Creates a new call

    :param user_id: Identifier of the user to be called
    :type user_id: :class:`Int53`
    :param protocol: The call protocols supported by the application
    :type protocol: :class:`CallProtocol`
    :param is_video: Pass true to create a video call
    :type is_video: :class:`Bool`
    """

    ID: typing.Literal["createCall"] = "createCall"
    user_id: Int53
    protocol: CallProtocol
    is_video: Bool = False
