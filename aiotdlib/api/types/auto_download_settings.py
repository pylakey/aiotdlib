# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AutoDownloadSettings(BaseObject):
    """
    Contains auto-download settings
    
    Params:
        is_auto_download_enabled (:class:`bool`)
            True, if the auto-download is enabled
        
        max_photo_file_size (:class:`int`)
            The maximum size of a photo file to be auto-downloaded
        
        max_video_file_size (:class:`int`)
            The maximum size of a video file to be auto-downloaded
        
        max_other_file_size (:class:`int`)
            The maximum size of other file types to be auto-downloaded
        
        video_upload_bitrate (:class:`int`)
            The maximum suggested bitrate for uploaded videos, in kbit/s
        
        preload_large_videos (:class:`bool`)
            True, if the beginning of video files needs to be preloaded for instant playback
        
        preload_next_audio (:class:`bool`)
            True, if the next audio track needs to be preloaded while the user is listening to an audio file
        
        use_less_data_for_calls (:class:`bool`)
            True, if "use less data for calls" option needs to be enabled
        
    """

    ID: str = Field("autoDownloadSettings", alias="@type")
    is_auto_download_enabled: bool
    max_photo_file_size: int
    max_video_file_size: int
    max_other_file_size: int
    video_upload_bitrate: int
    preload_large_videos: bool
    preload_next_audio: bool
    use_less_data_for_calls: bool

    @staticmethod
    def read(q: dict) -> AutoDownloadSettings:
        return AutoDownloadSettings.construct(**q)
