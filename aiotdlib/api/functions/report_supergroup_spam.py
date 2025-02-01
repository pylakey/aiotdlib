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
    :param message_ids: Identifiers of messages to report. Use messageProperties.can_report_supergroup_spam to check whether the message can be reported
    :type message_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["reportSupergroupSpam"] = Field("reportSupergroupSpam", validation_alias="@type", alias="@type")
    supergroup_id: Int53
    message_ids: Vector[Int53]
