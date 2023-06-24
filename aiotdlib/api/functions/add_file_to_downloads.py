# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AddFileToDownloads(BaseObject):
    """
    Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates. If message database is used, the list of file downloads is persistent across application restarts. The downloading is independent from download using downloadFile, i.e. it continues if downloadFile is canceled or is used to download a part of the file

    :param file_id: Identifier of the file to download
    :type file_id: :class:`Int32`
    :param chat_id: Chat identifier of the message with the file
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param priority: Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first
    :type priority: :class:`Int32`
    """

    ID: typing.Literal["addFileToDownloads"] = "addFileToDownloads"
    file_id: Int32
    chat_id: Int53
    message_id: Int53
    priority: Int32
