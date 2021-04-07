# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteAccount(BaseObject):
    """
    Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword
    
    Params:
        reason (:class:`str`)
            The reason why the account was deleted; optional
        
    """

    ID: str = Field("deleteAccount", alias="@type")
    reason: str

    @staticmethod
    def read(q: dict) -> DeleteAccount:
        return DeleteAccount.construct(**q)
