# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputFile
from ..base_object import BaseObject


class ImportMessages(BaseObject):
    """
    Imports messages exported from another app
    
    :param chat_id: Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
    :type chat_id: :class:`int`
    
    :param message_file: File with messages to import. Only inputFileLocal and inputFileGenerated are supported. The file must not be previously uploaded
    :type message_file: :class:`InputFile`
    
    :param attached_files: Files used in the imported messages. Only inputFileLocal and inputFileGenerated are supported. The files must not be previously uploaded
    :type attached_files: :class:`list[InputFile]`
    
    """

    ID: str = Field("importMessages", alias="@type")
    chat_id: int
    message_file: InputFile
    attached_files: list[InputFile]

    @staticmethod
    def read(q: dict) -> ImportMessages:
        return ImportMessages.construct(**q)
