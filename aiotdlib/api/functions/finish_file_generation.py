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
    Error,
)


class FinishFileGeneration(BaseObject):
    """
    Finishes the file generation

    :param generation_id: The identifier of the generation process
    :type generation_id: :class:`Int64`
    :param error: If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded, defaults to None
    :type error: :class:`Error`, optional
    """

    ID: typing.Literal["finishFileGeneration"] = "finishFileGeneration"
    generation_id: Int64
    error: typing.Optional[Error] = None
