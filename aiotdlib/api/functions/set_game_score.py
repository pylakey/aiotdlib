# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetGameScore(BaseObject):
    """
    Updates the game score of the specified user in the game; for bots only

    :param chat_id: The chat to which the message with the game belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param score: The new score
    :type score: :class:`Int32`
    :param edit_message: Pass true to edit the game message to include the current scoreboard
    :type edit_message: :class:`Bool`
    :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
    :type force: :class:`Bool`
    """

    ID: typing.Literal["setGameScore"] = "setGameScore"
    chat_id: Int53
    message_id: Int53
    user_id: Int53
    score: Int32
    edit_message: Bool = False
    force: Bool = False
