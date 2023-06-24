# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveFileFromDownloads(BaseObject):
    """
    Removes a file from the file download list

    :param file_id: Identifier of the downloaded file
    :type file_id: :class:`Int32`
    :param delete_from_cache: Pass true to delete the file from the TDLib file cache
    :type delete_from_cache: :class:`Bool`
    """

    ID: typing.Literal["removeFileFromDownloads"] = "removeFileFromDownloads"
    file_id: Int32
    delete_from_cache: Bool = False
