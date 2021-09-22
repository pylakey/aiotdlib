# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class StorageStatisticsFast(BaseObject):
    """
    Contains approximate storage usage statistics, excluding files of unknown file type
    
    :param files_size: Approximate total size of files, in bytes
    :type files_size: :class:`int`
    
    :param file_count: Approximate number of files
    :type file_count: :class:`int`
    
    :param database_size: Size of the database
    :type database_size: :class:`int`
    
    :param language_pack_database_size: Size of the language pack database
    :type language_pack_database_size: :class:`int`
    
    :param log_size: Size of the TDLib internal log
    :type log_size: :class:`int`
    
    """

    ID: str = Field("storageStatisticsFast", alias="@type")
    files_size: int
    file_count: int
    database_size: int
    language_pack_database_size: int
    log_size: int

    @staticmethod
    def read(q: dict) -> StorageStatisticsFast:
        return StorageStatisticsFast.construct(**q)
