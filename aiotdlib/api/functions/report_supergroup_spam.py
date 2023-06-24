# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReportSupergroupSpam(BaseObject):
    """
    Reports messages in a supergroup as spam; requires administrator rights in the supergroup

    :param supergroup_id: Supergroup identifier
    :type supergroup_id: :class:`Int53`
    :param message_ids: Identifiers of messages to report
    :type message_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["reportSupergroupSpam"] = "reportSupergroupSpam"
    supergroup_id: Int53
    message_ids: Vector[Int53]
