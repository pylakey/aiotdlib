# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .formatted_text import FormattedText
from ..base_object import BaseObject


class MessageCopyOptions(BaseObject):
    """
    Options to be used when a message content is copied without a link to the original message. Service messages and messageInvoice can't be copied
    
    Params:
        send_copy (:class:`bool`)
            True, if content of the message needs to be copied without a link to the original message. Always true if the message is forwarded to a secret chat
        
        replace_caption (:class:`bool`)
            True, if media caption of the message copy needs to be replaced. Ignored if send_copy is false
        
        new_caption (:class:`FormattedText`)
            New message caption. Ignored if replace_caption is false
        
    """

    ID: str = Field("messageCopyOptions", alias="@type")
    send_copy: bool
    replace_caption: bool
    new_caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageCopyOptions:
        return MessageCopyOptions.construct(**q)
