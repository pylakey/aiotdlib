# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CreatePrivateChat(BaseObject):
    """
    Returns an existing chat corresponding to a given user

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param force: Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect
    :type force: :class:`Bool`
    """

    ID: typing.Literal["createPrivateChat"] = "createPrivateChat"
    user_id: Int53
    force: Bool = False
