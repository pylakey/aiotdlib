# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageImportConfirmationText(BaseObject):
    """
    Returns a confirmation text to be shown to the user before starting message import
    
    Params:
        chat_id (:class:`int`)
            Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
        
    """

    ID: str = Field("getMessageImportConfirmationText", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetMessageImportConfirmationText:
        return GetMessageImportConfirmationText.construct(**q)
