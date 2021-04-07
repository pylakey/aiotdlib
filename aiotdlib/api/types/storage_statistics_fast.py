# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class StorageStatisticsFast(BaseObject):
    """
    Contains approximate storage usage statistics, excluding files of unknown file type
    
    Params:
        files_size (:class:`int`)
            Approximate total size of files
        
        file_count (:class:`int`)
            Approximate number of files
        
        database_size (:class:`int`)
            Size of the database
        
        language_pack_database_size (:class:`int`)
            Size of the language pack database
        
        log_size (:class:`int`)
            Size of the TDLib internal log
        
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
