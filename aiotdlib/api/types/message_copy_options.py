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
    Options to be used when a message content is copied without reference to the original sender. Service messages and messageInvoice can't be copied
    
    :param send_copy: True, if content of the message needs to be copied without reference to the original sender. Always true if the message is forwarded to a secret chat or is local
    :type send_copy: :class:`bool`
    
    :param replace_caption: True, if media caption of the message copy needs to be replaced. Ignored if send_copy is false
    :type replace_caption: :class:`bool`
    
    :param new_caption: New message caption; pass null to copy message without caption. Ignored if replace_caption is false
    :type new_caption: :class:`FormattedText`
    
    """

    ID: str = Field("messageCopyOptions", alias="@type")
    send_copy: bool
    replace_caption: bool
    new_caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageCopyOptions:
        return MessageCopyOptions.construct(**q)
