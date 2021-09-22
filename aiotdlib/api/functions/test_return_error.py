# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import Error
from ..base_object import BaseObject


class TestReturnError(BaseObject):
    """
    Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously
    
    :param error: The error to be returned
    :type error: :class:`Error`
    
    """

    ID: str = Field("testReturnError", alias="@type")
    error: Error

    @staticmethod
    def read(q: dict) -> TestReturnError:
        return TestReturnError.construct(**q)
