# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveAllFilesFromDownloads(BaseObject):
    """
    Removes all files from the file download list

    :param only_active: Pass true to remove only active downloads, including paused
    :type only_active: :class:`Bool`
    :param only_completed: Pass true to remove only completed downloads
    :type only_completed: :class:`Bool`
    :param delete_from_cache: Pass true to delete the file from the TDLib file cache
    :type delete_from_cache: :class:`Bool`
    """

    ID: typing.Literal["removeAllFilesFromDownloads"] = "removeAllFilesFromDownloads"
    only_active: Bool = False
    only_completed: Bool = False
    delete_from_cache: Bool = False
