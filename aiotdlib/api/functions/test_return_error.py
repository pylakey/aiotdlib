# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import Error


class TestReturnError(BaseObject):
    """
    Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously
    
    Params:
        error (:class:`Error`)
            The error to be returned
        
    """

    ID: str = Field("testReturnError", alias="@type")
    error: Error

    @staticmethod
    def read(q: dict) -> TestReturnError:
        return TestReturnError.construct(**q)
