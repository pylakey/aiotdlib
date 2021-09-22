# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class AutoDownloadSettings(BaseObject):
    """
    Contains auto-download settings
    
    :param is_auto_download_enabled: True, if the auto-download is enabled
    :type is_auto_download_enabled: :class:`bool`
    
    :param max_photo_file_size: The maximum size of a photo file to be auto-downloaded, in bytes
    :type max_photo_file_size: :class:`int`
    
    :param max_video_file_size: The maximum size of a video file to be auto-downloaded, in bytes
    :type max_video_file_size: :class:`int`
    
    :param max_other_file_size: The maximum size of other file types to be auto-downloaded, in bytes
    :type max_other_file_size: :class:`int`
    
    :param video_upload_bitrate: The maximum suggested bitrate for uploaded videos, in kbit/s
    :type video_upload_bitrate: :class:`int`
    
    :param preload_large_videos: True, if the beginning of video files needs to be preloaded for instant playback
    :type preload_large_videos: :class:`bool`
    
    :param preload_next_audio: True, if the next audio track needs to be preloaded while the user is listening to an audio file
    :type preload_next_audio: :class:`bool`
    
    :param use_less_data_for_calls: True, if "use less data for calls" option needs to be enabled
    :type use_less_data_for_calls: :class:`bool`
    
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
