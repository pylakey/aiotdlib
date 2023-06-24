# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetInlineGameScore(BaseObject):
    """
    Updates the game score of the specified user in a game; for bots only

    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`String`
    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param score: The new score
    :type score: :class:`Int32`
    :param edit_message: Pass true to edit the game message to include the current scoreboard
    :type edit_message: :class:`Bool`
    :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
    :type force: :class:`Bool`
    """

    ID: typing.Literal["setInlineGameScore"] = "setInlineGameScore"
    inline_message_id: String
    user_id: Int53
    score: Int32
    edit_message: Bool = False
    force: Bool = False
