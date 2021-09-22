# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ResetPasswordResult(BaseObject):
    """
    Represents result of 2-step verification password reset
    
    """

    ID: str = Field("resetPasswordResult", alias="@type")


class ResetPasswordResultDeclined(ResetPasswordResult):
    """
    The password reset request was declined
    
    :param retry_date: Point in time (Unix timestamp) when the password reset can be retried
    :type retry_date: :class:`int`
    
    """

    ID: str = Field("resetPasswordResultDeclined", alias="@type")
    retry_date: int

    @staticmethod
    def read(q: dict) -> ResetPasswordResultDeclined:
        return ResetPasswordResultDeclined.construct(**q)


class ResetPasswordResultOk(ResetPasswordResult):
    """
    The password was reset
    
    """

    ID: str = Field("resetPasswordResultOk", alias="@type")

    @staticmethod
    def read(q: dict) -> ResetPasswordResultOk:
        return ResetPasswordResultOk.construct(**q)


class ResetPasswordResultPending(ResetPasswordResult):
    """
    The password reset request is pending
    
    :param pending_reset_date: Point in time (Unix timestamp) after which the password can be reset immediately using resetPassword
    :type pending_reset_date: :class:`int`
    
    """

    ID: str = Field("resetPasswordResultPending", alias="@type")
    pending_reset_date: int

    @staticmethod
    def read(q: dict) -> ResetPasswordResultPending:
        return ResetPasswordResultPending.construct(**q)
