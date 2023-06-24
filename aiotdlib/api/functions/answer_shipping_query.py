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
    ShippingOption,
)


class AnswerShippingQuery(BaseObject):
    """
    Sets the result of a shipping query; for bots only

    :param shipping_query_id: Identifier of the shipping query
    :type shipping_query_id: :class:`Int64`
    :param shipping_options: Available shipping options
    :type shipping_options: :class:`Vector[ShippingOption]`
    :param error_message: An error message, empty on success
    :type error_message: :class:`String`
    """

    ID: typing.Literal["answerShippingQuery"] = "answerShippingQuery"
    shipping_query_id: Int64
    shipping_options: Vector[ShippingOption]
    error_message: String
