# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .base import *


class AccountTtl(BaseObject):
    """
    Contains information about the period of inactivity after which the current user's account will automatically be deleted

    :param days: Number of days of inactivity before the account will be flagged for deletion; 30-366 days
    :type days: :class:`Int32`
    """

    ID: typing.Literal["accountTtl"] = "accountTtl"
    days: Int32


class AddedReaction(BaseObject):
    """
    Represents a reaction applied to a message

    :param type_: Type of the reaction
    :type type_: :class:`ReactionType`
    :param sender_id: Identifier of the chat member, applied the reaction
    :type sender_id: :class:`MessageSender`
    :param date: Point in time (Unix timestamp) when the reaction was added
    :type date: :class:`Int32`
    """

    ID: typing.Literal["addedReaction"] = "addedReaction"
    type_: ReactionType = Field(..., alias="type")
    sender_id: MessageSender
    date: Int32


class AddedReactions(BaseObject):
    """
    Represents a list of reactions added to a message

    :param total_count: The total number of found reactions
    :type total_count: :class:`Int32`
    :param reactions: The list of added reactions
    :type reactions: :class:`Vector[AddedReaction]`
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`String`
    """

    ID: typing.Literal["addedReactions"] = "addedReactions"
    total_count: Int32
    reactions: Vector[AddedReaction]
    next_offset: String


class Address(BaseObject):
    """
    Describes an address

    :param country_code: A two-letter ISO 3166-1 alpha-2 country code
    :type country_code: :class:`String`
    :param state: State, if applicable
    :type state: :class:`String`
    :param city: City
    :type city: :class:`String`
    :param street_line1: First line of the address
    :type street_line1: :class:`String`
    :param street_line2: Second line of the address
    :type street_line2: :class:`String`
    :param postal_code: Address postal code
    :type postal_code: :class:`String`
    """

    ID: typing.Literal["address"] = "address"
    country_code: String
    state: String
    city: String
    street_line1: String
    street_line2: String
    postal_code: String


class AnimatedChatPhoto(BaseObject):
    """
    Animated variant of a chat photo in MPEG4 format

    :param length: Animation width and height
    :type length: :class:`Int32`
    :param file: Information about the animation file
    :type file: :class:`File`
    :param main_frame_timestamp: Timestamp of the frame, used as a static chat photo
    :type main_frame_timestamp: :class:`Double`
    """

    ID: typing.Literal["animatedChatPhoto"] = "animatedChatPhoto"
    length: Int32
    file: File
    main_frame_timestamp: Double


class AnimatedEmoji(BaseObject):
    """
    Describes an animated or custom representation of an emoji

    :param sticker_width: Expected width of the sticker, which can be used if the sticker is null
    :type sticker_width: :class:`Int32`
    :param sticker_height: Expected height of the sticker, which can be used if the sticker is null
    :type sticker_height: :class:`Int32`
    :param sticker: Sticker for the emoji; may be null if yet unknown for a custom emoji. If the sticker is a custom emoji, it can have arbitrary format different from stickerFormatTgs, defaults to None
    :type sticker: :class:`Sticker`, optional
    :param sound: File containing the sound to be played when the sticker is clicked; may be null. The sound is encoded with the Opus codec, and stored inside an OGG container, defaults to None
    :type sound: :class:`File`, optional
    :param fitzpatrick_type: Emoji modifier fitzpatrick type; 0-6; 0 if none, defaults to None
    :type fitzpatrick_type: :class:`Int32`, optional
    """

    ID: typing.Literal["animatedEmoji"] = "animatedEmoji"
    sticker_width: Int32
    sticker_height: Int32
    sticker: typing.Optional[Sticker] = None
    sound: typing.Optional[File] = None
    fitzpatrick_type: typing.Optional[Int32] = 0


class Animation(BaseObject):
    """
    Describes an animation file. The animation must be encoded in GIF or MPEG4 format

    :param duration: Duration of the animation, in seconds; as defined by the sender
    :type duration: :class:`Int32`
    :param width: Width of the animation
    :type width: :class:`Int32`
    :param height: Height of the animation
    :type height: :class:`Int32`
    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`String`
    :param mime_type: MIME type of the file, usually "image/gif" or "video/mp4"
    :type mime_type: :class:`String`
    :param animation: File containing the animation
    :type animation: :class:`File`
    :param minithumbnail: Animation minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param thumbnail: Animation thumbnail in JPEG or MPEG4 format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param has_stickers: True, if stickers were added to the animation. The list of corresponding sticker set can be received using getAttachedStickerSets
    :type has_stickers: :class:`Bool`
    """

    ID: typing.Literal["animation"] = "animation"
    duration: Int32
    width: Int32
    height: Int32
    file_name: String
    mime_type: String
    animation: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    has_stickers: Bool = False


class Animations(BaseObject):
    """
    Represents a list of animations

    :param animations: List of animations
    :type animations: :class:`Vector[Animation]`
    """

    ID: typing.Literal["animations"] = "animations"
    animations: Vector[Animation]


class ArchiveChatListSettings(BaseObject):
    """
    Contains settings for automatic moving of chats to and from the Archive chat lists

    :param archive_and_mute_new_chats_from_unknown_users: True, if new chats from non-contacts will be automatically archived and muted. Can be set to true only if the option "can_archive_and_mute_new_chats_from_unknown_users" is true
    :type archive_and_mute_new_chats_from_unknown_users: :class:`Bool`
    :param keep_unmuted_chats_archived: True, if unmuted chats will be kept in the Archive chat list when they get a new message
    :type keep_unmuted_chats_archived: :class:`Bool`
    :param keep_chats_from_folders_archived: True, if unmuted chats, that are always included or pinned in a folder, will be kept in the Archive chat list when they get a new message. Ignored if keep_unmuted_chats_archived == true
    :type keep_chats_from_folders_archived: :class:`Bool`
    """

    ID: typing.Literal["archiveChatListSettings"] = "archiveChatListSettings"
    archive_and_mute_new_chats_from_unknown_users: Bool = False
    keep_unmuted_chats_archived: Bool = False
    keep_chats_from_folders_archived: Bool = False


class AttachmentMenuBot(BaseObject):
    """
    Represents a bot, which can be added to attachment or side menu

    :param bot_user_id: User identifier of the bot
    :type bot_user_id: :class:`Int53`
    :param name: Name for the bot in attachment menu
    :type name: :class:`String`
    :param name_color: Color to highlight selected name of the bot if appropriate; may be null, defaults to None
    :type name_color: :class:`AttachmentMenuBotColor`, optional
    :param default_icon: Default icon for the bot in SVG format; may be null, defaults to None
    :type default_icon: :class:`File`, optional
    :param ios_static_icon: Icon for the bot in SVG format for the official iOS app; may be null, defaults to None
    :type ios_static_icon: :class:`File`, optional
    :param ios_animated_icon: Icon for the bot in TGS format for the official iOS app; may be null, defaults to None
    :type ios_animated_icon: :class:`File`, optional
    :param ios_side_menu_icon: Icon for the bot in PNG format for the official iOS app side menu; may be null, defaults to None
    :type ios_side_menu_icon: :class:`File`, optional
    :param android_icon: Icon for the bot in TGS format for the official Android app; may be null, defaults to None
    :type android_icon: :class:`File`, optional
    :param android_side_menu_icon: Icon for the bot in SVG format for the official Android app side menu; may be null, defaults to None
    :type android_side_menu_icon: :class:`File`, optional
    :param macos_icon: Icon for the bot in TGS format for the official native macOS app; may be null, defaults to None
    :type macos_icon: :class:`File`, optional
    :param macos_side_menu_icon: Icon for the bot in PNG format for the official macOS app side menu; may be null, defaults to None
    :type macos_side_menu_icon: :class:`File`, optional
    :param icon_color: Color to highlight selected icon of the bot if appropriate; may be null, defaults to None
    :type icon_color: :class:`AttachmentMenuBotColor`, optional
    :param web_app_placeholder: Default placeholder for opened Web Apps in SVG format; may be null, defaults to None
    :type web_app_placeholder: :class:`File`, optional
    :param supports_self_chat: True, if the bot supports opening from attachment menu in the chat with the bot
    :type supports_self_chat: :class:`Bool`
    :param supports_user_chats: True, if the bot supports opening from attachment menu in private chats with ordinary users
    :type supports_user_chats: :class:`Bool`
    :param supports_bot_chats: True, if the bot supports opening from attachment menu in private chats with other bots
    :type supports_bot_chats: :class:`Bool`
    :param supports_group_chats: True, if the bot supports opening from attachment menu in basic group and supergroup chats
    :type supports_group_chats: :class:`Bool`
    :param supports_channel_chats: True, if the bot supports opening from attachment menu in channel chats
    :type supports_channel_chats: :class:`Bool`
    :param supports_settings: True, if the bot supports "settings_button_pressed" event
    :type supports_settings: :class:`Bool`
    :param request_write_access: True, if the user must be asked for the permission to send messages to the bot
    :type request_write_access: :class:`Bool`
    :param is_added: True, if the bot was explicitly added by the user. If the bot isn't added, then on the first bot launch toggleBotIsAddedToAttachmentMenu must be called and the bot must be added or removed
    :type is_added: :class:`Bool`
    :param show_in_attachment_menu: True, if the bot must be shown in the attachment menu
    :type show_in_attachment_menu: :class:`Bool`
    :param show_in_side_menu: True, if the bot must be shown in the side menu
    :type show_in_side_menu: :class:`Bool`
    :param show_disclaimer_in_side_menu: True, if a disclaimer, why the bot is shown in the side menu, is needed
    :type show_disclaimer_in_side_menu: :class:`Bool`
    """

    ID: typing.Literal["attachmentMenuBot"] = "attachmentMenuBot"
    bot_user_id: Int53
    name: String
    name_color: typing.Optional[AttachmentMenuBotColor] = None
    default_icon: typing.Optional[File] = None
    ios_static_icon: typing.Optional[File] = None
    ios_animated_icon: typing.Optional[File] = None
    ios_side_menu_icon: typing.Optional[File] = None
    android_icon: typing.Optional[File] = None
    android_side_menu_icon: typing.Optional[File] = None
    macos_icon: typing.Optional[File] = None
    macos_side_menu_icon: typing.Optional[File] = None
    icon_color: typing.Optional[AttachmentMenuBotColor] = None
    web_app_placeholder: typing.Optional[File] = None
    supports_self_chat: Bool = False
    supports_user_chats: Bool = False
    supports_bot_chats: Bool = False
    supports_group_chats: Bool = False
    supports_channel_chats: Bool = False
    supports_settings: Bool = False
    request_write_access: Bool = False
    is_added: Bool = False
    show_in_attachment_menu: Bool = False
    show_in_side_menu: Bool = False
    show_disclaimer_in_side_menu: Bool = False


class AttachmentMenuBotColor(BaseObject):
    """
    Describes a color to highlight a bot added to attachment menu

    :param light_color: Color in the RGB24 format for light themes
    :type light_color: :class:`Int32`
    :param dark_color: Color in the RGB24 format for dark themes
    :type dark_color: :class:`Int32`
    """

    ID: typing.Literal["attachmentMenuBotColor"] = "attachmentMenuBotColor"
    light_color: Int32
    dark_color: Int32


class Audio(BaseObject):
    """
    Describes an audio file. Audio is usually in MP3 or M4A format

    :param duration: Duration of the audio, in seconds; as defined by the sender
    :type duration: :class:`Int32`
    :param title: Title of the audio; as defined by the sender
    :type title: :class:`String`
    :param performer: Performer of the audio; as defined by the sender
    :type performer: :class:`String`
    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`String`
    :param mime_type: The MIME type of the file; as defined by the sender
    :type mime_type: :class:`String`
    :param external_album_covers: Album cover variants to use if the downloaded audio file contains no album cover. Provided thumbnail dimensions are approximate
    :type external_album_covers: :class:`Vector[Thumbnail]`
    :param audio: File containing the audio
    :type audio: :class:`File`
    :param album_cover_minithumbnail: The minithumbnail of the album cover; may be null, defaults to None
    :type album_cover_minithumbnail: :class:`Minithumbnail`, optional
    :param album_cover_thumbnail: The thumbnail of the album cover in JPEG format; as defined by the sender. The full size thumbnail is supposed to be extracted from the downloaded audio file; may be null, defaults to None
    :type album_cover_thumbnail: :class:`Thumbnail`, optional
    """

    ID: typing.Literal["audio"] = "audio"
    duration: Int32
    title: String
    performer: String
    file_name: String
    mime_type: String
    external_album_covers: Vector[Thumbnail]
    audio: File
    album_cover_minithumbnail: typing.Optional[Minithumbnail] = None
    album_cover_thumbnail: typing.Optional[Thumbnail] = None


class AuthenticationCodeInfo(BaseObject):
    """
    Information about the authentication code that was sent

    :param phone_number: A phone number that is being authenticated
    :type phone_number: :class:`String`
    :param type_: The way the code was sent to the user
    :type type_: :class:`AuthenticationCodeType`
    :param timeout: Timeout before the code can be re-sent, in seconds
    :type timeout: :class:`Int32`
    :param next_type: The way the next code will be sent to the user; may be null, defaults to None
    :type next_type: :class:`AuthenticationCodeType`, optional
    """

    ID: typing.Literal["authenticationCodeInfo"] = "authenticationCodeInfo"
    phone_number: String
    type_: AuthenticationCodeType = Field(..., alias="type")
    timeout: Int32
    next_type: typing.Optional[AuthenticationCodeType] = None


class AuthenticationCodeTypeCall(BaseObject):
    """
    An authentication code is delivered via a phone call to the specified phone number

    :param length: Length of the code
    :type length: :class:`Int32`
    """

    ID: typing.Literal["authenticationCodeTypeCall"] = "authenticationCodeTypeCall"
    length: Int32


class AuthenticationCodeTypeFirebaseAndroid(BaseObject):
    """
    An authentication code is delivered via Firebase Authentication to the official Android application

    :param nonce: Nonce to pass to the SafetyNet Attestation API
    :type nonce: :class:`Bytes`
    :param length: Length of the code
    :type length: :class:`Int32`
    """

    ID: typing.Literal["authenticationCodeTypeFirebaseAndroid"] = "authenticationCodeTypeFirebaseAndroid"
    nonce: Bytes
    length: Int32


class AuthenticationCodeTypeFirebaseIos(BaseObject):
    """
    An authentication code is delivered via Firebase Authentication to the official iOS application

    :param receipt: Receipt of successful application token validation to compare with receipt from push notification
    :type receipt: :class:`String`
    :param push_timeout: Time after the next authentication method is supposed to be used if verification push notification isn't received, in seconds
    :type push_timeout: :class:`Int32`
    :param length: Length of the code
    :type length: :class:`Int32`
    """

    ID: typing.Literal["authenticationCodeTypeFirebaseIos"] = "authenticationCodeTypeFirebaseIos"
    receipt: String
    push_timeout: Int32
    length: Int32


class AuthenticationCodeTypeFlashCall(BaseObject):
    """
    An authentication code is delivered by an immediately canceled call to the specified phone number. The phone number that calls is the code that must be entered automatically

    :param pattern: Pattern of the phone number from which the call will be made
    :type pattern: :class:`String`
    """

    ID: typing.Literal["authenticationCodeTypeFlashCall"] = "authenticationCodeTypeFlashCall"
    pattern: String


class AuthenticationCodeTypeFragment(BaseObject):
    """
    An authentication code is delivered to https://fragment.com. The user must be logged in there via a wallet owning the phone number's NFT

    :param url: URL to open to receive the code
    :type url: :class:`String`
    :param length: Length of the code
    :type length: :class:`Int32`
    """

    ID: typing.Literal["authenticationCodeTypeFragment"] = "authenticationCodeTypeFragment"
    url: String
    length: Int32


class AuthenticationCodeTypeMissedCall(BaseObject):
    """
    An authentication code is delivered by an immediately canceled call to the specified phone number. The last digits of the phone number that calls are the code that must be entered manually by the user

    :param phone_number_prefix: Prefix of the phone number from which the call will be made
    :type phone_number_prefix: :class:`String`
    :param length: Number of digits in the code, excluding the prefix
    :type length: :class:`Int32`
    """

    ID: typing.Literal["authenticationCodeTypeMissedCall"] = "authenticationCodeTypeMissedCall"
    phone_number_prefix: String
    length: Int32


class AuthenticationCodeTypeSms(BaseObject):
    """
    An authentication code is delivered via an SMS message to the specified phone number; applications may not receive this type of code

    :param length: Length of the code
    :type length: :class:`Int32`
    """

    ID: typing.Literal["authenticationCodeTypeSms"] = "authenticationCodeTypeSms"
    length: Int32


class AuthenticationCodeTypeTelegramMessage(BaseObject):
    """
    An authentication code is delivered via a private Telegram message, which can be viewed from another active session

    :param length: Length of the code
    :type length: :class:`Int32`
    """

    ID: typing.Literal["authenticationCodeTypeTelegramMessage"] = "authenticationCodeTypeTelegramMessage"
    length: Int32


AuthenticationCodeType = typing.Union[
    AuthenticationCodeTypeCall,
    AuthenticationCodeTypeFirebaseAndroid,
    AuthenticationCodeTypeFirebaseIos,
    AuthenticationCodeTypeFlashCall,
    AuthenticationCodeTypeFragment,
    AuthenticationCodeTypeMissedCall,
    AuthenticationCodeTypeSms,
    AuthenticationCodeTypeTelegramMessage,
]


class AuthorizationStateClosed(BaseObject):
    """
    TDLib client is in its final state. All databases are closed and all resources are released. No other updates will be received after this. All queries will be responded to with error code 500. To continue working, one must create a new instance of the TDLib client
    """

    ID: typing.Literal["authorizationStateClosed"] = "authorizationStateClosed"


class AuthorizationStateClosing(BaseObject):
    """
    TDLib is closing, all subsequent queries will be answered with the error 500. Note that closing TDLib can take a while. All resources will be freed only after authorizationStateClosed has been received
    """

    ID: typing.Literal["authorizationStateClosing"] = "authorizationStateClosing"


class AuthorizationStateLoggingOut(BaseObject):
    """
    The user is currently logging out
    """

    ID: typing.Literal["authorizationStateLoggingOut"] = "authorizationStateLoggingOut"


class AuthorizationStateReady(BaseObject):
    """
    The user has been successfully authorized. TDLib is now ready to answer general requests
    """

    ID: typing.Literal["authorizationStateReady"] = "authorizationStateReady"


class AuthorizationStateWaitCode(BaseObject):
    """
    TDLib needs the user's authentication code to authorize. Call checkAuthenticationCode to check the code

    :param code_info: Information about the authorization code that was sent
    :type code_info: :class:`AuthenticationCodeInfo`
    """

    ID: typing.Literal["authorizationStateWaitCode"] = "authorizationStateWaitCode"
    code_info: AuthenticationCodeInfo


class AuthorizationStateWaitEmailAddress(BaseObject):
    """
    TDLib needs the user's email address to authorize. Call setAuthenticationEmailAddress to provide the email address, or directly call checkAuthenticationEmailCode with Apple ID/Google ID token if allowed

    :param allow_apple_id: True, if authorization through Apple ID is allowed
    :type allow_apple_id: :class:`Bool`
    :param allow_google_id: True, if authorization through Google ID is allowed
    :type allow_google_id: :class:`Bool`
    """

    ID: typing.Literal["authorizationStateWaitEmailAddress"] = "authorizationStateWaitEmailAddress"
    allow_apple_id: Bool = False
    allow_google_id: Bool = False


class AuthorizationStateWaitEmailCode(BaseObject):
    """
    TDLib needs the user's authentication code sent to an email address to authorize. Call checkAuthenticationEmailCode to provide the code

    :param code_info: Information about the sent authentication code
    :type code_info: :class:`EmailAddressAuthenticationCodeInfo`
    :param email_address_reset_state: Reset state of the email address; may be null if the email address can't be reset, defaults to None
    :type email_address_reset_state: :class:`EmailAddressResetState`, optional
    :param allow_apple_id: True, if authorization through Apple ID is allowed
    :type allow_apple_id: :class:`Bool`
    :param allow_google_id: True, if authorization through Google ID is allowed
    :type allow_google_id: :class:`Bool`
    """

    ID: typing.Literal["authorizationStateWaitEmailCode"] = "authorizationStateWaitEmailCode"
    code_info: EmailAddressAuthenticationCodeInfo
    email_address_reset_state: typing.Optional[EmailAddressResetState] = None
    allow_apple_id: Bool = False
    allow_google_id: Bool = False


class AuthorizationStateWaitOtherDeviceConfirmation(BaseObject):
    """
    The user needs to confirm authorization on another logged in device by scanning a QR code with the provided link

    :param link: A tg:// URL for the QR code. The link will be updated frequently
    :type link: :class:`String`
    """

    ID: typing.Literal[
        "authorizationStateWaitOtherDeviceConfirmation"
    ] = "authorizationStateWaitOtherDeviceConfirmation"
    link: String


class AuthorizationStateWaitPassword(BaseObject):
    """
    The user has been authorized, but needs to enter a 2-step verification password to start using the application. Call checkAuthenticationPassword to provide the password, or requestAuthenticationPasswordRecovery to recover the password, or deleteAccount to delete the account after a week

    :param recovery_email_address_pattern: Pattern of the email address to which the recovery email was sent; empty until a recovery email has been sent
    :type recovery_email_address_pattern: :class:`String`
    :param password_hint: Hint for the password; may be empty
    :type password_hint: :class:`String`
    :param has_recovery_email_address: True, if a recovery email address has been set up
    :type has_recovery_email_address: :class:`Bool`
    :param has_passport_data: True, if some Telegram Passport elements were saved
    :type has_passport_data: :class:`Bool`
    """

    ID: typing.Literal["authorizationStateWaitPassword"] = "authorizationStateWaitPassword"
    recovery_email_address_pattern: String
    password_hint: String = ""
    has_recovery_email_address: Bool = False
    has_passport_data: Bool = False


class AuthorizationStateWaitPhoneNumber(BaseObject):
    """
    TDLib needs the user's phone number to authorize. Call setAuthenticationPhoneNumber to provide the phone number, or use requestQrCodeAuthentication or checkAuthenticationBotToken for other authentication options
    """

    ID: typing.Literal["authorizationStateWaitPhoneNumber"] = "authorizationStateWaitPhoneNumber"


class AuthorizationStateWaitRegistration(BaseObject):
    """
    The user is unregistered and need to accept terms of service and enter their first name and last name to finish registration. Call registerUser to accept the terms of service and provide the data

    :param terms_of_service: Telegram terms of service
    :type terms_of_service: :class:`TermsOfService`
    """

    ID: typing.Literal["authorizationStateWaitRegistration"] = "authorizationStateWaitRegistration"
    terms_of_service: TermsOfService


class AuthorizationStateWaitTdlibParameters(BaseObject):
    """
    Initialization parameters are needed. Call setTdlibParameters to provide them
    """

    ID: typing.Literal["authorizationStateWaitTdlibParameters"] = "authorizationStateWaitTdlibParameters"


AuthorizationState = typing.Union[
    AuthorizationStateClosed,
    AuthorizationStateClosing,
    AuthorizationStateLoggingOut,
    AuthorizationStateReady,
    AuthorizationStateWaitCode,
    AuthorizationStateWaitEmailAddress,
    AuthorizationStateWaitEmailCode,
    AuthorizationStateWaitOtherDeviceConfirmation,
    AuthorizationStateWaitPassword,
    AuthorizationStateWaitPhoneNumber,
    AuthorizationStateWaitRegistration,
    AuthorizationStateWaitTdlibParameters,
]


class AutoDownloadSettings(BaseObject):
    """
    Contains auto-download settings

    :param max_photo_file_size: The maximum size of a photo file to be auto-downloaded, in bytes
    :type max_photo_file_size: :class:`Int32`
    :param max_video_file_size: The maximum size of a video file to be auto-downloaded, in bytes
    :type max_video_file_size: :class:`Int53`
    :param max_other_file_size: The maximum size of other file types to be auto-downloaded, in bytes
    :type max_other_file_size: :class:`Int53`
    :param video_upload_bitrate: The maximum suggested bitrate for uploaded videos, in kbit/s
    :type video_upload_bitrate: :class:`Int32`
    :param is_auto_download_enabled: True, if the auto-download is enabled
    :type is_auto_download_enabled: :class:`Bool`
    :param preload_large_videos: True, if the beginning of video files needs to be preloaded for instant playback
    :type preload_large_videos: :class:`Bool`
    :param preload_next_audio: True, if the next audio track needs to be preloaded while the user is listening to an audio file
    :type preload_next_audio: :class:`Bool`
    :param preload_stories: True, if stories needs to be preloaded
    :type preload_stories: :class:`Bool`
    :param use_less_data_for_calls: True, if "use less data for calls" option needs to be enabled
    :type use_less_data_for_calls: :class:`Bool`
    """

    ID: typing.Literal["autoDownloadSettings"] = "autoDownloadSettings"
    max_photo_file_size: Int32
    max_video_file_size: Int53
    max_other_file_size: Int53
    video_upload_bitrate: Int32
    is_auto_download_enabled: Bool = False
    preload_large_videos: Bool = False
    preload_next_audio: Bool = False
    preload_stories: Bool = False
    use_less_data_for_calls: Bool = False


class AutoDownloadSettingsPresets(BaseObject):
    """
    Contains auto-download settings presets for the current user

    :param low: Preset with lowest settings; supposed to be used by default when roaming
    :type low: :class:`AutoDownloadSettings`
    :param medium: Preset with medium settings; supposed to be used by default when using mobile data
    :type medium: :class:`AutoDownloadSettings`
    :param high: Preset with highest settings; supposed to be used by default when connected on Wi-Fi
    :type high: :class:`AutoDownloadSettings`
    """

    ID: typing.Literal["autoDownloadSettingsPresets"] = "autoDownloadSettingsPresets"
    low: AutoDownloadSettings
    medium: AutoDownloadSettings
    high: AutoDownloadSettings


class AutosaveSettings(BaseObject):
    """
    Describes autosave settings

    :param private_chat_settings: Default autosave settings for private chats
    :type private_chat_settings: :class:`ScopeAutosaveSettings`
    :param group_settings: Default autosave settings for basic group and supergroup chats
    :type group_settings: :class:`ScopeAutosaveSettings`
    :param channel_settings: Default autosave settings for channel chats
    :type channel_settings: :class:`ScopeAutosaveSettings`
    :param exceptions: Autosave settings for specific chats
    :type exceptions: :class:`Vector[AutosaveSettingsException]`
    """

    ID: typing.Literal["autosaveSettings"] = "autosaveSettings"
    private_chat_settings: ScopeAutosaveSettings
    group_settings: ScopeAutosaveSettings
    channel_settings: ScopeAutosaveSettings
    exceptions: Vector[AutosaveSettingsException]


class AutosaveSettingsException(BaseObject):
    """
    Contains autosave settings for a chat, which overrides default settings for the corresponding scope

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param settings: Autosave settings for the chat
    :type settings: :class:`ScopeAutosaveSettings`
    """

    ID: typing.Literal["autosaveSettingsException"] = "autosaveSettingsException"
    chat_id: Int53
    settings: ScopeAutosaveSettings


class AutosaveSettingsScopeChannelChats(BaseObject):
    """
    Autosave settings applied to all channel chats without chat-specific settings
    """

    ID: typing.Literal["autosaveSettingsScopeChannelChats"] = "autosaveSettingsScopeChannelChats"


class AutosaveSettingsScopeChat(BaseObject):
    """
    Autosave settings applied to a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["autosaveSettingsScopeChat"] = "autosaveSettingsScopeChat"
    chat_id: Int53


class AutosaveSettingsScopeGroupChats(BaseObject):
    """
    Autosave settings applied to all basic group and supergroup chats without chat-specific settings
    """

    ID: typing.Literal["autosaveSettingsScopeGroupChats"] = "autosaveSettingsScopeGroupChats"


class AutosaveSettingsScopePrivateChats(BaseObject):
    """
    Autosave settings applied to all private chats without chat-specific settings
    """

    ID: typing.Literal["autosaveSettingsScopePrivateChats"] = "autosaveSettingsScopePrivateChats"


AutosaveSettingsScope = typing.Union[
    AutosaveSettingsScopeChannelChats,
    AutosaveSettingsScopeChat,
    AutosaveSettingsScopeGroupChats,
    AutosaveSettingsScopePrivateChats,
]


class AvailableReaction(BaseObject):
    """
    Represents an available reaction

    :param type_: Type of the reaction
    :type type_: :class:`ReactionType`
    :param needs_premium: True, if Telegram Premium is needed to send the reaction
    :type needs_premium: :class:`Bool`
    """

    ID: typing.Literal["availableReaction"] = "availableReaction"
    type_: ReactionType = Field(..., alias="type")
    needs_premium: Bool = False


class AvailableReactions(BaseObject):
    """
    Represents a list of reactions that can be added to a message

    :param top_reactions: List of reactions to be shown at the top
    :type top_reactions: :class:`Vector[AvailableReaction]`
    :param recent_reactions: List of recently used reactions
    :type recent_reactions: :class:`Vector[AvailableReaction]`
    :param popular_reactions: List of popular reactions
    :type popular_reactions: :class:`Vector[AvailableReaction]`
    :param allow_custom_emoji: True, if custom emoji reactions could be added by Telegram Premium subscribers
    :type allow_custom_emoji: :class:`Bool`
    """

    ID: typing.Literal["availableReactions"] = "availableReactions"
    top_reactions: Vector[AvailableReaction]
    recent_reactions: Vector[AvailableReaction]
    popular_reactions: Vector[AvailableReaction]
    allow_custom_emoji: Bool = False


class Background(BaseObject):
    """
    Describes a chat background

    :param id: Unique background identifier
    :type id: :class:`Int64`
    :param name: Unique background name
    :type name: :class:`String`
    :param type_: Type of the background
    :type type_: :class:`BackgroundType`
    :param document: Document with the background; may be null. Null only for filled backgrounds, defaults to None
    :type document: :class:`Document`, optional
    :param is_default: True, if this is one of default backgrounds
    :type is_default: :class:`Bool`
    :param is_dark: True, if the background is dark and is recommended to be used with dark theme
    :type is_dark: :class:`Bool`
    """

    ID: typing.Literal["background"] = "background"
    id: Int64
    name: String
    type_: BackgroundType = Field(..., alias="type")
    document: typing.Optional[Document] = None
    is_default: Bool = False
    is_dark: Bool = False


class BackgroundFillFreeformGradient(BaseObject):
    """
    Describes a freeform gradient fill of a background

    :param colors: A list of 3 or 4 colors of the freeform gradients in the RGB24 format
    :type colors: :class:`Vector[Int32]`
    """

    ID: typing.Literal["backgroundFillFreeformGradient"] = "backgroundFillFreeformGradient"
    colors: Vector[Int32]


class BackgroundFillGradient(BaseObject):
    """
    Describes a gradient fill of a background

    :param top_color: A top color of the background in the RGB24 format
    :type top_color: :class:`Int32`
    :param bottom_color: A bottom color of the background in the RGB24 format
    :type bottom_color: :class:`Int32`
    :param rotation_angle: Clockwise rotation angle of the gradient, in degrees; 0-359. Must always be divisible by 45
    :type rotation_angle: :class:`Int32`
    """

    ID: typing.Literal["backgroundFillGradient"] = "backgroundFillGradient"
    top_color: Int32
    bottom_color: Int32
    rotation_angle: Int32


class BackgroundFillSolid(BaseObject):
    """
    Describes a solid fill of a background

    :param color: A color of the background in the RGB24 format
    :type color: :class:`Int32`
    """

    ID: typing.Literal["backgroundFillSolid"] = "backgroundFillSolid"
    color: Int32


BackgroundFill = typing.Union[
    BackgroundFillFreeformGradient,
    BackgroundFillGradient,
    BackgroundFillSolid,
]


class BackgroundTypeFill(BaseObject):
    """
    A filled background

    :param fill: The background fill
    :type fill: :class:`BackgroundFill`
    """

    ID: typing.Literal["backgroundTypeFill"] = "backgroundTypeFill"
    fill: BackgroundFill


class BackgroundTypePattern(BaseObject):
    """
    A PNG or TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user

    :param fill: Fill of the background
    :type fill: :class:`BackgroundFill`
    :param intensity: Intensity of the pattern when it is shown above the filled background; 0-100.
    :type intensity: :class:`Int32`
    :param is_inverted: True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only
    :type is_inverted: :class:`Bool`
    :param is_moving: True, if the background needs to be slightly moved when device is tilted
    :type is_moving: :class:`Bool`
    """

    ID: typing.Literal["backgroundTypePattern"] = "backgroundTypePattern"
    fill: BackgroundFill
    intensity: Int32
    is_inverted: Bool = False
    is_moving: Bool = False


class BackgroundTypeWallpaper(BaseObject):
    """
    A wallpaper in JPEG format

    :param is_blurred: True, if the wallpaper must be downscaled to fit in 450x450 square and then box-blurred with radius 12
    :type is_blurred: :class:`Bool`
    :param is_moving: True, if the background needs to be slightly moved when device is tilted
    :type is_moving: :class:`Bool`
    """

    ID: typing.Literal["backgroundTypeWallpaper"] = "backgroundTypeWallpaper"
    is_blurred: Bool = False
    is_moving: Bool = False


BackgroundType = typing.Union[
    BackgroundTypeFill,
    BackgroundTypePattern,
    BackgroundTypeWallpaper,
]


class Backgrounds(BaseObject):
    """
    Contains a list of backgrounds

    :param backgrounds: A list of backgrounds
    :type backgrounds: :class:`Vector[Background]`
    """

    ID: typing.Literal["backgrounds"] = "backgrounds"
    backgrounds: Vector[Background]


class BankCardActionOpenUrl(BaseObject):
    """
    Describes an action associated with a bank card number

    :param text: Action text
    :type text: :class:`String`
    :param url: The URL to be opened
    :type url: :class:`String`
    """

    ID: typing.Literal["bankCardActionOpenUrl"] = "bankCardActionOpenUrl"
    text: String
    url: String


class BankCardInfo(BaseObject):
    """
    Information about a bank card

    :param title: Title of the bank card description
    :type title: :class:`String`
    :param actions: Actions that can be done with the bank card number
    :type actions: :class:`Vector[BankCardActionOpenUrl]`
    """

    ID: typing.Literal["bankCardInfo"] = "bankCardInfo"
    title: String
    actions: Vector[BankCardActionOpenUrl]


class BasicGroup(BaseObject):
    """
    Represents a basic group of 0-200 users (must be upgraded to a supergroup to accommodate more than 200 users)

    :param id: Group identifier
    :type id: :class:`Int53`
    :param member_count: Number of members in the group
    :type member_count: :class:`Int32`
    :param status: Status of the current user in the group
    :type status: :class:`ChatMemberStatus`
    :param is_active: True, if the group is active
    :type is_active: :class:`Bool`
    :param upgraded_to_supergroup_id: Identifier of the supergroup to which this group was upgraded; 0 if none, defaults to None
    :type upgraded_to_supergroup_id: :class:`Int53`, optional
    """

    ID: typing.Literal["basicGroup"] = "basicGroup"
    id: Int53
    member_count: Int32
    status: ChatMemberStatus
    is_active: Bool = False
    upgraded_to_supergroup_id: typing.Optional[Int53] = 0


class BasicGroupFullInfo(BaseObject):
    """
    Contains full information about a basic group

    :param description: Group description. Updated only after the basic group is opened
    :type description: :class:`String`
    :param members: Group members
    :type members: :class:`Vector[ChatMember]`
    :param bot_commands: List of commands of bots in the group
    :type bot_commands: :class:`Vector[BotCommands]`
    :param photo: Chat photo; may be null if empty or unknown. If non-null, then it is the same photo as in chat.photo, defaults to None
    :type photo: :class:`ChatPhoto`, optional
    :param invite_link: Primary invite link for this group; may be null. For chat administrators with can_invite_users right only. Updated only after the basic group is opened, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    :param can_hide_members: True, if non-administrators and non-bots can be hidden in responses to getSupergroupMembers and searchChatMembers for non-administrators after upgrading the basic group to a supergroup
    :type can_hide_members: :class:`Bool`
    :param can_toggle_aggressive_anti_spam: True, if aggressive anti-spam checks can be enabled or disabled in the supergroup after upgrading the basic group to a supergroup
    :type can_toggle_aggressive_anti_spam: :class:`Bool`
    :param creator_user_id: User identifier of the creator of the group; 0 if unknown, defaults to None
    :type creator_user_id: :class:`Int53`, optional
    """

    ID: typing.Literal["basicGroupFullInfo"] = "basicGroupFullInfo"
    description: String
    members: Vector[ChatMember]
    bot_commands: Vector[BotCommands]
    photo: typing.Optional[ChatPhoto] = None
    invite_link: typing.Optional[ChatInviteLink] = None
    can_hide_members: Bool = False
    can_toggle_aggressive_anti_spam: Bool = False
    creator_user_id: typing.Optional[Int53] = 0


class BlockListMain(BaseObject):
    """
    The main block list that disallows writing messages to the current user, receiving their status and photo, viewing of stories, and some other actions
    """

    ID: typing.Literal["blockListMain"] = "blockListMain"


class BlockListStories(BaseObject):
    """
    The block list that disallows viewing of stories of the current user
    """

    ID: typing.Literal["blockListStories"] = "blockListStories"


BlockList = typing.Union[
    BlockListMain,
    BlockListStories,
]


class BotCommand(BaseObject):
    """
    Represents a command supported by a bot

    :param command: Text of the bot command
    :type command: :class:`String`
    :param description: Description of the bot command
    :type description: :class:`String`
    """

    ID: typing.Literal["botCommand"] = "botCommand"
    command: String
    description: String


class BotCommandScopeAllChatAdministrators(BaseObject):
    """
    A scope covering all group and supergroup chat administrators
    """

    ID: typing.Literal["botCommandScopeAllChatAdministrators"] = "botCommandScopeAllChatAdministrators"


class BotCommandScopeAllGroupChats(BaseObject):
    """
    A scope covering all group and supergroup chats
    """

    ID: typing.Literal["botCommandScopeAllGroupChats"] = "botCommandScopeAllGroupChats"


class BotCommandScopeAllPrivateChats(BaseObject):
    """
    A scope covering all private chats
    """

    ID: typing.Literal["botCommandScopeAllPrivateChats"] = "botCommandScopeAllPrivateChats"


class BotCommandScopeChat(BaseObject):
    """
    A scope covering all members of a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["botCommandScopeChat"] = "botCommandScopeChat"
    chat_id: Int53


class BotCommandScopeChatAdministrators(BaseObject):
    """
    A scope covering all administrators of a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["botCommandScopeChatAdministrators"] = "botCommandScopeChatAdministrators"
    chat_id: Int53


class BotCommandScopeChatMember(BaseObject):
    """
    A scope covering a member of a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["botCommandScopeChatMember"] = "botCommandScopeChatMember"
    chat_id: Int53
    user_id: Int53


class BotCommandScopeDefault(BaseObject):
    """
    A scope covering all users
    """

    ID: typing.Literal["botCommandScopeDefault"] = "botCommandScopeDefault"


BotCommandScope = typing.Union[
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
    BotCommandScopeDefault,
]


class BotCommands(BaseObject):
    """
    Contains a list of bot commands

    :param bot_user_id: Bot's user identifier
    :type bot_user_id: :class:`Int53`
    :param commands: List of bot commands
    :type commands: :class:`Vector[BotCommand]`
    """

    ID: typing.Literal["botCommands"] = "botCommands"
    bot_user_id: Int53
    commands: Vector[BotCommand]


class BotInfo(BaseObject):
    """
    Contains information about a bot

    :param short_description: The text that is shown on the bot's profile page and is sent together with the link when users share the bot
    :type short_description: :class:`String`
    :param description: The text shown in the chat with the bot if the chat is empty
    :type description: :class:`String`
    :param commands: List of the bot commands
    :type commands: :class:`Vector[BotCommand]`
    :param photo: Photo shown in the chat with the bot if the chat is empty; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    :param animation: Animation shown in the chat with the bot if the chat is empty; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    :param menu_button: Information about a button to show instead of the bot commands menu button; may be null if ordinary bot commands menu must be shown, defaults to None
    :type menu_button: :class:`BotMenuButton`, optional
    :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; may be null, defaults to None
    :type default_group_administrator_rights: :class:`ChatAdministratorRights`, optional
    :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; may be null, defaults to None
    :type default_channel_administrator_rights: :class:`ChatAdministratorRights`, optional
    :param edit_commands_link: The internal link, which can be used to edit bot commands; may be null, defaults to None
    :type edit_commands_link: :class:`InternalLinkType`, optional
    :param edit_description_link: The internal link, which can be used to edit bot description; may be null, defaults to None
    :type edit_description_link: :class:`InternalLinkType`, optional
    :param edit_description_media_link: The internal link, which can be used to edit the photo or animation shown in the chat with the bot if the chat is empty; may be null, defaults to None
    :type edit_description_media_link: :class:`InternalLinkType`, optional
    :param edit_settings_link: The internal link, which can be used to edit bot settings; may be null, defaults to None
    :type edit_settings_link: :class:`InternalLinkType`, optional
    """

    ID: typing.Literal["botInfo"] = "botInfo"
    short_description: String
    description: String
    commands: Vector[BotCommand]
    photo: typing.Optional[Photo] = None
    animation: typing.Optional[Animation] = None
    menu_button: typing.Optional[BotMenuButton] = None
    default_group_administrator_rights: typing.Optional[ChatAdministratorRights] = None
    default_channel_administrator_rights: typing.Optional[ChatAdministratorRights] = None
    edit_commands_link: typing.Optional[InternalLinkType] = None
    edit_description_link: typing.Optional[InternalLinkType] = None
    edit_description_media_link: typing.Optional[InternalLinkType] = None
    edit_settings_link: typing.Optional[InternalLinkType] = None


class BotMenuButton(BaseObject):
    """
    Describes a button to be shown instead of bot commands menu button

    :param text: Text of the button
    :type text: :class:`String`
    :param url: URL to be passed to openWebApp
    :type url: :class:`String`
    """

    ID: typing.Literal["botMenuButton"] = "botMenuButton"
    text: String
    url: String


class Call(BaseObject):
    """
    Describes a call

    :param id: Call identifier, not persistent
    :type id: :class:`Int32`
    :param user_id: Peer user identifier
    :type user_id: :class:`Int53`
    :param state: Call state
    :type state: :class:`CallState`
    :param is_outgoing: True, if the call is outgoing
    :type is_outgoing: :class:`Bool`
    :param is_video: True, if the call is a video call
    :type is_video: :class:`Bool`
    """

    ID: typing.Literal["call"] = "call"
    id: Int32
    user_id: Int53
    state: CallState
    is_outgoing: Bool = False
    is_video: Bool = False


class CallDiscardReasonDeclined(BaseObject):
    """
    The call was ended before the conversation started. It was declined by the other party
    """

    ID: typing.Literal["callDiscardReasonDeclined"] = "callDiscardReasonDeclined"


class CallDiscardReasonDisconnected(BaseObject):
    """
    The call was ended during the conversation because the users were disconnected
    """

    ID: typing.Literal["callDiscardReasonDisconnected"] = "callDiscardReasonDisconnected"


class CallDiscardReasonEmpty(BaseObject):
    """
    The call wasn't discarded, or the reason is unknown
    """

    ID: typing.Literal["callDiscardReasonEmpty"] = "callDiscardReasonEmpty"


class CallDiscardReasonHungUp(BaseObject):
    """
    The call was ended because one of the parties hung up
    """

    ID: typing.Literal["callDiscardReasonHungUp"] = "callDiscardReasonHungUp"


class CallDiscardReasonMissed(BaseObject):
    """
    The call was ended before the conversation started. It was canceled by the caller or missed by the other party
    """

    ID: typing.Literal["callDiscardReasonMissed"] = "callDiscardReasonMissed"


CallDiscardReason = typing.Union[
    CallDiscardReasonDeclined,
    CallDiscardReasonDisconnected,
    CallDiscardReasonEmpty,
    CallDiscardReasonHungUp,
    CallDiscardReasonMissed,
]


class CallId(BaseObject):
    """
    Contains the call identifier

    :param id: Call identifier
    :type id: :class:`Int32`
    """

    ID: typing.Literal["callId"] = "callId"
    id: Int32


class CallProblemDistortedSpeech(BaseObject):
    """
    The speech was distorted
    """

    ID: typing.Literal["callProblemDistortedSpeech"] = "callProblemDistortedSpeech"


class CallProblemDistortedVideo(BaseObject):
    """
    The video was distorted
    """

    ID: typing.Literal["callProblemDistortedVideo"] = "callProblemDistortedVideo"


class CallProblemDropped(BaseObject):
    """
    The call ended unexpectedly
    """

    ID: typing.Literal["callProblemDropped"] = "callProblemDropped"


class CallProblemEcho(BaseObject):
    """
    The user heard their own voice
    """

    ID: typing.Literal["callProblemEcho"] = "callProblemEcho"


class CallProblemInterruptions(BaseObject):
    """
    The other side kept disappearing
    """

    ID: typing.Literal["callProblemInterruptions"] = "callProblemInterruptions"


class CallProblemNoise(BaseObject):
    """
    The user heard background noise
    """

    ID: typing.Literal["callProblemNoise"] = "callProblemNoise"


class CallProblemPixelatedVideo(BaseObject):
    """
    The video was pixelated
    """

    ID: typing.Literal["callProblemPixelatedVideo"] = "callProblemPixelatedVideo"


class CallProblemSilentLocal(BaseObject):
    """
    The user couldn't hear the other side
    """

    ID: typing.Literal["callProblemSilentLocal"] = "callProblemSilentLocal"


class CallProblemSilentRemote(BaseObject):
    """
    The other side couldn't hear the user
    """

    ID: typing.Literal["callProblemSilentRemote"] = "callProblemSilentRemote"


CallProblem = typing.Union[
    CallProblemDistortedSpeech,
    CallProblemDistortedVideo,
    CallProblemDropped,
    CallProblemEcho,
    CallProblemInterruptions,
    CallProblemNoise,
    CallProblemPixelatedVideo,
    CallProblemSilentLocal,
    CallProblemSilentRemote,
]


class CallProtocol(BaseObject):
    """
    Specifies the supported call protocols

    :param min_layer: The minimum supported API layer; use 65
    :type min_layer: :class:`Int32`
    :param max_layer: The maximum supported API layer; use 92
    :type max_layer: :class:`Int32`
    :param library_versions: List of supported tgcalls versions
    :type library_versions: :class:`Vector[String]`
    :param udp_p2p: True, if UDP peer-to-peer connections are supported
    :type udp_p2p: :class:`Bool`
    :param udp_reflector: True, if connection through UDP reflectors is supported
    :type udp_reflector: :class:`Bool`
    """

    ID: typing.Literal["callProtocol"] = "callProtocol"
    min_layer: Int32
    max_layer: Int32
    library_versions: Vector[String]
    udp_p2p: Bool = False
    udp_reflector: Bool = False


class CallServer(BaseObject):
    """
    Describes a server for relaying call data

    :param id: Server identifier
    :type id: :class:`Int64`
    :param ip_address: Server IPv4 address
    :type ip_address: :class:`String`
    :param ipv6_address: Server IPv6 address
    :type ipv6_address: :class:`String`
    :param port: Server port number
    :type port: :class:`Int32`
    :param type_: Server type
    :type type_: :class:`CallServerType`
    """

    ID: typing.Literal["callServer"] = "callServer"
    id: Int64
    ip_address: String
    ipv6_address: String
    port: Int32
    type_: CallServerType = Field(..., alias="type")


class CallServerTypeTelegramReflector(BaseObject):
    """
    A Telegram call reflector

    :param peer_tag: A peer tag to be used with the reflector
    :type peer_tag: :class:`Bytes`
    :param is_tcp: True, if the server uses TCP instead of UDP
    :type is_tcp: :class:`Bool`
    """

    ID: typing.Literal["callServerTypeTelegramReflector"] = "callServerTypeTelegramReflector"
    peer_tag: Bytes
    is_tcp: Bool = False


class CallServerTypeWebrtc(BaseObject):
    """
    A WebRTC server

    :param username: Username to be used for authentication
    :type username: :class:`String`
    :param password: Authentication password
    :type password: :class:`String`
    :param supports_turn: True, if the server supports TURN
    :type supports_turn: :class:`Bool`
    :param supports_stun: True, if the server supports STUN
    :type supports_stun: :class:`Bool`
    """

    ID: typing.Literal["callServerTypeWebrtc"] = "callServerTypeWebrtc"
    username: String
    password: String
    supports_turn: Bool = False
    supports_stun: Bool = False


CallServerType = typing.Union[
    CallServerTypeTelegramReflector,
    CallServerTypeWebrtc,
]


class CallStateDiscarded(BaseObject):
    """
    The call has ended successfully

    :param reason: The reason, why the call has ended
    :type reason: :class:`CallDiscardReason`
    :param need_rating: True, if the call rating must be sent to the server
    :type need_rating: :class:`Bool`
    :param need_debug_information: True, if the call debug information must be sent to the server
    :type need_debug_information: :class:`Bool`
    :param need_log: True, if the call log must be sent to the server
    :type need_log: :class:`Bool`
    """

    ID: typing.Literal["callStateDiscarded"] = "callStateDiscarded"
    reason: CallDiscardReason
    need_rating: Bool = False
    need_debug_information: Bool = False
    need_log: Bool = False


class CallStateError(BaseObject):
    """
    The call has ended with an error

    :param error: Error. An error with the code 4005000 will be returned if an outgoing call is missed because of an expired timeout
    :type error: :class:`Error`
    """

    ID: typing.Literal["callStateError"] = "callStateError"
    error: Error


class CallStateExchangingKeys(BaseObject):
    """
    The call has been answered and encryption keys are being exchanged
    """

    ID: typing.Literal["callStateExchangingKeys"] = "callStateExchangingKeys"


class CallStateHangingUp(BaseObject):
    """
    The call is hanging up after discardCall has been called
    """

    ID: typing.Literal["callStateHangingUp"] = "callStateHangingUp"


class CallStatePending(BaseObject):
    """
    The call is pending, waiting to be accepted by a user

    :param is_created: True, if the call has already been created by the server
    :type is_created: :class:`Bool`
    :param is_received: True, if the call has already been received by the other party
    :type is_received: :class:`Bool`
    """

    ID: typing.Literal["callStatePending"] = "callStatePending"
    is_created: Bool = False
    is_received: Bool = False


class CallStateReady(BaseObject):
    """
    The call is ready to use

    :param protocol: Call protocols supported by the peer
    :type protocol: :class:`CallProtocol`
    :param servers: List of available call servers
    :type servers: :class:`Vector[CallServer]`
    :param config: A JSON-encoded call config
    :type config: :class:`String`
    :param encryption_key: Call encryption key
    :type encryption_key: :class:`Bytes`
    :param emojis: Encryption key emojis fingerprint
    :type emojis: :class:`Vector[String]`
    :param allow_p2p: True, if peer-to-peer connection is allowed by users privacy settings
    :type allow_p2p: :class:`Bool`
    """

    ID: typing.Literal["callStateReady"] = "callStateReady"
    protocol: CallProtocol
    servers: Vector[CallServer]
    config: String
    encryption_key: Bytes
    emojis: Vector[String]
    allow_p2p: Bool = False


CallState = typing.Union[
    CallStateDiscarded,
    CallStateError,
    CallStateExchangingKeys,
    CallStateHangingUp,
    CallStatePending,
    CallStateReady,
]


class CallbackQueryAnswer(BaseObject):
    """
    Contains a bot's answer to a callback query

    :param text: Text of the answer
    :type text: :class:`String`
    :param url: URL to be opened
    :type url: :class:`String`
    :param show_alert: True, if an alert must be shown to the user instead of a toast notification
    :type show_alert: :class:`Bool`
    """

    ID: typing.Literal["callbackQueryAnswer"] = "callbackQueryAnswer"
    text: String
    url: String
    show_alert: Bool = False


class CallbackQueryPayloadData(BaseObject):
    """
    The payload for a general callback button

    :param data: Data that was attached to the callback button
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["callbackQueryPayloadData"] = "callbackQueryPayloadData"
    data: Bytes


class CallbackQueryPayloadDataWithPassword(BaseObject):
    """
    The payload for a callback button requiring password

    :param password: The 2-step verification password for the current user
    :type password: :class:`String`
    :param data: Data that was attached to the callback button
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["callbackQueryPayloadDataWithPassword"] = "callbackQueryPayloadDataWithPassword"
    password: String
    data: Bytes


class CallbackQueryPayloadGame(BaseObject):
    """
    The payload for a game callback button

    :param game_short_name: A short name of the game that was attached to the callback button
    :type game_short_name: :class:`String`
    """

    ID: typing.Literal["callbackQueryPayloadGame"] = "callbackQueryPayloadGame"
    game_short_name: String


CallbackQueryPayload = typing.Union[
    CallbackQueryPayloadData,
    CallbackQueryPayloadDataWithPassword,
    CallbackQueryPayloadGame,
]


class CanSendStoryResultActiveStoryLimitExceeded(BaseObject):
    """
    The limit for the number of active stories exceeded. The user can buy Telegram Premium, delete an active story, or wait for the oldest story to expire
    """

    ID: typing.Literal["canSendStoryResultActiveStoryLimitExceeded"] = "canSendStoryResultActiveStoryLimitExceeded"


class CanSendStoryResultMonthlyLimitExceeded(BaseObject):
    """
    The monthly limit for the number of posted stories exceeded. The user needs to buy Telegram Premium or wait specified time

    :param retry_after: Time left before the user can send the next story
    :type retry_after: :class:`Int32`
    """

    ID: typing.Literal["canSendStoryResultMonthlyLimitExceeded"] = "canSendStoryResultMonthlyLimitExceeded"
    retry_after: Int32


class CanSendStoryResultOk(BaseObject):
    """
    A story can be sent
    """

    ID: typing.Literal["canSendStoryResultOk"] = "canSendStoryResultOk"


class CanSendStoryResultPremiumNeeded(BaseObject):
    """
    The user must subscribe to Telegram Premium to be able to post stories
    """

    ID: typing.Literal["canSendStoryResultPremiumNeeded"] = "canSendStoryResultPremiumNeeded"


class CanSendStoryResultWeeklyLimitExceeded(BaseObject):
    """
    The weekly limit for the number of posted stories exceeded. The user needs to buy Telegram Premium or wait specified time

    :param retry_after: Time left before the user can send the next story
    :type retry_after: :class:`Int32`
    """

    ID: typing.Literal["canSendStoryResultWeeklyLimitExceeded"] = "canSendStoryResultWeeklyLimitExceeded"
    retry_after: Int32


CanSendStoryResult = typing.Union[
    CanSendStoryResultActiveStoryLimitExceeded,
    CanSendStoryResultMonthlyLimitExceeded,
    CanSendStoryResultOk,
    CanSendStoryResultPremiumNeeded,
    CanSendStoryResultWeeklyLimitExceeded,
]


class CanTransferOwnershipResultOk(BaseObject):
    """
    The session can be used
    """

    ID: typing.Literal["canTransferOwnershipResultOk"] = "canTransferOwnershipResultOk"


class CanTransferOwnershipResultPasswordNeeded(BaseObject):
    """
    The 2-step verification needs to be enabled first
    """

    ID: typing.Literal["canTransferOwnershipResultPasswordNeeded"] = "canTransferOwnershipResultPasswordNeeded"


class CanTransferOwnershipResultPasswordTooFresh(BaseObject):
    """
    The 2-step verification was enabled recently, user needs to wait

    :param retry_after: Time left before the session can be used to transfer ownership of a chat, in seconds
    :type retry_after: :class:`Int32`
    """

    ID: typing.Literal["canTransferOwnershipResultPasswordTooFresh"] = "canTransferOwnershipResultPasswordTooFresh"
    retry_after: Int32


class CanTransferOwnershipResultSessionTooFresh(BaseObject):
    """
    The session was created recently, user needs to wait

    :param retry_after: Time left before the session can be used to transfer ownership of a chat, in seconds
    :type retry_after: :class:`Int32`
    """

    ID: typing.Literal["canTransferOwnershipResultSessionTooFresh"] = "canTransferOwnershipResultSessionTooFresh"
    retry_after: Int32


CanTransferOwnershipResult = typing.Union[
    CanTransferOwnershipResultOk,
    CanTransferOwnershipResultPasswordNeeded,
    CanTransferOwnershipResultPasswordTooFresh,
    CanTransferOwnershipResultSessionTooFresh,
]


class Chat(BaseObject):
    """
    A chat. (Can be a private chat, basic group, supergroup, or secret chat)

    :param id: Chat unique identifier
    :type id: :class:`Int53`
    :param type_: Type of the chat
    :type type_: :class:`ChatType`
    :param title: Chat title
    :type title: :class:`String`
    :param permissions: Actions that non-administrator chat members are allowed to take in the chat
    :type permissions: :class:`ChatPermissions`
    :param positions: Positions of the chat in chat lists
    :type positions: :class:`Vector[ChatPosition]`
    :param default_disable_notification: Default value of the disable_notification parameter, used when a message is sent to the chat
    :type default_disable_notification: :class:`Bool`
    :param unread_count: Number of unread messages in the chat
    :type unread_count: :class:`Int32`
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :type last_read_inbox_message_id: :class:`Int53`
    :param last_read_outbox_message_id: Identifier of the last read outgoing message
    :type last_read_outbox_message_id: :class:`Int53`
    :param unread_mention_count: Number of unread messages with a mention/reply in the chat
    :type unread_mention_count: :class:`Int32`
    :param unread_reaction_count: Number of messages with unread reactions in the chat
    :type unread_reaction_count: :class:`Int32`
    :param notification_settings: Notification settings for the chat
    :type notification_settings: :class:`ChatNotificationSettings`
    :param available_reactions: Types of reaction, available in the chat
    :type available_reactions: :class:`ChatAvailableReactions`
    :param message_auto_delete_time: Current message auto-delete or self-destruct timer setting for the chat, in seconds; 0 if disabled. Self-destruct timer in secret chats starts after the message or its content is viewed. Auto-delete timer in other chats starts from the send date
    :type message_auto_delete_time: :class:`Int32`
    :param theme_name: If non-empty, name of a theme, set for the chat
    :type theme_name: :class:`String`
    :param video_chat: Information about video chat of the chat
    :type video_chat: :class:`VideoChat`
    :param reply_markup_message_id: Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
    :type reply_markup_message_id: :class:`Int53`
    :param client_data: Application-specific data associated with the chat. (For example, the chat scroll position or local chat notification settings can be stored here.) Persistent if the message database is used
    :type client_data: :class:`String`
    :param photo: Chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    :param last_message: Last message in the chat; may be null if none or unknown, defaults to None
    :type last_message: :class:`Message`, optional
    :param message_sender_id: Identifier of a user or chat that is selected to send messages in the chat; may be null if the user can't change message sender, defaults to None
    :type message_sender_id: :class:`MessageSender`, optional
    :param block_list: Block list to which the chat is added; may be null if none, defaults to None
    :type block_list: :class:`BlockList`, optional
    :param background: Background set for the chat; may be null if none, defaults to None
    :type background: :class:`ChatBackground`, optional
    :param action_bar: Information about actions which must be possible to do through the chat action bar; may be null if none, defaults to None
    :type action_bar: :class:`ChatActionBar`, optional
    :param pending_join_requests: Information about pending join requests; may be null if none, defaults to None
    :type pending_join_requests: :class:`ChatJoinRequestsInfo`, optional
    :param draft_message: A draft of a message in the chat; may be null if none, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    :param has_protected_content: True, if chat content can't be saved locally, forwarded, or copied
    :type has_protected_content: :class:`Bool`
    :param is_translatable: True, if translation of all messages in the chat must be suggested to the user
    :type is_translatable: :class:`Bool`
    :param is_marked_as_unread: True, if the chat is marked as unread
    :type is_marked_as_unread: :class:`Bool`
    :param has_scheduled_messages: True, if the chat has scheduled messages
    :type has_scheduled_messages: :class:`Bool`
    :param can_be_deleted_only_for_self: True, if the chat messages can be deleted only for the current user while other users will continue to see the messages
    :type can_be_deleted_only_for_self: :class:`Bool`
    :param can_be_deleted_for_all_users: True, if the chat messages can be deleted for all users
    :type can_be_deleted_for_all_users: :class:`Bool`
    :param can_be_reported: True, if the chat can be reported to Telegram moderators through reportChat or reportChatPhoto
    :type can_be_reported: :class:`Bool`
    """

    ID: typing.Literal["chat"] = "chat"
    id: Int53
    type_: ChatType = Field(..., alias="type")
    title: String
    permissions: ChatPermissions
    positions: Vector[ChatPosition]
    default_disable_notification: Bool
    unread_count: Int32
    last_read_inbox_message_id: Int53
    last_read_outbox_message_id: Int53
    unread_mention_count: Int32
    unread_reaction_count: Int32
    notification_settings: ChatNotificationSettings
    available_reactions: ChatAvailableReactions
    message_auto_delete_time: Int32
    theme_name: String
    video_chat: VideoChat
    reply_markup_message_id: Int53
    client_data: String
    photo: typing.Optional[ChatPhotoInfo] = None
    last_message: typing.Optional[Message] = None
    message_sender_id: typing.Optional[MessageSender] = None
    block_list: typing.Optional[BlockList] = None
    background: typing.Optional[ChatBackground] = None
    action_bar: typing.Optional[ChatActionBar] = None
    pending_join_requests: typing.Optional[ChatJoinRequestsInfo] = None
    draft_message: typing.Optional[DraftMessage] = None
    has_protected_content: Bool = False
    is_translatable: Bool = False
    is_marked_as_unread: Bool = False
    has_scheduled_messages: Bool = False
    can_be_deleted_only_for_self: Bool = False
    can_be_deleted_for_all_users: Bool = False
    can_be_reported: Bool = False


class ChatActionCancel(BaseObject):
    """
    The user has canceled the previous action
    """

    ID: typing.Literal["chatActionCancel"] = "chatActionCancel"


class ChatActionChoosingContact(BaseObject):
    """
    The user is picking a contact to send
    """

    ID: typing.Literal["chatActionChoosingContact"] = "chatActionChoosingContact"


class ChatActionChoosingLocation(BaseObject):
    """
    The user is picking a location or venue to send
    """

    ID: typing.Literal["chatActionChoosingLocation"] = "chatActionChoosingLocation"


class ChatActionChoosingSticker(BaseObject):
    """
    The user is picking a sticker to send
    """

    ID: typing.Literal["chatActionChoosingSticker"] = "chatActionChoosingSticker"


class ChatActionRecordingVideo(BaseObject):
    """
    The user is recording a video
    """

    ID: typing.Literal["chatActionRecordingVideo"] = "chatActionRecordingVideo"


class ChatActionRecordingVideoNote(BaseObject):
    """
    The user is recording a video note
    """

    ID: typing.Literal["chatActionRecordingVideoNote"] = "chatActionRecordingVideoNote"


class ChatActionRecordingVoiceNote(BaseObject):
    """
    The user is recording a voice note
    """

    ID: typing.Literal["chatActionRecordingVoiceNote"] = "chatActionRecordingVoiceNote"


class ChatActionStartPlayingGame(BaseObject):
    """
    The user has started to play a game
    """

    ID: typing.Literal["chatActionStartPlayingGame"] = "chatActionStartPlayingGame"


class ChatActionTyping(BaseObject):
    """
    The user is typing a message
    """

    ID: typing.Literal["chatActionTyping"] = "chatActionTyping"


class ChatActionUploadingDocument(BaseObject):
    """
    The user is uploading a document

    :param progress: Upload progress, as a percentage
    :type progress: :class:`Int32`
    """

    ID: typing.Literal["chatActionUploadingDocument"] = "chatActionUploadingDocument"
    progress: Int32


class ChatActionUploadingPhoto(BaseObject):
    """
    The user is uploading a photo

    :param progress: Upload progress, as a percentage
    :type progress: :class:`Int32`
    """

    ID: typing.Literal["chatActionUploadingPhoto"] = "chatActionUploadingPhoto"
    progress: Int32


class ChatActionUploadingVideo(BaseObject):
    """
    The user is uploading a video

    :param progress: Upload progress, as a percentage
    :type progress: :class:`Int32`
    """

    ID: typing.Literal["chatActionUploadingVideo"] = "chatActionUploadingVideo"
    progress: Int32


class ChatActionUploadingVideoNote(BaseObject):
    """
    The user is uploading a video note

    :param progress: Upload progress, as a percentage
    :type progress: :class:`Int32`
    """

    ID: typing.Literal["chatActionUploadingVideoNote"] = "chatActionUploadingVideoNote"
    progress: Int32


class ChatActionUploadingVoiceNote(BaseObject):
    """
    The user is uploading a voice note

    :param progress: Upload progress, as a percentage
    :type progress: :class:`Int32`
    """

    ID: typing.Literal["chatActionUploadingVoiceNote"] = "chatActionUploadingVoiceNote"
    progress: Int32


class ChatActionWatchingAnimations(BaseObject):
    """
    The user is watching animations sent by the other party by clicking on an animated emoji

    :param emoji: The animated emoji
    :type emoji: :class:`String`
    """

    ID: typing.Literal["chatActionWatchingAnimations"] = "chatActionWatchingAnimations"
    emoji: String


ChatAction = typing.Union[
    ChatActionCancel,
    ChatActionChoosingContact,
    ChatActionChoosingLocation,
    ChatActionChoosingSticker,
    ChatActionRecordingVideo,
    ChatActionRecordingVideoNote,
    ChatActionRecordingVoiceNote,
    ChatActionStartPlayingGame,
    ChatActionTyping,
    ChatActionUploadingDocument,
    ChatActionUploadingPhoto,
    ChatActionUploadingVideo,
    ChatActionUploadingVideoNote,
    ChatActionUploadingVoiceNote,
    ChatActionWatchingAnimations,
]


class ChatActionBarAddContact(BaseObject):
    """
    The chat is a private or secret chat and the other user can be added to the contact list using the method addContact
    """

    ID: typing.Literal["chatActionBarAddContact"] = "chatActionBarAddContact"


class ChatActionBarInviteMembers(BaseObject):
    """
    The chat is a recently created group chat to which new members can be invited
    """

    ID: typing.Literal["chatActionBarInviteMembers"] = "chatActionBarInviteMembers"


class ChatActionBarJoinRequest(BaseObject):
    """
    The chat is a private chat with an administrator of a chat to which the user sent join request

    :param title: Title of the chat to which the join request was sent
    :type title: :class:`String`
    :param request_date: Point in time (Unix timestamp) when the join request was sent
    :type request_date: :class:`Int32`
    :param is_channel: True, if the join request was sent to a channel chat
    :type is_channel: :class:`Bool`
    """

    ID: typing.Literal["chatActionBarJoinRequest"] = "chatActionBarJoinRequest"
    title: String
    request_date: Int32
    is_channel: Bool = False


class ChatActionBarReportAddBlock(BaseObject):
    """
    The chat is a private or secret chat, which can be reported using the method reportChat, or the other user can be blocked using the method setMessageSenderBlockList, or the other user can be added to the contact list using the method addContact. If the chat is a private chat with a user with an emoji status, then a notice about emoji status usage must be shown

    :param can_unarchive: If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings
    :type can_unarchive: :class:`Bool`
    :param distance: If non-negative, the current user was found by the peer through searchChatsNearby and this is the distance between the users
    :type distance: :class:`Int32`
    """

    ID: typing.Literal["chatActionBarReportAddBlock"] = "chatActionBarReportAddBlock"
    can_unarchive: Bool
    distance: Int32


class ChatActionBarReportSpam(BaseObject):
    """
    The chat can be reported as spam using the method reportChat with the reason reportReasonSpam. If the chat is a private chat with a user with an emoji status, then a notice about emoji status usage must be shown

    :param can_unarchive: If true, the chat was automatically archived and can be moved back to the main chat list using addChatToList simultaneously with setting chat notification settings to default using setChatNotificationSettings
    :type can_unarchive: :class:`Bool`
    """

    ID: typing.Literal["chatActionBarReportSpam"] = "chatActionBarReportSpam"
    can_unarchive: Bool


class ChatActionBarReportUnrelatedLocation(BaseObject):
    """
    The chat is a location-based supergroup, which can be reported as having unrelated location using the method reportChat with the reason reportReasonUnrelatedLocation
    """

    ID: typing.Literal["chatActionBarReportUnrelatedLocation"] = "chatActionBarReportUnrelatedLocation"


class ChatActionBarSharePhoneNumber(BaseObject):
    """
    The chat is a private or secret chat with a mutual contact and the user's phone number can be shared with the other user using the method sharePhoneNumber
    """

    ID: typing.Literal["chatActionBarSharePhoneNumber"] = "chatActionBarSharePhoneNumber"


ChatActionBar = typing.Union[
    ChatActionBarAddContact,
    ChatActionBarInviteMembers,
    ChatActionBarJoinRequest,
    ChatActionBarReportAddBlock,
    ChatActionBarReportSpam,
    ChatActionBarReportUnrelatedLocation,
    ChatActionBarSharePhoneNumber,
]


class ChatActiveStories(BaseObject):
    """
    Describes active stories posted by a chat

    :param chat_id: Identifier of the chat that posted the stories
    :type chat_id: :class:`Int53`
    :param order: A parameter used to determine order of the stories in the story list; 0 if the stories doesn't need to be shown in the story list. Stories must be sorted by the pair (order, story_sender_chat_id) in descending order
    :type order: :class:`Int53`
    :param max_read_story_id: Identifier of the last read active story
    :type max_read_story_id: :class:`Int32`
    :param stories: Basic information about the stories; use getStory to get full information about the stories. The stories are in a chronological order (i.e., in order of increasing story identifiers)
    :type stories: :class:`Vector[StoryInfo]`
    :param list: Identifier of the story list in which the stories are shown; may be null if the stories aren't shown in a story list, defaults to None
    :type list: :class:`StoryList`, optional
    """

    ID: typing.Literal["chatActiveStories"] = "chatActiveStories"
    chat_id: Int53
    order: Int53
    max_read_story_id: Int32
    stories: Vector[StoryInfo]
    list: typing.Optional[StoryList] = None


class ChatAdministrator(BaseObject):
    """
    Contains information about a chat administrator

    :param user_id: User identifier of the administrator
    :type user_id: :class:`Int53`
    :param custom_title: Custom title of the administrator
    :type custom_title: :class:`String`
    :param is_owner: True, if the user is the owner of the chat
    :type is_owner: :class:`Bool`
    """

    ID: typing.Literal["chatAdministrator"] = "chatAdministrator"
    user_id: Int53
    custom_title: String
    is_owner: Bool = False


class ChatAdministratorRights(BaseObject):
    """
    Describes rights of the administrator

    :param can_manage_chat: True, if the administrator can get chat event log, get chat statistics, get message statistics in channels, get channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other privilege; applicable to supergroups and channels only
    :type can_manage_chat: :class:`Bool`
    :param can_change_info: True, if the administrator can change the chat title, photo, and other settings
    :type can_change_info: :class:`Bool`
    :param can_post_messages: True, if the administrator can create channel posts; applicable to channels only
    :type can_post_messages: :class:`Bool`
    :param can_edit_messages: True, if the administrator can edit messages of other users and pin messages; applicable to channels only
    :type can_edit_messages: :class:`Bool`
    :param can_delete_messages: True, if the administrator can delete messages of other users
    :type can_delete_messages: :class:`Bool`
    :param can_invite_users: True, if the administrator can invite new users to the chat
    :type can_invite_users: :class:`Bool`
    :param can_restrict_members: True, if the administrator can restrict, ban, or unban chat members; always true for channels
    :type can_restrict_members: :class:`Bool`
    :param can_pin_messages: True, if the administrator can pin messages; applicable to basic groups and supergroups only
    :type can_pin_messages: :class:`Bool`
    :param can_manage_topics: True, if the administrator can manage topics; applicable to forum supergroups only
    :type can_manage_topics: :class:`Bool`
    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that were directly or indirectly promoted by them
    :type can_promote_members: :class:`Bool`
    :param can_manage_video_chats: True, if the administrator can manage video chats
    :type can_manage_video_chats: :class:`Bool`
    :param is_anonymous: True, if the administrator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only
    :type is_anonymous: :class:`Bool`
    """

    ID: typing.Literal["chatAdministratorRights"] = "chatAdministratorRights"
    can_manage_chat: Bool = False
    can_change_info: Bool = False
    can_post_messages: Bool = False
    can_edit_messages: Bool = False
    can_delete_messages: Bool = False
    can_invite_users: Bool = False
    can_restrict_members: Bool = False
    can_pin_messages: Bool = False
    can_manage_topics: Bool = False
    can_promote_members: Bool = False
    can_manage_video_chats: Bool = False
    is_anonymous: Bool = False


class ChatAdministrators(BaseObject):
    """
    Represents a list of chat administrators

    :param administrators: A list of chat administrators
    :type administrators: :class:`Vector[ChatAdministrator]`
    """

    ID: typing.Literal["chatAdministrators"] = "chatAdministrators"
    administrators: Vector[ChatAdministrator]


class ChatAvailableReactionsAll(BaseObject):
    """
    All reactions are available in the chat
    """

    ID: typing.Literal["chatAvailableReactionsAll"] = "chatAvailableReactionsAll"


class ChatAvailableReactionsSome(BaseObject):
    """
    Only specific reactions are available in the chat

    :param reactions: The list of reactions
    :type reactions: :class:`Vector[ReactionType]`
    """

    ID: typing.Literal["chatAvailableReactionsSome"] = "chatAvailableReactionsSome"
    reactions: Vector[ReactionType]


ChatAvailableReactions = typing.Union[
    ChatAvailableReactionsAll,
    ChatAvailableReactionsSome,
]


class ChatBackground(BaseObject):
    """
    Describes a background set for a specific chat

    :param background: The background
    :type background: :class:`Background`
    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100
    :type dark_theme_dimming: :class:`Int32`
    """

    ID: typing.Literal["chatBackground"] = "chatBackground"
    background: Background
    dark_theme_dimming: Int32


class ChatEvent(BaseObject):
    """
    Represents a chat event

    :param id: Chat event identifier
    :type id: :class:`Int64`
    :param date: Point in time (Unix timestamp) when the event happened
    :type date: :class:`Int32`
    :param member_id: Identifier of the user or chat who performed the action
    :type member_id: :class:`MessageSender`
    :param action: The action
    :type action: :class:`ChatEventAction`
    """

    ID: typing.Literal["chatEvent"] = "chatEvent"
    id: Int64
    date: Int32
    member_id: MessageSender
    action: ChatEventAction


class ChatEventActiveUsernamesChanged(BaseObject):
    """
    The chat active usernames were changed

    :param old_usernames: Previous list of active usernames
    :type old_usernames: :class:`Vector[String]`
    :param new_usernames: New list of active usernames
    :type new_usernames: :class:`Vector[String]`
    """

    ID: typing.Literal["chatEventActiveUsernamesChanged"] = "chatEventActiveUsernamesChanged"
    old_usernames: Vector[String]
    new_usernames: Vector[String]


class ChatEventAvailableReactionsChanged(BaseObject):
    """
    The chat available reactions were changed

    :param old_available_reactions: Previous chat available reactions
    :type old_available_reactions: :class:`ChatAvailableReactions`
    :param new_available_reactions: New chat available reactions
    :type new_available_reactions: :class:`ChatAvailableReactions`
    """

    ID: typing.Literal["chatEventAvailableReactionsChanged"] = "chatEventAvailableReactionsChanged"
    old_available_reactions: ChatAvailableReactions
    new_available_reactions: ChatAvailableReactions


class ChatEventDescriptionChanged(BaseObject):
    """
    The chat description was changed

    :param old_description: Previous chat description
    :type old_description: :class:`String`
    :param new_description: New chat description
    :type new_description: :class:`String`
    """

    ID: typing.Literal["chatEventDescriptionChanged"] = "chatEventDescriptionChanged"
    old_description: String
    new_description: String


class ChatEventForumTopicCreated(BaseObject):
    """
    A new forum topic was created

    :param topic_info: Information about the topic
    :type topic_info: :class:`ForumTopicInfo`
    """

    ID: typing.Literal["chatEventForumTopicCreated"] = "chatEventForumTopicCreated"
    topic_info: ForumTopicInfo


class ChatEventForumTopicDeleted(BaseObject):
    """
    A forum topic was deleted

    :param topic_info: Information about the topic
    :type topic_info: :class:`ForumTopicInfo`
    """

    ID: typing.Literal["chatEventForumTopicDeleted"] = "chatEventForumTopicDeleted"
    topic_info: ForumTopicInfo


class ChatEventForumTopicEdited(BaseObject):
    """
    A forum topic was edited

    :param old_topic_info: Old information about the topic
    :type old_topic_info: :class:`ForumTopicInfo`
    :param new_topic_info: New information about the topic
    :type new_topic_info: :class:`ForumTopicInfo`
    """

    ID: typing.Literal["chatEventForumTopicEdited"] = "chatEventForumTopicEdited"
    old_topic_info: ForumTopicInfo
    new_topic_info: ForumTopicInfo


class ChatEventForumTopicPinned(BaseObject):
    """
    A pinned forum topic was changed

    :param old_topic_info: Information about the old pinned topic; may be null, defaults to None
    :type old_topic_info: :class:`ForumTopicInfo`, optional
    :param new_topic_info: Information about the new pinned topic; may be null, defaults to None
    :type new_topic_info: :class:`ForumTopicInfo`, optional
    """

    ID: typing.Literal["chatEventForumTopicPinned"] = "chatEventForumTopicPinned"
    old_topic_info: typing.Optional[ForumTopicInfo] = None
    new_topic_info: typing.Optional[ForumTopicInfo] = None


class ChatEventForumTopicToggleIsClosed(BaseObject):
    """
    A forum topic was closed or reopened

    :param topic_info: New information about the topic
    :type topic_info: :class:`ForumTopicInfo`
    """

    ID: typing.Literal["chatEventForumTopicToggleIsClosed"] = "chatEventForumTopicToggleIsClosed"
    topic_info: ForumTopicInfo


class ChatEventForumTopicToggleIsHidden(BaseObject):
    """
    The General forum topic was hidden or unhidden

    :param topic_info: New information about the topic
    :type topic_info: :class:`ForumTopicInfo`
    """

    ID: typing.Literal["chatEventForumTopicToggleIsHidden"] = "chatEventForumTopicToggleIsHidden"
    topic_info: ForumTopicInfo


class ChatEventHasAggressiveAntiSpamEnabledToggled(BaseObject):
    """
    The has_aggressive_anti_spam_enabled setting of a supergroup was toggled

    :param has_aggressive_anti_spam_enabled: New value of has_aggressive_anti_spam_enabled
    :type has_aggressive_anti_spam_enabled: :class:`Bool`
    """

    ID: typing.Literal["chatEventHasAggressiveAntiSpamEnabledToggled"] = "chatEventHasAggressiveAntiSpamEnabledToggled"
    has_aggressive_anti_spam_enabled: Bool


class ChatEventHasProtectedContentToggled(BaseObject):
    """
    The has_protected_content setting of a channel was toggled

    :param has_protected_content: New value of has_protected_content
    :type has_protected_content: :class:`Bool`
    """

    ID: typing.Literal["chatEventHasProtectedContentToggled"] = "chatEventHasProtectedContentToggled"
    has_protected_content: Bool


class ChatEventInviteLinkDeleted(BaseObject):
    """
    A revoked chat invite link was deleted

    :param invite_link: The invite link
    :type invite_link: :class:`ChatInviteLink`
    """

    ID: typing.Literal["chatEventInviteLinkDeleted"] = "chatEventInviteLinkDeleted"
    invite_link: ChatInviteLink


class ChatEventInviteLinkEdited(BaseObject):
    """
    A chat invite link was edited

    :param old_invite_link: Previous information about the invite link
    :type old_invite_link: :class:`ChatInviteLink`
    :param new_invite_link: New information about the invite link
    :type new_invite_link: :class:`ChatInviteLink`
    """

    ID: typing.Literal["chatEventInviteLinkEdited"] = "chatEventInviteLinkEdited"
    old_invite_link: ChatInviteLink
    new_invite_link: ChatInviteLink


class ChatEventInviteLinkRevoked(BaseObject):
    """
    A chat invite link was revoked

    :param invite_link: The invite link
    :type invite_link: :class:`ChatInviteLink`
    """

    ID: typing.Literal["chatEventInviteLinkRevoked"] = "chatEventInviteLinkRevoked"
    invite_link: ChatInviteLink


class ChatEventInvitesToggled(BaseObject):
    """
    The can_invite_users permission of a supergroup chat was toggled

    :param can_invite_users: New value of can_invite_users permission
    :type can_invite_users: :class:`Bool`
    """

    ID: typing.Literal["chatEventInvitesToggled"] = "chatEventInvitesToggled"
    can_invite_users: Bool


class ChatEventIsAllHistoryAvailableToggled(BaseObject):
    """
    The is_all_history_available setting of a supergroup was toggled

    :param is_all_history_available: New value of is_all_history_available
    :type is_all_history_available: :class:`Bool`
    """

    ID: typing.Literal["chatEventIsAllHistoryAvailableToggled"] = "chatEventIsAllHistoryAvailableToggled"
    is_all_history_available: Bool


class ChatEventIsForumToggled(BaseObject):
    """
    The is_forum setting of a channel was toggled

    :param is_forum: New value of is_forum
    :type is_forum: :class:`Bool`
    """

    ID: typing.Literal["chatEventIsForumToggled"] = "chatEventIsForumToggled"
    is_forum: Bool


class ChatEventLinkedChatChanged(BaseObject):
    """
    The linked chat of a supergroup was changed

    :param old_linked_chat_id: Previous supergroup linked chat identifier
    :type old_linked_chat_id: :class:`Int53`
    :param new_linked_chat_id: New supergroup linked chat identifier
    :type new_linked_chat_id: :class:`Int53`
    """

    ID: typing.Literal["chatEventLinkedChatChanged"] = "chatEventLinkedChatChanged"
    old_linked_chat_id: Int53
    new_linked_chat_id: Int53


class ChatEventLocationChanged(BaseObject):
    """
    The supergroup location was changed

    :param old_location: Previous location; may be null, defaults to None
    :type old_location: :class:`ChatLocation`, optional
    :param new_location: New location; may be null, defaults to None
    :type new_location: :class:`ChatLocation`, optional
    """

    ID: typing.Literal["chatEventLocationChanged"] = "chatEventLocationChanged"
    old_location: typing.Optional[ChatLocation] = None
    new_location: typing.Optional[ChatLocation] = None


class ChatEventMemberInvited(BaseObject):
    """
    A new chat member was invited

    :param user_id: New member user identifier
    :type user_id: :class:`Int53`
    :param status: New member status
    :type status: :class:`ChatMemberStatus`
    """

    ID: typing.Literal["chatEventMemberInvited"] = "chatEventMemberInvited"
    user_id: Int53
    status: ChatMemberStatus


class ChatEventMemberJoined(BaseObject):
    """
    A new member joined the chat
    """

    ID: typing.Literal["chatEventMemberJoined"] = "chatEventMemberJoined"


class ChatEventMemberJoinedByInviteLink(BaseObject):
    """
    A new member joined the chat via an invite link

    :param invite_link: Invite link used to join the chat
    :type invite_link: :class:`ChatInviteLink`
    :param via_chat_folder_invite_link: True, if the user has joined the chat using an invite link for a chat folder
    :type via_chat_folder_invite_link: :class:`Bool`
    """

    ID: typing.Literal["chatEventMemberJoinedByInviteLink"] = "chatEventMemberJoinedByInviteLink"
    invite_link: ChatInviteLink
    via_chat_folder_invite_link: Bool = False


class ChatEventMemberJoinedByRequest(BaseObject):
    """
    A new member was accepted to the chat by an administrator

    :param approver_user_id: User identifier of the chat administrator, approved user join request
    :type approver_user_id: :class:`Int53`
    :param invite_link: Invite link used to join the chat; may be null, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    """

    ID: typing.Literal["chatEventMemberJoinedByRequest"] = "chatEventMemberJoinedByRequest"
    approver_user_id: Int53
    invite_link: typing.Optional[ChatInviteLink] = None


class ChatEventMemberLeft(BaseObject):
    """
    A member left the chat
    """

    ID: typing.Literal["chatEventMemberLeft"] = "chatEventMemberLeft"


class ChatEventMemberPromoted(BaseObject):
    """
    A chat member has gained/lost administrator status, or the list of their administrator privileges has changed

    :param user_id: Affected chat member user identifier
    :type user_id: :class:`Int53`
    :param old_status: Previous status of the chat member
    :type old_status: :class:`ChatMemberStatus`
    :param new_status: New status of the chat member
    :type new_status: :class:`ChatMemberStatus`
    """

    ID: typing.Literal["chatEventMemberPromoted"] = "chatEventMemberPromoted"
    user_id: Int53
    old_status: ChatMemberStatus
    new_status: ChatMemberStatus


class ChatEventMemberRestricted(BaseObject):
    """
    A chat member was restricted/unrestricted or banned/unbanned, or the list of their restrictions has changed

    :param member_id: Affected chat member identifier
    :type member_id: :class:`MessageSender`
    :param old_status: Previous status of the chat member
    :type old_status: :class:`ChatMemberStatus`
    :param new_status: New status of the chat member
    :type new_status: :class:`ChatMemberStatus`
    """

    ID: typing.Literal["chatEventMemberRestricted"] = "chatEventMemberRestricted"
    member_id: MessageSender
    old_status: ChatMemberStatus
    new_status: ChatMemberStatus


class ChatEventMessageAutoDeleteTimeChanged(BaseObject):
    """
    The message auto-delete timer was changed

    :param old_message_auto_delete_time: Previous value of message_auto_delete_time
    :type old_message_auto_delete_time: :class:`Int32`
    :param new_message_auto_delete_time: New value of message_auto_delete_time
    :type new_message_auto_delete_time: :class:`Int32`
    """

    ID: typing.Literal["chatEventMessageAutoDeleteTimeChanged"] = "chatEventMessageAutoDeleteTimeChanged"
    old_message_auto_delete_time: Int32
    new_message_auto_delete_time: Int32


class ChatEventMessageDeleted(BaseObject):
    """
    A message was deleted

    :param message: Deleted message
    :type message: :class:`Message`
    :param can_report_anti_spam_false_positive: True, if the message deletion can be reported via reportSupergroupAntiSpamFalsePositive
    :type can_report_anti_spam_false_positive: :class:`Bool`
    """

    ID: typing.Literal["chatEventMessageDeleted"] = "chatEventMessageDeleted"
    message: Message
    can_report_anti_spam_false_positive: Bool = False


class ChatEventMessageEdited(BaseObject):
    """
    A message was edited

    :param old_message: The original message before the edit
    :type old_message: :class:`Message`
    :param new_message: The message after it was edited
    :type new_message: :class:`Message`
    """

    ID: typing.Literal["chatEventMessageEdited"] = "chatEventMessageEdited"
    old_message: Message
    new_message: Message


class ChatEventMessagePinned(BaseObject):
    """
    A message was pinned

    :param message: Pinned message
    :type message: :class:`Message`
    """

    ID: typing.Literal["chatEventMessagePinned"] = "chatEventMessagePinned"
    message: Message


class ChatEventMessageUnpinned(BaseObject):
    """
    A message was unpinned

    :param message: Unpinned message
    :type message: :class:`Message`
    """

    ID: typing.Literal["chatEventMessageUnpinned"] = "chatEventMessageUnpinned"
    message: Message


class ChatEventPermissionsChanged(BaseObject):
    """
    The chat permissions was changed

    :param old_permissions: Previous chat permissions
    :type old_permissions: :class:`ChatPermissions`
    :param new_permissions: New chat permissions
    :type new_permissions: :class:`ChatPermissions`
    """

    ID: typing.Literal["chatEventPermissionsChanged"] = "chatEventPermissionsChanged"
    old_permissions: ChatPermissions
    new_permissions: ChatPermissions


class ChatEventPhotoChanged(BaseObject):
    """
    The chat photo was changed

    :param old_photo: Previous chat photo value; may be null, defaults to None
    :type old_photo: :class:`ChatPhoto`, optional
    :param new_photo: New chat photo value; may be null, defaults to None
    :type new_photo: :class:`ChatPhoto`, optional
    """

    ID: typing.Literal["chatEventPhotoChanged"] = "chatEventPhotoChanged"
    old_photo: typing.Optional[ChatPhoto] = None
    new_photo: typing.Optional[ChatPhoto] = None


class ChatEventPollStopped(BaseObject):
    """
    A poll in a message was stopped

    :param message: The message with the poll
    :type message: :class:`Message`
    """

    ID: typing.Literal["chatEventPollStopped"] = "chatEventPollStopped"
    message: Message


class ChatEventSignMessagesToggled(BaseObject):
    """
    The sign_messages setting of a channel was toggled

    :param sign_messages: New value of sign_messages
    :type sign_messages: :class:`Bool`
    """

    ID: typing.Literal["chatEventSignMessagesToggled"] = "chatEventSignMessagesToggled"
    sign_messages: Bool


class ChatEventSlowModeDelayChanged(BaseObject):
    """
    The slow_mode_delay setting of a supergroup was changed

    :param old_slow_mode_delay: Previous value of slow_mode_delay, in seconds
    :type old_slow_mode_delay: :class:`Int32`
    :param new_slow_mode_delay: New value of slow_mode_delay, in seconds
    :type new_slow_mode_delay: :class:`Int32`
    """

    ID: typing.Literal["chatEventSlowModeDelayChanged"] = "chatEventSlowModeDelayChanged"
    old_slow_mode_delay: Int32
    new_slow_mode_delay: Int32


class ChatEventStickerSetChanged(BaseObject):
    """
    The supergroup sticker set was changed

    :param old_sticker_set_id: Previous identifier of the chat sticker set; 0 if none, defaults to None
    :type old_sticker_set_id: :class:`Int64`, optional
    :param new_sticker_set_id: New identifier of the chat sticker set; 0 if none, defaults to None
    :type new_sticker_set_id: :class:`Int64`, optional
    """

    ID: typing.Literal["chatEventStickerSetChanged"] = "chatEventStickerSetChanged"
    old_sticker_set_id: typing.Optional[Int64] = 0
    new_sticker_set_id: typing.Optional[Int64] = 0


class ChatEventTitleChanged(BaseObject):
    """
    The chat title was changed

    :param old_title: Previous chat title
    :type old_title: :class:`String`
    :param new_title: New chat title
    :type new_title: :class:`String`
    """

    ID: typing.Literal["chatEventTitleChanged"] = "chatEventTitleChanged"
    old_title: String
    new_title: String


class ChatEventUsernameChanged(BaseObject):
    """
    The chat editable username was changed

    :param old_username: Previous chat username
    :type old_username: :class:`String`
    :param new_username: New chat username
    :type new_username: :class:`String`
    """

    ID: typing.Literal["chatEventUsernameChanged"] = "chatEventUsernameChanged"
    old_username: String
    new_username: String


class ChatEventVideoChatCreated(BaseObject):
    """
    A video chat was created

    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["chatEventVideoChatCreated"] = "chatEventVideoChatCreated"
    group_call_id: Int32


class ChatEventVideoChatEnded(BaseObject):
    """
    A video chat was ended

    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["chatEventVideoChatEnded"] = "chatEventVideoChatEnded"
    group_call_id: Int32


class ChatEventVideoChatMuteNewParticipantsToggled(BaseObject):
    """
    The mute_new_participants setting of a video chat was toggled

    :param mute_new_participants: New value of the mute_new_participants setting
    :type mute_new_participants: :class:`Bool`
    """

    ID: typing.Literal["chatEventVideoChatMuteNewParticipantsToggled"] = "chatEventVideoChatMuteNewParticipantsToggled"
    mute_new_participants: Bool


class ChatEventVideoChatParticipantIsMutedToggled(BaseObject):
    """
    A video chat participant was muted or unmuted

    :param participant_id: Identifier of the affected group call participant
    :type participant_id: :class:`MessageSender`
    :param is_muted: New value of is_muted
    :type is_muted: :class:`Bool`
    """

    ID: typing.Literal["chatEventVideoChatParticipantIsMutedToggled"] = "chatEventVideoChatParticipantIsMutedToggled"
    participant_id: MessageSender
    is_muted: Bool


class ChatEventVideoChatParticipantVolumeLevelChanged(BaseObject):
    """
    A video chat participant volume level was changed

    :param participant_id: Identifier of the affected group call participant
    :type participant_id: :class:`MessageSender`
    :param volume_level: New value of volume_level; 1-20000 in hundreds of percents
    :type volume_level: :class:`Int32`
    """

    ID: typing.Literal[
        "chatEventVideoChatParticipantVolumeLevelChanged"
    ] = "chatEventVideoChatParticipantVolumeLevelChanged"
    participant_id: MessageSender
    volume_level: Int32


ChatEventAction = typing.Union[
    ChatEventActiveUsernamesChanged,
    ChatEventAvailableReactionsChanged,
    ChatEventDescriptionChanged,
    ChatEventForumTopicCreated,
    ChatEventForumTopicDeleted,
    ChatEventForumTopicEdited,
    ChatEventForumTopicPinned,
    ChatEventForumTopicToggleIsClosed,
    ChatEventForumTopicToggleIsHidden,
    ChatEventHasAggressiveAntiSpamEnabledToggled,
    ChatEventHasProtectedContentToggled,
    ChatEventInviteLinkDeleted,
    ChatEventInviteLinkEdited,
    ChatEventInviteLinkRevoked,
    ChatEventInvitesToggled,
    ChatEventIsAllHistoryAvailableToggled,
    ChatEventIsForumToggled,
    ChatEventLinkedChatChanged,
    ChatEventLocationChanged,
    ChatEventMemberInvited,
    ChatEventMemberJoined,
    ChatEventMemberJoinedByInviteLink,
    ChatEventMemberJoinedByRequest,
    ChatEventMemberLeft,
    ChatEventMemberPromoted,
    ChatEventMemberRestricted,
    ChatEventMessageAutoDeleteTimeChanged,
    ChatEventMessageDeleted,
    ChatEventMessageEdited,
    ChatEventMessagePinned,
    ChatEventMessageUnpinned,
    ChatEventPermissionsChanged,
    ChatEventPhotoChanged,
    ChatEventPollStopped,
    ChatEventSignMessagesToggled,
    ChatEventSlowModeDelayChanged,
    ChatEventStickerSetChanged,
    ChatEventTitleChanged,
    ChatEventUsernameChanged,
    ChatEventVideoChatCreated,
    ChatEventVideoChatEnded,
    ChatEventVideoChatMuteNewParticipantsToggled,
    ChatEventVideoChatParticipantIsMutedToggled,
    ChatEventVideoChatParticipantVolumeLevelChanged,
]


class ChatEventLogFilters(BaseObject):
    """
    Represents a set of filters used to obtain a chat event log

    :param message_edits: True, if message edits need to be returned
    :type message_edits: :class:`Bool`
    :param message_deletions: True, if message deletions need to be returned
    :type message_deletions: :class:`Bool`
    :param message_pins: True, if pin/unpin events need to be returned
    :type message_pins: :class:`Bool`
    :param member_joins: True, if members joining events need to be returned
    :type member_joins: :class:`Bool`
    :param member_leaves: True, if members leaving events need to be returned
    :type member_leaves: :class:`Bool`
    :param member_invites: True, if invited member events need to be returned
    :type member_invites: :class:`Bool`
    :param member_promotions: True, if member promotion/demotion events need to be returned
    :type member_promotions: :class:`Bool`
    :param member_restrictions: True, if member restricted/unrestricted/banned/unbanned events need to be returned
    :type member_restrictions: :class:`Bool`
    :param info_changes: True, if changes in chat information need to be returned
    :type info_changes: :class:`Bool`
    :param setting_changes: True, if changes in chat settings need to be returned
    :type setting_changes: :class:`Bool`
    :param invite_link_changes: True, if changes to invite links need to be returned
    :type invite_link_changes: :class:`Bool`
    :param video_chat_changes: True, if video chat actions need to be returned
    :type video_chat_changes: :class:`Bool`
    :param forum_changes: True, if forum-related actions need to be returned
    :type forum_changes: :class:`Bool`
    """

    ID: typing.Literal["chatEventLogFilters"] = "chatEventLogFilters"
    message_edits: Bool = False
    message_deletions: Bool = False
    message_pins: Bool = False
    member_joins: Bool = False
    member_leaves: Bool = False
    member_invites: Bool = False
    member_promotions: Bool = False
    member_restrictions: Bool = False
    info_changes: Bool = False
    setting_changes: Bool = False
    invite_link_changes: Bool = False
    video_chat_changes: Bool = False
    forum_changes: Bool = False


class ChatEvents(BaseObject):
    """
    Contains a list of chat events

    :param events: List of events
    :type events: :class:`Vector[ChatEvent]`
    """

    ID: typing.Literal["chatEvents"] = "chatEvents"
    events: Vector[ChatEvent]


class ChatFolder(BaseObject):
    """
    Represents a folder for user chats

    :param title: The title of the folder; 1-12 characters without line feeds
    :type title: :class:`String`
    :param pinned_chat_ids: The chat identifiers of pinned chats in the folder. There can be up to getOption("chat_folder_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :type pinned_chat_ids: :class:`Vector[Int53]`
    :param included_chat_ids: The chat identifiers of always included chats in the folder. There can be up to getOption("chat_folder_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :type included_chat_ids: :class:`Vector[Int53]`
    :param excluded_chat_ids: The chat identifiers of always excluded chats in the folder. There can be up to getOption("chat_folder_chosen_chat_count_max") always excluded non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :type excluded_chat_ids: :class:`Vector[Int53]`
    :param icon: The chosen icon for the chat folder; may be null. If null, use getChatFolderDefaultIconName to get default icon name for the folder, defaults to None
    :type icon: :class:`ChatFolderIcon`, optional
    :param is_shareable: True, if at least one link has been created for the folder
    :type is_shareable: :class:`Bool`
    :param exclude_muted: True, if muted chats need to be excluded
    :type exclude_muted: :class:`Bool`
    :param exclude_read: True, if read chats need to be excluded
    :type exclude_read: :class:`Bool`
    :param exclude_archived: True, if archived chats need to be excluded
    :type exclude_archived: :class:`Bool`
    :param include_contacts: True, if contacts need to be included
    :type include_contacts: :class:`Bool`
    :param include_non_contacts: True, if non-contact users need to be included
    :type include_non_contacts: :class:`Bool`
    :param include_bots: True, if bots need to be included
    :type include_bots: :class:`Bool`
    :param include_groups: True, if basic groups and supergroups need to be included
    :type include_groups: :class:`Bool`
    :param include_channels: True, if channels need to be included
    :type include_channels: :class:`Bool`
    """

    ID: typing.Literal["chatFolder"] = "chatFolder"
    title: String = Field(..., min_length=1, max_length=12)
    pinned_chat_ids: Vector[Int53]
    included_chat_ids: Vector[Int53]
    excluded_chat_ids: Vector[Int53]
    icon: typing.Optional[ChatFolderIcon] = None
    is_shareable: Bool = False
    exclude_muted: Bool = False
    exclude_read: Bool = False
    exclude_archived: Bool = False
    include_contacts: Bool = False
    include_non_contacts: Bool = False
    include_bots: Bool = False
    include_groups: Bool = False
    include_channels: Bool = False


class ChatFolderIcon(BaseObject):
    """
    Represents an icon for a chat folder

    :param name: The chosen icon name for short folder representation; one of "All", "Unread", "Unmuted", "Bots", "Channels", "Groups", "Private", "Custom", "Setup", "Cat", "Crown", "Favorite", "Flower", "Game", "Home", "Love", "Mask", "Party", "Sport", "Study", "Trade", "Travel", "Work", "Airplane", "Book", "Light", "Like", "Money", "Note", "Palette"
    :type name: :class:`String`
    """

    ID: typing.Literal["chatFolderIcon"] = "chatFolderIcon"
    name: String


class ChatFolderInfo(BaseObject):
    """
    Contains basic information about a chat folder

    :param id: Unique chat folder identifier
    :type id: :class:`Int32`
    :param title: The title of the folder; 1-12 characters without line feeds
    :type title: :class:`String`
    :param icon: The chosen or default icon for the chat folder
    :type icon: :class:`ChatFolderIcon`
    :param is_shareable: True, if at least one link has been created for the folder
    :type is_shareable: :class:`Bool`
    :param has_my_invite_links: True, if the chat folder has invite links created by the current user
    :type has_my_invite_links: :class:`Bool`
    """

    ID: typing.Literal["chatFolderInfo"] = "chatFolderInfo"
    id: Int32
    title: String = Field(..., min_length=1, max_length=12)
    icon: ChatFolderIcon
    is_shareable: Bool = False
    has_my_invite_links: Bool = False


class ChatFolderInviteLink(BaseObject):
    """
    Contains a chat folder invite link

    :param invite_link: The chat folder invite link
    :type invite_link: :class:`String`
    :param name: Name of the link
    :type name: :class:`String`
    :param chat_ids: Identifiers of chats, included in the link
    :type chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["chatFolderInviteLink"] = "chatFolderInviteLink"
    invite_link: String
    name: String
    chat_ids: Vector[Int53]


class ChatFolderInviteLinkInfo(BaseObject):
    """
    Contains information about an invite link to a chat folder

    :param chat_folder_info: Basic information about the chat folder; chat folder identifier will be 0 if the user didn't have the chat folder yet
    :type chat_folder_info: :class:`ChatFolderInfo`
    :param missing_chat_ids: Identifiers of the chats from the link, which aren't added to the folder yet
    :type missing_chat_ids: :class:`Vector[Int53]`
    :param added_chat_ids: Identifiers of the chats from the link, which are added to the folder already
    :type added_chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["chatFolderInviteLinkInfo"] = "chatFolderInviteLinkInfo"
    chat_folder_info: ChatFolderInfo
    missing_chat_ids: Vector[Int53]
    added_chat_ids: Vector[Int53]


class ChatFolderInviteLinks(BaseObject):
    """
    Represents a list of chat folder invite links

    :param invite_links: List of the invite links
    :type invite_links: :class:`Vector[ChatFolderInviteLink]`
    """

    ID: typing.Literal["chatFolderInviteLinks"] = "chatFolderInviteLinks"
    invite_links: Vector[ChatFolderInviteLink]


class ChatInviteLink(BaseObject):
    """
    Contains a chat invite link

    :param invite_link: Chat invite link
    :type invite_link: :class:`String`
    :param name: Name of the link
    :type name: :class:`String`
    :param creator_user_id: User identifier of an administrator created the link
    :type creator_user_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) when the link was created
    :type date: :class:`Int32`
    :param edit_date: Point in time (Unix timestamp) when the link was last edited; 0 if never or unknown
    :type edit_date: :class:`Int32`
    :param expiration_date: Point in time (Unix timestamp) when the link will expire; 0 if never
    :type expiration_date: :class:`Int32`
    :param member_limit: The maximum number of members, which can join the chat using the link simultaneously; 0 if not limited. Always 0 if the link requires approval
    :type member_limit: :class:`Int32`
    :param member_count: Number of chat members, which joined the chat using the link
    :type member_count: :class:`Int32`
    :param pending_join_request_count: Number of pending join requests created using this link
    :type pending_join_request_count: :class:`Int32`
    :param creates_join_request: True, if the link only creates join request. If true, total number of joining members will be unlimited
    :type creates_join_request: :class:`Bool`
    :param is_primary: True, if the link is primary. Primary invite link can't have name, expiration date, or usage limit. There is exactly one primary invite link for each administrator with can_invite_users right at a given time
    :type is_primary: :class:`Bool`
    :param is_revoked: True, if the link was revoked
    :type is_revoked: :class:`Bool`
    """

    ID: typing.Literal["chatInviteLink"] = "chatInviteLink"
    invite_link: String
    name: String
    creator_user_id: Int53
    date: Int32
    edit_date: Int32
    expiration_date: Int32
    member_limit: Int32
    member_count: Int32
    pending_join_request_count: Int32
    creates_join_request: Bool = False
    is_primary: Bool = False
    is_revoked: Bool = False


class ChatInviteLinkCount(BaseObject):
    """
    Describes a chat administrator with a number of active and revoked chat invite links

    :param user_id: Administrator's user identifier
    :type user_id: :class:`Int53`
    :param invite_link_count: Number of active invite links
    :type invite_link_count: :class:`Int32`
    :param revoked_invite_link_count: Number of revoked invite links
    :type revoked_invite_link_count: :class:`Int32`
    """

    ID: typing.Literal["chatInviteLinkCount"] = "chatInviteLinkCount"
    user_id: Int53
    invite_link_count: Int32
    revoked_invite_link_count: Int32


class ChatInviteLinkCounts(BaseObject):
    """
    Contains a list of chat invite link counts

    :param invite_link_counts: List of invite link counts
    :type invite_link_counts: :class:`Vector[ChatInviteLinkCount]`
    """

    ID: typing.Literal["chatInviteLinkCounts"] = "chatInviteLinkCounts"
    invite_link_counts: Vector[ChatInviteLinkCount]


class ChatInviteLinkInfo(BaseObject):
    """
    Contains information about a chat invite link

    :param chat_id: Chat identifier of the invite link; 0 if the user has no access to the chat before joining
    :type chat_id: :class:`Int53`
    :param accessible_for: If non-zero, the amount of time for which read access to the chat will remain available, in seconds
    :type accessible_for: :class:`Int32`
    :param type_: Type of the chat
    :type type_: :class:`InviteLinkChatType`
    :param title: Title of the chat
    :type title: :class:`String`
    :param description: Chat description
    :type description: :class:`String`
    :param member_count: Number of members in the chat
    :type member_count: :class:`Int32`
    :param member_user_ids: User identifiers of some chat members that may be known to the current user
    :type member_user_ids: :class:`Vector[Int53]`
    :param photo: Chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    :param creates_join_request: True, if the link only creates join request
    :type creates_join_request: :class:`Bool`
    :param is_public: True, if the chat is a public supergroup or channel, i.e. it has a username or it is a location-based supergroup
    :type is_public: :class:`Bool`
    :param is_verified: True, if the chat is verified
    :type is_verified: :class:`Bool`
    :param is_scam: True, if many users reported this chat as a scam
    :type is_scam: :class:`Bool`
    :param is_fake: True, if many users reported this chat as a fake account
    :type is_fake: :class:`Bool`
    """

    ID: typing.Literal["chatInviteLinkInfo"] = "chatInviteLinkInfo"
    chat_id: Int53
    accessible_for: Int32
    type_: InviteLinkChatType = Field(..., alias="type")
    title: String
    description: String
    member_count: Int32
    member_user_ids: Vector[Int53]
    photo: typing.Optional[ChatPhotoInfo] = None
    creates_join_request: Bool = False
    is_public: Bool = False
    is_verified: Bool = False
    is_scam: Bool = False
    is_fake: Bool = False


class ChatInviteLinkMember(BaseObject):
    """
    Describes a chat member joined a chat via an invite link

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param joined_chat_date: Point in time (Unix timestamp) when the user joined the chat
    :type joined_chat_date: :class:`Int32`
    :param approver_user_id: User identifier of the chat administrator, approved user join request
    :type approver_user_id: :class:`Int53`
    :param via_chat_folder_invite_link: True, if the user has joined the chat using an invite link for a chat folder
    :type via_chat_folder_invite_link: :class:`Bool`
    """

    ID: typing.Literal["chatInviteLinkMember"] = "chatInviteLinkMember"
    user_id: Int53
    joined_chat_date: Int32
    approver_user_id: Int53
    via_chat_folder_invite_link: Bool = False


class ChatInviteLinkMembers(BaseObject):
    """
    Contains a list of chat members joined a chat via an invite link

    :param total_count: Approximate total number of chat members found
    :type total_count: :class:`Int32`
    :param members: List of chat members, joined a chat via an invite link
    :type members: :class:`Vector[ChatInviteLinkMember]`
    """

    ID: typing.Literal["chatInviteLinkMembers"] = "chatInviteLinkMembers"
    total_count: Int32
    members: Vector[ChatInviteLinkMember]


class ChatInviteLinks(BaseObject):
    """
    Contains a list of chat invite links

    :param total_count: Approximate total number of chat invite links found
    :type total_count: :class:`Int32`
    :param invite_links: List of invite links
    :type invite_links: :class:`Vector[ChatInviteLink]`
    """

    ID: typing.Literal["chatInviteLinks"] = "chatInviteLinks"
    total_count: Int32
    invite_links: Vector[ChatInviteLink]


class ChatJoinRequest(BaseObject):
    """
    Describes a user that sent a join request and waits for administrator approval

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) when the user sent the join request
    :type date: :class:`Int32`
    :param bio: A short bio of the user
    :type bio: :class:`String`
    """

    ID: typing.Literal["chatJoinRequest"] = "chatJoinRequest"
    user_id: Int53
    date: Int32
    bio: String


class ChatJoinRequests(BaseObject):
    """
    Contains a list of requests to join a chat

    :param total_count: Approximate total number of requests found
    :type total_count: :class:`Int32`
    :param requests: List of the requests
    :type requests: :class:`Vector[ChatJoinRequest]`
    """

    ID: typing.Literal["chatJoinRequests"] = "chatJoinRequests"
    total_count: Int32
    requests: Vector[ChatJoinRequest]


class ChatJoinRequestsInfo(BaseObject):
    """
    Contains information about pending join requests for a chat

    :param total_count: Total number of pending join requests
    :type total_count: :class:`Int32`
    :param user_ids: Identifiers of at most 3 users sent the newest pending join requests
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["chatJoinRequestsInfo"] = "chatJoinRequestsInfo"
    total_count: Int32
    user_ids: Vector[Int53]


class ChatListArchive(BaseObject):
    """
    A list of chats usually located at the top of the main chat list. Unmuted chats are automatically moved from the Archive to the Main chat list when a new message arrives
    """

    ID: typing.Literal["chatListArchive"] = "chatListArchive"


class ChatListFolder(BaseObject):
    """
    A list of chats added to a chat folder

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    """

    ID: typing.Literal["chatListFolder"] = "chatListFolder"
    chat_folder_id: Int32


class ChatListMain(BaseObject):
    """
    A main list of chats
    """

    ID: typing.Literal["chatListMain"] = "chatListMain"


ChatList = typing.Union[
    ChatListArchive,
    ChatListFolder,
    ChatListMain,
]


class ChatLists(BaseObject):
    """
    Contains a list of chat lists

    :param chat_lists: List of chat lists
    :type chat_lists: :class:`Vector[ChatList]`
    """

    ID: typing.Literal["chatLists"] = "chatLists"
    chat_lists: Vector[ChatList]


class ChatLocation(BaseObject):
    """
    Represents a location to which a chat is connected

    :param location: The location
    :type location: :class:`Location`
    :param address: Location address; 1-64 characters, as defined by the chat owner
    :type address: :class:`String`
    """

    ID: typing.Literal["chatLocation"] = "chatLocation"
    location: Location
    address: String = Field(..., min_length=1, max_length=64)


class ChatMember(BaseObject):
    """
    Describes a user or a chat as a member of another chat

    :param member_id: Identifier of the chat member. Currently, other chats can be only Left or Banned. Only supergroups and channels can have other chats as Left or Banned members and these chats must be supergroups or channels
    :type member_id: :class:`MessageSender`
    :param joined_chat_date: Point in time (Unix timestamp) when the user joined/was promoted/was banned in the chat
    :type joined_chat_date: :class:`Int32`
    :param status: Status of the member in the chat
    :type status: :class:`ChatMemberStatus`
    :param inviter_user_id: Identifier of a user that invited/promoted/banned this member in the chat; 0 if unknown, defaults to None
    :type inviter_user_id: :class:`Int53`, optional
    """

    ID: typing.Literal["chatMember"] = "chatMember"
    member_id: MessageSender
    joined_chat_date: Int32
    status: ChatMemberStatus
    inviter_user_id: typing.Optional[Int53] = 0


class ChatMemberStatusAdministrator(BaseObject):
    """
    The user is a member of the chat and has some additional privileges. In basic groups, administrators can edit and delete messages sent by others, add new members, ban unprivileged members, and manage video chats. In supergroups and channels, there are more detailed options for administrator privileges

    :param rights: Rights of the administrator
    :type rights: :class:`ChatAdministratorRights`
    :param custom_title: A custom title of the administrator; 0-16 characters without emojis; applicable to supergroups only
    :type custom_title: :class:`String`
    :param can_be_edited: True, if the current user can edit the administrator privileges for the called user
    :type can_be_edited: :class:`Bool`
    """

    ID: typing.Literal["chatMemberStatusAdministrator"] = "chatMemberStatusAdministrator"
    rights: ChatAdministratorRights
    custom_title: String = Field("", max_length=16)
    can_be_edited: Bool = False


class ChatMemberStatusBanned(BaseObject):
    """
    The user or the chat was banned (and hence is not a member of the chat). Implies the user can't return to the chat, view messages, or be used as a participant identifier to join a video chat of the chat

    :param banned_until_date: Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Always 0 in basic groups
    :type banned_until_date: :class:`Int32`
    """

    ID: typing.Literal["chatMemberStatusBanned"] = "chatMemberStatusBanned"
    banned_until_date: Int32


class ChatMemberStatusCreator(BaseObject):
    """
    The user is the owner of the chat and has all the administrator privileges

    :param custom_title: A custom title of the owner; 0-16 characters without emojis; applicable to supergroups only
    :type custom_title: :class:`String`
    :param is_anonymous: True, if the creator isn't shown in the chat member list and sends messages anonymously; applicable to supergroups only
    :type is_anonymous: :class:`Bool`
    :param is_member: True, if the user is a member of the chat
    :type is_member: :class:`Bool`
    """

    ID: typing.Literal["chatMemberStatusCreator"] = "chatMemberStatusCreator"
    custom_title: String = Field("", max_length=16)
    is_anonymous: Bool = False
    is_member: Bool = False


class ChatMemberStatusLeft(BaseObject):
    """
    The user or the chat is not a chat member
    """

    ID: typing.Literal["chatMemberStatusLeft"] = "chatMemberStatusLeft"


class ChatMemberStatusMember(BaseObject):
    """
    The user is a member of the chat, without any additional privileges or restrictions
    """

    ID: typing.Literal["chatMemberStatusMember"] = "chatMemberStatusMember"


class ChatMemberStatusRestricted(BaseObject):
    """
    The user is under certain restrictions in the chat. Not supported in basic groups and channels

    :param restricted_until_date: Point in time (Unix timestamp) when restrictions will be lifted from the user; 0 if never. If the user is restricted for more than 366 days or for less than 30 seconds from the current time, the user is considered to be restricted forever
    :type restricted_until_date: :class:`Int32`
    :param permissions: User permissions in the chat
    :type permissions: :class:`ChatPermissions`
    :param is_member: True, if the user is a member of the chat
    :type is_member: :class:`Bool`
    """

    ID: typing.Literal["chatMemberStatusRestricted"] = "chatMemberStatusRestricted"
    restricted_until_date: Int32
    permissions: ChatPermissions
    is_member: Bool = False


ChatMemberStatus = typing.Union[
    ChatMemberStatusAdministrator,
    ChatMemberStatusBanned,
    ChatMemberStatusCreator,
    ChatMemberStatusLeft,
    ChatMemberStatusMember,
    ChatMemberStatusRestricted,
]


class ChatMembers(BaseObject):
    """
    Contains a list of chat members

    :param total_count: Approximate total number of chat members found
    :type total_count: :class:`Int32`
    :param members: A list of chat members
    :type members: :class:`Vector[ChatMember]`
    """

    ID: typing.Literal["chatMembers"] = "chatMembers"
    total_count: Int32
    members: Vector[ChatMember]


class ChatMembersFilterAdministrators(BaseObject):
    """
    Returns the owner and administrators
    """

    ID: typing.Literal["chatMembersFilterAdministrators"] = "chatMembersFilterAdministrators"


class ChatMembersFilterBanned(BaseObject):
    """
    Returns users banned from the chat; can be used only by administrators in a supergroup or in a channel
    """

    ID: typing.Literal["chatMembersFilterBanned"] = "chatMembersFilterBanned"


class ChatMembersFilterBots(BaseObject):
    """
    Returns bot members of the chat
    """

    ID: typing.Literal["chatMembersFilterBots"] = "chatMembersFilterBots"


class ChatMembersFilterContacts(BaseObject):
    """
    Returns contacts of the user
    """

    ID: typing.Literal["chatMembersFilterContacts"] = "chatMembersFilterContacts"


class ChatMembersFilterMembers(BaseObject):
    """
    Returns all chat members, including restricted chat members
    """

    ID: typing.Literal["chatMembersFilterMembers"] = "chatMembersFilterMembers"


class ChatMembersFilterMention(BaseObject):
    """
    Returns users which can be mentioned in the chat

    :param message_thread_id: If non-zero, the identifier of the current message thread
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["chatMembersFilterMention"] = "chatMembersFilterMention"
    message_thread_id: Int53


class ChatMembersFilterRestricted(BaseObject):
    """
    Returns users under certain restrictions in the chat; can be used only by administrators in a supergroup
    """

    ID: typing.Literal["chatMembersFilterRestricted"] = "chatMembersFilterRestricted"


ChatMembersFilter = typing.Union[
    ChatMembersFilterAdministrators,
    ChatMembersFilterBanned,
    ChatMembersFilterBots,
    ChatMembersFilterContacts,
    ChatMembersFilterMembers,
    ChatMembersFilterMention,
    ChatMembersFilterRestricted,
]


class ChatMessageSender(BaseObject):
    """
    Represents a message sender, which can be used to send messages in a chat

    :param sender: Available message senders
    :type sender: :class:`MessageSender`
    :param needs_premium: True, if Telegram Premium is needed to use the message sender
    :type needs_premium: :class:`Bool`
    """

    ID: typing.Literal["chatMessageSender"] = "chatMessageSender"
    sender: MessageSender
    needs_premium: Bool = False


class ChatMessageSenders(BaseObject):
    """
    Represents a list of message senders, which can be used to send messages in a chat

    :param senders: List of available message senders
    :type senders: :class:`Vector[ChatMessageSender]`
    """

    ID: typing.Literal["chatMessageSenders"] = "chatMessageSenders"
    senders: Vector[ChatMessageSender]


class ChatNearby(BaseObject):
    """
    Describes a chat located nearby

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param distance: Distance to the chat location, in meters
    :type distance: :class:`Int32`
    """

    ID: typing.Literal["chatNearby"] = "chatNearby"
    chat_id: Int53
    distance: Int32


class ChatNotificationSettings(BaseObject):
    """
    Contains information about notification settings for a chat or a forum topic

    :param use_default_mute_for: If true, mute_for is ignored and the value for the relevant type of chat or the forum chat is used instead
    :type use_default_mute_for: :class:`Bool`
    :param mute_for: Time left before notifications will be unmuted, in seconds
    :type mute_for: :class:`Int32`
    :param use_default_sound: If true, the value for the relevant type of chat or the forum chat is used instead of sound_id
    :type use_default_sound: :class:`Bool`
    :param sound_id: Identifier of the notification sound to be played for messages; 0 if sound is disabled
    :type sound_id: :class:`Int64`
    :param use_default_show_preview: If true, show_preview is ignored and the value for the relevant type of chat or the forum chat is used instead
    :type use_default_show_preview: :class:`Bool`
    :param use_default_mute_stories: If true, mute_stories is ignored and the value for the relevant type of chat is used instead
    :type use_default_mute_stories: :class:`Bool`
    :param use_default_story_sound: If true, the value for the relevant type of chat is used instead of story_sound_id
    :type use_default_story_sound: :class:`Bool`
    :param story_sound_id: Identifier of the notification sound to be played for stories; 0 if sound is disabled
    :type story_sound_id: :class:`Int64`
    :param use_default_show_story_sender: If true, show_story_sender is ignored and the value for the relevant type of chat is used instead
    :type use_default_show_story_sender: :class:`Bool`
    :param use_default_disable_pinned_message_notifications: If true, disable_pinned_message_notifications is ignored and the value for the relevant type of chat or the forum chat is used instead
    :type use_default_disable_pinned_message_notifications: :class:`Bool`
    :param disable_pinned_message_notifications: If true, notifications for incoming pinned messages will be created as for an ordinary unread message
    :type disable_pinned_message_notifications: :class:`Bool`
    :param use_default_disable_mention_notifications: If true, disable_mention_notifications is ignored and the value for the relevant type of chat or the forum chat is used instead
    :type use_default_disable_mention_notifications: :class:`Bool`
    :param disable_mention_notifications: If true, notifications for messages with mentions will be created as for an ordinary unread message
    :type disable_mention_notifications: :class:`Bool`
    :param show_preview: True, if message content must be displayed in notifications
    :type show_preview: :class:`Bool`
    :param mute_stories: True, if story notifications are disabled for the chat
    :type mute_stories: :class:`Bool`
    :param show_story_sender: True, if the sender of stories must be displayed in notifications
    :type show_story_sender: :class:`Bool`
    """

    ID: typing.Literal["chatNotificationSettings"] = "chatNotificationSettings"
    use_default_mute_for: Bool
    mute_for: Int32
    use_default_sound: Bool
    sound_id: Int64
    use_default_show_preview: Bool
    use_default_mute_stories: Bool
    use_default_story_sound: Bool
    story_sound_id: Int64
    use_default_show_story_sender: Bool
    use_default_disable_pinned_message_notifications: Bool
    disable_pinned_message_notifications: Bool
    use_default_disable_mention_notifications: Bool
    disable_mention_notifications: Bool
    show_preview: Bool = False
    mute_stories: Bool = False
    show_story_sender: Bool = False


class ChatPermissions(BaseObject):
    """
    Describes actions that a user is allowed to take in a chat

    :param can_send_basic_messages: True, if the user can send text messages, contacts, invoices, locations, and venues
    :type can_send_basic_messages: :class:`Bool`
    :param can_send_audios: True, if the user can send music files
    :type can_send_audios: :class:`Bool`
    :param can_send_documents: True, if the user can send documents
    :type can_send_documents: :class:`Bool`
    :param can_send_photos: True, if the user can send audio photos
    :type can_send_photos: :class:`Bool`
    :param can_send_videos: True, if the user can send audio videos
    :type can_send_videos: :class:`Bool`
    :param can_send_video_notes: True, if the user can send video notes
    :type can_send_video_notes: :class:`Bool`
    :param can_send_voice_notes: True, if the user can send voice notes
    :type can_send_voice_notes: :class:`Bool`
    :param can_send_polls: True, if the user can send polls
    :type can_send_polls: :class:`Bool`
    :param can_send_other_messages: True, if the user can send animations, games, stickers, and dice and use inline bots
    :type can_send_other_messages: :class:`Bool`
    :param can_add_web_page_previews: True, if the user may add a web page preview to their messages
    :type can_add_web_page_previews: :class:`Bool`
    :param can_change_info: True, if the user can change the chat title, photo, and other settings
    :type can_change_info: :class:`Bool`
    :param can_invite_users: True, if the user can invite new users to the chat
    :type can_invite_users: :class:`Bool`
    :param can_pin_messages: True, if the user can pin messages
    :type can_pin_messages: :class:`Bool`
    :param can_manage_topics: True, if the user can manage topics
    :type can_manage_topics: :class:`Bool`
    """

    ID: typing.Literal["chatPermissions"] = "chatPermissions"
    can_send_basic_messages: Bool = False
    can_send_audios: Bool = False
    can_send_documents: Bool = False
    can_send_photos: Bool = False
    can_send_videos: Bool = False
    can_send_video_notes: Bool = False
    can_send_voice_notes: Bool = False
    can_send_polls: Bool = False
    can_send_other_messages: Bool = False
    can_add_web_page_previews: Bool = False
    can_change_info: Bool = False
    can_invite_users: Bool = False
    can_pin_messages: Bool = False
    can_manage_topics: Bool = False


class ChatPhoto(BaseObject):
    """
    Describes a chat or user profile photo

    :param id: Unique photo identifier
    :type id: :class:`Int64`
    :param added_date: Point in time (Unix timestamp) when the photo has been added
    :type added_date: :class:`Int32`
    :param sizes: Available variants of the photo in JPEG format, in different size
    :type sizes: :class:`Vector[PhotoSize]`
    :param minithumbnail: Photo minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param animation: A big (up to 1280x1280) animated variant of the photo in MPEG4 format; may be null, defaults to None
    :type animation: :class:`AnimatedChatPhoto`, optional
    :param small_animation: A small (160x160) animated variant of the photo in MPEG4 format; may be null even the big animation is available, defaults to None
    :type small_animation: :class:`AnimatedChatPhoto`, optional
    :param sticker: Sticker-based version of the chat photo; may be null, defaults to None
    :type sticker: :class:`ChatPhotoSticker`, optional
    """

    ID: typing.Literal["chatPhoto"] = "chatPhoto"
    id: Int64
    added_date: Int32
    sizes: Vector[PhotoSize]
    minithumbnail: typing.Optional[Minithumbnail] = None
    animation: typing.Optional[AnimatedChatPhoto] = None
    small_animation: typing.Optional[AnimatedChatPhoto] = None
    sticker: typing.Optional[ChatPhotoSticker] = None


class ChatPhotoInfo(BaseObject):
    """
    Contains basic information about the photo of a chat

    :param small: A small (160x160) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed
    :type small: :class:`File`
    :param big: A big (640x640) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed
    :type big: :class:`File`
    :param minithumbnail: Chat photo minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param has_animation: True, if the photo has animated variant
    :type has_animation: :class:`Bool`
    :param is_personal: True, if the photo is visible only for the current user
    :type is_personal: :class:`Bool`
    """

    ID: typing.Literal["chatPhotoInfo"] = "chatPhotoInfo"
    small: File
    big: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    has_animation: Bool = False
    is_personal: Bool = False


class ChatPhotoSticker(BaseObject):
    """
    Information about the sticker, which was used to create the chat photo. The sticker is shown at the center of the photo and occupies at most 67% of it

    :param type_: Type of the sticker
    :type type_: :class:`ChatPhotoStickerType`
    :param background_fill: The fill to be used as background for the sticker; rotation angle in backgroundFillGradient isn't supported
    :type background_fill: :class:`BackgroundFill`
    """

    ID: typing.Literal["chatPhotoSticker"] = "chatPhotoSticker"
    type_: ChatPhotoStickerType = Field(..., alias="type")
    background_fill: BackgroundFill


class ChatPhotoStickerTypeCustomEmoji(BaseObject):
    """
    Information about the custom emoji, which was used to create the chat photo

    :param custom_emoji_id: Identifier of the custom emoji
    :type custom_emoji_id: :class:`Int64`
    """

    ID: typing.Literal["chatPhotoStickerTypeCustomEmoji"] = "chatPhotoStickerTypeCustomEmoji"
    custom_emoji_id: Int64


class ChatPhotoStickerTypeRegularOrMask(BaseObject):
    """
    Information about the sticker, which was used to create the chat photo

    :param sticker_set_id: Sticker set identifier
    :type sticker_set_id: :class:`Int64`
    :param sticker_id: Identifier of the sticker in the set
    :type sticker_id: :class:`Int64`
    """

    ID: typing.Literal["chatPhotoStickerTypeRegularOrMask"] = "chatPhotoStickerTypeRegularOrMask"
    sticker_set_id: Int64
    sticker_id: Int64


ChatPhotoStickerType = typing.Union[
    ChatPhotoStickerTypeCustomEmoji,
    ChatPhotoStickerTypeRegularOrMask,
]


class ChatPhotos(BaseObject):
    """
    Contains a list of chat or user profile photos

    :param total_count: Total number of photos
    :type total_count: :class:`Int32`
    :param photos: List of photos
    :type photos: :class:`Vector[ChatPhoto]`
    """

    ID: typing.Literal["chatPhotos"] = "chatPhotos"
    total_count: Int32
    photos: Vector[ChatPhoto]


class ChatPosition(BaseObject):
    """
    Describes a position of a chat in a chat list

    :param list: The chat list
    :type list: :class:`ChatList`
    :param order: A parameter used to determine order of the chat in the chat list. Chats must be sorted by the pair (order, chat.id) in descending order
    :type order: :class:`Int64`
    :param source: Source of the chat in the chat list; may be null, defaults to None
    :type source: :class:`ChatSource`, optional
    :param is_pinned: True, if the chat is pinned in the chat list
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["chatPosition"] = "chatPosition"
    list: ChatList
    order: Int64
    source: typing.Optional[ChatSource] = None
    is_pinned: Bool = False


class ChatSourceMtprotoProxy(BaseObject):
    """
    The chat is sponsored by the user's MTProxy server
    """

    ID: typing.Literal["chatSourceMtprotoProxy"] = "chatSourceMtprotoProxy"


class ChatSourcePublicServiceAnnouncement(BaseObject):
    """
    The chat contains a public service announcement

    :param type_: The type of the announcement
    :type type_: :class:`String`
    :param text: The text of the announcement
    :type text: :class:`String`
    """

    ID: typing.Literal["chatSourcePublicServiceAnnouncement"] = "chatSourcePublicServiceAnnouncement"
    type_: String = Field(..., alias="type")
    text: String


ChatSource = typing.Union[
    ChatSourceMtprotoProxy,
    ChatSourcePublicServiceAnnouncement,
]


class ChatStatisticsChannel(BaseObject):
    """
    A detailed statistics about a channel chat

    :param period: A period to which the statistics applies
    :type period: :class:`DateRange`
    :param member_count: Number of members in the chat
    :type member_count: :class:`StatisticalValue`
    :param mean_view_count: Mean number of times the recently sent messages was viewed
    :type mean_view_count: :class:`StatisticalValue`
    :param mean_share_count: Mean number of times the recently sent messages was shared
    :type mean_share_count: :class:`StatisticalValue`
    :param enabled_notifications_percentage: A percentage of users with enabled notifications for the chat
    :type enabled_notifications_percentage: :class:`Double`
    :param member_count_graph: A graph containing number of members in the chat
    :type member_count_graph: :class:`StatisticalGraph`
    :param join_graph: A graph containing number of members joined and left the chat
    :type join_graph: :class:`StatisticalGraph`
    :param mute_graph: A graph containing number of members muted and unmuted the chat
    :type mute_graph: :class:`StatisticalGraph`
    :param view_count_by_hour_graph: A graph containing number of message views in a given hour in the last two weeks
    :type view_count_by_hour_graph: :class:`StatisticalGraph`
    :param view_count_by_source_graph: A graph containing number of message views per source
    :type view_count_by_source_graph: :class:`StatisticalGraph`
    :param join_by_source_graph: A graph containing number of new member joins per source
    :type join_by_source_graph: :class:`StatisticalGraph`
    :param language_graph: A graph containing number of users viewed chat messages per language
    :type language_graph: :class:`StatisticalGraph`
    :param message_interaction_graph: A graph containing number of chat message views and shares
    :type message_interaction_graph: :class:`StatisticalGraph`
    :param instant_view_interaction_graph: A graph containing number of views of associated with the chat instant views
    :type instant_view_interaction_graph: :class:`StatisticalGraph`
    :param recent_message_interactions: Detailed statistics about number of views and shares of recently sent messages
    :type recent_message_interactions: :class:`Vector[ChatStatisticsMessageInteractionInfo]`
    """

    ID: typing.Literal["chatStatisticsChannel"] = "chatStatisticsChannel"
    period: DateRange
    member_count: StatisticalValue
    mean_view_count: StatisticalValue
    mean_share_count: StatisticalValue
    enabled_notifications_percentage: Double
    member_count_graph: StatisticalGraph
    join_graph: StatisticalGraph
    mute_graph: StatisticalGraph
    view_count_by_hour_graph: StatisticalGraph
    view_count_by_source_graph: StatisticalGraph
    join_by_source_graph: StatisticalGraph
    language_graph: StatisticalGraph
    message_interaction_graph: StatisticalGraph
    instant_view_interaction_graph: StatisticalGraph
    recent_message_interactions: Vector[ChatStatisticsMessageInteractionInfo]


class ChatStatisticsSupergroup(BaseObject):
    """
    A detailed statistics about a supergroup chat

    :param period: A period to which the statistics applies
    :type period: :class:`DateRange`
    :param member_count: Number of members in the chat
    :type member_count: :class:`StatisticalValue`
    :param message_count: Number of messages sent to the chat
    :type message_count: :class:`StatisticalValue`
    :param viewer_count: Number of users who viewed messages in the chat
    :type viewer_count: :class:`StatisticalValue`
    :param sender_count: Number of users who sent messages to the chat
    :type sender_count: :class:`StatisticalValue`
    :param member_count_graph: A graph containing number of members in the chat
    :type member_count_graph: :class:`StatisticalGraph`
    :param join_graph: A graph containing number of members joined and left the chat
    :type join_graph: :class:`StatisticalGraph`
    :param join_by_source_graph: A graph containing number of new member joins per source
    :type join_by_source_graph: :class:`StatisticalGraph`
    :param language_graph: A graph containing distribution of active users per language
    :type language_graph: :class:`StatisticalGraph`
    :param message_content_graph: A graph containing distribution of sent messages by content type
    :type message_content_graph: :class:`StatisticalGraph`
    :param action_graph: A graph containing number of different actions in the chat
    :type action_graph: :class:`StatisticalGraph`
    :param day_graph: A graph containing distribution of message views per hour
    :type day_graph: :class:`StatisticalGraph`
    :param week_graph: A graph containing distribution of message views per day of week
    :type week_graph: :class:`StatisticalGraph`
    :param top_senders: List of users sent most messages in the last week
    :type top_senders: :class:`Vector[ChatStatisticsMessageSenderInfo]`
    :param top_administrators: List of most active administrators in the last week
    :type top_administrators: :class:`Vector[ChatStatisticsAdministratorActionsInfo]`
    :param top_inviters: List of most active inviters of new members in the last week
    :type top_inviters: :class:`Vector[ChatStatisticsInviterInfo]`
    """

    ID: typing.Literal["chatStatisticsSupergroup"] = "chatStatisticsSupergroup"
    period: DateRange
    member_count: StatisticalValue
    message_count: StatisticalValue
    viewer_count: StatisticalValue
    sender_count: StatisticalValue
    member_count_graph: StatisticalGraph
    join_graph: StatisticalGraph
    join_by_source_graph: StatisticalGraph
    language_graph: StatisticalGraph
    message_content_graph: StatisticalGraph
    action_graph: StatisticalGraph
    day_graph: StatisticalGraph
    week_graph: StatisticalGraph
    top_senders: Vector[ChatStatisticsMessageSenderInfo]
    top_administrators: Vector[ChatStatisticsAdministratorActionsInfo]
    top_inviters: Vector[ChatStatisticsInviterInfo]


ChatStatistics = typing.Union[
    ChatStatisticsChannel,
    ChatStatisticsSupergroup,
]


class ChatStatisticsAdministratorActionsInfo(BaseObject):
    """
    Contains statistics about administrator actions done by a user

    :param user_id: Administrator user identifier
    :type user_id: :class:`Int53`
    :param deleted_message_count: Number of messages deleted by the administrator
    :type deleted_message_count: :class:`Int32`
    :param banned_user_count: Number of users banned by the administrator
    :type banned_user_count: :class:`Int32`
    :param restricted_user_count: Number of users restricted by the administrator
    :type restricted_user_count: :class:`Int32`
    """

    ID: typing.Literal["chatStatisticsAdministratorActionsInfo"] = "chatStatisticsAdministratorActionsInfo"
    user_id: Int53
    deleted_message_count: Int32
    banned_user_count: Int32
    restricted_user_count: Int32


class ChatStatisticsInviterInfo(BaseObject):
    """
    Contains statistics about number of new members invited by a user

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param added_member_count: Number of new members invited by the user
    :type added_member_count: :class:`Int32`
    """

    ID: typing.Literal["chatStatisticsInviterInfo"] = "chatStatisticsInviterInfo"
    user_id: Int53
    added_member_count: Int32


class ChatStatisticsMessageInteractionInfo(BaseObject):
    """
    Contains statistics about interactions with a message

    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param view_count: Number of times the message was viewed
    :type view_count: :class:`Int32`
    :param forward_count: Number of times the message was forwarded
    :type forward_count: :class:`Int32`
    """

    ID: typing.Literal["chatStatisticsMessageInteractionInfo"] = "chatStatisticsMessageInteractionInfo"
    message_id: Int53
    view_count: Int32
    forward_count: Int32


class ChatStatisticsMessageSenderInfo(BaseObject):
    """
    Contains statistics about messages sent by a user

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param sent_message_count: Number of sent messages
    :type sent_message_count: :class:`Int32`
    :param average_character_count: Average number of characters in sent messages; 0 if unknown, defaults to None
    :type average_character_count: :class:`Int32`, optional
    """

    ID: typing.Literal["chatStatisticsMessageSenderInfo"] = "chatStatisticsMessageSenderInfo"
    user_id: Int53
    sent_message_count: Int32
    average_character_count: typing.Optional[Int32] = 0


class ChatTheme(BaseObject):
    """
    Describes a chat theme

    :param name: Theme name
    :type name: :class:`String`
    :param light_settings: Theme settings for a light chat theme
    :type light_settings: :class:`ThemeSettings`
    :param dark_settings: Theme settings for a dark chat theme
    :type dark_settings: :class:`ThemeSettings`
    """

    ID: typing.Literal["chatTheme"] = "chatTheme"
    name: String
    light_settings: ThemeSettings
    dark_settings: ThemeSettings


class ChatTypeBasicGroup(BaseObject):
    """
    A basic group (a chat with 0-200 other users)

    :param basic_group_id: Basic group identifier
    :type basic_group_id: :class:`Int53`
    """

    ID: typing.Literal["chatTypeBasicGroup"] = "chatTypeBasicGroup"
    basic_group_id: Int53


class ChatTypePrivate(BaseObject):
    """
    An ordinary chat with a user

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["chatTypePrivate"] = "chatTypePrivate"
    user_id: Int53


class ChatTypeSecret(BaseObject):
    """
    A secret chat with a user

    :param secret_chat_id: Secret chat identifier
    :type secret_chat_id: :class:`Int32`
    :param user_id: User identifier of the secret chat peer
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["chatTypeSecret"] = "chatTypeSecret"
    secret_chat_id: Int32
    user_id: Int53


class ChatTypeSupergroup(BaseObject):
    """
    A supergroup or channel (with unlimited members)

    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`Int53`
    :param is_channel: True, if the supergroup is a channel
    :type is_channel: :class:`Bool`
    """

    ID: typing.Literal["chatTypeSupergroup"] = "chatTypeSupergroup"
    supergroup_id: Int53
    is_channel: Bool = False


ChatType = typing.Union[
    ChatTypeBasicGroup,
    ChatTypePrivate,
    ChatTypeSecret,
    ChatTypeSupergroup,
]


class Chats(BaseObject):
    """
    Represents a list of chats

    :param total_count: Approximate total number of chats found
    :type total_count: :class:`Int32`
    :param chat_ids: List of chat identifiers
    :type chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["chats"] = "chats"
    total_count: Int32
    chat_ids: Vector[Int53]


class ChatsNearby(BaseObject):
    """
    Represents a list of chats located nearby

    :param users_nearby: List of users nearby
    :type users_nearby: :class:`Vector[ChatNearby]`
    :param supergroups_nearby: List of location-based supergroups nearby
    :type supergroups_nearby: :class:`Vector[ChatNearby]`
    """

    ID: typing.Literal["chatsNearby"] = "chatsNearby"
    users_nearby: Vector[ChatNearby]
    supergroups_nearby: Vector[ChatNearby]


class CheckChatUsernameResultOk(BaseObject):
    """
    The username can be set
    """

    ID: typing.Literal["checkChatUsernameResultOk"] = "checkChatUsernameResultOk"


class CheckChatUsernameResultPublicChatsTooMany(BaseObject):
    """
    The user has too many chats with username, one of them must be made private first
    """

    ID: typing.Literal["checkChatUsernameResultPublicChatsTooMany"] = "checkChatUsernameResultPublicChatsTooMany"


class CheckChatUsernameResultPublicGroupsUnavailable(BaseObject):
    """
    The user can't be a member of a public supergroup
    """

    ID: typing.Literal[
        "checkChatUsernameResultPublicGroupsUnavailable"
    ] = "checkChatUsernameResultPublicGroupsUnavailable"


class CheckChatUsernameResultUsernameInvalid(BaseObject):
    """
    The username is invalid
    """

    ID: typing.Literal["checkChatUsernameResultUsernameInvalid"] = "checkChatUsernameResultUsernameInvalid"


class CheckChatUsernameResultUsernameOccupied(BaseObject):
    """
    The username is occupied
    """

    ID: typing.Literal["checkChatUsernameResultUsernameOccupied"] = "checkChatUsernameResultUsernameOccupied"


class CheckChatUsernameResultUsernamePurchasable(BaseObject):
    """
    The username can be purchased at fragment.com
    """

    ID: typing.Literal["checkChatUsernameResultUsernamePurchasable"] = "checkChatUsernameResultUsernamePurchasable"


CheckChatUsernameResult = typing.Union[
    CheckChatUsernameResultOk,
    CheckChatUsernameResultPublicChatsTooMany,
    CheckChatUsernameResultPublicGroupsUnavailable,
    CheckChatUsernameResultUsernameInvalid,
    CheckChatUsernameResultUsernameOccupied,
    CheckChatUsernameResultUsernamePurchasable,
]


class CheckStickerSetNameResultNameInvalid(BaseObject):
    """
    The name is invalid
    """

    ID: typing.Literal["checkStickerSetNameResultNameInvalid"] = "checkStickerSetNameResultNameInvalid"


class CheckStickerSetNameResultNameOccupied(BaseObject):
    """
    The name is occupied
    """

    ID: typing.Literal["checkStickerSetNameResultNameOccupied"] = "checkStickerSetNameResultNameOccupied"


class CheckStickerSetNameResultOk(BaseObject):
    """
    The name can be set
    """

    ID: typing.Literal["checkStickerSetNameResultOk"] = "checkStickerSetNameResultOk"


CheckStickerSetNameResult = typing.Union[
    CheckStickerSetNameResultNameInvalid,
    CheckStickerSetNameResultNameOccupied,
    CheckStickerSetNameResultOk,
]


class ClosedVectorPath(BaseObject):
    """
    Represents a closed vector path. The path begins at the end point of the last command

    :param commands: List of vector path commands
    :type commands: :class:`Vector[VectorPathCommand]`
    """

    ID: typing.Literal["closedVectorPath"] = "closedVectorPath"
    commands: Vector[VectorPathCommand]


class ConnectedWebsite(BaseObject):
    """
    Contains information about one website the current user is logged in with Telegram

    :param id: Website identifier
    :type id: :class:`Int64`
    :param domain_name: The domain name of the website
    :type domain_name: :class:`String`
    :param bot_user_id: User identifier of a bot linked with the website
    :type bot_user_id: :class:`Int53`
    :param browser: The version of a browser used to log in
    :type browser: :class:`String`
    :param platform: Operating system the browser is running on
    :type platform: :class:`String`
    :param log_in_date: Point in time (Unix timestamp) when the user was logged in
    :type log_in_date: :class:`Int32`
    :param last_active_date: Point in time (Unix timestamp) when obtained authorization was last used
    :type last_active_date: :class:`Int32`
    :param ip_address: IP address from which the user was logged in, in human-readable format
    :type ip_address: :class:`String`
    :param location: Human-readable description of a country and a region from which the user was logged in, based on the IP address
    :type location: :class:`String`
    """

    ID: typing.Literal["connectedWebsite"] = "connectedWebsite"
    id: Int64
    domain_name: String
    bot_user_id: Int53
    browser: String
    platform: String
    log_in_date: Int32
    last_active_date: Int32
    ip_address: String
    location: String


class ConnectedWebsites(BaseObject):
    """
    Contains a list of websites the current user is logged in with Telegram

    :param websites: List of connected websites
    :type websites: :class:`Vector[ConnectedWebsite]`
    """

    ID: typing.Literal["connectedWebsites"] = "connectedWebsites"
    websites: Vector[ConnectedWebsite]


class ConnectionStateConnecting(BaseObject):
    """
    Currently establishing a connection to the Telegram servers
    """

    ID: typing.Literal["connectionStateConnecting"] = "connectionStateConnecting"


class ConnectionStateConnectingToProxy(BaseObject):
    """
    Currently establishing a connection with a proxy server
    """

    ID: typing.Literal["connectionStateConnectingToProxy"] = "connectionStateConnectingToProxy"


class ConnectionStateReady(BaseObject):
    """
    There is a working connection to the Telegram servers
    """

    ID: typing.Literal["connectionStateReady"] = "connectionStateReady"


class ConnectionStateUpdating(BaseObject):
    """
    Downloading data received while the application was offline
    """

    ID: typing.Literal["connectionStateUpdating"] = "connectionStateUpdating"


class ConnectionStateWaitingForNetwork(BaseObject):
    """
    Currently waiting for the network to become available. Use setNetworkType to change the available network type
    """

    ID: typing.Literal["connectionStateWaitingForNetwork"] = "connectionStateWaitingForNetwork"


ConnectionState = typing.Union[
    ConnectionStateConnecting,
    ConnectionStateConnectingToProxy,
    ConnectionStateReady,
    ConnectionStateUpdating,
    ConnectionStateWaitingForNetwork,
]


class Contact(BaseObject):
    """
    Describes a user contact

    :param phone_number: Phone number of the user
    :type phone_number: :class:`String`
    :param first_name: First name of the user; 1-255 characters in length
    :type first_name: :class:`String`
    :param last_name: Last name of the user
    :type last_name: :class:`String`
    :param vcard: Additional data about the user in a form of vCard; 0-2048 bytes in length
    :type vcard: :class:`String`
    :param user_id: Identifier of the user, if known; 0 otherwise
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["contact"] = "contact"
    phone_number: String
    first_name: String = Field(..., min_length=1, max_length=255)
    last_name: String
    vcard: String
    user_id: Int53


class Count(BaseObject):
    """
    Contains a counter

    :param count: Count
    :type count: :class:`Int32`
    """

    ID: typing.Literal["count"] = "count"
    count: Int32


class Countries(BaseObject):
    """
    Contains information about countries

    :param countries: The list of countries
    :type countries: :class:`Vector[CountryInfo]`
    """

    ID: typing.Literal["countries"] = "countries"
    countries: Vector[CountryInfo]


class CountryInfo(BaseObject):
    """
    Contains information about a country

    :param country_code: A two-letter ISO 3166-1 alpha-2 country code
    :type country_code: :class:`String`
    :param name: Native name of the country
    :type name: :class:`String`
    :param english_name: English name of the country
    :type english_name: :class:`String`
    :param calling_codes: List of country calling codes
    :type calling_codes: :class:`Vector[String]`
    :param is_hidden: True, if the country must be hidden from the list of all countries
    :type is_hidden: :class:`Bool`
    """

    ID: typing.Literal["countryInfo"] = "countryInfo"
    country_code: String
    name: String
    english_name: String
    calling_codes: Vector[String]
    is_hidden: Bool = False


class CustomRequestResult(BaseObject):
    """
    Contains the result of a custom request

    :param result: A JSON-serialized result
    :type result: :class:`String`
    """

    ID: typing.Literal["customRequestResult"] = "customRequestResult"
    result: String


class DatabaseStatistics(BaseObject):
    """
    Contains database statistics

    :param statistics: Database statistics in an unspecified human-readable format
    :type statistics: :class:`String`
    """

    ID: typing.Literal["databaseStatistics"] = "databaseStatistics"
    statistics: String


class Date(BaseObject):
    """
    Represents a date according to the Gregorian calendar

    :param day: Day of the month; 1-31
    :type day: :class:`Int32`
    :param month: Month; 1-12
    :type month: :class:`Int32`
    :param year: Year; 1-9999
    :type year: :class:`Int32`
    """

    ID: typing.Literal["date"] = "date"
    day: Int32
    month: Int32
    year: Int32


class DateRange(BaseObject):
    """
    Represents a date range

    :param start_date: Point in time (Unix timestamp) at which the date range begins
    :type start_date: :class:`Int32`
    :param end_date: Point in time (Unix timestamp) at which the date range ends
    :type end_date: :class:`Int32`
    """

    ID: typing.Literal["dateRange"] = "dateRange"
    start_date: Int32
    end_date: Int32


class DatedFile(BaseObject):
    """
    File with the date it was uploaded

    :param file: The file
    :type file: :class:`File`
    :param date: Point in time (Unix timestamp) when the file was uploaded
    :type date: :class:`Int32`
    """

    ID: typing.Literal["datedFile"] = "datedFile"
    file: File
    date: Int32


class DeepLinkInfo(BaseObject):
    """
    Contains information about a tg: deep link

    :param text: Text to be shown to the user
    :type text: :class:`FormattedText`
    :param need_update_application: True, if the user must be asked to update the application
    :type need_update_application: :class:`Bool`
    """

    ID: typing.Literal["deepLinkInfo"] = "deepLinkInfo"
    text: FormattedText
    need_update_application: Bool = False


class DeviceTokenApplePush(BaseObject):
    """
    A token for Apple Push Notification service

    :param device_token: Device token; may be empty to deregister a device
    :type device_token: :class:`String`
    :param is_app_sandbox: True, if App Sandbox is enabled
    :type is_app_sandbox: :class:`Bool`
    """

    ID: typing.Literal["deviceTokenApplePush"] = "deviceTokenApplePush"
    device_token: String = ""
    is_app_sandbox: Bool = False


class DeviceTokenApplePushVoIP(BaseObject):
    """
    A token for Apple Push Notification service VoIP notifications

    :param device_token: Device token; may be empty to deregister a device
    :type device_token: :class:`String`
    :param is_app_sandbox: True, if App Sandbox is enabled
    :type is_app_sandbox: :class:`Bool`
    :param encrypt: True, if push notifications must be additionally encrypted
    :type encrypt: :class:`Bool`
    """

    ID: typing.Literal["deviceTokenApplePushVoIP"] = "deviceTokenApplePushVoIP"
    device_token: String = ""
    is_app_sandbox: Bool = False
    encrypt: Bool = False


class DeviceTokenBlackBerryPush(BaseObject):
    """
    A token for BlackBerry Push Service

    :param token: Token; may be empty to deregister a device
    :type token: :class:`String`
    """

    ID: typing.Literal["deviceTokenBlackBerryPush"] = "deviceTokenBlackBerryPush"
    token: String = ""


class DeviceTokenFirebaseCloudMessaging(BaseObject):
    """
    A token for Firebase Cloud Messaging

    :param token: Device registration token; may be empty to deregister a device
    :type token: :class:`String`
    :param encrypt: True, if push notifications must be additionally encrypted
    :type encrypt: :class:`Bool`
    """

    ID: typing.Literal["deviceTokenFirebaseCloudMessaging"] = "deviceTokenFirebaseCloudMessaging"
    token: String = ""
    encrypt: Bool = False


class DeviceTokenHuaweiPush(BaseObject):
    """
    A token for HUAWEI Push Service

    :param token: Device registration token; may be empty to deregister a device
    :type token: :class:`String`
    :param encrypt: True, if push notifications must be additionally encrypted
    :type encrypt: :class:`Bool`
    """

    ID: typing.Literal["deviceTokenHuaweiPush"] = "deviceTokenHuaweiPush"
    token: String = ""
    encrypt: Bool = False


class DeviceTokenMicrosoftPush(BaseObject):
    """
    A token for Microsoft Push Notification Service

    :param channel_uri: Push notification channel URI; may be empty to deregister a device
    :type channel_uri: :class:`String`
    """

    ID: typing.Literal["deviceTokenMicrosoftPush"] = "deviceTokenMicrosoftPush"
    channel_uri: String = ""


class DeviceTokenMicrosoftPushVoIP(BaseObject):
    """
    A token for Microsoft Push Notification Service VoIP channel

    :param channel_uri: Push notification channel URI; may be empty to deregister a device
    :type channel_uri: :class:`String`
    """

    ID: typing.Literal["deviceTokenMicrosoftPushVoIP"] = "deviceTokenMicrosoftPushVoIP"
    channel_uri: String = ""


class DeviceTokenSimplePush(BaseObject):
    """
    A token for Simple Push API for Firefox OS

    :param endpoint: Absolute URL exposed by the push service where the application server can send push messages; may be empty to deregister a device
    :type endpoint: :class:`String`
    """

    ID: typing.Literal["deviceTokenSimplePush"] = "deviceTokenSimplePush"
    endpoint: String = ""


class DeviceTokenTizenPush(BaseObject):
    """
    A token for Tizen Push Service

    :param reg_id: Push service registration identifier; may be empty to deregister a device
    :type reg_id: :class:`String`
    """

    ID: typing.Literal["deviceTokenTizenPush"] = "deviceTokenTizenPush"
    reg_id: String = ""


class DeviceTokenUbuntuPush(BaseObject):
    """
    A token for Ubuntu Push Client service

    :param token: Token; may be empty to deregister a device
    :type token: :class:`String`
    """

    ID: typing.Literal["deviceTokenUbuntuPush"] = "deviceTokenUbuntuPush"
    token: String = ""


class DeviceTokenWebPush(BaseObject):
    """
    A token for web Push API

    :param p256dh_base64url: Base64url-encoded P-256 elliptic curve Diffie-Hellman public key
    :type p256dh_base64url: :class:`String`
    :param auth_base64url: Base64url-encoded authentication secret
    :type auth_base64url: :class:`String`
    :param endpoint: Absolute URL exposed by the push service where the application server can send push messages; may be empty to deregister a device
    :type endpoint: :class:`String`
    """

    ID: typing.Literal["deviceTokenWebPush"] = "deviceTokenWebPush"
    p256dh_base64url: String
    auth_base64url: String
    endpoint: String = ""


class DeviceTokenWindowsPush(BaseObject):
    """
    A token for Windows Push Notification Services

    :param access_token: The access token that will be used to send notifications; may be empty to deregister a device
    :type access_token: :class:`String`
    """

    ID: typing.Literal["deviceTokenWindowsPush"] = "deviceTokenWindowsPush"
    access_token: String = ""


DeviceToken = typing.Union[
    DeviceTokenApplePush,
    DeviceTokenApplePushVoIP,
    DeviceTokenBlackBerryPush,
    DeviceTokenFirebaseCloudMessaging,
    DeviceTokenHuaweiPush,
    DeviceTokenMicrosoftPush,
    DeviceTokenMicrosoftPushVoIP,
    DeviceTokenSimplePush,
    DeviceTokenTizenPush,
    DeviceTokenUbuntuPush,
    DeviceTokenWebPush,
    DeviceTokenWindowsPush,
]


class DiceStickersRegular(BaseObject):
    """
    A regular animated sticker

    :param sticker: The animated sticker with the dice animation
    :type sticker: :class:`Sticker`
    """

    ID: typing.Literal["diceStickersRegular"] = "diceStickersRegular"
    sticker: Sticker


class DiceStickersSlotMachine(BaseObject):
    """
    Animated stickers to be combined into a slot machine

    :param background: The animated sticker with the slot machine background. The background animation must start playing after all reel animations finish
    :type background: :class:`Sticker`
    :param lever: The animated sticker with the lever animation. The lever animation must play once in the initial dice state
    :type lever: :class:`Sticker`
    :param left_reel: The animated sticker with the left reel
    :type left_reel: :class:`Sticker`
    :param center_reel: The animated sticker with the center reel
    :type center_reel: :class:`Sticker`
    :param right_reel: The animated sticker with the right reel
    :type right_reel: :class:`Sticker`
    """

    ID: typing.Literal["diceStickersSlotMachine"] = "diceStickersSlotMachine"
    background: Sticker
    lever: Sticker
    left_reel: Sticker
    center_reel: Sticker
    right_reel: Sticker


DiceStickers = typing.Union[
    DiceStickersRegular,
    DiceStickersSlotMachine,
]


class Document(BaseObject):
    """
    Describes a document of any type

    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`String`
    :param mime_type: MIME type of the file; as defined by the sender
    :type mime_type: :class:`String`
    :param document: File containing the document
    :type document: :class:`File`
    :param minithumbnail: Document minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param thumbnail: Document thumbnail in JPEG or PNG format (PNG will be used only for background patterns); as defined by the sender; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    """

    ID: typing.Literal["document"] = "document"
    file_name: String
    mime_type: String
    document: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None


class DownloadedFileCounts(BaseObject):
    """
    Contains number of being downloaded and recently downloaded files found

    :param active_count: Number of active file downloads found, including paused
    :type active_count: :class:`Int32`
    :param paused_count: Number of paused file downloads found
    :type paused_count: :class:`Int32`
    :param completed_count: Number of completed file downloads found
    :type completed_count: :class:`Int32`
    """

    ID: typing.Literal["downloadedFileCounts"] = "downloadedFileCounts"
    active_count: Int32
    paused_count: Int32
    completed_count: Int32


class DraftMessage(BaseObject):
    """
    Contains information about a message draft

    :param date: Point in time (Unix timestamp) when the draft was created
    :type date: :class:`Int32`
    :param input_message_text: Content of the message draft; must be of the type inputMessageText
    :type input_message_text: :class:`InputMessageContent`
    :param reply_to_message_id: Identifier of the replied message; 0 if none, defaults to None
    :type reply_to_message_id: :class:`Int53`, optional
    """

    ID: typing.Literal["draftMessage"] = "draftMessage"
    date: Int32
    input_message_text: InputMessageContent
    reply_to_message_id: typing.Optional[Int53] = 0


class EmailAddressAuthenticationAppleId(BaseObject):
    """
    An authentication token received through Apple ID

    :param token: The token
    :type token: :class:`String`
    """

    ID: typing.Literal["emailAddressAuthenticationAppleId"] = "emailAddressAuthenticationAppleId"
    token: String


class EmailAddressAuthenticationCode(BaseObject):
    """
    An authentication code delivered to a user's email address

    :param code: The code
    :type code: :class:`String`
    """

    ID: typing.Literal["emailAddressAuthenticationCode"] = "emailAddressAuthenticationCode"
    code: String


class EmailAddressAuthenticationGoogleId(BaseObject):
    """
    An authentication token received through Google ID

    :param token: The token
    :type token: :class:`String`
    """

    ID: typing.Literal["emailAddressAuthenticationGoogleId"] = "emailAddressAuthenticationGoogleId"
    token: String


EmailAddressAuthentication = typing.Union[
    EmailAddressAuthenticationAppleId,
    EmailAddressAuthenticationCode,
    EmailAddressAuthenticationGoogleId,
]


class EmailAddressAuthenticationCodeInfo(BaseObject):
    """
    Information about the email address authentication code that was sent

    :param email_address_pattern: Pattern of the email address to which an authentication code was sent
    :type email_address_pattern: :class:`String`
    :param length: Length of the code; 0 if unknown, defaults to None
    :type length: :class:`Int32`, optional
    """

    ID: typing.Literal["emailAddressAuthenticationCodeInfo"] = "emailAddressAuthenticationCodeInfo"
    email_address_pattern: String
    length: typing.Optional[Int32] = 0


class EmailAddressResetStateAvailable(BaseObject):
    """
    Email address can be reset after the given period. Call resetAuthenticationEmailAddress to reset it and allow the user to authorize with a code sent to the user's phone number

    :param wait_period: Time required to wait before the email address can be reset; 0 if the user is subscribed to Telegram Premium
    :type wait_period: :class:`Int32`
    """

    ID: typing.Literal["emailAddressResetStateAvailable"] = "emailAddressResetStateAvailable"
    wait_period: Int32


class EmailAddressResetStatePending(BaseObject):
    """
    Email address reset has already been requested. Call resetAuthenticationEmailAddress to check whether immediate reset is possible

    :param reset_in: Left time before the email address will be reset, in seconds. updateAuthorizationState is not sent when this field changes
    :type reset_in: :class:`Int32`
    """

    ID: typing.Literal["emailAddressResetStatePending"] = "emailAddressResetStatePending"
    reset_in: Int32


EmailAddressResetState = typing.Union[
    EmailAddressResetStateAvailable,
    EmailAddressResetStatePending,
]


class EmojiCategories(BaseObject):
    """
    Represents a list of emoji categories

    :param categories: List of categories
    :type categories: :class:`Vector[EmojiCategory]`
    """

    ID: typing.Literal["emojiCategories"] = "emojiCategories"
    categories: Vector[EmojiCategory]


class EmojiCategory(BaseObject):
    """
    Contains a list of similar emoji to search for in getStickers and searchStickers

    :param name: Name of the category
    :type name: :class:`String`
    :param icon: Custom emoji sticker, which represents icon of the category
    :type icon: :class:`Sticker`
    :param emojis: List of emojis in the category
    :type emojis: :class:`Vector[String]`
    """

    ID: typing.Literal["emojiCategory"] = "emojiCategory"
    name: String
    icon: Sticker
    emojis: Vector[String]


class EmojiCategoryTypeChatPhoto(BaseObject):
    """
    The category must be used for chat photo emoji selection
    """

    ID: typing.Literal["emojiCategoryTypeChatPhoto"] = "emojiCategoryTypeChatPhoto"


class EmojiCategoryTypeDefault(BaseObject):
    """
    The category must be used by default
    """

    ID: typing.Literal["emojiCategoryTypeDefault"] = "emojiCategoryTypeDefault"


class EmojiCategoryTypeEmojiStatus(BaseObject):
    """
    The category must be used for emoji status selection
    """

    ID: typing.Literal["emojiCategoryTypeEmojiStatus"] = "emojiCategoryTypeEmojiStatus"


EmojiCategoryType = typing.Union[
    EmojiCategoryTypeChatPhoto,
    EmojiCategoryTypeDefault,
    EmojiCategoryTypeEmojiStatus,
]


class EmojiReaction(BaseObject):
    """
    Contains information about a emoji reaction

    :param emoji: Text representation of the reaction
    :type emoji: :class:`String`
    :param title: Reaction title
    :type title: :class:`String`
    :param static_icon: Static icon for the reaction
    :type static_icon: :class:`Sticker`
    :param appear_animation: Appear animation for the reaction
    :type appear_animation: :class:`Sticker`
    :param select_animation: Select animation for the reaction
    :type select_animation: :class:`Sticker`
    :param activate_animation: Activate animation for the reaction
    :type activate_animation: :class:`Sticker`
    :param effect_animation: Effect animation for the reaction
    :type effect_animation: :class:`Sticker`
    :param around_animation: Around animation for the reaction; may be null, defaults to None
    :type around_animation: :class:`Sticker`, optional
    :param center_animation: Center animation for the reaction; may be null, defaults to None
    :type center_animation: :class:`Sticker`, optional
    :param is_active: True, if the reaction can be added to new messages and enabled in chats
    :type is_active: :class:`Bool`
    """

    ID: typing.Literal["emojiReaction"] = "emojiReaction"
    emoji: String
    title: String
    static_icon: Sticker
    appear_animation: Sticker
    select_animation: Sticker
    activate_animation: Sticker
    effect_animation: Sticker
    around_animation: typing.Optional[Sticker] = None
    center_animation: typing.Optional[Sticker] = None
    is_active: Bool = False


class EmojiStatus(BaseObject):
    """
    Describes a custom emoji to be shown instead of the Telegram Premium badge

    :param custom_emoji_id: Identifier of the custom emoji in stickerFormatTgs format
    :type custom_emoji_id: :class:`Int64`
    :param expiration_date: Point in time (Unix timestamp) when the status will expire; 0 if never
    :type expiration_date: :class:`Int32`
    """

    ID: typing.Literal["emojiStatus"] = "emojiStatus"
    custom_emoji_id: Int64
    expiration_date: Int32


class EmojiStatuses(BaseObject):
    """
    Contains a list of custom emoji identifiers, which can be set as emoji statuses

    :param custom_emoji_ids: The list of custom emoji identifiers
    :type custom_emoji_ids: :class:`Vector[Int64]`
    """

    ID: typing.Literal["emojiStatuses"] = "emojiStatuses"
    custom_emoji_ids: Vector[Int64]


class Emojis(BaseObject):
    """
    Represents a list of emoji

    :param emojis: List of emojis
    :type emojis: :class:`Vector[String]`
    """

    ID: typing.Literal["emojis"] = "emojis"
    emojis: Vector[String]


class EncryptedCredentials(BaseObject):
    """
    Contains encrypted Telegram Passport data credentials

    :param data: The encrypted credentials
    :type data: :class:`Bytes`
    :param hash_: The decrypted data hash
    :type hash_: :class:`Bytes`
    :param secret: Secret for data decryption, encrypted with the service's public key
    :type secret: :class:`Bytes`
    """

    ID: typing.Literal["encryptedCredentials"] = "encryptedCredentials"
    data: Bytes
    hash_: Bytes = Field(..., alias="hash")
    secret: Bytes


class EncryptedPassportElement(BaseObject):
    """
    Contains information about an encrypted Telegram Passport element; for bots only

    :param type_: Type of Telegram Passport element
    :type type_: :class:`PassportElementType`
    :param data: Encrypted JSON-encoded data about the user
    :type data: :class:`Bytes`
    :param front_side: The front side of an identity document
    :type front_side: :class:`DatedFile`
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`Vector[DatedFile]`
    :param files: List of attached files
    :type files: :class:`Vector[DatedFile]`
    :param value: Unencrypted data, phone number or email address
    :type value: :class:`String`
    :param hash_: Hash of the entire element
    :type hash_: :class:`String`
    :param reverse_side: The reverse side of an identity document; may be null, defaults to None
    :type reverse_side: :class:`DatedFile`, optional
    :param selfie: Selfie with the document; may be null, defaults to None
    :type selfie: :class:`DatedFile`, optional
    """

    ID: typing.Literal["encryptedPassportElement"] = "encryptedPassportElement"
    type_: PassportElementType = Field(..., alias="type")
    data: Bytes
    front_side: DatedFile
    translation: Vector[DatedFile]
    files: Vector[DatedFile]
    value: String
    hash_: String = Field(..., alias="hash")
    reverse_side: typing.Optional[DatedFile] = None
    selfie: typing.Optional[DatedFile] = None


class Error(BaseObject):
    """
    An object of this type can be returned on every function call, in case of an error

    :param code: Error code; subject to future changes. If the error code is 406, the error message must not be processed in any way and must not be displayed to the user
    :type code: :class:`Int32`
    :param message: Error message; subject to future changes
    :type message: :class:`String`
    """

    ID: typing.Literal["error"] = "error"
    code: Int32
    message: String


class File(BaseObject):
    """
    Represents a file

    :param id: Unique file identifier
    :type id: :class:`Int32`
    :param expected_size: Approximate file size in bytes in case the exact file size is unknown. Can be used to show download/upload progress
    :type expected_size: :class:`Int53`
    :param local: Information about the local copy of the file
    :type local: :class:`LocalFile`
    :param remote: Information about the remote copy of the file
    :type remote: :class:`RemoteFile`
    :param size: File size, in bytes; 0 if unknown, defaults to None
    :type size: :class:`Int53`, optional
    """

    ID: typing.Literal["file"] = "file"
    id: Int32
    expected_size: Int53
    local: LocalFile
    remote: RemoteFile
    size: typing.Optional[Int53] = 0


class FileDownload(BaseObject):
    """
    Describes a file added to file download list

    :param file_id: File identifier
    :type file_id: :class:`Int32`
    :param message: The message with the file
    :type message: :class:`Message`
    :param add_date: Point in time (Unix timestamp) when the file was added to the download list
    :type add_date: :class:`Int32`
    :param complete_date: Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed
    :type complete_date: :class:`Int32`
    :param is_paused: True, if downloading of the file is paused
    :type is_paused: :class:`Bool`
    """

    ID: typing.Literal["fileDownload"] = "fileDownload"
    file_id: Int32
    message: Message
    add_date: Int32
    complete_date: Int32
    is_paused: Bool = False


class FileDownloadedPrefixSize(BaseObject):
    """
    Contains size of downloaded prefix of a file

    :param size: The prefix size, in bytes
    :type size: :class:`Int53`
    """

    ID: typing.Literal["fileDownloadedPrefixSize"] = "fileDownloadedPrefixSize"
    size: Int53


class FilePart(BaseObject):
    """
    Contains a part of a file

    :param data: File bytes
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["filePart"] = "filePart"
    data: Bytes


class FileTypeAnimation(BaseObject):
    """
    The file is an animation
    """

    ID: typing.Literal["fileTypeAnimation"] = "fileTypeAnimation"


class FileTypeAudio(BaseObject):
    """
    The file is an audio file
    """

    ID: typing.Literal["fileTypeAudio"] = "fileTypeAudio"


class FileTypeDocument(BaseObject):
    """
    The file is a document
    """

    ID: typing.Literal["fileTypeDocument"] = "fileTypeDocument"


class FileTypeNone(BaseObject):
    """
    The data is not a file
    """

    ID: typing.Literal["fileTypeNone"] = "fileTypeNone"


class FileTypeNotificationSound(BaseObject):
    """
    The file is a notification sound
    """

    ID: typing.Literal["fileTypeNotificationSound"] = "fileTypeNotificationSound"


class FileTypePhoto(BaseObject):
    """
    The file is a photo
    """

    ID: typing.Literal["fileTypePhoto"] = "fileTypePhoto"


class FileTypePhotoStory(BaseObject):
    """
    The file is a photo published as a story
    """

    ID: typing.Literal["fileTypePhotoStory"] = "fileTypePhotoStory"


class FileTypeProfilePhoto(BaseObject):
    """
    The file is a profile photo
    """

    ID: typing.Literal["fileTypeProfilePhoto"] = "fileTypeProfilePhoto"


class FileTypeSecret(BaseObject):
    """
    The file was sent to a secret chat (the file type is not known to the server)
    """

    ID: typing.Literal["fileTypeSecret"] = "fileTypeSecret"


class FileTypeSecretThumbnail(BaseObject):
    """
    The file is a thumbnail of a file from a secret chat
    """

    ID: typing.Literal["fileTypeSecretThumbnail"] = "fileTypeSecretThumbnail"


class FileTypeSecure(BaseObject):
    """
    The file is a file from Secure storage used for storing Telegram Passport files
    """

    ID: typing.Literal["fileTypeSecure"] = "fileTypeSecure"


class FileTypeSticker(BaseObject):
    """
    The file is a sticker
    """

    ID: typing.Literal["fileTypeSticker"] = "fileTypeSticker"


class FileTypeThumbnail(BaseObject):
    """
    The file is a thumbnail of another file
    """

    ID: typing.Literal["fileTypeThumbnail"] = "fileTypeThumbnail"


class FileTypeUnknown(BaseObject):
    """
    The file type is not yet known
    """

    ID: typing.Literal["fileTypeUnknown"] = "fileTypeUnknown"


class FileTypeVideo(BaseObject):
    """
    The file is a video
    """

    ID: typing.Literal["fileTypeVideo"] = "fileTypeVideo"


class FileTypeVideoNote(BaseObject):
    """
    The file is a video note
    """

    ID: typing.Literal["fileTypeVideoNote"] = "fileTypeVideoNote"


class FileTypeVideoStory(BaseObject):
    """
    The file is a video published as a story
    """

    ID: typing.Literal["fileTypeVideoStory"] = "fileTypeVideoStory"


class FileTypeVoiceNote(BaseObject):
    """
    The file is a voice note
    """

    ID: typing.Literal["fileTypeVoiceNote"] = "fileTypeVoiceNote"


class FileTypeWallpaper(BaseObject):
    """
    The file is a wallpaper or a background pattern
    """

    ID: typing.Literal["fileTypeWallpaper"] = "fileTypeWallpaper"


FileType = typing.Union[
    FileTypeAnimation,
    FileTypeAudio,
    FileTypeDocument,
    FileTypeNone,
    FileTypeNotificationSound,
    FileTypePhoto,
    FileTypePhotoStory,
    FileTypeProfilePhoto,
    FileTypeSecret,
    FileTypeSecretThumbnail,
    FileTypeSecure,
    FileTypeSticker,
    FileTypeThumbnail,
    FileTypeUnknown,
    FileTypeVideo,
    FileTypeVideoNote,
    FileTypeVideoStory,
    FileTypeVoiceNote,
    FileTypeWallpaper,
]


class FirebaseAuthenticationSettingsAndroid(BaseObject):
    """
    Settings for Firebase Authentication in the official Android application
    """

    ID: typing.Literal["firebaseAuthenticationSettingsAndroid"] = "firebaseAuthenticationSettingsAndroid"


class FirebaseAuthenticationSettingsIos(BaseObject):
    """
    Settings for Firebase Authentication in the official iOS application

    :param device_token: Device token from Apple Push Notification service
    :type device_token: :class:`String`
    :param is_app_sandbox: True, if App Sandbox is enabled
    :type is_app_sandbox: :class:`Bool`
    """

    ID: typing.Literal["firebaseAuthenticationSettingsIos"] = "firebaseAuthenticationSettingsIos"
    device_token: String
    is_app_sandbox: Bool = False


FirebaseAuthenticationSettings = typing.Union[
    FirebaseAuthenticationSettingsAndroid,
    FirebaseAuthenticationSettingsIos,
]


class FormattedText(BaseObject):
    """
    A text with some entities

    :param text: The text
    :type text: :class:`String`
    :param entities: Entities contained in the text. Entities can be nested, but must not mutually intersect with each other. Pre, Code and PreCode entities can't contain other entities. Bold, Italic, Underline, Strikethrough, and Spoiler entities can contain and can be part of any other entities. All other entities can't contain each other
    :type entities: :class:`Vector[TextEntity]`
    """

    ID: typing.Literal["formattedText"] = "formattedText"
    text: String
    entities: Vector[TextEntity]


class ForumTopic(BaseObject):
    """
    Describes a forum topic

    :param info: Basic information about the topic
    :type info: :class:`ForumTopicInfo`
    :param unread_count: Number of unread messages in the topic
    :type unread_count: :class:`Int32`
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :type last_read_inbox_message_id: :class:`Int53`
    :param last_read_outbox_message_id: Identifier of the last read outgoing message
    :type last_read_outbox_message_id: :class:`Int53`
    :param unread_mention_count: Number of unread messages with a mention/reply in the topic
    :type unread_mention_count: :class:`Int32`
    :param unread_reaction_count: Number of messages with unread reactions in the topic
    :type unread_reaction_count: :class:`Int32`
    :param notification_settings: Notification settings for the topic
    :type notification_settings: :class:`ChatNotificationSettings`
    :param last_message: Last message in the topic; may be null if unknown, defaults to None
    :type last_message: :class:`Message`, optional
    :param draft_message: A draft of a message in the topic; may be null if none, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    :param is_pinned: True, if the topic is pinned in the topic list
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["forumTopic"] = "forumTopic"
    info: ForumTopicInfo
    unread_count: Int32
    last_read_inbox_message_id: Int53
    last_read_outbox_message_id: Int53
    unread_mention_count: Int32
    unread_reaction_count: Int32
    notification_settings: ChatNotificationSettings
    last_message: typing.Optional[Message] = None
    draft_message: typing.Optional[DraftMessage] = None
    is_pinned: Bool = False


class ForumTopicIcon(BaseObject):
    """
    Describes a forum topic icon

    :param color: Color of the topic icon in RGB format
    :type color: :class:`Int32`
    :param custom_emoji_id: Unique identifier of the custom emoji shown on the topic icon; 0 if none, defaults to None
    :type custom_emoji_id: :class:`Int64`, optional
    """

    ID: typing.Literal["forumTopicIcon"] = "forumTopicIcon"
    color: Int32
    custom_emoji_id: typing.Optional[Int64] = 0


class ForumTopicInfo(BaseObject):
    """
    Contains basic information about a forum topic

    :param message_thread_id: Message thread identifier of the topic
    :type message_thread_id: :class:`Int53`
    :param name: Name of the topic
    :type name: :class:`String`
    :param icon: Icon of the topic
    :type icon: :class:`ForumTopicIcon`
    :param creation_date: Point in time (Unix timestamp) when the topic was created
    :type creation_date: :class:`Int32`
    :param creator_id: Identifier of the creator of the topic
    :type creator_id: :class:`MessageSender`
    :param is_general: True, if the topic is the General topic list
    :type is_general: :class:`Bool`
    :param is_outgoing: True, if the topic was created by the current user
    :type is_outgoing: :class:`Bool`
    :param is_closed: True, if the topic is closed
    :type is_closed: :class:`Bool`
    :param is_hidden: True, if the topic is hidden above the topic list and closed; for General topic only
    :type is_hidden: :class:`Bool`
    """

    ID: typing.Literal["forumTopicInfo"] = "forumTopicInfo"
    message_thread_id: Int53
    name: String
    icon: ForumTopicIcon
    creation_date: Int32
    creator_id: MessageSender
    is_general: Bool = False
    is_outgoing: Bool = False
    is_closed: Bool = False
    is_hidden: Bool = False


class ForumTopics(BaseObject):
    """
    Describes a list of forum topics

    :param total_count: Approximate total number of forum topics found
    :type total_count: :class:`Int32`
    :param topics: List of forum topics
    :type topics: :class:`Vector[ForumTopic]`
    :param next_offset_date: Offset date for the next getForumTopics request
    :type next_offset_date: :class:`Int32`
    :param next_offset_message_id: Offset message identifier for the next getForumTopics request
    :type next_offset_message_id: :class:`Int53`
    :param next_offset_message_thread_id: Offset message thread identifier for the next getForumTopics request
    :type next_offset_message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["forumTopics"] = "forumTopics"
    total_count: Int32
    topics: Vector[ForumTopic]
    next_offset_date: Int32
    next_offset_message_id: Int53
    next_offset_message_thread_id: Int53


class FoundChatMessages(BaseObject):
    """
    Contains a list of messages found by a search in a given chat

    :param total_count: Approximate total number of messages found; -1 if unknown
    :type total_count: :class:`Int32`
    :param messages: List of messages
    :type messages: :class:`Vector[Message]`
    :param next_from_message_id: The offset for the next request. If 0, there are no more results
    :type next_from_message_id: :class:`Int53`
    """

    ID: typing.Literal["foundChatMessages"] = "foundChatMessages"
    total_count: Int32
    messages: Vector[Message]
    next_from_message_id: Int53 = 0


class FoundFileDownloads(BaseObject):
    """
    Contains a list of downloaded files, found by a search

    :param total_counts: Total number of suitable files, ignoring offset
    :type total_counts: :class:`DownloadedFileCounts`
    :param files: The list of files
    :type files: :class:`Vector[FileDownload]`
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`String`
    """

    ID: typing.Literal["foundFileDownloads"] = "foundFileDownloads"
    total_counts: DownloadedFileCounts
    files: Vector[FileDownload]
    next_offset: String


class FoundMessages(BaseObject):
    """
    Contains a list of messages found by a search

    :param total_count: Approximate total number of messages found; -1 if unknown
    :type total_count: :class:`Int32`
    :param messages: List of messages
    :type messages: :class:`Vector[Message]`
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`String`
    """

    ID: typing.Literal["foundMessages"] = "foundMessages"
    total_count: Int32
    messages: Vector[Message]
    next_offset: String


class FoundPositions(BaseObject):
    """
    Contains 0-based positions of matched objects

    :param total_count: Total number of matched objects
    :type total_count: :class:`Int32`
    :param positions: The positions of the matched objects
    :type positions: :class:`Vector[Int32]`
    """

    ID: typing.Literal["foundPositions"] = "foundPositions"
    total_count: Int32
    positions: Vector[Int32]


class FoundWebApp(BaseObject):
    """
    Contains information about a Web App found by its short name

    :param web_app: The Web App
    :type web_app: :class:`WebApp`
    :param supports_settings: True, if the app supports "settings_button_pressed" event
    :type supports_settings: :class:`Bool`
    :param request_write_access: True, if the user must be asked for the permission to the bot to send them messages
    :type request_write_access: :class:`Bool`
    :param skip_confirmation: True, if there is no need to show an ordinary open URL confirmation before opening the Web App. The field must be ignored and confirmation must be shown anyway if the Web App link was hidden
    :type skip_confirmation: :class:`Bool`
    """

    ID: typing.Literal["foundWebApp"] = "foundWebApp"
    web_app: WebApp
    supports_settings: Bool = False
    request_write_access: Bool = False
    skip_confirmation: Bool = False


class Game(BaseObject):
    """
    Describes a game. Use getInternalLink with internalLinkTypeGame to share the game

    :param id: Unique game identifier
    :type id: :class:`Int64`
    :param short_name: Game short name
    :type short_name: :class:`String`
    :param title: Game title
    :type title: :class:`String`
    :param text: Game text, usually containing scoreboards for a game
    :type text: :class:`FormattedText`
    :param description: Game description
    :type description: :class:`String`
    :param photo: Game photo
    :type photo: :class:`Photo`
    :param animation: Game animation; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    """

    ID: typing.Literal["game"] = "game"
    id: Int64
    short_name: String
    title: String
    text: FormattedText
    description: String
    photo: Photo
    animation: typing.Optional[Animation] = None


class GameHighScore(BaseObject):
    """
    Contains one row of the game high score table

    :param position: Position in the high score table
    :type position: :class:`Int32`
    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param score: User score
    :type score: :class:`Int32`
    """

    ID: typing.Literal["gameHighScore"] = "gameHighScore"
    position: Int32
    user_id: Int53
    score: Int32


class GameHighScores(BaseObject):
    """
    Contains a list of game high scores

    :param scores: A list of game high scores
    :type scores: :class:`Vector[GameHighScore]`
    """

    ID: typing.Literal["gameHighScores"] = "gameHighScores"
    scores: Vector[GameHighScore]


class GroupCall(BaseObject):
    """
    Describes a group call

    :param id: Group call identifier
    :type id: :class:`Int32`
    :param title: Group call title
    :type title: :class:`String`
    :param scheduled_start_date: Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 if it is already active or was ended
    :type scheduled_start_date: :class:`Int32`
    :param participant_count: Number of participants in the group call
    :type participant_count: :class:`Int32`
    :param recent_speakers: At most 3 recently speaking users in the group call
    :type recent_speakers: :class:`Vector[GroupCallRecentSpeaker]`
    :param duration: Call duration, in seconds; for ended calls only
    :type duration: :class:`Int32`
    :param enabled_start_notification: True, if the group call is scheduled and the current user will receive a notification when the group call will start
    :type enabled_start_notification: :class:`Bool`
    :param is_active: True, if the call is active
    :type is_active: :class:`Bool`
    :param is_rtmp_stream: True, if the chat is an RTMP stream instead of an ordinary video chat
    :type is_rtmp_stream: :class:`Bool`
    :param is_joined: True, if the call is joined
    :type is_joined: :class:`Bool`
    :param need_rejoin: True, if user was kicked from the call because of network loss and the call needs to be rejoined
    :type need_rejoin: :class:`Bool`
    :param can_be_managed: True, if the current user can manage the group call
    :type can_be_managed: :class:`Bool`
    :param has_hidden_listeners: True, if group call participants, which are muted, aren't returned in participant list
    :type has_hidden_listeners: :class:`Bool`
    :param loaded_all_participants: True, if all group call participants are loaded
    :type loaded_all_participants: :class:`Bool`
    :param is_my_video_enabled: True, if the current user's video is enabled
    :type is_my_video_enabled: :class:`Bool`
    :param is_my_video_paused: True, if the current user's video is paused
    :type is_my_video_paused: :class:`Bool`
    :param can_enable_video: True, if the current user can broadcast video or share screen
    :type can_enable_video: :class:`Bool`
    :param mute_new_participants: True, if only group call administrators can unmute new participants
    :type mute_new_participants: :class:`Bool`
    :param can_toggle_mute_new_participants: True, if the current user can enable or disable mute_new_participants setting
    :type can_toggle_mute_new_participants: :class:`Bool`
    :param is_video_recorded: True, if a video file is being recorded for the call
    :type is_video_recorded: :class:`Bool`
    :param record_duration: Duration of the ongoing group call recording, in seconds; 0 if none. An updateGroupCall update is not triggered when value of this field changes, but the same recording goes on, defaults to None
    :type record_duration: :class:`Int32`, optional
    """

    ID: typing.Literal["groupCall"] = "groupCall"
    id: Int32
    title: String
    scheduled_start_date: Int32
    participant_count: Int32
    recent_speakers: Vector[GroupCallRecentSpeaker]
    duration: Int32
    enabled_start_notification: Bool = False
    is_active: Bool = False
    is_rtmp_stream: Bool = False
    is_joined: Bool = False
    need_rejoin: Bool = False
    can_be_managed: Bool = False
    has_hidden_listeners: Bool = False
    loaded_all_participants: Bool = False
    is_my_video_enabled: Bool = False
    is_my_video_paused: Bool = False
    can_enable_video: Bool = False
    mute_new_participants: Bool = False
    can_toggle_mute_new_participants: Bool = False
    is_video_recorded: Bool = False
    record_duration: typing.Optional[Int32] = 0


class GroupCallId(BaseObject):
    """
    Contains the group call identifier

    :param id: Group call identifier
    :type id: :class:`Int32`
    """

    ID: typing.Literal["groupCallId"] = "groupCallId"
    id: Int32


class GroupCallParticipant(BaseObject):
    """
    Represents a group call participant

    :param participant_id: Identifier of the group call participant
    :type participant_id: :class:`MessageSender`
    :param audio_source_id: User's audio channel synchronization source identifier
    :type audio_source_id: :class:`Int32`
    :param screen_sharing_audio_source_id: User's screen sharing audio channel synchronization source identifier
    :type screen_sharing_audio_source_id: :class:`Int32`
    :param bio: The participant user's bio or the participant chat's description
    :type bio: :class:`String`
    :param volume_level: Participant's volume level; 1-20000 in hundreds of percents
    :type volume_level: :class:`Int32`
    :param order: User's order in the group call participant list. Orders must be compared lexicographically. The bigger is order, the higher is user in the list. If order is empty, the user must be removed from the participant list
    :type order: :class:`String`
    :param video_info: Information about user's video channel; may be null if there is no active video, defaults to None
    :type video_info: :class:`GroupCallParticipantVideoInfo`, optional
    :param screen_sharing_video_info: Information about user's screen sharing video channel; may be null if there is no active screen sharing video, defaults to None
    :type screen_sharing_video_info: :class:`GroupCallParticipantVideoInfo`, optional
    :param is_current_user: True, if the participant is the current user
    :type is_current_user: :class:`Bool`
    :param is_speaking: True, if the participant is speaking as set by setGroupCallParticipantIsSpeaking
    :type is_speaking: :class:`Bool`
    :param is_hand_raised: True, if the participant hand is raised
    :type is_hand_raised: :class:`Bool`
    :param can_be_muted_for_all_users: True, if the current user can mute the participant for all other group call participants
    :type can_be_muted_for_all_users: :class:`Bool`
    :param can_be_unmuted_for_all_users: True, if the current user can allow the participant to unmute themselves or unmute the participant (if the participant is the current user)
    :type can_be_unmuted_for_all_users: :class:`Bool`
    :param can_be_muted_for_current_user: True, if the current user can mute the participant only for self
    :type can_be_muted_for_current_user: :class:`Bool`
    :param can_be_unmuted_for_current_user: True, if the current user can unmute the participant for self
    :type can_be_unmuted_for_current_user: :class:`Bool`
    :param is_muted_for_all_users: True, if the participant is muted for all users
    :type is_muted_for_all_users: :class:`Bool`
    :param is_muted_for_current_user: True, if the participant is muted for the current user
    :type is_muted_for_current_user: :class:`Bool`
    :param can_unmute_self: True, if the participant is muted for all users, but can unmute themselves
    :type can_unmute_self: :class:`Bool`
    """

    ID: typing.Literal["groupCallParticipant"] = "groupCallParticipant"
    participant_id: MessageSender
    audio_source_id: Int32
    screen_sharing_audio_source_id: Int32
    bio: String
    volume_level: Int32
    order: String
    video_info: typing.Optional[GroupCallParticipantVideoInfo] = None
    screen_sharing_video_info: typing.Optional[GroupCallParticipantVideoInfo] = None
    is_current_user: Bool = False
    is_speaking: Bool = False
    is_hand_raised: Bool = False
    can_be_muted_for_all_users: Bool = False
    can_be_unmuted_for_all_users: Bool = False
    can_be_muted_for_current_user: Bool = False
    can_be_unmuted_for_current_user: Bool = False
    is_muted_for_all_users: Bool = False
    is_muted_for_current_user: Bool = False
    can_unmute_self: Bool = False


class GroupCallParticipantVideoInfo(BaseObject):
    """
    Contains information about a group call participant's video channel

    :param source_groups: List of synchronization source groups of the video
    :type source_groups: :class:`Vector[GroupCallVideoSourceGroup]`
    :param endpoint_id: Video channel endpoint identifier
    :type endpoint_id: :class:`String`
    :param is_paused: True, if the video is paused. This flag needs to be ignored, if new video frames are received
    :type is_paused: :class:`Bool`
    """

    ID: typing.Literal["groupCallParticipantVideoInfo"] = "groupCallParticipantVideoInfo"
    source_groups: Vector[GroupCallVideoSourceGroup]
    endpoint_id: String
    is_paused: Bool = False


class GroupCallRecentSpeaker(BaseObject):
    """
    Describes a recently speaking participant in a group call

    :param participant_id: Group call participant identifier
    :type participant_id: :class:`MessageSender`
    :param is_speaking: True, is the user has spoken recently
    :type is_speaking: :class:`Bool`
    """

    ID: typing.Literal["groupCallRecentSpeaker"] = "groupCallRecentSpeaker"
    participant_id: MessageSender
    is_speaking: Bool


class GroupCallStream(BaseObject):
    """
    Describes an available stream in a group call

    :param channel_id: Identifier of an audio/video channel
    :type channel_id: :class:`Int32`
    :param scale: Scale of segment durations in the stream. The duration is 1000/(2**scale) milliseconds
    :type scale: :class:`Int32`
    :param time_offset: Point in time when the stream currently ends; Unix timestamp in milliseconds
    :type time_offset: :class:`Int53`
    """

    ID: typing.Literal["groupCallStream"] = "groupCallStream"
    channel_id: Int32
    scale: Int32
    time_offset: Int53


class GroupCallStreams(BaseObject):
    """
    Represents a list of group call streams

    :param streams: A list of group call streams
    :type streams: :class:`Vector[GroupCallStream]`
    """

    ID: typing.Literal["groupCallStreams"] = "groupCallStreams"
    streams: Vector[GroupCallStream]


class GroupCallVideoQualityFull(BaseObject):
    """
    The best available video quality
    """

    ID: typing.Literal["groupCallVideoQualityFull"] = "groupCallVideoQualityFull"


class GroupCallVideoQualityMedium(BaseObject):
    """
    The medium video quality
    """

    ID: typing.Literal["groupCallVideoQualityMedium"] = "groupCallVideoQualityMedium"


class GroupCallVideoQualityThumbnail(BaseObject):
    """
    The worst available video quality
    """

    ID: typing.Literal["groupCallVideoQualityThumbnail"] = "groupCallVideoQualityThumbnail"


GroupCallVideoQuality = typing.Union[
    GroupCallVideoQualityFull,
    GroupCallVideoQualityMedium,
    GroupCallVideoQualityThumbnail,
]


class GroupCallVideoSourceGroup(BaseObject):
    """
    Describes a group of video synchronization source identifiers

    :param semantics: The semantics of sources, one of "SIM" or "FID"
    :type semantics: :class:`String`
    :param source_ids: The list of synchronization source identifiers
    :type source_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["groupCallVideoSourceGroup"] = "groupCallVideoSourceGroup"
    semantics: String
    source_ids: Vector[Int32]


class Hashtags(BaseObject):
    """
    Contains a list of hashtags

    :param hashtags: A list of hashtags
    :type hashtags: :class:`Vector[String]`
    """

    ID: typing.Literal["hashtags"] = "hashtags"
    hashtags: Vector[String]


class HttpUrl(BaseObject):
    """
    Contains an HTTP URL

    :param url: The URL
    :type url: :class:`String`
    """

    ID: typing.Literal["httpUrl"] = "httpUrl"
    url: String


class IdentityDocument(BaseObject):
    """
    An identity document

    :param number: Document number; 1-24 characters
    :type number: :class:`String`
    :param front_side: Front side of the document
    :type front_side: :class:`DatedFile`
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`Vector[DatedFile]`
    :param expiration_date: Document expiration date; may be null if not applicable, defaults to None
    :type expiration_date: :class:`Date`, optional
    :param reverse_side: Reverse side of the document; only for driver license and identity card; may be null, defaults to None
    :type reverse_side: :class:`DatedFile`, optional
    :param selfie: Selfie with the document; may be null, defaults to None
    :type selfie: :class:`DatedFile`, optional
    """

    ID: typing.Literal["identityDocument"] = "identityDocument"
    number: String = Field(..., min_length=1, max_length=24)
    front_side: DatedFile
    translation: Vector[DatedFile]
    expiration_date: typing.Optional[Date] = None
    reverse_side: typing.Optional[DatedFile] = None
    selfie: typing.Optional[DatedFile] = None


class ImportedContacts(BaseObject):
    """
    Represents the result of an importContacts request

    :param user_ids: User identifiers of the imported contacts in the same order as they were specified in the request; 0 if the contact is not yet a registered user
    :type user_ids: :class:`Vector[Int53]`
    :param importer_count: The number of users that imported the corresponding contact; 0 for already registered users or if unavailable
    :type importer_count: :class:`Vector[Int32]`
    """

    ID: typing.Literal["importedContacts"] = "importedContacts"
    user_ids: Vector[Int53]
    importer_count: Vector[Int32]


class InlineKeyboardButton(BaseObject):
    """
    Represents a single button in an inline keyboard

    :param text: Text of the button
    :type text: :class:`String`
    :param type_: Type of the button
    :type type_: :class:`InlineKeyboardButtonType`
    """

    ID: typing.Literal["inlineKeyboardButton"] = "inlineKeyboardButton"
    text: String
    type_: InlineKeyboardButtonType = Field(..., alias="type")


class InlineKeyboardButtonTypeBuy(BaseObject):
    """
    A button to buy something. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageInvoice
    """

    ID: typing.Literal["inlineKeyboardButtonTypeBuy"] = "inlineKeyboardButtonTypeBuy"


class InlineKeyboardButtonTypeCallback(BaseObject):
    """
    A button that sends a callback query to a bot

    :param data: Data to be sent to the bot via a callback query
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["inlineKeyboardButtonTypeCallback"] = "inlineKeyboardButtonTypeCallback"
    data: Bytes


class InlineKeyboardButtonTypeCallbackGame(BaseObject):
    """
    A button with a game that sends a callback query to a bot. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageGame
    """

    ID: typing.Literal["inlineKeyboardButtonTypeCallbackGame"] = "inlineKeyboardButtonTypeCallbackGame"


class InlineKeyboardButtonTypeCallbackWithPassword(BaseObject):
    """
    A button that asks for the 2-step verification password of the current user and then sends a callback query to a bot

    :param data: Data to be sent to the bot via a callback query
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["inlineKeyboardButtonTypeCallbackWithPassword"] = "inlineKeyboardButtonTypeCallbackWithPassword"
    data: Bytes


class InlineKeyboardButtonTypeLoginUrl(BaseObject):
    """
    A button that opens a specified URL and automatically authorize the current user by calling getLoginUrlInfo

    :param url: An HTTP URL to pass to getLoginUrlInfo
    :type url: :class:`String`
    :param id: Unique button identifier
    :type id: :class:`Int53`
    :param forward_text: If non-empty, new text of the button in forwarded messages
    :type forward_text: :class:`String`
    """

    ID: typing.Literal["inlineKeyboardButtonTypeLoginUrl"] = "inlineKeyboardButtonTypeLoginUrl"
    url: String
    id: Int53
    forward_text: String


class InlineKeyboardButtonTypeSwitchInline(BaseObject):
    """
    A button that forces an inline query to the bot to be inserted in the input field

    :param query: Inline query to be sent to the bot
    :type query: :class:`String`
    :param target_chat: Target chat from which to send the inline query
    :type target_chat: :class:`TargetChat`
    """

    ID: typing.Literal["inlineKeyboardButtonTypeSwitchInline"] = "inlineKeyboardButtonTypeSwitchInline"
    query: String
    target_chat: TargetChat


class InlineKeyboardButtonTypeUrl(BaseObject):
    """
    A button that opens a specified URL

    :param url: HTTP or tg:// URL to open
    :type url: :class:`String`
    """

    ID: typing.Literal["inlineKeyboardButtonTypeUrl"] = "inlineKeyboardButtonTypeUrl"
    url: String


class InlineKeyboardButtonTypeUser(BaseObject):
    """
    A button with a user reference to be handled in the same way as textEntityTypeMentionName entities

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["inlineKeyboardButtonTypeUser"] = "inlineKeyboardButtonTypeUser"
    user_id: Int53


class InlineKeyboardButtonTypeWebApp(BaseObject):
    """
    A button that opens a Web App by calling openWebApp

    :param url: An HTTP URL to pass to openWebApp
    :type url: :class:`String`
    """

    ID: typing.Literal["inlineKeyboardButtonTypeWebApp"] = "inlineKeyboardButtonTypeWebApp"
    url: String


InlineKeyboardButtonType = typing.Union[
    InlineKeyboardButtonTypeBuy,
    InlineKeyboardButtonTypeCallback,
    InlineKeyboardButtonTypeCallbackGame,
    InlineKeyboardButtonTypeCallbackWithPassword,
    InlineKeyboardButtonTypeLoginUrl,
    InlineKeyboardButtonTypeSwitchInline,
    InlineKeyboardButtonTypeUrl,
    InlineKeyboardButtonTypeUser,
    InlineKeyboardButtonTypeWebApp,
]


class InlineQueryResultAnimation(BaseObject):
    """
    Represents an animation file

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param animation: Animation file
    :type animation: :class:`Animation`
    :param title: Animation title
    :type title: :class:`String`
    """

    ID: typing.Literal["inlineQueryResultAnimation"] = "inlineQueryResultAnimation"
    id: String
    animation: Animation
    title: String


class InlineQueryResultArticle(BaseObject):
    """
    Represents a link to an article or web page

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param url: URL of the result, if it exists
    :type url: :class:`String`
    :param title: Title of the result
    :type title: :class:`String`
    :param description: A short description of the result
    :type description: :class:`String`
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param hide_url: True, if the URL must be not shown
    :type hide_url: :class:`Bool`
    """

    ID: typing.Literal["inlineQueryResultArticle"] = "inlineQueryResultArticle"
    id: String
    url: String
    title: String
    description: String
    thumbnail: typing.Optional[Thumbnail] = None
    hide_url: Bool = False


class InlineQueryResultAudio(BaseObject):
    """
    Represents an audio file

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param audio: Audio file
    :type audio: :class:`Audio`
    """

    ID: typing.Literal["inlineQueryResultAudio"] = "inlineQueryResultAudio"
    id: String
    audio: Audio


class InlineQueryResultContact(BaseObject):
    """
    Represents a user contact

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param contact: A user contact
    :type contact: :class:`Contact`
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    """

    ID: typing.Literal["inlineQueryResultContact"] = "inlineQueryResultContact"
    id: String
    contact: Contact
    thumbnail: typing.Optional[Thumbnail] = None


class InlineQueryResultDocument(BaseObject):
    """
    Represents a document

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param document: Document
    :type document: :class:`Document`
    :param title: Document title
    :type title: :class:`String`
    :param description: Document description
    :type description: :class:`String`
    """

    ID: typing.Literal["inlineQueryResultDocument"] = "inlineQueryResultDocument"
    id: String
    document: Document
    title: String
    description: String


class InlineQueryResultGame(BaseObject):
    """
    Represents information about a game

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param game: Game result
    :type game: :class:`Game`
    """

    ID: typing.Literal["inlineQueryResultGame"] = "inlineQueryResultGame"
    id: String
    game: Game


class InlineQueryResultLocation(BaseObject):
    """
    Represents a point on the map

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param location: Location result
    :type location: :class:`Location`
    :param title: Title of the result
    :type title: :class:`String`
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    """

    ID: typing.Literal["inlineQueryResultLocation"] = "inlineQueryResultLocation"
    id: String
    location: Location
    title: String
    thumbnail: typing.Optional[Thumbnail] = None


class InlineQueryResultPhoto(BaseObject):
    """
    Represents a photo

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param photo: Photo
    :type photo: :class:`Photo`
    :param title: Title of the result, if known
    :type title: :class:`String`
    :param description: A short description of the result, if known
    :type description: :class:`String`
    """

    ID: typing.Literal["inlineQueryResultPhoto"] = "inlineQueryResultPhoto"
    id: String
    photo: Photo
    title: String
    description: String


class InlineQueryResultSticker(BaseObject):
    """
    Represents a sticker

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param sticker: Sticker
    :type sticker: :class:`Sticker`
    """

    ID: typing.Literal["inlineQueryResultSticker"] = "inlineQueryResultSticker"
    id: String
    sticker: Sticker


class InlineQueryResultVenue(BaseObject):
    """
    Represents information about a venue

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param venue: Venue result
    :type venue: :class:`Venue`
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    """

    ID: typing.Literal["inlineQueryResultVenue"] = "inlineQueryResultVenue"
    id: String
    venue: Venue
    thumbnail: typing.Optional[Thumbnail] = None


class InlineQueryResultVideo(BaseObject):
    """
    Represents a video

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param video: Video
    :type video: :class:`Video`
    :param title: Title of the video
    :type title: :class:`String`
    :param description: Description of the video
    :type description: :class:`String`
    """

    ID: typing.Literal["inlineQueryResultVideo"] = "inlineQueryResultVideo"
    id: String
    video: Video
    title: String
    description: String


class InlineQueryResultVoiceNote(BaseObject):
    """
    Represents a voice note

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param voice_note: Voice note
    :type voice_note: :class:`VoiceNote`
    :param title: Title of the voice note
    :type title: :class:`String`
    """

    ID: typing.Literal["inlineQueryResultVoiceNote"] = "inlineQueryResultVoiceNote"
    id: String
    voice_note: VoiceNote
    title: String


InlineQueryResult = typing.Union[
    InlineQueryResultAnimation,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultContact,
    InlineQueryResultDocument,
    InlineQueryResultGame,
    InlineQueryResultLocation,
    InlineQueryResultPhoto,
    InlineQueryResultSticker,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoiceNote,
]


class InlineQueryResults(BaseObject):
    """
    Represents the results of the inline query. Use sendInlineQueryResultMessage to send the result of the query

    :param inline_query_id: Unique identifier of the inline query
    :type inline_query_id: :class:`Int64`
    :param results: Results of the query
    :type results: :class:`Vector[InlineQueryResult]`
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`String`
    :param button: Button to be shown above inline query results; may be null, defaults to None
    :type button: :class:`InlineQueryResultsButton`, optional
    """

    ID: typing.Literal["inlineQueryResults"] = "inlineQueryResults"
    inline_query_id: Int64
    results: Vector[InlineQueryResult]
    next_offset: String
    button: typing.Optional[InlineQueryResultsButton] = None


class InlineQueryResultsButton(BaseObject):
    """
    Represents a button to be shown above inline query results

    :param text: The text of the button
    :type text: :class:`String`
    :param type_: Type of the button
    :type type_: :class:`InlineQueryResultsButtonType`
    """

    ID: typing.Literal["inlineQueryResultsButton"] = "inlineQueryResultsButton"
    text: String
    type_: InlineQueryResultsButtonType = Field(..., alias="type")


class InlineQueryResultsButtonTypeStartBot(BaseObject):
    """
    Describes the button that opens a private chat with the bot and sends a start message to the bot with the given parameter

    :param parameter: The parameter for the bot start message
    :type parameter: :class:`String`
    """

    ID: typing.Literal["inlineQueryResultsButtonTypeStartBot"] = "inlineQueryResultsButtonTypeStartBot"
    parameter: String


class InlineQueryResultsButtonTypeWebApp(BaseObject):
    """
    Describes the button that opens a Web App by calling getWebAppUrl

    :param url: An HTTP URL to pass to getWebAppUrl
    :type url: :class:`String`
    """

    ID: typing.Literal["inlineQueryResultsButtonTypeWebApp"] = "inlineQueryResultsButtonTypeWebApp"
    url: String


InlineQueryResultsButtonType = typing.Union[
    InlineQueryResultsButtonTypeStartBot,
    InlineQueryResultsButtonTypeWebApp,
]


class InputBackgroundLocal(BaseObject):
    """
    A background from a local file

    :param background: Background file to use. Only inputFileLocal and inputFileGenerated are supported. The file must be in JPEG format for wallpapers and in PNG format for patterns
    :type background: :class:`InputFile`
    """

    ID: typing.Literal["inputBackgroundLocal"] = "inputBackgroundLocal"
    background: InputFile


class InputBackgroundPrevious(BaseObject):
    """
    A background previously set in the chat; for chat backgrounds only

    :param message_id: Identifier of the message with the background
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["inputBackgroundPrevious"] = "inputBackgroundPrevious"
    message_id: Int53


class InputBackgroundRemote(BaseObject):
    """
    A background from the server

    :param background_id: The background identifier
    :type background_id: :class:`Int64`
    """

    ID: typing.Literal["inputBackgroundRemote"] = "inputBackgroundRemote"
    background_id: Int64


InputBackground = typing.Union[
    InputBackgroundLocal,
    InputBackgroundPrevious,
    InputBackgroundRemote,
]


class InputChatPhotoAnimation(BaseObject):
    """
    An animation in MPEG4 format; must be square, at most 10 seconds long, have width between 160 and 1280 and be at most 2MB in size

    :param animation: Animation to be set as profile photo. Only inputFileLocal and inputFileGenerated are allowed
    :type animation: :class:`InputFile`
    :param main_frame_timestamp: Timestamp of the frame, which will be used as static chat photo
    :type main_frame_timestamp: :class:`Double`
    """

    ID: typing.Literal["inputChatPhotoAnimation"] = "inputChatPhotoAnimation"
    animation: InputFile
    main_frame_timestamp: Double


class InputChatPhotoPrevious(BaseObject):
    """
    A previously used profile photo of the current user

    :param chat_photo_id: Identifier of the current user's profile photo to reuse
    :type chat_photo_id: :class:`Int64`
    """

    ID: typing.Literal["inputChatPhotoPrevious"] = "inputChatPhotoPrevious"
    chat_photo_id: Int64


class InputChatPhotoStatic(BaseObject):
    """
    A static photo in JPEG format

    :param photo: Photo to be set as profile photo. Only inputFileLocal and inputFileGenerated are allowed
    :type photo: :class:`InputFile`
    """

    ID: typing.Literal["inputChatPhotoStatic"] = "inputChatPhotoStatic"
    photo: InputFile


class InputChatPhotoSticker(BaseObject):
    """
    A sticker on a custom background

    :param sticker: Information about the sticker
    :type sticker: :class:`ChatPhotoSticker`
    """

    ID: typing.Literal["inputChatPhotoSticker"] = "inputChatPhotoSticker"
    sticker: ChatPhotoSticker


InputChatPhoto = typing.Union[
    InputChatPhotoAnimation,
    InputChatPhotoPrevious,
    InputChatPhotoStatic,
    InputChatPhotoSticker,
]


class InputCredentialsApplePay(BaseObject):
    """
    Applies if a user enters new credentials using Apple Pay

    :param data: JSON-encoded data with the credential identifier
    :type data: :class:`String`
    """

    ID: typing.Literal["inputCredentialsApplePay"] = "inputCredentialsApplePay"
    data: String


class InputCredentialsGooglePay(BaseObject):
    """
    Applies if a user enters new credentials using Google Pay

    :param data: JSON-encoded data with the credential identifier
    :type data: :class:`String`
    """

    ID: typing.Literal["inputCredentialsGooglePay"] = "inputCredentialsGooglePay"
    data: String


class InputCredentialsNew(BaseObject):
    """
    Applies if a user enters new credentials on a payment provider website

    :param data: JSON-encoded data with the credential identifier from the payment provider
    :type data: :class:`String`
    :param allow_save: True, if the credential identifier can be saved on the server side
    :type allow_save: :class:`Bool`
    """

    ID: typing.Literal["inputCredentialsNew"] = "inputCredentialsNew"
    data: String
    allow_save: Bool = False


class InputCredentialsSaved(BaseObject):
    """
    Applies if a user chooses some previously saved payment credentials. To use their previously saved credentials, the user must have a valid temporary password

    :param saved_credentials_id: Identifier of the saved credentials
    :type saved_credentials_id: :class:`String`
    """

    ID: typing.Literal["inputCredentialsSaved"] = "inputCredentialsSaved"
    saved_credentials_id: String


InputCredentials = typing.Union[
    InputCredentialsApplePay,
    InputCredentialsGooglePay,
    InputCredentialsNew,
    InputCredentialsSaved,
]


class InputFileGenerated(BaseObject):
    """
    A file generated by the application

    :param conversion: String specifying the conversion applied to the original file; must be persistent across application restarts. Conversions beginning with '#' are reserved for internal TDLib usage
    :type conversion: :class:`String`
    :param original_path: Local path to a file from which the file is generated; may be empty if there is no such file
    :type original_path: :class:`String`
    :param expected_size: Expected size of the generated file, in bytes; 0 if unknown, defaults to None
    :type expected_size: :class:`Int53`, optional
    """

    ID: typing.Literal["inputFileGenerated"] = "inputFileGenerated"
    conversion: String
    original_path: String = ""
    expected_size: typing.Optional[Int53] = 0


class InputFileId(BaseObject):
    """
    A file defined by its unique identifier

    :param id: Unique file identifier
    :type id: :class:`Int32`
    """

    ID: typing.Literal["inputFileId"] = "inputFileId"
    id: Int32


class InputFileLocal(BaseObject):
    """
    A file defined by a local path

    :param path: Local path to the file
    :type path: :class:`String`
    """

    ID: typing.Literal["inputFileLocal"] = "inputFileLocal"
    path: String


class InputFileRemote(BaseObject):
    """
    A file defined by its remote identifier. The remote identifier is guaranteed to be usable only if the corresponding file is still accessible to the user and known to TDLib. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application

    :param id: Remote file identifier
    :type id: :class:`String`
    """

    ID: typing.Literal["inputFileRemote"] = "inputFileRemote"
    id: String


InputFile = typing.Union[
    InputFileGenerated,
    InputFileId,
    InputFileLocal,
    InputFileRemote,
]


class InputIdentityDocument(BaseObject):
    """
    An identity document to be saved to Telegram Passport

    :param number: Document number; 1-24 characters
    :type number: :class:`String`
    :param front_side: Front side of the document
    :type front_side: :class:`InputFile`
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`Vector[InputFile]`
    :param expiration_date: Document expiration date; pass null if not applicable, defaults to None
    :type expiration_date: :class:`Date`, optional
    :param reverse_side: Reverse side of the document; only for driver license and identity card; pass null otherwise, defaults to None
    :type reverse_side: :class:`InputFile`, optional
    :param selfie: Selfie with the document; pass null if unavailable, defaults to None
    :type selfie: :class:`InputFile`, optional
    """

    ID: typing.Literal["inputIdentityDocument"] = "inputIdentityDocument"
    number: String = Field(..., min_length=1, max_length=24)
    front_side: InputFile
    translation: Vector[InputFile]
    expiration_date: typing.Optional[Date] = None
    reverse_side: typing.Optional[InputFile] = None
    selfie: typing.Optional[InputFile] = None


class InputInlineQueryResultAnimation(BaseObject):
    """
    Represents a link to an animated GIF or an animated (i.e., without sound) H.264/MPEG-4 AVC video

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param title: Title of the query result
    :type title: :class:`String`
    :param thumbnail_url: URL of the result thumbnail (JPEG, GIF, or MPEG4), if it exists
    :type thumbnail_url: :class:`String`
    :param thumbnail_mime_type: MIME type of the video thumbnail. If non-empty, must be one of "image/jpeg", "image/gif" and "video/mp4"
    :type thumbnail_mime_type: :class:`String`
    :param video_url: The URL of the video file (file size must not exceed 1MB)
    :type video_url: :class:`String`
    :param video_mime_type: MIME type of the video file. Must be one of "image/gif" and "video/mp4"
    :type video_mime_type: :class:`String`
    :param video_duration: Duration of the video, in seconds
    :type video_duration: :class:`Int32`
    :param video_width: Width of the video
    :type video_width: :class:`Int32`
    :param video_height: Height of the video
    :type video_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultAnimation"] = "inputInlineQueryResultAnimation"
    id: String
    title: String
    thumbnail_url: String
    thumbnail_mime_type: String
    video_url: String
    video_mime_type: String
    video_duration: Int32
    video_width: Int32
    video_height: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultArticle(BaseObject):
    """
    Represents a link to an article or web page

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param url: URL of the result, if it exists
    :type url: :class:`String`
    :param title: Title of the result
    :type title: :class:`String`
    :param description: A short description of the result
    :type description: :class:`String`
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`String`
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`Int32`
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param hide_url: True, if the URL must be not shown
    :type hide_url: :class:`Bool`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultArticle"] = "inputInlineQueryResultArticle"
    id: String
    url: String
    title: String
    description: String
    thumbnail_url: String
    thumbnail_width: Int32
    thumbnail_height: Int32
    input_message_content: InputMessageContent
    hide_url: Bool = False
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultAudio(BaseObject):
    """
    Represents a link to an MP3 audio file

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param title: Title of the audio file
    :type title: :class:`String`
    :param performer: Performer of the audio file
    :type performer: :class:`String`
    :param audio_url: The URL of the audio file
    :type audio_url: :class:`String`
    :param audio_duration: Audio file duration, in seconds
    :type audio_duration: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAudio, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultAudio"] = "inputInlineQueryResultAudio"
    id: String
    title: String
    performer: String
    audio_url: String
    audio_duration: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultContact(BaseObject):
    """
    Represents a user contact

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param contact: User contact
    :type contact: :class:`Contact`
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`String`
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`Int32`
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultContact"] = "inputInlineQueryResultContact"
    id: String
    contact: Contact
    thumbnail_url: String
    thumbnail_width: Int32
    thumbnail_height: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultDocument(BaseObject):
    """
    Represents a link to a file

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param title: Title of the resulting file
    :type title: :class:`String`
    :param description: Short description of the result, if known
    :type description: :class:`String`
    :param document_url: URL of the file
    :type document_url: :class:`String`
    :param mime_type: MIME type of the file content; only "application/pdf" and "application/zip" are currently allowed
    :type mime_type: :class:`String`
    :param thumbnail_url: The URL of the file thumbnail, if it exists
    :type thumbnail_url: :class:`String`
    :param thumbnail_width: Width of the thumbnail
    :type thumbnail_width: :class:`Int32`
    :param thumbnail_height: Height of the thumbnail
    :type thumbnail_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageDocument, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultDocument"] = "inputInlineQueryResultDocument"
    id: String
    title: String
    description: String
    document_url: String
    mime_type: String
    thumbnail_url: String
    thumbnail_width: Int32
    thumbnail_height: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultGame(BaseObject):
    """
    Represents a game

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param game_short_name: Short name of the game
    :type game_short_name: :class:`String`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultGame"] = "inputInlineQueryResultGame"
    id: String
    game_short_name: String
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultLocation(BaseObject):
    """
    Represents a point on the map

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param location: Location result
    :type location: :class:`Location`
    :param live_period: Amount of time relative to the message sent time until the location can be updated, in seconds
    :type live_period: :class:`Int32`
    :param title: Title of the result
    :type title: :class:`String`
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`String`
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`Int32`
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultLocation"] = "inputInlineQueryResultLocation"
    id: String
    location: Location
    live_period: Int32
    title: String
    thumbnail_url: String
    thumbnail_width: Int32
    thumbnail_height: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultPhoto(BaseObject):
    """
    Represents link to a JPEG image

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param title: Title of the result, if known
    :type title: :class:`String`
    :param description: A short description of the result, if known
    :type description: :class:`String`
    :param thumbnail_url: URL of the photo thumbnail, if it exists
    :type thumbnail_url: :class:`String`
    :param photo_url: The URL of the JPEG photo (photo size must not exceed 5MB)
    :type photo_url: :class:`String`
    :param photo_width: Width of the photo
    :type photo_width: :class:`Int32`
    :param photo_height: Height of the photo
    :type photo_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessagePhoto, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultPhoto"] = "inputInlineQueryResultPhoto"
    id: String
    title: String
    description: String
    thumbnail_url: String
    photo_url: String
    photo_width: Int32
    photo_height: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultSticker(BaseObject):
    """
    Represents a link to a WEBP, TGS, or WEBM sticker

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param thumbnail_url: URL of the sticker thumbnail, if it exists
    :type thumbnail_url: :class:`String`
    :param sticker_url: The URL of the WEBP, TGS, or WEBM sticker (sticker file size must not exceed 5MB)
    :type sticker_url: :class:`String`
    :param sticker_width: Width of the sticker
    :type sticker_width: :class:`Int32`
    :param sticker_height: Height of the sticker
    :type sticker_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageSticker, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultSticker"] = "inputInlineQueryResultSticker"
    id: String
    thumbnail_url: String
    sticker_url: String
    sticker_width: Int32
    sticker_height: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultVenue(BaseObject):
    """
    Represents information about a venue

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param venue: Venue result
    :type venue: :class:`Venue`
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`String`
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`Int32`
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultVenue"] = "inputInlineQueryResultVenue"
    id: String
    venue: Venue
    thumbnail_url: String
    thumbnail_width: Int32
    thumbnail_height: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultVideo(BaseObject):
    """
    Represents a link to a page containing an embedded video player or a video file

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param title: Title of the result
    :type title: :class:`String`
    :param description: A short description of the result, if known
    :type description: :class:`String`
    :param thumbnail_url: The URL of the video thumbnail (JPEG), if it exists
    :type thumbnail_url: :class:`String`
    :param video_url: URL of the embedded video player or video file
    :type video_url: :class:`String`
    :param mime_type: MIME type of the content of the video URL, only "text/html" or "video/mp4" are currently supported
    :type mime_type: :class:`String`
    :param video_width: Width of the video
    :type video_width: :class:`Int32`
    :param video_height: Height of the video
    :type video_height: :class:`Int32`
    :param video_duration: Video duration, in seconds
    :type video_duration: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVideo, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultVideo"] = "inputInlineQueryResultVideo"
    id: String
    title: String
    description: String
    thumbnail_url: String
    video_url: String
    mime_type: String
    video_width: Int32
    video_height: Int32
    video_duration: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


class InputInlineQueryResultVoiceNote(BaseObject):
    """
    Represents a link to an opus-encoded audio file within an OGG container, single channel audio

    :param id: Unique identifier of the query result
    :type id: :class:`String`
    :param title: Title of the voice note
    :type title: :class:`String`
    :param voice_note_url: The URL of the voice note file
    :type voice_note_url: :class:`String`
    :param voice_note_duration: Duration of the voice note, in seconds
    :type voice_note_duration: :class:`Int32`
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVoiceNote, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The message reply markup; pass null if none. Must be of type replyMarkupInlineKeyboard or null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["inputInlineQueryResultVoiceNote"] = "inputInlineQueryResultVoiceNote"
    id: String
    title: String
    voice_note_url: String
    voice_note_duration: Int32
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None


InputInlineQueryResult = typing.Union[
    InputInlineQueryResultAnimation,
    InputInlineQueryResultArticle,
    InputInlineQueryResultAudio,
    InputInlineQueryResultContact,
    InputInlineQueryResultDocument,
    InputInlineQueryResultGame,
    InputInlineQueryResultLocation,
    InputInlineQueryResultPhoto,
    InputInlineQueryResultSticker,
    InputInlineQueryResultVenue,
    InputInlineQueryResultVideo,
    InputInlineQueryResultVoiceNote,
]


class InputInvoiceMessage(BaseObject):
    """
    An invoice from a message of the type messageInvoice

    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["inputInvoiceMessage"] = "inputInvoiceMessage"
    chat_id: Int53
    message_id: Int53


class InputInvoiceName(BaseObject):
    """
    An invoice from a link of the type internalLinkTypeInvoice

    :param name: Name of the invoice
    :type name: :class:`String`
    """

    ID: typing.Literal["inputInvoiceName"] = "inputInvoiceName"
    name: String


InputInvoice = typing.Union[
    InputInvoiceMessage,
    InputInvoiceName,
]


class InputMessageAnimation(BaseObject):
    """
    An animation message (GIF-style).

    :param animation: Animation file to be sent
    :type animation: :class:`InputFile`
    :param added_sticker_file_ids: File identifiers of the stickers added to the animation, if applicable
    :type added_sticker_file_ids: :class:`Vector[Int32]`
    :param duration: Duration of the animation, in seconds
    :type duration: :class:`Int32`
    :param width: Width of the animation; may be replaced by the server
    :type width: :class:`Int32`
    :param height: Height of the animation; may be replaced by the server
    :type height: :class:`Int32`
    :param has_spoiler: True, if the animation preview must be covered by a spoiler animation; not supported in secret chats
    :type has_spoiler: :class:`Bool`
    :param thumbnail: Animation thumbnail; pass null to skip thumbnail uploading, defaults to None
    :type thumbnail: :class:`InputThumbnail`, optional
    :param caption: Animation caption; pass null to use an empty caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["inputMessageAnimation"] = "inputMessageAnimation"
    animation: InputFile
    added_sticker_file_ids: Vector[Int32]
    duration: Int32
    width: Int32
    height: Int32
    has_spoiler: Bool = False
    thumbnail: typing.Optional[InputThumbnail] = None
    caption: typing.Optional[FormattedText] = None


class InputMessageAudio(BaseObject):
    """
    An audio message

    :param audio: Audio file to be sent
    :type audio: :class:`InputFile`
    :param duration: Duration of the audio, in seconds; may be replaced by the server
    :type duration: :class:`Int32`
    :param title: Title of the audio; 0-64 characters; may be replaced by the server
    :type title: :class:`String`
    :param performer: Performer of the audio; 0-64 characters, may be replaced by the server
    :type performer: :class:`String`
    :param album_cover_thumbnail: Thumbnail of the cover for the album; pass null to skip thumbnail uploading, defaults to None
    :type album_cover_thumbnail: :class:`InputThumbnail`, optional
    :param caption: Audio caption; pass null to use an empty caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["inputMessageAudio"] = "inputMessageAudio"
    audio: InputFile
    duration: Int32
    title: String = Field("", max_length=64)
    performer: String = Field("", max_length=64)
    album_cover_thumbnail: typing.Optional[InputThumbnail] = None
    caption: typing.Optional[FormattedText] = None


class InputMessageContact(BaseObject):
    """
    A message containing a user contact

    :param contact: Contact to send
    :type contact: :class:`Contact`
    """

    ID: typing.Literal["inputMessageContact"] = "inputMessageContact"
    contact: Contact


class InputMessageDice(BaseObject):
    """
    A dice message

    :param emoji: Emoji on which the dice throw animation is based
    :type emoji: :class:`String`
    :param clear_draft: True, if the chat message draft must be deleted
    :type clear_draft: :class:`Bool`
    """

    ID: typing.Literal["inputMessageDice"] = "inputMessageDice"
    emoji: String
    clear_draft: Bool = False


class InputMessageDocument(BaseObject):
    """
    A document message (general file)

    :param document: Document to be sent
    :type document: :class:`InputFile`
    :param disable_content_type_detection: If true, automatic file type detection will be disabled and the document will always be sent as file. Always true for files sent to secret chats
    :type disable_content_type_detection: :class:`Bool`
    :param thumbnail: Document thumbnail; pass null to skip thumbnail uploading, defaults to None
    :type thumbnail: :class:`InputThumbnail`, optional
    :param caption: Document caption; pass null to use an empty caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["inputMessageDocument"] = "inputMessageDocument"
    document: InputFile
    disable_content_type_detection: Bool
    thumbnail: typing.Optional[InputThumbnail] = None
    caption: typing.Optional[FormattedText] = None


class InputMessageForwarded(BaseObject):
    """
    A forwarded message

    :param from_chat_id: Identifier for the chat this forwarded message came from
    :type from_chat_id: :class:`Int53`
    :param message_id: Identifier of the message to forward
    :type message_id: :class:`Int53`
    :param in_game_share: True, if a game message is being shared from a launched game; applies only to game messages
    :type in_game_share: :class:`Bool`
    :param copy_options: Options to be used to copy content of the message without reference to the original sender; pass null to forward the message as usual, defaults to None
    :type copy_options: :class:`MessageCopyOptions`, optional
    """

    ID: typing.Literal["inputMessageForwarded"] = "inputMessageForwarded"
    from_chat_id: Int53
    message_id: Int53
    in_game_share: Bool = False
    copy_options: typing.Optional[MessageCopyOptions] = None


class InputMessageGame(BaseObject):
    """
    A message with a game; not supported for channels or secret chats

    :param bot_user_id: User identifier of the bot that owns the game
    :type bot_user_id: :class:`Int53`
    :param game_short_name: Short name of the game
    :type game_short_name: :class:`String`
    """

    ID: typing.Literal["inputMessageGame"] = "inputMessageGame"
    bot_user_id: Int53
    game_short_name: String


class InputMessageInvoice(BaseObject):
    """
    A message with an invoice; can be used only by bots

    :param invoice: Invoice
    :type invoice: :class:`Invoice`
    :param title: Product title; 1-32 characters
    :type title: :class:`String`
    :param photo_url: Product photo URL; optional
    :type photo_url: :class:`String`
    :param photo_size: Product photo size
    :type photo_size: :class:`Int32`
    :param photo_width: Product photo width
    :type photo_width: :class:`Int32`
    :param photo_height: Product photo height
    :type photo_height: :class:`Int32`
    :param payload: The invoice payload
    :type payload: :class:`Bytes`
    :param provider_token: Payment provider token
    :type provider_token: :class:`String`
    :param provider_data: JSON-encoded data about the invoice, which will be shared with the payment provider
    :type provider_data: :class:`String`
    :param start_parameter: Unique invoice bot deep link parameter for the generation of this invoice. If empty, it would be possible to pay directly from forwards of the invoice message
    :type start_parameter: :class:`String`
    :param extended_media_content: The content of extended media attached to the invoice. The content of the message to be sent. Must be one of the following types: inputMessagePhoto, inputMessageVideo
    :type extended_media_content: :class:`InputMessageContent`
    :param description: Product description; 0-255 characters
    :type description: :class:`String`
    """

    ID: typing.Literal["inputMessageInvoice"] = "inputMessageInvoice"
    invoice: Invoice
    title: String = Field(..., min_length=1, max_length=32)
    photo_url: String
    photo_size: Int32
    photo_width: Int32
    photo_height: Int32
    payload: Bytes
    provider_token: String
    provider_data: String
    start_parameter: String
    extended_media_content: InputMessageContent
    description: String = Field("", max_length=255)


class InputMessageLocation(BaseObject):
    """
    A message with a location

    :param location: Location to be sent
    :type location: :class:`Location`
    :param live_period: Period for which the location can be updated, in seconds; must be between 60 and 86400 for a live location and 0 otherwise
    :type live_period: :class:`Int32`
    :param heading: For live locations, a direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
    :type heading: :class:`Int32`
    :param proximity_alert_radius: For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled. Can't be enabled in channels and Saved Messages
    :type proximity_alert_radius: :class:`Int32`
    """

    ID: typing.Literal["inputMessageLocation"] = "inputMessageLocation"
    location: Location
    live_period: Int32
    heading: Int32 = 0
    proximity_alert_radius: Int32 = 0


class InputMessagePhoto(BaseObject):
    """
    A photo message

    :param photo: Photo to send. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20
    :type photo: :class:`InputFile`
    :param added_sticker_file_ids: File identifiers of the stickers added to the photo, if applicable
    :type added_sticker_file_ids: :class:`Vector[Int32]`
    :param width: Photo width
    :type width: :class:`Int32`
    :param height: Photo height
    :type height: :class:`Int32`
    :param has_spoiler: True, if the photo preview must be covered by a spoiler animation; not supported in secret chats
    :type has_spoiler: :class:`Bool`
    :param thumbnail: Photo thumbnail to be sent; pass null to skip thumbnail uploading. The thumbnail is sent to the other party only in secret chats, defaults to None
    :type thumbnail: :class:`InputThumbnail`, optional
    :param caption: Photo caption; pass null to use an empty caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    :param self_destruct_type: Photo self-destruct type; pass null if none; private chats only, defaults to None
    :type self_destruct_type: :class:`MessageSelfDestructType`, optional
    """

    ID: typing.Literal["inputMessagePhoto"] = "inputMessagePhoto"
    photo: InputFile
    added_sticker_file_ids: Vector[Int32]
    width: Int32
    height: Int32
    has_spoiler: Bool = False
    thumbnail: typing.Optional[InputThumbnail] = None
    caption: typing.Optional[FormattedText] = None
    self_destruct_type: typing.Optional[MessageSelfDestructType] = None


class InputMessagePoll(BaseObject):
    """
    A message with a poll. Polls can't be sent to secret chats. Polls can be sent only to a private chat with a bot

    :param question: Poll question; 1-255 characters (up to 300 characters for bots)
    :type question: :class:`String`
    :param options: List of poll answer options, 2-10 strings 1-100 characters each
    :type options: :class:`Vector[String]`
    :param type_: Type of the poll
    :type type_: :class:`PollType`
    :param open_period: Amount of time the poll will be active after creation, in seconds; for bots only
    :type open_period: :class:`Int32`
    :param close_date: Point in time (Unix timestamp) when the poll will automatically be closed; for bots only
    :type close_date: :class:`Int32`
    :param is_anonymous: True, if the poll voters are anonymous. Non-anonymous polls can't be sent or forwarded to channels
    :type is_anonymous: :class:`Bool`
    :param is_closed: True, if the poll needs to be sent already closed; for bots only
    :type is_closed: :class:`Bool`
    """

    ID: typing.Literal["inputMessagePoll"] = "inputMessagePoll"
    question: String = Field(..., min_length=1, max_length=255)
    options: Vector[String]
    type_: PollType = Field(..., alias="type")
    open_period: Int32
    close_date: Int32
    is_anonymous: Bool = False
    is_closed: Bool = False


class InputMessageSticker(BaseObject):
    """
    A sticker message

    :param sticker: Sticker to be sent
    :type sticker: :class:`InputFile`
    :param width: Sticker width
    :type width: :class:`Int32`
    :param height: Sticker height
    :type height: :class:`Int32`
    :param emoji: Emoji used to choose the sticker
    :type emoji: :class:`String`
    :param thumbnail: Sticker thumbnail; pass null to skip thumbnail uploading, defaults to None
    :type thumbnail: :class:`InputThumbnail`, optional
    """

    ID: typing.Literal["inputMessageSticker"] = "inputMessageSticker"
    sticker: InputFile
    width: Int32
    height: Int32
    emoji: String
    thumbnail: typing.Optional[InputThumbnail] = None


class InputMessageStory(BaseObject):
    """
    A message with a forwarded story. Stories can't be sent to secret chats. A story can be forwarded only if story.can_be_forwarded

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["inputMessageStory"] = "inputMessageStory"
    story_sender_chat_id: Int53
    story_id: Int32


class InputMessageText(BaseObject):
    """
    A text message

    :param text: Formatted text to be sent; 1-getOption("message_text_length_max") characters. Only Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, Code, Pre, PreCode, TextUrl and MentionName entities are allowed to be specified manually
    :type text: :class:`FormattedText`
    :param disable_web_page_preview: True, if rich web page previews for URLs in the message text must be disabled
    :type disable_web_page_preview: :class:`Bool`
    :param clear_draft: True, if a chat message draft must be deleted
    :type clear_draft: :class:`Bool`
    """

    ID: typing.Literal["inputMessageText"] = "inputMessageText"
    text: FormattedText
    disable_web_page_preview: Bool = False
    clear_draft: Bool = False


class InputMessageVenue(BaseObject):
    """
    A message with information about a venue

    :param venue: Venue to send
    :type venue: :class:`Venue`
    """

    ID: typing.Literal["inputMessageVenue"] = "inputMessageVenue"
    venue: Venue


class InputMessageVideo(BaseObject):
    """
    A video message

    :param video: Video to be sent
    :type video: :class:`InputFile`
    :param added_sticker_file_ids: File identifiers of the stickers added to the video, if applicable
    :type added_sticker_file_ids: :class:`Vector[Int32]`
    :param duration: Duration of the video, in seconds
    :type duration: :class:`Int32`
    :param width: Video width
    :type width: :class:`Int32`
    :param height: Video height
    :type height: :class:`Int32`
    :param supports_streaming: True, if the video is supposed to be streamed
    :type supports_streaming: :class:`Bool`
    :param has_spoiler: True, if the video preview must be covered by a spoiler animation; not supported in secret chats
    :type has_spoiler: :class:`Bool`
    :param thumbnail: Video thumbnail; pass null to skip thumbnail uploading, defaults to None
    :type thumbnail: :class:`InputThumbnail`, optional
    :param caption: Video caption; pass null to use an empty caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    :param self_destruct_type: Video self-destruct type; pass null if none; private chats only, defaults to None
    :type self_destruct_type: :class:`MessageSelfDestructType`, optional
    """

    ID: typing.Literal["inputMessageVideo"] = "inputMessageVideo"
    video: InputFile
    added_sticker_file_ids: Vector[Int32]
    duration: Int32
    width: Int32
    height: Int32
    supports_streaming: Bool = False
    has_spoiler: Bool = False
    thumbnail: typing.Optional[InputThumbnail] = None
    caption: typing.Optional[FormattedText] = None
    self_destruct_type: typing.Optional[MessageSelfDestructType] = None


class InputMessageVideoNote(BaseObject):
    """
    A video note message

    :param video_note: Video note to be sent
    :type video_note: :class:`InputFile`
    :param duration: Duration of the video, in seconds
    :type duration: :class:`Int32`
    :param length: Video width and height; must be positive and not greater than 640
    :type length: :class:`Int32`
    :param thumbnail: Video thumbnail; pass null to skip thumbnail uploading, defaults to None
    :type thumbnail: :class:`InputThumbnail`, optional
    """

    ID: typing.Literal["inputMessageVideoNote"] = "inputMessageVideoNote"
    video_note: InputFile
    duration: Int32
    length: Int32
    thumbnail: typing.Optional[InputThumbnail] = None


class InputMessageVoiceNote(BaseObject):
    """
    A voice note message

    :param voice_note: Voice note to be sent
    :type voice_note: :class:`InputFile`
    :param duration: Duration of the voice note, in seconds
    :type duration: :class:`Int32`
    :param waveform: Waveform representation of the voice note in 5-bit format
    :type waveform: :class:`Bytes`
    :param caption: Voice note caption; pass null to use an empty caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["inputMessageVoiceNote"] = "inputMessageVoiceNote"
    voice_note: InputFile
    duration: Int32
    waveform: Bytes
    caption: typing.Optional[FormattedText] = None


InputMessageContent = typing.Union[
    InputMessageAnimation,
    InputMessageAudio,
    InputMessageContact,
    InputMessageDice,
    InputMessageDocument,
    InputMessageForwarded,
    InputMessageGame,
    InputMessageInvoice,
    InputMessageLocation,
    InputMessagePhoto,
    InputMessagePoll,
    InputMessageSticker,
    InputMessageStory,
    InputMessageText,
    InputMessageVenue,
    InputMessageVideo,
    InputMessageVideoNote,
    InputMessageVoiceNote,
]


class InputPassportElementAddress(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's address

    :param address: The address to be saved
    :type address: :class:`Address`
    """

    ID: typing.Literal["inputPassportElementAddress"] = "inputPassportElementAddress"
    address: Address


class InputPassportElementBankStatement(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's bank statement

    :param bank_statement: The bank statement to be saved
    :type bank_statement: :class:`InputPersonalDocument`
    """

    ID: typing.Literal["inputPassportElementBankStatement"] = "inputPassportElementBankStatement"
    bank_statement: InputPersonalDocument


class InputPassportElementDriverLicense(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's driver license

    :param driver_license: The driver license to be saved
    :type driver_license: :class:`InputIdentityDocument`
    """

    ID: typing.Literal["inputPassportElementDriverLicense"] = "inputPassportElementDriverLicense"
    driver_license: InputIdentityDocument


class InputPassportElementEmailAddress(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's email address

    :param email_address: The email address to be saved
    :type email_address: :class:`String`
    """

    ID: typing.Literal["inputPassportElementEmailAddress"] = "inputPassportElementEmailAddress"
    email_address: String


class InputPassportElementIdentityCard(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's identity card

    :param identity_card: The identity card to be saved
    :type identity_card: :class:`InputIdentityDocument`
    """

    ID: typing.Literal["inputPassportElementIdentityCard"] = "inputPassportElementIdentityCard"
    identity_card: InputIdentityDocument


class InputPassportElementInternalPassport(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's internal passport

    :param internal_passport: The internal passport to be saved
    :type internal_passport: :class:`InputIdentityDocument`
    """

    ID: typing.Literal["inputPassportElementInternalPassport"] = "inputPassportElementInternalPassport"
    internal_passport: InputIdentityDocument


class InputPassportElementPassport(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's passport

    :param passport: The passport to be saved
    :type passport: :class:`InputIdentityDocument`
    """

    ID: typing.Literal["inputPassportElementPassport"] = "inputPassportElementPassport"
    passport: InputIdentityDocument


class InputPassportElementPassportRegistration(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's passport registration

    :param passport_registration: The passport registration page to be saved
    :type passport_registration: :class:`InputPersonalDocument`
    """

    ID: typing.Literal["inputPassportElementPassportRegistration"] = "inputPassportElementPassportRegistration"
    passport_registration: InputPersonalDocument


class InputPassportElementPersonalDetails(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's personal details

    :param personal_details: Personal details of the user
    :type personal_details: :class:`PersonalDetails`
    """

    ID: typing.Literal["inputPassportElementPersonalDetails"] = "inputPassportElementPersonalDetails"
    personal_details: PersonalDetails


class InputPassportElementPhoneNumber(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's phone number

    :param phone_number: The phone number to be saved
    :type phone_number: :class:`String`
    """

    ID: typing.Literal["inputPassportElementPhoneNumber"] = "inputPassportElementPhoneNumber"
    phone_number: String


class InputPassportElementRentalAgreement(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's rental agreement

    :param rental_agreement: The rental agreement to be saved
    :type rental_agreement: :class:`InputPersonalDocument`
    """

    ID: typing.Literal["inputPassportElementRentalAgreement"] = "inputPassportElementRentalAgreement"
    rental_agreement: InputPersonalDocument


class InputPassportElementTemporaryRegistration(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's temporary registration

    :param temporary_registration: The temporary registration document to be saved
    :type temporary_registration: :class:`InputPersonalDocument`
    """

    ID: typing.Literal["inputPassportElementTemporaryRegistration"] = "inputPassportElementTemporaryRegistration"
    temporary_registration: InputPersonalDocument


class InputPassportElementUtilityBill(BaseObject):
    """
    A Telegram Passport element to be saved containing the user's utility bill

    :param utility_bill: The utility bill to be saved
    :type utility_bill: :class:`InputPersonalDocument`
    """

    ID: typing.Literal["inputPassportElementUtilityBill"] = "inputPassportElementUtilityBill"
    utility_bill: InputPersonalDocument


InputPassportElement = typing.Union[
    InputPassportElementAddress,
    InputPassportElementBankStatement,
    InputPassportElementDriverLicense,
    InputPassportElementEmailAddress,
    InputPassportElementIdentityCard,
    InputPassportElementInternalPassport,
    InputPassportElementPassport,
    InputPassportElementPassportRegistration,
    InputPassportElementPersonalDetails,
    InputPassportElementPhoneNumber,
    InputPassportElementRentalAgreement,
    InputPassportElementTemporaryRegistration,
    InputPassportElementUtilityBill,
]


class InputPassportElementError(BaseObject):
    """
    Contains the description of an error in a Telegram Passport element; for bots only

    :param type_: Type of Telegram Passport element that has the error
    :type type_: :class:`PassportElementType`
    :param message: Error message
    :type message: :class:`String`
    :param source: Error source
    :type source: :class:`InputPassportElementErrorSource`
    """

    ID: typing.Literal["inputPassportElementError"] = "inputPassportElementError"
    type_: PassportElementType = Field(..., alias="type")
    message: String
    source: InputPassportElementErrorSource


class InputPassportElementErrorSourceDataField(BaseObject):
    """
    A data field contains an error. The error is considered resolved when the field's value changes

    :param field_name: Field name
    :type field_name: :class:`String`
    :param data_hash: Current data hash
    :type data_hash: :class:`Bytes`
    """

    ID: typing.Literal["inputPassportElementErrorSourceDataField"] = "inputPassportElementErrorSourceDataField"
    field_name: String
    data_hash: Bytes


class InputPassportElementErrorSourceFile(BaseObject):
    """
    The file contains an error. The error is considered resolved when the file changes

    :param file_hash: Current hash of the file which has the error
    :type file_hash: :class:`Bytes`
    """

    ID: typing.Literal["inputPassportElementErrorSourceFile"] = "inputPassportElementErrorSourceFile"
    file_hash: Bytes


class InputPassportElementErrorSourceFiles(BaseObject):
    """
    The list of attached files contains an error. The error is considered resolved when the file list changes

    :param file_hashes: Current hashes of all attached files
    :type file_hashes: :class:`Vector[Bytes]`
    """

    ID: typing.Literal["inputPassportElementErrorSourceFiles"] = "inputPassportElementErrorSourceFiles"
    file_hashes: Vector[Bytes]


class InputPassportElementErrorSourceFrontSide(BaseObject):
    """
    The front side of the document contains an error. The error is considered resolved when the file with the front side of the document changes

    :param file_hash: Current hash of the file containing the front side
    :type file_hash: :class:`Bytes`
    """

    ID: typing.Literal["inputPassportElementErrorSourceFrontSide"] = "inputPassportElementErrorSourceFrontSide"
    file_hash: Bytes


class InputPassportElementErrorSourceReverseSide(BaseObject):
    """
    The reverse side of the document contains an error. The error is considered resolved when the file with the reverse side of the document changes

    :param file_hash: Current hash of the file containing the reverse side
    :type file_hash: :class:`Bytes`
    """

    ID: typing.Literal["inputPassportElementErrorSourceReverseSide"] = "inputPassportElementErrorSourceReverseSide"
    file_hash: Bytes


class InputPassportElementErrorSourceSelfie(BaseObject):
    """
    The selfie contains an error. The error is considered resolved when the file with the selfie changes

    :param file_hash: Current hash of the file containing the selfie
    :type file_hash: :class:`Bytes`
    """

    ID: typing.Literal["inputPassportElementErrorSourceSelfie"] = "inputPassportElementErrorSourceSelfie"
    file_hash: Bytes


class InputPassportElementErrorSourceTranslationFile(BaseObject):
    """
    One of the files containing the translation of the document contains an error. The error is considered resolved when the file with the translation changes

    :param file_hash: Current hash of the file containing the translation
    :type file_hash: :class:`Bytes`
    """

    ID: typing.Literal[
        "inputPassportElementErrorSourceTranslationFile"
    ] = "inputPassportElementErrorSourceTranslationFile"
    file_hash: Bytes


class InputPassportElementErrorSourceTranslationFiles(BaseObject):
    """
    The translation of the document contains an error. The error is considered resolved when the list of files changes

    :param file_hashes: Current hashes of all files with the translation
    :type file_hashes: :class:`Vector[Bytes]`
    """

    ID: typing.Literal[
        "inputPassportElementErrorSourceTranslationFiles"
    ] = "inputPassportElementErrorSourceTranslationFiles"
    file_hashes: Vector[Bytes]


class InputPassportElementErrorSourceUnspecified(BaseObject):
    """
    The element contains an error in an unspecified place. The error will be considered resolved when new data is added

    :param element_hash: Current hash of the entire element
    :type element_hash: :class:`Bytes`
    """

    ID: typing.Literal["inputPassportElementErrorSourceUnspecified"] = "inputPassportElementErrorSourceUnspecified"
    element_hash: Bytes


InputPassportElementErrorSource = typing.Union[
    InputPassportElementErrorSourceDataField,
    InputPassportElementErrorSourceFile,
    InputPassportElementErrorSourceFiles,
    InputPassportElementErrorSourceFrontSide,
    InputPassportElementErrorSourceReverseSide,
    InputPassportElementErrorSourceSelfie,
    InputPassportElementErrorSourceTranslationFile,
    InputPassportElementErrorSourceTranslationFiles,
    InputPassportElementErrorSourceUnspecified,
]


class InputPersonalDocument(BaseObject):
    """
    A personal document to be saved to Telegram Passport

    :param files: List of files containing the pages of the document
    :type files: :class:`Vector[InputFile]`
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`Vector[InputFile]`
    """

    ID: typing.Literal["inputPersonalDocument"] = "inputPersonalDocument"
    files: Vector[InputFile]
    translation: Vector[InputFile]


class InputSticker(BaseObject):
    """
    A sticker to be added to a sticker set

    :param sticker: File with the sticker; must fit in a 512x512 square. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server-side. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
    :type sticker: :class:`InputFile`
    :param emojis: String with 1-20 emoji corresponding to the sticker
    :type emojis: :class:`String`
    :param keywords: List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker
    :type keywords: :class:`Vector[String]`
    :param mask_position: Position where the mask is placed; pass null if not specified, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    """

    ID: typing.Literal["inputSticker"] = "inputSticker"
    sticker: InputFile
    emojis: String
    keywords: Vector[String]
    mask_position: typing.Optional[MaskPosition] = None


class InputStoryArea(BaseObject):
    """
    Describes a clickable rectangle area on a story media to be added

    :param position: Position of the area
    :type position: :class:`StoryAreaPosition`
    :param type_: Type of the area
    :type type_: :class:`InputStoryAreaType`
    """

    ID: typing.Literal["inputStoryArea"] = "inputStoryArea"
    position: StoryAreaPosition
    type_: InputStoryAreaType = Field(..., alias="type")


class InputStoryAreaTypeFoundVenue(BaseObject):
    """
    An area pointing to a venue found by the bot getOption("venue_search_bot_username")

    :param query_id: Identifier of the inline query, used to found the venue
    :type query_id: :class:`Int64`
    :param result_id: Identifier of the inline query result
    :type result_id: :class:`String`
    """

    ID: typing.Literal["inputStoryAreaTypeFoundVenue"] = "inputStoryAreaTypeFoundVenue"
    query_id: Int64
    result_id: String


class InputStoryAreaTypeLocation(BaseObject):
    """
    An area pointing to a location

    :param location: The location
    :type location: :class:`Location`
    """

    ID: typing.Literal["inputStoryAreaTypeLocation"] = "inputStoryAreaTypeLocation"
    location: Location


class InputStoryAreaTypePreviousVenue(BaseObject):
    """
    An area pointing to a venue already added to the story

    :param venue_provider: Provider of the venue
    :type venue_provider: :class:`String`
    :param venue_id: Identifier of the venue in the provider database
    :type venue_id: :class:`String`
    """

    ID: typing.Literal["inputStoryAreaTypePreviousVenue"] = "inputStoryAreaTypePreviousVenue"
    venue_provider: String
    venue_id: String


InputStoryAreaType = typing.Union[
    InputStoryAreaTypeFoundVenue,
    InputStoryAreaTypeLocation,
    InputStoryAreaTypePreviousVenue,
]


class InputStoryAreas(BaseObject):
    """
    Contains a list of story areas to be added

    :param areas: List of 0-10 input story areas
    :type areas: :class:`Vector[InputStoryArea]`
    """

    ID: typing.Literal["inputStoryAreas"] = "inputStoryAreas"
    areas: Vector[InputStoryArea]


class InputStoryContentPhoto(BaseObject):
    """
    A photo story

    :param photo: Photo to send. The photo must be at most 10 MB in size. The photo size must be 1080x1920
    :type photo: :class:`InputFile`
    :param added_sticker_file_ids: File identifiers of the stickers added to the photo, if applicable
    :type added_sticker_file_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["inputStoryContentPhoto"] = "inputStoryContentPhoto"
    photo: InputFile
    added_sticker_file_ids: Vector[Int32]


class InputStoryContentVideo(BaseObject):
    """
    A video story

    :param video: Video to be sent. The video size must be 720x1280. The video must be streamable and stored in MPEG4 format, after encoding with x265 codec and key frames added each second
    :type video: :class:`InputFile`
    :param added_sticker_file_ids: File identifiers of the stickers added to the video, if applicable
    :type added_sticker_file_ids: :class:`Vector[Int32]`
    :param duration: Precise duration of the video, in seconds; 0-60
    :type duration: :class:`Double`
    :param is_animation: True, if the video has no sound
    :type is_animation: :class:`Bool`
    """

    ID: typing.Literal["inputStoryContentVideo"] = "inputStoryContentVideo"
    video: InputFile
    added_sticker_file_ids: Vector[Int32]
    duration: Double
    is_animation: Bool = False


InputStoryContent = typing.Union[
    InputStoryContentPhoto,
    InputStoryContentVideo,
]


class InputThumbnail(BaseObject):
    """
    A thumbnail to be sent along with a file; must be in JPEG or WEBP format for stickers, and less than 200 KB in size

    :param thumbnail: Thumbnail file to send. Sending thumbnails by file_id is currently not supported
    :type thumbnail: :class:`InputFile`
    :param width: Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown
    :type width: :class:`Int32`
    :param height: Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown
    :type height: :class:`Int32`
    """

    ID: typing.Literal["inputThumbnail"] = "inputThumbnail"
    thumbnail: InputFile
    width: Int32
    height: Int32


class InternalLinkTypeActiveSessions(BaseObject):
    """
    The link is a link to the active sessions section of the application. Use getActiveSessions to handle the link
    """

    ID: typing.Literal["internalLinkTypeActiveSessions"] = "internalLinkTypeActiveSessions"


class InternalLinkTypeAttachmentMenuBot(BaseObject):
    """
    The link is a link to an attachment menu bot to be opened in the specified or a chosen chat. Process given target_chat to open the chat. Then, call searchPublicChat with the given bot username, check that the user is a bot and can be added to attachment menu. Then, use getAttachmentMenuBot to receive information about the bot. If the bot isn't added to attachment menu, then show a disclaimer about Mini Apps being a third-party apps, ask the user to accept their Terms of service and confirm adding the bot to side and attachment menu. If the user accept the terms and confirms adding, then use toggleBotIsAddedToAttachmentMenu to add the bot. If the attachment menu bot can't be used in the opened chat, show an error to the user. If the bot is added to attachment menu and can be used in the chat, then use openWebApp with the given URL

    :param target_chat: Target chat to be opened
    :type target_chat: :class:`TargetChat`
    :param bot_username: Username of the bot
    :type bot_username: :class:`String`
    :param url: URL to be passed to openWebApp
    :type url: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeAttachmentMenuBot"] = "internalLinkTypeAttachmentMenuBot"
    target_chat: TargetChat
    bot_username: String
    url: String


class InternalLinkTypeAuthenticationCode(BaseObject):
    """
    The link contains an authentication code. Call checkAuthenticationCode with the code if the current authorization state is authorizationStateWaitCode

    :param code: The authentication code
    :type code: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeAuthenticationCode"] = "internalLinkTypeAuthenticationCode"
    code: String


class InternalLinkTypeBackground(BaseObject):
    """
    The link is a link to a background. Call searchBackground with the given background name to process the link

    :param background_name: Name of the background
    :type background_name: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeBackground"] = "internalLinkTypeBackground"
    background_name: String


class InternalLinkTypeBotAddToChannel(BaseObject):
    """
    The link is a link to a Telegram bot, which is supposed to be added to a channel chat as an administrator. Call searchPublicChat with the given bot username and check that the user is a bot, ask the current user to select a channel chat to add the bot to as an administrator. Then, call getChatMember to receive the current bot rights in the chat and if the bot already is an administrator, check that the current user can edit its administrator rights and combine received rights with the requested administrator rights. Then, show confirmation box to the user, and call setChatMemberStatus with the chosen chat and confirmed rights

    :param bot_username: Username of the bot
    :type bot_username: :class:`String`
    :param administrator_rights: Expected administrator rights for the bot
    :type administrator_rights: :class:`ChatAdministratorRights`
    """

    ID: typing.Literal["internalLinkTypeBotAddToChannel"] = "internalLinkTypeBotAddToChannel"
    bot_username: String
    administrator_rights: ChatAdministratorRights


class InternalLinkTypeBotStart(BaseObject):
    """
    The link is a link to a chat with a Telegram bot. Call searchPublicChat with the given bot username, check that the user is a bot, show START button in the chat with the bot, and then call sendBotStartMessage with the given start parameter after the button is pressed

    :param bot_username: Username of the bot
    :type bot_username: :class:`String`
    :param start_parameter: The parameter to be passed to sendBotStartMessage
    :type start_parameter: :class:`String`
    :param autostart: True, if sendBotStartMessage must be called automatically without showing the START button
    :type autostart: :class:`Bool`
    """

    ID: typing.Literal["internalLinkTypeBotStart"] = "internalLinkTypeBotStart"
    bot_username: String
    start_parameter: String
    autostart: Bool = False


class InternalLinkTypeBotStartInGroup(BaseObject):
    """
    The link is a link to a Telegram bot, which is supposed to be added to a group chat. Call searchPublicChat with the given bot username, check that the user is a bot and can be added to groups, ask the current user to select a basic group or a supergroup chat to add the bot to, taking into account that bots can be added to a public supergroup only by administrators of the supergroup. If administrator rights are provided by the link, call getChatMember to receive the current bot rights in the chat and if the bot already is an administrator, check that the current user can edit its administrator rights, combine received rights with the requested administrator rights, show confirmation box to the user, and call setChatMemberStatus with the chosen chat and confirmed administrator rights. Before call to setChatMemberStatus it may be required to upgrade the chosen basic group chat to a supergroup chat. Then, if start_parameter isn't empty, call sendBotStartMessage with the given start parameter and the chosen chat; otherwise, just send /start message with bot's username added to the chat.

    :param bot_username: Username of the bot
    :type bot_username: :class:`String`
    :param start_parameter: The parameter to be passed to sendBotStartMessage
    :type start_parameter: :class:`String`
    :param administrator_rights: Expected administrator rights for the bot; may be null, defaults to None
    :type administrator_rights: :class:`ChatAdministratorRights`, optional
    """

    ID: typing.Literal["internalLinkTypeBotStartInGroup"] = "internalLinkTypeBotStartInGroup"
    bot_username: String
    start_parameter: String
    administrator_rights: typing.Optional[ChatAdministratorRights] = None


class InternalLinkTypeChangePhoneNumber(BaseObject):
    """
    The link is a link to the change phone number section of the app
    """

    ID: typing.Literal["internalLinkTypeChangePhoneNumber"] = "internalLinkTypeChangePhoneNumber"


class InternalLinkTypeChatFolderInvite(BaseObject):
    """
    The link is an invite link to a chat folder. Call checkChatFolderInviteLink with the given invite link to process the link

    :param invite_link: Internal representation of the invite link
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeChatFolderInvite"] = "internalLinkTypeChatFolderInvite"
    invite_link: String


class InternalLinkTypeChatFolderSettings(BaseObject):
    """
    The link is a link to the folder section of the app settings
    """

    ID: typing.Literal["internalLinkTypeChatFolderSettings"] = "internalLinkTypeChatFolderSettings"


class InternalLinkTypeChatInvite(BaseObject):
    """
    The link is a chat invite link. Call checkChatInviteLink with the given invite link to process the link

    :param invite_link: Internal representation of the invite link
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeChatInvite"] = "internalLinkTypeChatInvite"
    invite_link: String


class InternalLinkTypeDefaultMessageAutoDeleteTimerSettings(BaseObject):
    """
    The link is a link to the default message auto-delete timer settings section of the app settings
    """

    ID: typing.Literal[
        "internalLinkTypeDefaultMessageAutoDeleteTimerSettings"
    ] = "internalLinkTypeDefaultMessageAutoDeleteTimerSettings"


class InternalLinkTypeEditProfileSettings(BaseObject):
    """
    The link is a link to the edit profile section of the app settings
    """

    ID: typing.Literal["internalLinkTypeEditProfileSettings"] = "internalLinkTypeEditProfileSettings"


class InternalLinkTypeGame(BaseObject):
    """
    The link is a link to a game. Call searchPublicChat with the given bot username, check that the user is a bot, ask the current user to select a chat to send the game, and then call sendMessage with inputMessageGame

    :param bot_username: Username of the bot that owns the game
    :type bot_username: :class:`String`
    :param game_short_name: Short name of the game
    :type game_short_name: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeGame"] = "internalLinkTypeGame"
    bot_username: String
    game_short_name: String


class InternalLinkTypeInstantView(BaseObject):
    """
    The link must be opened in an Instant View. Call getWebPageInstantView with the given URL to process the link

    :param url: URL to be passed to getWebPageInstantView
    :type url: :class:`String`
    :param fallback_url: An URL to open if getWebPageInstantView fails
    :type fallback_url: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeInstantView"] = "internalLinkTypeInstantView"
    url: String
    fallback_url: String


class InternalLinkTypeInvoice(BaseObject):
    """
    The link is a link to an invoice. Call getPaymentForm with the given invoice name to process the link

    :param invoice_name: Name of the invoice
    :type invoice_name: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeInvoice"] = "internalLinkTypeInvoice"
    invoice_name: String


class InternalLinkTypeLanguagePack(BaseObject):
    """
    The link is a link to a language pack. Call getLanguagePackInfo with the given language pack identifier to process the link

    :param language_pack_id: Language pack identifier
    :type language_pack_id: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeLanguagePack"] = "internalLinkTypeLanguagePack"
    language_pack_id: String


class InternalLinkTypeLanguageSettings(BaseObject):
    """
    The link is a link to the language section of the app settings
    """

    ID: typing.Literal["internalLinkTypeLanguageSettings"] = "internalLinkTypeLanguageSettings"


class InternalLinkTypeMessage(BaseObject):
    """
    The link is a link to a Telegram message or a forum topic. Call getMessageLinkInfo with the given URL to process the link

    :param url: URL to be passed to getMessageLinkInfo
    :type url: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeMessage"] = "internalLinkTypeMessage"
    url: String


class InternalLinkTypeMessageDraft(BaseObject):
    """
    The link contains a message draft text. A share screen needs to be shown to the user, then the chosen chat must be opened and the text is added to the input field

    :param text: Message draft text
    :type text: :class:`FormattedText`
    :param contains_link: True, if the first line of the text contains a link. If true, the input field needs to be focused and the text after the link must be selected
    :type contains_link: :class:`Bool`
    """

    ID: typing.Literal["internalLinkTypeMessageDraft"] = "internalLinkTypeMessageDraft"
    text: FormattedText
    contains_link: Bool = False


class InternalLinkTypePassportDataRequest(BaseObject):
    """
    The link contains a request of Telegram passport data. Call getPassportAuthorizationForm with the given parameters to process the link if the link was received from outside of the application; otherwise, ignore it

    :param bot_user_id: User identifier of the service's bot
    :type bot_user_id: :class:`Int53`
    :param scope: Telegram Passport element types requested by the service
    :type scope: :class:`String`
    :param public_key: Service's public key
    :type public_key: :class:`String`
    :param nonce: Unique request identifier provided by the service
    :type nonce: :class:`String`
    :param callback_url: An HTTP URL to open once the request is finished, canceled, or failed with the parameters tg_passport=success, tg_passport=cancel, or tg_passport=error&error=... respectively. If empty, then onActivityResult method must be used to return response on Android, or the link tgbot{bot_user_id}://passport/success or tgbot{bot_user_id}://passport/cancel must be opened otherwise
    :type callback_url: :class:`String`
    """

    ID: typing.Literal["internalLinkTypePassportDataRequest"] = "internalLinkTypePassportDataRequest"
    bot_user_id: Int53
    scope: String
    public_key: String
    nonce: String
    callback_url: String


class InternalLinkTypePhoneNumberConfirmation(BaseObject):
    """
    The link can be used to confirm ownership of a phone number to prevent account deletion. Call sendPhoneNumberConfirmationCode with the given hash and phone number to process the link

    :param hash_: Hash value from the link
    :type hash_: :class:`String`
    :param phone_number: Phone number value from the link
    :type phone_number: :class:`String`
    """

    ID: typing.Literal["internalLinkTypePhoneNumberConfirmation"] = "internalLinkTypePhoneNumberConfirmation"
    hash_: String = Field(..., alias="hash")
    phone_number: String


class InternalLinkTypePremiumFeatures(BaseObject):
    """
    The link is a link to the Premium features screen of the application from which the user can subscribe to Telegram Premium. Call getPremiumFeatures with the given referrer to process the link

    :param referrer: Referrer specified in the link
    :type referrer: :class:`String`
    """

    ID: typing.Literal["internalLinkTypePremiumFeatures"] = "internalLinkTypePremiumFeatures"
    referrer: String


class InternalLinkTypePrivacyAndSecuritySettings(BaseObject):
    """
    The link is a link to the privacy and security section of the app settings
    """

    ID: typing.Literal["internalLinkTypePrivacyAndSecuritySettings"] = "internalLinkTypePrivacyAndSecuritySettings"


class InternalLinkTypeProxy(BaseObject):
    """
    The link is a link to a proxy. Call addProxy with the given parameters to process the link and add the proxy

    :param server: Proxy server domain or IP address
    :type server: :class:`String`
    :param port: Proxy server port
    :type port: :class:`Int32`
    :param type_: Type of the proxy
    :type type_: :class:`ProxyType`
    """

    ID: typing.Literal["internalLinkTypeProxy"] = "internalLinkTypeProxy"
    server: String
    port: Int32
    type_: ProxyType = Field(..., alias="type")


class InternalLinkTypePublicChat(BaseObject):
    """
    The link is a link to a chat by its username. Call searchPublicChat with the given chat username to process the link

    :param chat_username: Username of the chat
    :type chat_username: :class:`String`
    """

    ID: typing.Literal["internalLinkTypePublicChat"] = "internalLinkTypePublicChat"
    chat_username: String


class InternalLinkTypeQrCodeAuthentication(BaseObject):
    """
    The link can be used to login the current user on another device, but it must be scanned from QR-code using in-app camera. An alert similar to "This code can be used to allow someone to log in to your Telegram account. To confirm Telegram login, please go to Settings > Devices > Scan QR and scan the code" needs to be shown
    """

    ID: typing.Literal["internalLinkTypeQrCodeAuthentication"] = "internalLinkTypeQrCodeAuthentication"


class InternalLinkTypeRestorePurchases(BaseObject):
    """
    The link forces restore of App Store purchases when opened. For official iOS application only
    """

    ID: typing.Literal["internalLinkTypeRestorePurchases"] = "internalLinkTypeRestorePurchases"


class InternalLinkTypeSettings(BaseObject):
    """
    The link is a link to application settings
    """

    ID: typing.Literal["internalLinkTypeSettings"] = "internalLinkTypeSettings"


class InternalLinkTypeSideMenuBot(BaseObject):
    """
    The link is a link to a bot, which can be installed to the side menu. Call searchPublicChat with the given bot username, check that the user is a bot and can be added to attachment menu. Then, use getAttachmentMenuBot to receive information about the bot. If the bot isn't added to side menu, then show a disclaimer about Mini Apps being a third-party apps, ask the user to accept their Terms of service and confirm adding the bot to side and attachment menu. If the user accept the terms and confirms adding, then use toggleBotIsAddedToAttachmentMenu to add the bot. If the bot is added to side menu, then use getWebAppUrl with the given URL

    :param bot_username: Username of the bot
    :type bot_username: :class:`String`
    :param url: URL to be passed to getWebAppUrl
    :type url: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeSideMenuBot"] = "internalLinkTypeSideMenuBot"
    bot_username: String
    url: String


class InternalLinkTypeStickerSet(BaseObject):
    """
    The link is a link to a sticker set. Call searchStickerSet with the given sticker set name to process the link and show the sticker set

    :param sticker_set_name: Name of the sticker set
    :type sticker_set_name: :class:`String`
    :param expect_custom_emoji: True, if the sticker set is expected to contain custom emoji
    :type expect_custom_emoji: :class:`Bool`
    """

    ID: typing.Literal["internalLinkTypeStickerSet"] = "internalLinkTypeStickerSet"
    sticker_set_name: String
    expect_custom_emoji: Bool = False


class InternalLinkTypeStory(BaseObject):
    """
    The link is a link to a story. Call searchPublicChat with the given sender username, then call getStory with the received chat identifier and the given story identifier

    :param story_sender_username: Username of the sender of the story
    :type story_sender_username: :class:`String`
    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["internalLinkTypeStory"] = "internalLinkTypeStory"
    story_sender_username: String
    story_id: Int32


class InternalLinkTypeTheme(BaseObject):
    """
    The link is a link to a theme. TDLib has no theme support yet

    :param theme_name: Name of the theme
    :type theme_name: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeTheme"] = "internalLinkTypeTheme"
    theme_name: String


class InternalLinkTypeThemeSettings(BaseObject):
    """
    The link is a link to the theme section of the app settings
    """

    ID: typing.Literal["internalLinkTypeThemeSettings"] = "internalLinkTypeThemeSettings"


class InternalLinkTypeUnknownDeepLink(BaseObject):
    """
    The link is an unknown tg: link. Call getDeepLinkInfo to process the link

    :param link: Link to be passed to getDeepLinkInfo
    :type link: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeUnknownDeepLink"] = "internalLinkTypeUnknownDeepLink"
    link: String


class InternalLinkTypeUnsupportedProxy(BaseObject):
    """
    The link is a link to an unsupported proxy. An alert can be shown to the user
    """

    ID: typing.Literal["internalLinkTypeUnsupportedProxy"] = "internalLinkTypeUnsupportedProxy"


class InternalLinkTypeUserPhoneNumber(BaseObject):
    """
    The link is a link to a user by its phone number. Call searchUserByPhoneNumber with the given phone number to process the link

    :param phone_number: Phone number of the user
    :type phone_number: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeUserPhoneNumber"] = "internalLinkTypeUserPhoneNumber"
    phone_number: String


class InternalLinkTypeUserToken(BaseObject):
    """
    The link is a link to a user by a temporary token. Call searchUserByToken with the given token to process the link

    :param token: The token
    :type token: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeUserToken"] = "internalLinkTypeUserToken"
    token: String


class InternalLinkTypeVideoChat(BaseObject):
    """
    The link is a link to a video chat. Call searchPublicChat with the given chat username, and then joinGroupCall with the given invite hash to process the link

    :param chat_username: Username of the chat with the video chat
    :type chat_username: :class:`String`
    :param invite_hash: If non-empty, invite hash to be used to join the video chat without being muted by administrators
    :type invite_hash: :class:`String`
    :param is_live_stream: True, if the video chat is expected to be a live stream in a channel or a broadcast group
    :type is_live_stream: :class:`Bool`
    """

    ID: typing.Literal["internalLinkTypeVideoChat"] = "internalLinkTypeVideoChat"
    chat_username: String
    invite_hash: String
    is_live_stream: Bool = False


class InternalLinkTypeWebApp(BaseObject):
    """
    The link is a link to a Web App. Call searchPublicChat with the given bot username, check that the user is a bot, then call searchWebApp with the received bot and the given web_app_short_name. Process received foundWebApp by showing a confirmation dialog if needed. If the bot can be added to attachment or side menu, but isn't added yet, then show a disclaimer about Mini Apps being a third-party apps instead of the dialog and ask the user to accept their Terms of service. If the user accept the terms and confirms adding, then use toggleBotIsAddedToAttachmentMenu to add the bot. Then call getWebAppLinkUrl and open the returned URL as a Web App

    :param bot_username: Username of the bot that owns the Web App
    :type bot_username: :class:`String`
    :param web_app_short_name: Short name of the Web App
    :type web_app_short_name: :class:`String`
    :param start_parameter: Start parameter to be passed to getWebAppLinkUrl
    :type start_parameter: :class:`String`
    """

    ID: typing.Literal["internalLinkTypeWebApp"] = "internalLinkTypeWebApp"
    bot_username: String
    web_app_short_name: String
    start_parameter: String


InternalLinkType = typing.Union[
    InternalLinkTypeActiveSessions,
    InternalLinkTypeAttachmentMenuBot,
    InternalLinkTypeAuthenticationCode,
    InternalLinkTypeBackground,
    InternalLinkTypeBotAddToChannel,
    InternalLinkTypeBotStart,
    InternalLinkTypeBotStartInGroup,
    InternalLinkTypeChangePhoneNumber,
    InternalLinkTypeChatFolderInvite,
    InternalLinkTypeChatFolderSettings,
    InternalLinkTypeChatInvite,
    InternalLinkTypeDefaultMessageAutoDeleteTimerSettings,
    InternalLinkTypeEditProfileSettings,
    InternalLinkTypeGame,
    InternalLinkTypeInstantView,
    InternalLinkTypeInvoice,
    InternalLinkTypeLanguagePack,
    InternalLinkTypeLanguageSettings,
    InternalLinkTypeMessage,
    InternalLinkTypeMessageDraft,
    InternalLinkTypePassportDataRequest,
    InternalLinkTypePhoneNumberConfirmation,
    InternalLinkTypePremiumFeatures,
    InternalLinkTypePrivacyAndSecuritySettings,
    InternalLinkTypeProxy,
    InternalLinkTypePublicChat,
    InternalLinkTypeQrCodeAuthentication,
    InternalLinkTypeRestorePurchases,
    InternalLinkTypeSettings,
    InternalLinkTypeSideMenuBot,
    InternalLinkTypeStickerSet,
    InternalLinkTypeStory,
    InternalLinkTypeTheme,
    InternalLinkTypeThemeSettings,
    InternalLinkTypeUnknownDeepLink,
    InternalLinkTypeUnsupportedProxy,
    InternalLinkTypeUserPhoneNumber,
    InternalLinkTypeUserToken,
    InternalLinkTypeVideoChat,
    InternalLinkTypeWebApp,
]


class InviteLinkChatTypeBasicGroup(BaseObject):
    """
    The link is an invite link for a basic group
    """

    ID: typing.Literal["inviteLinkChatTypeBasicGroup"] = "inviteLinkChatTypeBasicGroup"


class InviteLinkChatTypeChannel(BaseObject):
    """
    The link is an invite link for a channel
    """

    ID: typing.Literal["inviteLinkChatTypeChannel"] = "inviteLinkChatTypeChannel"


class InviteLinkChatTypeSupergroup(BaseObject):
    """
    The link is an invite link for a supergroup
    """

    ID: typing.Literal["inviteLinkChatTypeSupergroup"] = "inviteLinkChatTypeSupergroup"


InviteLinkChatType = typing.Union[
    InviteLinkChatTypeBasicGroup,
    InviteLinkChatTypeChannel,
    InviteLinkChatTypeSupergroup,
]


class Invoice(BaseObject):
    """
    Product invoice

    :param currency: ISO 4217 currency code
    :type currency: :class:`String`
    :param price_parts: A list of objects used to calculate the total price of the product
    :type price_parts: :class:`Vector[LabeledPricePart]`
    :param max_tip_amount: The maximum allowed amount of tip in the smallest units of the currency
    :type max_tip_amount: :class:`Int53`
    :param suggested_tip_amounts: Suggested amounts of tip in the smallest units of the currency
    :type suggested_tip_amounts: :class:`Vector[Int53]`
    :param recurring_payment_terms_of_service_url: An HTTP URL with terms of service for recurring payments. If non-empty, the invoice payment will result in recurring payments and the user must accept the terms of service before allowed to pay
    :type recurring_payment_terms_of_service_url: :class:`String`
    :param is_test: True, if the payment is a test payment
    :type is_test: :class:`Bool`
    :param need_name: True, if the user's name is needed for payment
    :type need_name: :class:`Bool`
    :param need_phone_number: True, if the user's phone number is needed for payment
    :type need_phone_number: :class:`Bool`
    :param need_email_address: True, if the user's email address is needed for payment
    :type need_email_address: :class:`Bool`
    :param need_shipping_address: True, if the user's shipping address is needed for payment
    :type need_shipping_address: :class:`Bool`
    :param send_phone_number_to_provider: True, if the user's phone number will be sent to the provider
    :type send_phone_number_to_provider: :class:`Bool`
    :param send_email_address_to_provider: True, if the user's email address will be sent to the provider
    :type send_email_address_to_provider: :class:`Bool`
    :param is_flexible: True, if the total price depends on the shipping method
    :type is_flexible: :class:`Bool`
    """

    ID: typing.Literal["invoice"] = "invoice"
    currency: String
    price_parts: Vector[LabeledPricePart]
    max_tip_amount: Int53
    suggested_tip_amounts: Vector[Int53]
    recurring_payment_terms_of_service_url: String
    is_test: Bool = False
    need_name: Bool = False
    need_phone_number: Bool = False
    need_email_address: Bool = False
    need_shipping_address: Bool = False
    send_phone_number_to_provider: Bool = False
    send_email_address_to_provider: Bool = False
    is_flexible: Bool = False


class JsonValueArray(BaseObject):
    """
    Represents a JSON array

    :param values: The list of array elements
    :type values: :class:`Vector[JsonValue]`
    """

    ID: typing.Literal["jsonValueArray"] = "jsonValueArray"
    values: Vector[JsonValue]


class JsonValueBoolean(BaseObject):
    """
    Represents a boolean JSON value

    :param value: The value
    :type value: :class:`Bool`
    """

    ID: typing.Literal["jsonValueBoolean"] = "jsonValueBoolean"
    value: Bool


class JsonValueNull(BaseObject):
    """
    Represents a null JSON value
    """

    ID: typing.Literal["jsonValueNull"] = "jsonValueNull"


class JsonValueNumber(BaseObject):
    """
    Represents a numeric JSON value

    :param value: The value
    :type value: :class:`Double`
    """

    ID: typing.Literal["jsonValueNumber"] = "jsonValueNumber"
    value: Double


class JsonValueObject(BaseObject):
    """
    Represents a JSON object

    :param members: The list of object members
    :type members: :class:`Vector[JsonObjectMember]`
    """

    ID: typing.Literal["jsonValueObject"] = "jsonValueObject"
    members: Vector[JsonObjectMember]


class JsonValueString(BaseObject):
    """
    Represents a string JSON value

    :param value: The value
    :type value: :class:`String`
    """

    ID: typing.Literal["jsonValueString"] = "jsonValueString"
    value: String


JsonValue = typing.Union[
    JsonValueArray,
    JsonValueBoolean,
    JsonValueNull,
    JsonValueNumber,
    JsonValueObject,
    JsonValueString,
]


class JsonObjectMember(BaseObject):
    """
    Represents one member of a JSON object

    :param key: Member's key
    :type key: :class:`String`
    :param value: Member's value
    :type value: :class:`JsonValue`
    """

    ID: typing.Literal["jsonObjectMember"] = "jsonObjectMember"
    key: String
    value: JsonValue


class KeyboardButton(BaseObject):
    """
    Represents a single button in a bot keyboard

    :param text: Text of the button
    :type text: :class:`String`
    :param type_: Type of the button
    :type type_: :class:`KeyboardButtonType`
    """

    ID: typing.Literal["keyboardButton"] = "keyboardButton"
    text: String
    type_: KeyboardButtonType = Field(..., alias="type")


class KeyboardButtonTypeRequestChat(BaseObject):
    """
    A button that requests a chat to be shared by the current user; available only in private chats. Use the method shareChatWithBot to complete the request

    :param id: Unique button identifier
    :type id: :class:`Int32`
    :param user_administrator_rights: Expected user administrator rights in the chat; may be null if they aren't restricted, defaults to None
    :type user_administrator_rights: :class:`ChatAdministratorRights`, optional
    :param bot_administrator_rights: Expected bot administrator rights in the chat; may be null if they aren't restricted, defaults to None
    :type bot_administrator_rights: :class:`ChatAdministratorRights`, optional
    :param chat_is_channel: True, if the chat must be a channel; otherwise, a basic group or a supergroup chat is shared
    :type chat_is_channel: :class:`Bool`
    :param restrict_chat_is_forum: True, if the chat must or must not be a forum supergroup
    :type restrict_chat_is_forum: :class:`Bool`
    :param chat_is_forum: True, if the chat must be a forum supergroup; otherwise, the chat must not be a forum supergroup. Ignored if restrict_chat_is_forum is false
    :type chat_is_forum: :class:`Bool`
    :param restrict_chat_has_username: True, if the chat must or must not have a username
    :type restrict_chat_has_username: :class:`Bool`
    :param chat_has_username: True, if the chat must have a username; otherwise, the chat must not have a username. Ignored if restrict_chat_has_username is false
    :type chat_has_username: :class:`Bool`
    :param chat_is_created: True, if the chat must be created by the current user
    :type chat_is_created: :class:`Bool`
    :param bot_is_member: True, if the bot must be a member of the chat; for basic group and supergroup chats only
    :type bot_is_member: :class:`Bool`
    """

    ID: typing.Literal["keyboardButtonTypeRequestChat"] = "keyboardButtonTypeRequestChat"
    id: Int32
    user_administrator_rights: typing.Optional[ChatAdministratorRights] = None
    bot_administrator_rights: typing.Optional[ChatAdministratorRights] = None
    chat_is_channel: Bool = False
    restrict_chat_is_forum: Bool = False
    chat_is_forum: Bool = False
    restrict_chat_has_username: Bool = False
    chat_has_username: Bool = False
    chat_is_created: Bool = False
    bot_is_member: Bool = False


class KeyboardButtonTypeRequestLocation(BaseObject):
    """
    A button that sends the user's location when pressed; available only in private chats
    """

    ID: typing.Literal["keyboardButtonTypeRequestLocation"] = "keyboardButtonTypeRequestLocation"


class KeyboardButtonTypeRequestPhoneNumber(BaseObject):
    """
    A button that sends the user's phone number when pressed; available only in private chats
    """

    ID: typing.Literal["keyboardButtonTypeRequestPhoneNumber"] = "keyboardButtonTypeRequestPhoneNumber"


class KeyboardButtonTypeRequestPoll(BaseObject):
    """
    A button that allows the user to create and send a poll when pressed; available only in private chats

    :param force_regular: If true, only regular polls must be allowed to create
    :type force_regular: :class:`Bool`
    :param force_quiz: If true, only polls in quiz mode must be allowed to create
    :type force_quiz: :class:`Bool`
    """

    ID: typing.Literal["keyboardButtonTypeRequestPoll"] = "keyboardButtonTypeRequestPoll"
    force_regular: Bool
    force_quiz: Bool


class KeyboardButtonTypeRequestUser(BaseObject):
    """
    A button that requests a user to be shared by the current user; available only in private chats. Use the method shareUserWithBot to complete the request

    :param id: Unique button identifier
    :type id: :class:`Int32`
    :param restrict_user_is_bot: True, if the shared user must or must not be a bot
    :type restrict_user_is_bot: :class:`Bool`
    :param user_is_bot: True, if the shared user must be a bot; otherwise, the shared user must no be a bot. Ignored if restrict_user_is_bot is false
    :type user_is_bot: :class:`Bool`
    :param restrict_user_is_premium: True, if the shared user must or must not be a Telegram Premium user
    :type restrict_user_is_premium: :class:`Bool`
    :param user_is_premium: True, if the shared user must be a Telegram Premium user; otherwise, the shared user must no be a Telegram Premium user. Ignored if restrict_user_is_premium is false
    :type user_is_premium: :class:`Bool`
    """

    ID: typing.Literal["keyboardButtonTypeRequestUser"] = "keyboardButtonTypeRequestUser"
    id: Int32
    restrict_user_is_bot: Bool = False
    user_is_bot: Bool = False
    restrict_user_is_premium: Bool = False
    user_is_premium: Bool = False


class KeyboardButtonTypeText(BaseObject):
    """
    A simple button, with text that must be sent when the button is pressed
    """

    ID: typing.Literal["keyboardButtonTypeText"] = "keyboardButtonTypeText"


class KeyboardButtonTypeWebApp(BaseObject):
    """
    A button that opens a Web App by calling getWebAppUrl

    :param url: An HTTP URL to pass to getWebAppUrl
    :type url: :class:`String`
    """

    ID: typing.Literal["keyboardButtonTypeWebApp"] = "keyboardButtonTypeWebApp"
    url: String


KeyboardButtonType = typing.Union[
    KeyboardButtonTypeRequestChat,
    KeyboardButtonTypeRequestLocation,
    KeyboardButtonTypeRequestPhoneNumber,
    KeyboardButtonTypeRequestPoll,
    KeyboardButtonTypeRequestUser,
    KeyboardButtonTypeText,
    KeyboardButtonTypeWebApp,
]


class LabeledPricePart(BaseObject):
    """
    Portion of the price of a product (e.g., "delivery cost", "tax amount")

    :param label: Label for this portion of the product price
    :type label: :class:`String`
    :param amount: Currency amount in the smallest units of the currency
    :type amount: :class:`Int53`
    """

    ID: typing.Literal["labeledPricePart"] = "labeledPricePart"
    label: String
    amount: Int53


class LanguagePackInfo(BaseObject):
    """
    Contains information about a language pack

    :param id: Unique language pack identifier
    :type id: :class:`String`
    :param name: Language name
    :type name: :class:`String`
    :param native_name: Name of the language in that language
    :type native_name: :class:`String`
    :param plural_code: A language code to be used to apply plural forms. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more information
    :type plural_code: :class:`String`
    :param total_string_count: Total number of non-deleted strings from the language pack
    :type total_string_count: :class:`Int32`
    :param translated_string_count: Total number of translated strings from the language pack
    :type translated_string_count: :class:`Int32`
    :param local_string_count: Total number of non-deleted strings from the language pack available locally
    :type local_string_count: :class:`Int32`
    :param translation_url: Link to language translation interface; empty for custom local language packs
    :type translation_url: :class:`String`
    :param base_language_pack_id: Identifier of a base language pack; may be empty. If a string is missed in the language pack, then it must be fetched from base language pack. Unsupported in custom language packs
    :type base_language_pack_id: :class:`String`
    :param is_official: True, if the language pack is official
    :type is_official: :class:`Bool`
    :param is_rtl: True, if the language pack strings are RTL
    :type is_rtl: :class:`Bool`
    :param is_beta: True, if the language pack is a beta language pack
    :type is_beta: :class:`Bool`
    :param is_installed: True, if the language pack is installed by the current user
    :type is_installed: :class:`Bool`
    """

    ID: typing.Literal["languagePackInfo"] = "languagePackInfo"
    id: String
    name: String
    native_name: String
    plural_code: String
    total_string_count: Int32
    translated_string_count: Int32
    local_string_count: Int32
    translation_url: String
    base_language_pack_id: String = ""
    is_official: Bool = False
    is_rtl: Bool = False
    is_beta: Bool = False
    is_installed: Bool = False


class LanguagePackString(BaseObject):
    """
    Represents one language pack string

    :param key: String key
    :type key: :class:`String`
    :param value: String value; pass null if the string needs to be taken from the built-in English language pack, defaults to None
    :type value: :class:`LanguagePackStringValue`, optional
    """

    ID: typing.Literal["languagePackString"] = "languagePackString"
    key: String
    value: typing.Optional[LanguagePackStringValue] = None


class LanguagePackStringValueDeleted(BaseObject):
    """
    A deleted language pack string, the value must be taken from the built-in English language pack
    """

    ID: typing.Literal["languagePackStringValueDeleted"] = "languagePackStringValueDeleted"


class LanguagePackStringValueOrdinary(BaseObject):
    """
    An ordinary language pack string

    :param value: String value
    :type value: :class:`String`
    """

    ID: typing.Literal["languagePackStringValueOrdinary"] = "languagePackStringValueOrdinary"
    value: String


class LanguagePackStringValuePluralized(BaseObject):
    """
    A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more information

    :param zero_value: Value for zero objects
    :type zero_value: :class:`String`
    :param one_value: Value for one object
    :type one_value: :class:`String`
    :param two_value: Value for two objects
    :type two_value: :class:`String`
    :param few_value: Value for few objects
    :type few_value: :class:`String`
    :param many_value: Value for many objects
    :type many_value: :class:`String`
    :param other_value: Default value
    :type other_value: :class:`String`
    """

    ID: typing.Literal["languagePackStringValuePluralized"] = "languagePackStringValuePluralized"
    zero_value: String
    one_value: String
    two_value: String
    few_value: String
    many_value: String
    other_value: String


LanguagePackStringValue = typing.Union[
    LanguagePackStringValueDeleted,
    LanguagePackStringValueOrdinary,
    LanguagePackStringValuePluralized,
]


class LanguagePackStrings(BaseObject):
    """
    Contains a list of language pack strings

    :param strings: A list of language pack strings
    :type strings: :class:`Vector[LanguagePackString]`
    """

    ID: typing.Literal["languagePackStrings"] = "languagePackStrings"
    strings: Vector[LanguagePackString]


class LocalFile(BaseObject):
    """
    Represents a local file

    :param download_offset: Download will be started from this offset. downloaded_prefix_size is calculated from this offset
    :type download_offset: :class:`Int53`
    :param downloaded_prefix_size: If is_downloading_completed is false, then only some prefix of the file starting from download_offset is ready to be read. downloaded_prefix_size is the size of that prefix in bytes
    :type downloaded_prefix_size: :class:`Int53`
    :param downloaded_size: Total downloaded file size, in bytes. Can be used only for calculating download progress. The actual file size may be bigger, and some parts of it may contain garbage
    :type downloaded_size: :class:`Int53`
    :param path: Local path to the locally available file part; may be empty
    :type path: :class:`String`
    :param can_be_downloaded: True, if it is possible to download or generate the file
    :type can_be_downloaded: :class:`Bool`
    :param can_be_deleted: True, if the file can be deleted
    :type can_be_deleted: :class:`Bool`
    :param is_downloading_active: True, if the file is currently being downloaded (or a local copy is being generated by some other means)
    :type is_downloading_active: :class:`Bool`
    :param is_downloading_completed: True, if the local copy is fully available
    :type is_downloading_completed: :class:`Bool`
    """

    ID: typing.Literal["localFile"] = "localFile"
    download_offset: Int53
    downloaded_prefix_size: Int53
    downloaded_size: Int53
    path: String = ""
    can_be_downloaded: Bool = False
    can_be_deleted: Bool = False
    is_downloading_active: Bool = False
    is_downloading_completed: Bool = False


class LocalizationTargetInfo(BaseObject):
    """
    Contains information about the current localization target

    :param language_packs: List of available language packs for this application
    :type language_packs: :class:`Vector[LanguagePackInfo]`
    """

    ID: typing.Literal["localizationTargetInfo"] = "localizationTargetInfo"
    language_packs: Vector[LanguagePackInfo]


class Location(BaseObject):
    """
    Describes a location on planet Earth

    :param latitude: Latitude of the location in degrees; as defined by the sender
    :type latitude: :class:`Double`
    :param longitude: Longitude of the location, in degrees; as defined by the sender
    :type longitude: :class:`Double`
    :param horizontal_accuracy: The estimated horizontal accuracy of the location, in meters; as defined by the sender. 0 if unknown
    :type horizontal_accuracy: :class:`Double`
    """

    ID: typing.Literal["location"] = "location"
    latitude: Double
    longitude: Double
    horizontal_accuracy: Double


class LogStreamDefault(BaseObject):
    """
    The log is written to stderr or an OS specific log
    """

    ID: typing.Literal["logStreamDefault"] = "logStreamDefault"


class LogStreamEmpty(BaseObject):
    """
    The log is written nowhere
    """

    ID: typing.Literal["logStreamEmpty"] = "logStreamEmpty"


class LogStreamFile(BaseObject):
    """
    The log is written to a file

    :param path: Path to the file to where the internal TDLib log will be written
    :type path: :class:`String`
    :param max_file_size: The maximum size of the file to where the internal TDLib log is written before the file will automatically be rotated, in bytes
    :type max_file_size: :class:`Int53`
    :param redirect_stderr: Pass true to additionally redirect stderr to the log file. Ignored on Windows
    :type redirect_stderr: :class:`Bool`
    """

    ID: typing.Literal["logStreamFile"] = "logStreamFile"
    path: String
    max_file_size: Int53
    redirect_stderr: Bool = False


LogStream = typing.Union[
    LogStreamDefault,
    LogStreamEmpty,
    LogStreamFile,
]


class LogTags(BaseObject):
    """
    Contains a list of available TDLib internal log tags

    :param tags: List of log tags
    :type tags: :class:`Vector[String]`
    """

    ID: typing.Literal["logTags"] = "logTags"
    tags: Vector[String]


class LogVerbosityLevel(BaseObject):
    """
    Contains a TDLib internal log verbosity level

    :param verbosity_level: Log verbosity level
    :type verbosity_level: :class:`Int32`
    """

    ID: typing.Literal["logVerbosityLevel"] = "logVerbosityLevel"
    verbosity_level: Int32


class LoginUrlInfoOpen(BaseObject):
    """
    An HTTP URL needs to be open

    :param url: The URL to open
    :type url: :class:`String`
    :param skip_confirmation: True, if there is no need to show an ordinary open URL confirmation
    :type skip_confirmation: :class:`Bool`
    """

    ID: typing.Literal["loginUrlInfoOpen"] = "loginUrlInfoOpen"
    url: String
    skip_confirmation: Bool = False


class LoginUrlInfoRequestConfirmation(BaseObject):
    """
    An authorization confirmation dialog needs to be shown to the user

    :param url: An HTTP URL to be opened
    :type url: :class:`String`
    :param domain: A domain of the URL
    :type domain: :class:`String`
    :param bot_user_id: User identifier of a bot linked with the website
    :type bot_user_id: :class:`Int53`
    :param request_write_access: True, if the user must be asked for the permission to the bot to send them messages
    :type request_write_access: :class:`Bool`
    """

    ID: typing.Literal["loginUrlInfoRequestConfirmation"] = "loginUrlInfoRequestConfirmation"
    url: String
    domain: String
    bot_user_id: Int53
    request_write_access: Bool = False


LoginUrlInfo = typing.Union[
    LoginUrlInfoOpen,
    LoginUrlInfoRequestConfirmation,
]


class MaskPointChin(BaseObject):
    """
    The mask is placed relatively to the chin
    """

    ID: typing.Literal["maskPointChin"] = "maskPointChin"


class MaskPointEyes(BaseObject):
    """
    The mask is placed relatively to the eyes
    """

    ID: typing.Literal["maskPointEyes"] = "maskPointEyes"


class MaskPointForehead(BaseObject):
    """
    The mask is placed relatively to the forehead
    """

    ID: typing.Literal["maskPointForehead"] = "maskPointForehead"


class MaskPointMouth(BaseObject):
    """
    The mask is placed relatively to the mouth
    """

    ID: typing.Literal["maskPointMouth"] = "maskPointMouth"


MaskPoint = typing.Union[
    MaskPointChin,
    MaskPointEyes,
    MaskPointForehead,
    MaskPointMouth,
]


class MaskPosition(BaseObject):
    """
    Position on a photo where a mask is placed

    :param point: Part of the face, relative to which the mask is placed
    :type point: :class:`MaskPoint`
    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)
    :type x_shift: :class:`Double`
    :param y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. (For example, 1.0 will place the mask just below the default mask position)
    :type y_shift: :class:`Double`
    :param scale: Mask scaling coefficient. (For example, 2.0 means a doubled size)
    :type scale: :class:`Double`
    """

    ID: typing.Literal["maskPosition"] = "maskPosition"
    point: MaskPoint
    x_shift: Double
    y_shift: Double
    scale: Double


class Message(BaseObject):
    """
    Describes a message

    :param id: Message identifier; unique for the chat to which the message belongs
    :type id: :class:`Int53`
    :param sender_id: Identifier of the sender of the message
    :type sender_id: :class:`MessageSender`
    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) when the message was sent
    :type date: :class:`Int32`
    :param edit_date: Point in time (Unix timestamp) when the message was last edited
    :type edit_date: :class:`Int32`
    :param unread_reactions: Information about unread reactions added to the message
    :type unread_reactions: :class:`Vector[UnreadReaction]`
    :param message_thread_id: If non-zero, the identifier of the message thread the message belongs to; unique within the chat to which the message belongs
    :type message_thread_id: :class:`Int53`
    :param self_destruct_in: Time left before the message self-destruct timer expires, in seconds; 0 if self-desctruction isn't scheduled yet
    :type self_destruct_in: :class:`Double`
    :param auto_delete_in: Time left before the message will be automatically deleted by message_auto_delete_time setting of the chat, in seconds; 0 if never
    :type auto_delete_in: :class:`Double`
    :param via_bot_user_id: If non-zero, the user identifier of the bot through which this message was sent
    :type via_bot_user_id: :class:`Int53`
    :param author_signature: For channel posts and anonymous group messages, optional author signature
    :type author_signature: :class:`String`
    :param media_album_id: Unique identifier of an album this message belongs to. Only audios, documents, photos and videos can be grouped together in albums
    :type media_album_id: :class:`Int64`
    :param restriction_reason: If non-empty, contains a human-readable description of the reason why access to this message must be restricted
    :type restriction_reason: :class:`String`
    :param content: Content of the message
    :type content: :class:`MessageContent`
    :param sending_state: The sending state of the message; may be null if the message isn't being sent and didn't fail to be sent, defaults to None
    :type sending_state: :class:`MessageSendingState`, optional
    :param scheduling_state: The scheduling state of the message; may be null if the message isn't scheduled, defaults to None
    :type scheduling_state: :class:`MessageSchedulingState`, optional
    :param forward_info: Information about the initial message sender; may be null if none or unknown, defaults to None
    :type forward_info: :class:`MessageForwardInfo`, optional
    :param interaction_info: Information about interactions with the message; may be null if none, defaults to None
    :type interaction_info: :class:`MessageInteractionInfo`, optional
    :param reply_to: Information about the message or the story this message is replying to; may be null if none, defaults to None
    :type reply_to: :class:`MessageReplyTo`, optional
    :param self_destruct_type: The message's self-destruct type; may be null if none, defaults to None
    :type self_destruct_type: :class:`MessageSelfDestructType`, optional
    :param reply_markup: Reply markup for the message; may be null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    :param is_outgoing: True, if the message is outgoing
    :type is_outgoing: :class:`Bool`
    :param is_pinned: True, if the message is pinned
    :type is_pinned: :class:`Bool`
    :param can_be_edited: True, if the message can be edited. For live location and poll messages this fields shows whether editMessageLiveLocation or stopPoll can be used with this message by the application
    :type can_be_edited: :class:`Bool`
    :param can_be_forwarded: True, if the message can be forwarded
    :type can_be_forwarded: :class:`Bool`
    :param can_be_saved: True, if content of the message can be saved locally or copied
    :type can_be_saved: :class:`Bool`
    :param can_be_deleted_only_for_self: True, if the message can be deleted only for the current user while other users will continue to see it
    :type can_be_deleted_only_for_self: :class:`Bool`
    :param can_be_deleted_for_all_users: True, if the message can be deleted for all users
    :type can_be_deleted_for_all_users: :class:`Bool`
    :param can_get_added_reactions: True, if the list of added reactions is available through getMessageAddedReactions
    :type can_get_added_reactions: :class:`Bool`
    :param can_get_statistics: True, if the message statistics are available through getMessageStatistics
    :type can_get_statistics: :class:`Bool`
    :param can_get_message_thread: True, if information about the message thread is available through getMessageThread and getMessageThreadHistory
    :type can_get_message_thread: :class:`Bool`
    :param can_get_viewers: True, if chat members already viewed the message can be received through getMessageViewers
    :type can_get_viewers: :class:`Bool`
    :param can_get_media_timestamp_links: True, if media timestamp links can be generated for media timestamp entities in the message text, caption or web page description through getMessageLink
    :type can_get_media_timestamp_links: :class:`Bool`
    :param can_report_reactions: True, if reactions on the message can be reported through reportMessageReactions
    :type can_report_reactions: :class:`Bool`
    :param has_timestamped_media: True, if media timestamp entities refers to a media in this message as opposed to a media in the replied message
    :type has_timestamped_media: :class:`Bool`
    :param is_channel_post: True, if the message is a channel post. All messages to channels are channel posts, all other messages are not channel posts
    :type is_channel_post: :class:`Bool`
    :param is_topic_message: True, if the message is a forum topic message
    :type is_topic_message: :class:`Bool`
    :param contains_unread_mention: True, if the message contains an unread mention for the current user
    :type contains_unread_mention: :class:`Bool`
    """

    ID: typing.Literal["message"] = "message"
    id: Int53
    sender_id: MessageSender
    chat_id: Int53
    date: Int32
    edit_date: Int32
    unread_reactions: Vector[UnreadReaction]
    message_thread_id: Int53
    self_destruct_in: Double
    auto_delete_in: Double
    via_bot_user_id: Int53
    author_signature: String
    media_album_id: Int64
    restriction_reason: String
    content: MessageContent
    sending_state: typing.Optional[MessageSendingState] = None
    scheduling_state: typing.Optional[MessageSchedulingState] = None
    forward_info: typing.Optional[MessageForwardInfo] = None
    interaction_info: typing.Optional[MessageInteractionInfo] = None
    reply_to: typing.Optional[MessageReplyTo] = None
    self_destruct_type: typing.Optional[MessageSelfDestructType] = None
    reply_markup: typing.Optional[ReplyMarkup] = None
    is_outgoing: Bool = False
    is_pinned: Bool = False
    can_be_edited: Bool = False
    can_be_forwarded: Bool = False
    can_be_saved: Bool = False
    can_be_deleted_only_for_self: Bool = False
    can_be_deleted_for_all_users: Bool = False
    can_get_added_reactions: Bool = False
    can_get_statistics: Bool = False
    can_get_message_thread: Bool = False
    can_get_viewers: Bool = False
    can_get_media_timestamp_links: Bool = False
    can_report_reactions: Bool = False
    has_timestamped_media: Bool = False
    is_channel_post: Bool = False
    is_topic_message: Bool = False
    contains_unread_mention: Bool = False


class MessageAutoDeleteTime(BaseObject):
    """
    Contains default auto-delete timer setting for new chats

    :param time: Message auto-delete time, in seconds. If 0, then messages aren't deleted automatically
    :type time: :class:`Int32`
    """

    ID: typing.Literal["messageAutoDeleteTime"] = "messageAutoDeleteTime"
    time: Int32 = 0


class MessageCalendar(BaseObject):
    """
    Contains information about found messages, split by days according to the option "utc_time_offset"

    :param total_count: Total number of found messages
    :type total_count: :class:`Int32`
    :param days: Information about messages sent
    :type days: :class:`Vector[MessageCalendarDay]`
    """

    ID: typing.Literal["messageCalendar"] = "messageCalendar"
    total_count: Int32
    days: Vector[MessageCalendarDay]


class MessageCalendarDay(BaseObject):
    """
    Contains information about found messages sent on a specific day

    :param total_count: Total number of found messages sent on the day
    :type total_count: :class:`Int32`
    :param message: First message sent on the day
    :type message: :class:`Message`
    """

    ID: typing.Literal["messageCalendarDay"] = "messageCalendarDay"
    total_count: Int32
    message: Message


class MessageAnimatedEmoji(BaseObject):
    """
    A message with an animated emoji

    :param animated_emoji: The animated emoji
    :type animated_emoji: :class:`AnimatedEmoji`
    :param emoji: The corresponding emoji
    :type emoji: :class:`String`
    """

    ID: typing.Literal["messageAnimatedEmoji"] = "messageAnimatedEmoji"
    animated_emoji: AnimatedEmoji
    emoji: String


class MessageAnimation(BaseObject):
    """
    An animation message (GIF-style).

    :param animation: The animation description
    :type animation: :class:`Animation`
    :param caption: Animation caption
    :type caption: :class:`FormattedText`
    :param has_spoiler: True, if the animation preview must be covered by a spoiler animation
    :type has_spoiler: :class:`Bool`
    :param is_secret: True, if the animation thumbnail must be blurred and the animation must be shown only while tapped
    :type is_secret: :class:`Bool`
    """

    ID: typing.Literal["messageAnimation"] = "messageAnimation"
    animation: Animation
    caption: FormattedText
    has_spoiler: Bool = False
    is_secret: Bool = False


class MessageAudio(BaseObject):
    """
    An audio message

    :param audio: The audio description
    :type audio: :class:`Audio`
    :param caption: Audio caption
    :type caption: :class:`FormattedText`
    """

    ID: typing.Literal["messageAudio"] = "messageAudio"
    audio: Audio
    caption: FormattedText


class MessageBasicGroupChatCreate(BaseObject):
    """
    A newly created basic group

    :param title: Title of the basic group
    :type title: :class:`String`
    :param member_user_ids: User identifiers of members in the basic group
    :type member_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["messageBasicGroupChatCreate"] = "messageBasicGroupChatCreate"
    title: String
    member_user_ids: Vector[Int53]


class MessageBotWriteAccessAllowed(BaseObject):
    """
    The user allowed the bot to send messages

    :param web_app: Information about the Web App, which requested the access; may be null if none or the Web App was opened from the attachment menu, defaults to None
    :type web_app: :class:`WebApp`, optional
    :param by_request: True, if user allowed the bot to send messages by an explicit call to allowBotToSendMessages
    :type by_request: :class:`Bool`
    """

    ID: typing.Literal["messageBotWriteAccessAllowed"] = "messageBotWriteAccessAllowed"
    web_app: typing.Optional[WebApp] = None
    by_request: Bool = False


class MessageCall(BaseObject):
    """
    A message with information about an ended call

    :param discard_reason: Reason why the call was discarded
    :type discard_reason: :class:`CallDiscardReason`
    :param duration: Call duration, in seconds
    :type duration: :class:`Int32`
    :param is_video: True, if the call was a video call
    :type is_video: :class:`Bool`
    """

    ID: typing.Literal["messageCall"] = "messageCall"
    discard_reason: CallDiscardReason
    duration: Int32
    is_video: Bool = False


class MessageChatAddMembers(BaseObject):
    """
    New chat members were added

    :param member_user_ids: User identifiers of the new members
    :type member_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["messageChatAddMembers"] = "messageChatAddMembers"
    member_user_ids: Vector[Int53]


class MessageChatChangePhoto(BaseObject):
    """
    An updated chat photo

    :param photo: New chat photo
    :type photo: :class:`ChatPhoto`
    """

    ID: typing.Literal["messageChatChangePhoto"] = "messageChatChangePhoto"
    photo: ChatPhoto


class MessageChatChangeTitle(BaseObject):
    """
    An updated chat title

    :param title: New chat title
    :type title: :class:`String`
    """

    ID: typing.Literal["messageChatChangeTitle"] = "messageChatChangeTitle"
    title: String


class MessageChatDeleteMember(BaseObject):
    """
    A chat member was deleted

    :param user_id: User identifier of the deleted chat member
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["messageChatDeleteMember"] = "messageChatDeleteMember"
    user_id: Int53


class MessageChatDeletePhoto(BaseObject):
    """
    A deleted chat photo
    """

    ID: typing.Literal["messageChatDeletePhoto"] = "messageChatDeletePhoto"


class MessageChatJoinByLink(BaseObject):
    """
    A new member joined the chat via an invite link
    """

    ID: typing.Literal["messageChatJoinByLink"] = "messageChatJoinByLink"


class MessageChatJoinByRequest(BaseObject):
    """
    A new member was accepted to the chat by an administrator
    """

    ID: typing.Literal["messageChatJoinByRequest"] = "messageChatJoinByRequest"


class MessageChatSetBackground(BaseObject):
    """
    A new background was set in the chat

    :param background: The new background
    :type background: :class:`ChatBackground`
    :param old_background_message_id: Identifier of the message with a previously set same background; 0 if none. Can be an identifier of a deleted message, defaults to None
    :type old_background_message_id: :class:`Int53`, optional
    """

    ID: typing.Literal["messageChatSetBackground"] = "messageChatSetBackground"
    background: ChatBackground
    old_background_message_id: typing.Optional[Int53] = 0


class MessageChatSetMessageAutoDeleteTime(BaseObject):
    """
    The auto-delete or self-destruct timer for messages in the chat has been changed

    :param message_auto_delete_time: New value auto-delete or self-destruct time, in seconds; 0 if disabled
    :type message_auto_delete_time: :class:`Int32`
    :param from_user_id: If not 0, a user identifier, which default setting was automatically applied
    :type from_user_id: :class:`Int53`
    """

    ID: typing.Literal["messageChatSetMessageAutoDeleteTime"] = "messageChatSetMessageAutoDeleteTime"
    message_auto_delete_time: Int32
    from_user_id: Int53 = 0


class MessageChatSetTheme(BaseObject):
    """
    A theme in the chat has been changed

    :param theme_name: If non-empty, name of a new theme, set for the chat. Otherwise, chat theme was reset to the default one
    :type theme_name: :class:`String`
    """

    ID: typing.Literal["messageChatSetTheme"] = "messageChatSetTheme"
    theme_name: String


class MessageChatShared(BaseObject):
    """
    The current user shared a chat, which was requested by the bot

    :param chat_id: Identifier of the shared chat
    :type chat_id: :class:`Int53`
    :param button_id: Identifier of the keyboard button with the request
    :type button_id: :class:`Int32`
    """

    ID: typing.Literal["messageChatShared"] = "messageChatShared"
    chat_id: Int53
    button_id: Int32


class MessageChatUpgradeFrom(BaseObject):
    """
    A supergroup has been created from a basic group

    :param title: Title of the newly created supergroup
    :type title: :class:`String`
    :param basic_group_id: The identifier of the original basic group
    :type basic_group_id: :class:`Int53`
    """

    ID: typing.Literal["messageChatUpgradeFrom"] = "messageChatUpgradeFrom"
    title: String
    basic_group_id: Int53


class MessageChatUpgradeTo(BaseObject):
    """
    A basic group was upgraded to a supergroup and was deactivated as the result

    :param supergroup_id: Identifier of the supergroup to which the basic group was upgraded
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["messageChatUpgradeTo"] = "messageChatUpgradeTo"
    supergroup_id: Int53


class MessageContact(BaseObject):
    """
    A message with a user contact

    :param contact: The contact description
    :type contact: :class:`Contact`
    """

    ID: typing.Literal["messageContact"] = "messageContact"
    contact: Contact


class MessageContactRegistered(BaseObject):
    """
    A contact has registered with Telegram
    """

    ID: typing.Literal["messageContactRegistered"] = "messageContactRegistered"


class MessageCustomServiceAction(BaseObject):
    """
    A non-standard action has happened in the chat

    :param text: Message text to be shown in the chat
    :type text: :class:`String`
    """

    ID: typing.Literal["messageCustomServiceAction"] = "messageCustomServiceAction"
    text: String


class MessageDice(BaseObject):
    """
    A dice message. The dice value is randomly generated by the server

    :param emoji: Emoji on which the dice throw animation is based
    :type emoji: :class:`String`
    :param value: The dice value. If the value is 0, the dice don't have final state yet
    :type value: :class:`Int32`
    :param success_animation_frame_number: Number of frame after which a success animation like a shower of confetti needs to be shown on updateMessageSendSucceeded
    :type success_animation_frame_number: :class:`Int32`
    :param initial_state: The animated stickers with the initial dice animation; may be null if unknown. updateMessageContent will be sent when the sticker became known, defaults to None
    :type initial_state: :class:`DiceStickers`, optional
    :param final_state: The animated stickers with the final dice animation; may be null if unknown. updateMessageContent will be sent when the sticker became known, defaults to None
    :type final_state: :class:`DiceStickers`, optional
    """

    ID: typing.Literal["messageDice"] = "messageDice"
    emoji: String
    value: Int32
    success_animation_frame_number: Int32
    initial_state: typing.Optional[DiceStickers] = None
    final_state: typing.Optional[DiceStickers] = None


class MessageDocument(BaseObject):
    """
    A document message (general file)

    :param document: The document description
    :type document: :class:`Document`
    :param caption: Document caption
    :type caption: :class:`FormattedText`
    """

    ID: typing.Literal["messageDocument"] = "messageDocument"
    document: Document
    caption: FormattedText


class MessageExpiredPhoto(BaseObject):
    """
    A self-destructed photo message
    """

    ID: typing.Literal["messageExpiredPhoto"] = "messageExpiredPhoto"


class MessageExpiredVideo(BaseObject):
    """
    A self-destructed video message
    """

    ID: typing.Literal["messageExpiredVideo"] = "messageExpiredVideo"


class MessageForumTopicCreated(BaseObject):
    """
    A forum topic has been created

    :param name: Name of the topic
    :type name: :class:`String`
    :param icon: Icon of the topic
    :type icon: :class:`ForumTopicIcon`
    """

    ID: typing.Literal["messageForumTopicCreated"] = "messageForumTopicCreated"
    name: String
    icon: ForumTopicIcon


class MessageForumTopicEdited(BaseObject):
    """
    A forum topic has been edited

    :param name: If non-empty, the new name of the topic
    :type name: :class:`String`
    :param edit_icon_custom_emoji_id: True, if icon's custom_emoji_id is changed
    :type edit_icon_custom_emoji_id: :class:`Bool`
    :param icon_custom_emoji_id: New unique identifier of the custom emoji shown on the topic icon; 0 if none. Must be ignored if edit_icon_custom_emoji_id is false, defaults to None
    :type icon_custom_emoji_id: :class:`Int64`, optional
    """

    ID: typing.Literal["messageForumTopicEdited"] = "messageForumTopicEdited"
    name: String
    edit_icon_custom_emoji_id: Bool = False
    icon_custom_emoji_id: typing.Optional[Int64] = 0


class MessageForumTopicIsClosedToggled(BaseObject):
    """
    A forum topic has been closed or opened

    :param is_closed: True, if the topic was closed; otherwise, the topic was reopened
    :type is_closed: :class:`Bool`
    """

    ID: typing.Literal["messageForumTopicIsClosedToggled"] = "messageForumTopicIsClosedToggled"
    is_closed: Bool = False


class MessageForumTopicIsHiddenToggled(BaseObject):
    """
    A General forum topic has been hidden or unhidden

    :param is_hidden: True, if the topic was hidden; otherwise, the topic was unhidden
    :type is_hidden: :class:`Bool`
    """

    ID: typing.Literal["messageForumTopicIsHiddenToggled"] = "messageForumTopicIsHiddenToggled"
    is_hidden: Bool = False


class MessageGame(BaseObject):
    """
    A message with a game

    :param game: The game description
    :type game: :class:`Game`
    """

    ID: typing.Literal["messageGame"] = "messageGame"
    game: Game


class MessageGameScore(BaseObject):
    """
    A new high score was achieved in a game

    :param game_message_id: Identifier of the message with the game, can be an identifier of a deleted message
    :type game_message_id: :class:`Int53`
    :param game_id: Identifier of the game; may be different from the games presented in the message with the game
    :type game_id: :class:`Int64`
    :param score: New score
    :type score: :class:`Int32`
    """

    ID: typing.Literal["messageGameScore"] = "messageGameScore"
    game_message_id: Int53
    game_id: Int64
    score: Int32


class MessageGiftedPremium(BaseObject):
    """
    Telegram Premium was gifted to the user

    :param gifter_user_id: The identifier of a user that gifted Telegram Premium; 0 if the gift was anonymous
    :type gifter_user_id: :class:`Int53`
    :param currency: Currency for the paid amount
    :type currency: :class:`String`
    :param amount: The paid amount, in the smallest units of the currency
    :type amount: :class:`Int53`
    :param cryptocurrency_amount: The paid amount, in the smallest units of the cryptocurrency
    :type cryptocurrency_amount: :class:`Int64`
    :param month_count: Number of month the Telegram Premium subscription will be active
    :type month_count: :class:`Int32`
    :param sticker: A sticker to be shown in the message; may be null if unknown, defaults to None
    :type sticker: :class:`Sticker`, optional
    :param cryptocurrency: Cryptocurrency used to pay for the gift; may be empty if none
    :type cryptocurrency: :class:`String`
    """

    ID: typing.Literal["messageGiftedPremium"] = "messageGiftedPremium"
    gifter_user_id: Int53
    currency: String
    amount: Int53
    cryptocurrency_amount: Int64
    month_count: Int32
    sticker: typing.Optional[Sticker] = None
    cryptocurrency: String = ""


class MessageInviteVideoChatParticipants(BaseObject):
    """
    A message with information about an invite to a video chat

    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`Int32`
    :param user_ids: Invited user identifiers
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["messageInviteVideoChatParticipants"] = "messageInviteVideoChatParticipants"
    group_call_id: Int32
    user_ids: Vector[Int53]


class MessageInvoice(BaseObject):
    """
    A message with an invoice from a bot. Use getInternalLink with internalLinkTypeBotStart to share the invoice

    :param title: Product title
    :type title: :class:`String`
    :param description: Product description
    :type description: :class:`FormattedText`
    :param currency: Currency for the product price
    :type currency: :class:`String`
    :param total_amount: Product total price in the smallest units of the currency
    :type total_amount: :class:`Int53`
    :param start_parameter: Unique invoice bot start_parameter to be passed to getInternalLink
    :type start_parameter: :class:`String`
    :param receipt_message_id: The identifier of the message with the receipt, after the product has been purchased
    :type receipt_message_id: :class:`Int53`
    :param photo: Product photo; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    :param extended_media: Extended media attached to the invoice; may be null, defaults to None
    :type extended_media: :class:`MessageExtendedMedia`, optional
    :param is_test: True, if the invoice is a test invoice
    :type is_test: :class:`Bool`
    :param need_shipping_address: True, if the shipping address must be specified
    :type need_shipping_address: :class:`Bool`
    """

    ID: typing.Literal["messageInvoice"] = "messageInvoice"
    title: String
    description: FormattedText
    currency: String
    total_amount: Int53
    start_parameter: String
    receipt_message_id: Int53
    photo: typing.Optional[Photo] = None
    extended_media: typing.Optional[MessageExtendedMedia] = None
    is_test: Bool = False
    need_shipping_address: Bool = False


class MessageLocation(BaseObject):
    """
    A message with a location

    :param location: The location description
    :type location: :class:`Location`
    :param live_period: Time relative to the message send date, for which the location can be updated, in seconds
    :type live_period: :class:`Int32`
    :param expires_in: Left time for which the location can be updated, in seconds. updateMessageContent is not sent when this field changes
    :type expires_in: :class:`Int32`
    :param proximity_alert_radius: For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). 0 if the notification is disabled. Available only to the message sender
    :type proximity_alert_radius: :class:`Int32`
    :param heading: For live locations, a direction in which the location moves, in degrees; 1-360. If 0 the direction is unknown
    :type heading: :class:`Int32`
    """

    ID: typing.Literal["messageLocation"] = "messageLocation"
    location: Location
    live_period: Int32
    expires_in: Int32
    proximity_alert_radius: Int32
    heading: Int32 = 0


class MessagePassportDataReceived(BaseObject):
    """
    Telegram Passport data has been received; for bots only

    :param elements: List of received Telegram Passport elements
    :type elements: :class:`Vector[EncryptedPassportElement]`
    :param credentials: Encrypted data credentials
    :type credentials: :class:`EncryptedCredentials`
    """

    ID: typing.Literal["messagePassportDataReceived"] = "messagePassportDataReceived"
    elements: Vector[EncryptedPassportElement]
    credentials: EncryptedCredentials


class MessagePassportDataSent(BaseObject):
    """
    Telegram Passport data has been sent to a bot

    :param types: List of Telegram Passport element types sent
    :type types: :class:`Vector[PassportElementType]`
    """

    ID: typing.Literal["messagePassportDataSent"] = "messagePassportDataSent"
    types: Vector[PassportElementType]


class MessagePaymentSuccessful(BaseObject):
    """
    A payment has been completed

    :param invoice_chat_id: Identifier of the chat, containing the corresponding invoice message
    :type invoice_chat_id: :class:`Int53`
    :param invoice_message_id: Identifier of the message with the corresponding invoice; can be 0 or an identifier of a deleted message
    :type invoice_message_id: :class:`Int53`
    :param currency: Currency for the price of the product
    :type currency: :class:`String`
    :param total_amount: Total price for the product, in the smallest units of the currency
    :type total_amount: :class:`Int53`
    :param is_recurring: True, if this is a recurring payment
    :type is_recurring: :class:`Bool`
    :param is_first_recurring: True, if this is the first recurring payment
    :type is_first_recurring: :class:`Bool`
    :param invoice_name: Name of the invoice; may be empty if unknown
    :type invoice_name: :class:`String`
    """

    ID: typing.Literal["messagePaymentSuccessful"] = "messagePaymentSuccessful"
    invoice_chat_id: Int53
    invoice_message_id: Int53
    currency: String
    total_amount: Int53
    is_recurring: Bool = False
    is_first_recurring: Bool = False
    invoice_name: String = ""


class MessagePaymentSuccessfulBot(BaseObject):
    """
    A payment has been completed; for bots only

    :param currency: Currency for price of the product
    :type currency: :class:`String`
    :param total_amount: Total price for the product, in the smallest units of the currency
    :type total_amount: :class:`Int53`
    :param invoice_payload: Invoice payload
    :type invoice_payload: :class:`Bytes`
    :param telegram_payment_charge_id: Telegram payment identifier
    :type telegram_payment_charge_id: :class:`String`
    :param provider_payment_charge_id: Provider payment identifier
    :type provider_payment_charge_id: :class:`String`
    :param order_info: Information about the order; may be null, defaults to None
    :type order_info: :class:`OrderInfo`, optional
    :param is_recurring: True, if this is a recurring payment
    :type is_recurring: :class:`Bool`
    :param is_first_recurring: True, if this is the first recurring payment
    :type is_first_recurring: :class:`Bool`
    :param shipping_option_id: Identifier of the shipping option chosen by the user; may be empty if not applicable
    :type shipping_option_id: :class:`String`
    """

    ID: typing.Literal["messagePaymentSuccessfulBot"] = "messagePaymentSuccessfulBot"
    currency: String
    total_amount: Int53
    invoice_payload: Bytes
    telegram_payment_charge_id: String
    provider_payment_charge_id: String
    order_info: typing.Optional[OrderInfo] = None
    is_recurring: Bool = False
    is_first_recurring: Bool = False
    shipping_option_id: String = ""


class MessagePhoto(BaseObject):
    """
    A photo message

    :param photo: The photo
    :type photo: :class:`Photo`
    :param caption: Photo caption
    :type caption: :class:`FormattedText`
    :param has_spoiler: True, if the photo preview must be covered by a spoiler animation
    :type has_spoiler: :class:`Bool`
    :param is_secret: True, if the photo must be blurred and must be shown only while tapped
    :type is_secret: :class:`Bool`
    """

    ID: typing.Literal["messagePhoto"] = "messagePhoto"
    photo: Photo
    caption: FormattedText
    has_spoiler: Bool = False
    is_secret: Bool = False


class MessagePinMessage(BaseObject):
    """
    A message has been pinned

    :param message_id: Identifier of the pinned message, can be an identifier of a deleted message or 0
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["messagePinMessage"] = "messagePinMessage"
    message_id: Int53


class MessagePoll(BaseObject):
    """
    A message with a poll

    :param poll: The poll description
    :type poll: :class:`Poll`
    """

    ID: typing.Literal["messagePoll"] = "messagePoll"
    poll: Poll


class MessageProximityAlertTriggered(BaseObject):
    """
    A user in the chat came within proximity alert range

    :param traveler_id: The identifier of a user or chat that triggered the proximity alert
    :type traveler_id: :class:`MessageSender`
    :param watcher_id: The identifier of a user or chat that subscribed for the proximity alert
    :type watcher_id: :class:`MessageSender`
    :param distance: The distance between the users
    :type distance: :class:`Int32`
    """

    ID: typing.Literal["messageProximityAlertTriggered"] = "messageProximityAlertTriggered"
    traveler_id: MessageSender
    watcher_id: MessageSender
    distance: Int32


class MessageScreenshotTaken(BaseObject):
    """
    A screenshot of a message in the chat has been taken
    """

    ID: typing.Literal["messageScreenshotTaken"] = "messageScreenshotTaken"


class MessageSticker(BaseObject):
    """
    A sticker message

    :param sticker: The sticker description
    :type sticker: :class:`Sticker`
    :param is_premium: True, if premium animation of the sticker must be played
    :type is_premium: :class:`Bool`
    """

    ID: typing.Literal["messageSticker"] = "messageSticker"
    sticker: Sticker
    is_premium: Bool = False


class MessageStory(BaseObject):
    """
    A message with a forwarded story

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    :param via_mention: True, if the story was automatically forwarded because of a mention of the user
    :type via_mention: :class:`Bool`
    """

    ID: typing.Literal["messageStory"] = "messageStory"
    story_sender_chat_id: Int53
    story_id: Int32
    via_mention: Bool = False


class MessageSuggestProfilePhoto(BaseObject):
    """
    A profile photo was suggested to a user in a private chat

    :param photo: The suggested chat photo. Use the method setProfilePhoto with inputChatPhotoPrevious to apply the photo
    :type photo: :class:`ChatPhoto`
    """

    ID: typing.Literal["messageSuggestProfilePhoto"] = "messageSuggestProfilePhoto"
    photo: ChatPhoto


class MessageSupergroupChatCreate(BaseObject):
    """
    A newly created supergroup or channel

    :param title: Title of the supergroup or channel
    :type title: :class:`String`
    """

    ID: typing.Literal["messageSupergroupChatCreate"] = "messageSupergroupChatCreate"
    title: String


class MessageText(BaseObject):
    """
    A text message

    :param text: Text of the message
    :type text: :class:`FormattedText`
    :param web_page: A preview of the web page that's mentioned in the text; may be null, defaults to None
    :type web_page: :class:`WebPage`, optional
    """

    ID: typing.Literal["messageText"] = "messageText"
    text: FormattedText
    web_page: typing.Optional[WebPage] = None


class MessageUnsupported(BaseObject):
    """
    A message content that is not supported in the current TDLib version
    """

    ID: typing.Literal["messageUnsupported"] = "messageUnsupported"


class MessageUserShared(BaseObject):
    """
    The current user shared a user, which was requested by the bot

    :param user_id: Identifier of the shared user
    :type user_id: :class:`Int53`
    :param button_id: Identifier of the keyboard button with the request
    :type button_id: :class:`Int32`
    """

    ID: typing.Literal["messageUserShared"] = "messageUserShared"
    user_id: Int53
    button_id: Int32


class MessageVenue(BaseObject):
    """
    A message with information about a venue

    :param venue: The venue description
    :type venue: :class:`Venue`
    """

    ID: typing.Literal["messageVenue"] = "messageVenue"
    venue: Venue


class MessageVideo(BaseObject):
    """
    A video message

    :param video: The video description
    :type video: :class:`Video`
    :param caption: Video caption
    :type caption: :class:`FormattedText`
    :param has_spoiler: True, if the video preview must be covered by a spoiler animation
    :type has_spoiler: :class:`Bool`
    :param is_secret: True, if the video thumbnail must be blurred and the video must be shown only while tapped
    :type is_secret: :class:`Bool`
    """

    ID: typing.Literal["messageVideo"] = "messageVideo"
    video: Video
    caption: FormattedText
    has_spoiler: Bool = False
    is_secret: Bool = False


class MessageVideoChatEnded(BaseObject):
    """
    A message with information about an ended video chat

    :param duration: Call duration, in seconds
    :type duration: :class:`Int32`
    """

    ID: typing.Literal["messageVideoChatEnded"] = "messageVideoChatEnded"
    duration: Int32


class MessageVideoChatScheduled(BaseObject):
    """
    A new video chat was scheduled

    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`Int32`
    :param start_date: Point in time (Unix timestamp) when the group call is supposed to be started by an administrator
    :type start_date: :class:`Int32`
    """

    ID: typing.Literal["messageVideoChatScheduled"] = "messageVideoChatScheduled"
    group_call_id: Int32
    start_date: Int32


class MessageVideoChatStarted(BaseObject):
    """
    A newly created video chat

    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`Int32`
    """

    ID: typing.Literal["messageVideoChatStarted"] = "messageVideoChatStarted"
    group_call_id: Int32


class MessageVideoNote(BaseObject):
    """
    A video note message

    :param video_note: The video note description
    :type video_note: :class:`VideoNote`
    :param is_viewed: True, if at least one of the recipients has viewed the video note
    :type is_viewed: :class:`Bool`
    :param is_secret: True, if the video note thumbnail must be blurred and the video note must be shown only while tapped
    :type is_secret: :class:`Bool`
    """

    ID: typing.Literal["messageVideoNote"] = "messageVideoNote"
    video_note: VideoNote
    is_viewed: Bool = False
    is_secret: Bool = False


class MessageVoiceNote(BaseObject):
    """
    A voice note message

    :param voice_note: The voice note description
    :type voice_note: :class:`VoiceNote`
    :param caption: Voice note caption
    :type caption: :class:`FormattedText`
    :param is_listened: True, if at least one of the recipients has listened to the voice note
    :type is_listened: :class:`Bool`
    """

    ID: typing.Literal["messageVoiceNote"] = "messageVoiceNote"
    voice_note: VoiceNote
    caption: FormattedText
    is_listened: Bool = False


class MessageWebAppDataReceived(BaseObject):
    """
    Data from a Web App has been received; for bots only

    :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
    :type button_text: :class:`String`
    :param data: The data
    :type data: :class:`String`
    """

    ID: typing.Literal["messageWebAppDataReceived"] = "messageWebAppDataReceived"
    button_text: String
    data: String


class MessageWebAppDataSent(BaseObject):
    """
    Data from a Web App has been sent to a bot

    :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
    :type button_text: :class:`String`
    """

    ID: typing.Literal["messageWebAppDataSent"] = "messageWebAppDataSent"
    button_text: String


class MessageWebsiteConnected(BaseObject):
    """
    The current user has connected a website by logging in using Telegram Login Widget on it

    :param domain_name: Domain name of the connected website
    :type domain_name: :class:`String`
    """

    ID: typing.Literal["messageWebsiteConnected"] = "messageWebsiteConnected"
    domain_name: String


MessageContent = typing.Union[
    MessageAnimatedEmoji,
    MessageAnimation,
    MessageAudio,
    MessageBasicGroupChatCreate,
    MessageBotWriteAccessAllowed,
    MessageCall,
    MessageChatAddMembers,
    MessageChatChangePhoto,
    MessageChatChangeTitle,
    MessageChatDeleteMember,
    MessageChatDeletePhoto,
    MessageChatJoinByLink,
    MessageChatJoinByRequest,
    MessageChatSetBackground,
    MessageChatSetMessageAutoDeleteTime,
    MessageChatSetTheme,
    MessageChatShared,
    MessageChatUpgradeFrom,
    MessageChatUpgradeTo,
    MessageContact,
    MessageContactRegistered,
    MessageCustomServiceAction,
    MessageDice,
    MessageDocument,
    MessageExpiredPhoto,
    MessageExpiredVideo,
    MessageForumTopicCreated,
    MessageForumTopicEdited,
    MessageForumTopicIsClosedToggled,
    MessageForumTopicIsHiddenToggled,
    MessageGame,
    MessageGameScore,
    MessageGiftedPremium,
    MessageInviteVideoChatParticipants,
    MessageInvoice,
    MessageLocation,
    MessagePassportDataReceived,
    MessagePassportDataSent,
    MessagePaymentSuccessful,
    MessagePaymentSuccessfulBot,
    MessagePhoto,
    MessagePinMessage,
    MessagePoll,
    MessageProximityAlertTriggered,
    MessageScreenshotTaken,
    MessageSticker,
    MessageStory,
    MessageSuggestProfilePhoto,
    MessageSupergroupChatCreate,
    MessageText,
    MessageUnsupported,
    MessageUserShared,
    MessageVenue,
    MessageVideo,
    MessageVideoChatEnded,
    MessageVideoChatScheduled,
    MessageVideoChatStarted,
    MessageVideoNote,
    MessageVoiceNote,
    MessageWebAppDataReceived,
    MessageWebAppDataSent,
    MessageWebsiteConnected,
]


class MessageCopyOptions(BaseObject):
    """
    Options to be used when a message content is copied without reference to the original sender. Service messages and messageInvoice can't be copied

    :param send_copy: True, if content of the message needs to be copied without reference to the original sender. Always true if the message is forwarded to a secret chat or is local
    :type send_copy: :class:`Bool`
    :param replace_caption: True, if media caption of the message copy needs to be replaced. Ignored if send_copy is false
    :type replace_caption: :class:`Bool`
    :param new_caption: New message caption; pass null to copy message without caption. Ignored if replace_caption is false, defaults to None
    :type new_caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["messageCopyOptions"] = "messageCopyOptions"
    send_copy: Bool = False
    replace_caption: Bool = False
    new_caption: typing.Optional[FormattedText] = None


class MessageExtendedMediaPhoto(BaseObject):
    """
    The media is a photo

    :param photo: The photo
    :type photo: :class:`Photo`
    :param caption: Photo caption
    :type caption: :class:`FormattedText`
    """

    ID: typing.Literal["messageExtendedMediaPhoto"] = "messageExtendedMediaPhoto"
    photo: Photo
    caption: FormattedText


class MessageExtendedMediaPreview(BaseObject):
    """
    The media is hidden until the invoice is paid

    :param caption: Media caption
    :type caption: :class:`FormattedText`
    :param minithumbnail: Media minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param width: Media width; 0 if unknown, defaults to None
    :type width: :class:`Int32`, optional
    :param height: Media height; 0 if unknown, defaults to None
    :type height: :class:`Int32`, optional
    :param duration: Media duration; 0 if unknown, defaults to None
    :type duration: :class:`Int32`, optional
    """

    ID: typing.Literal["messageExtendedMediaPreview"] = "messageExtendedMediaPreview"
    caption: FormattedText
    minithumbnail: typing.Optional[Minithumbnail] = None
    width: typing.Optional[Int32] = 0
    height: typing.Optional[Int32] = 0
    duration: typing.Optional[Int32] = 0


class MessageExtendedMediaUnsupported(BaseObject):
    """
    The media is unsupported

    :param caption: Media caption
    :type caption: :class:`FormattedText`
    """

    ID: typing.Literal["messageExtendedMediaUnsupported"] = "messageExtendedMediaUnsupported"
    caption: FormattedText


class MessageExtendedMediaVideo(BaseObject):
    """
    The media is a video

    :param video: The video
    :type video: :class:`Video`
    :param caption: Photo caption
    :type caption: :class:`FormattedText`
    """

    ID: typing.Literal["messageExtendedMediaVideo"] = "messageExtendedMediaVideo"
    video: Video
    caption: FormattedText


MessageExtendedMedia = typing.Union[
    MessageExtendedMediaPhoto,
    MessageExtendedMediaPreview,
    MessageExtendedMediaUnsupported,
    MessageExtendedMediaVideo,
]


class MessageFileTypeGroup(BaseObject):
    """
    The messages was exported from a group chat

    :param title: Title of the group chat; may be empty if unrecognized
    :type title: :class:`String`
    """

    ID: typing.Literal["messageFileTypeGroup"] = "messageFileTypeGroup"
    title: String = ""


class MessageFileTypePrivate(BaseObject):
    """
    The messages was exported from a private chat

    :param name: Name of the other party; may be empty if unrecognized
    :type name: :class:`String`
    """

    ID: typing.Literal["messageFileTypePrivate"] = "messageFileTypePrivate"
    name: String = ""


class MessageFileTypeUnknown(BaseObject):
    """
    The messages was exported from a chat of unknown type
    """

    ID: typing.Literal["messageFileTypeUnknown"] = "messageFileTypeUnknown"


MessageFileType = typing.Union[
    MessageFileTypeGroup,
    MessageFileTypePrivate,
    MessageFileTypeUnknown,
]


class MessageForwardInfo(BaseObject):
    """
    Contains information about a forwarded message

    :param origin: Origin of a forwarded message
    :type origin: :class:`MessageForwardOrigin`
    :param date: Point in time (Unix timestamp) when the message was originally sent
    :type date: :class:`Int32`
    :param public_service_announcement_type: The type of a public service announcement for the forwarded message
    :type public_service_announcement_type: :class:`String`
    :param from_chat_id: For messages forwarded to the chat with the current user (Saved Messages), to the Replies bot chat, or to the channel's discussion group, the identifier of the chat from which the message was forwarded last time; 0 if unknown, defaults to None
    :type from_chat_id: :class:`Int53`, optional
    :param from_message_id: For messages forwarded to the chat with the current user (Saved Messages), to the Replies bot chat, or to the channel's discussion group, the identifier of the original message from which the new message was forwarded last time; 0 if unknown, defaults to None
    :type from_message_id: :class:`Int53`, optional
    """

    ID: typing.Literal["messageForwardInfo"] = "messageForwardInfo"
    origin: MessageForwardOrigin
    date: Int32
    public_service_announcement_type: String
    from_chat_id: typing.Optional[Int53] = 0
    from_message_id: typing.Optional[Int53] = 0


class MessageForwardOriginChannel(BaseObject):
    """
    The message was originally a post in a channel

    :param chat_id: Identifier of the chat from which the message was originally forwarded
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier of the original message
    :type message_id: :class:`Int53`
    :param author_signature: Original post author signature
    :type author_signature: :class:`String`
    """

    ID: typing.Literal["messageForwardOriginChannel"] = "messageForwardOriginChannel"
    chat_id: Int53
    message_id: Int53
    author_signature: String


class MessageForwardOriginChat(BaseObject):
    """
    The message was originally sent on behalf of a chat

    :param sender_chat_id: Identifier of the chat that originally sent the message
    :type sender_chat_id: :class:`Int53`
    :param author_signature: For messages originally sent by an anonymous chat administrator, original message author signature
    :type author_signature: :class:`String`
    """

    ID: typing.Literal["messageForwardOriginChat"] = "messageForwardOriginChat"
    sender_chat_id: Int53
    author_signature: String


class MessageForwardOriginHiddenUser(BaseObject):
    """
    The message was originally sent by a user, which is hidden by their privacy settings

    :param sender_name: Name of the sender
    :type sender_name: :class:`String`
    """

    ID: typing.Literal["messageForwardOriginHiddenUser"] = "messageForwardOriginHiddenUser"
    sender_name: String


class MessageForwardOriginMessageImport(BaseObject):
    """
    The message was imported from an exported message history

    :param sender_name: Name of the sender
    :type sender_name: :class:`String`
    """

    ID: typing.Literal["messageForwardOriginMessageImport"] = "messageForwardOriginMessageImport"
    sender_name: String


class MessageForwardOriginUser(BaseObject):
    """
    The message was originally sent by a known user

    :param sender_user_id: Identifier of the user that originally sent the message
    :type sender_user_id: :class:`Int53`
    """

    ID: typing.Literal["messageForwardOriginUser"] = "messageForwardOriginUser"
    sender_user_id: Int53


MessageForwardOrigin = typing.Union[
    MessageForwardOriginChannel,
    MessageForwardOriginChat,
    MessageForwardOriginHiddenUser,
    MessageForwardOriginMessageImport,
    MessageForwardOriginUser,
]


class MessageInteractionInfo(BaseObject):
    """
    Contains information about interactions with a message

    :param view_count: Number of times the message was viewed
    :type view_count: :class:`Int32`
    :param forward_count: Number of times the message was forwarded
    :type forward_count: :class:`Int32`
    :param reactions: The list of reactions added to the message
    :type reactions: :class:`Vector[MessageReaction]`
    :param reply_info: Information about direct or indirect replies to the message; may be null. Currently, available only in channels with a discussion supergroup and discussion supergroups for messages, which are not replies itself, defaults to None
    :type reply_info: :class:`MessageReplyInfo`, optional
    """

    ID: typing.Literal["messageInteractionInfo"] = "messageInteractionInfo"
    view_count: Int32
    forward_count: Int32
    reactions: Vector[MessageReaction]
    reply_info: typing.Optional[MessageReplyInfo] = None


class MessageLink(BaseObject):
    """
    Contains an HTTPS link to a message in a supergroup or channel, or a forum topic

    :param link: The link
    :type link: :class:`String`
    :param is_public: True, if the link will work for non-members of the chat
    :type is_public: :class:`Bool`
    """

    ID: typing.Literal["messageLink"] = "messageLink"
    link: String
    is_public: Bool = False


class MessageLinkInfo(BaseObject):
    """
    Contains information about a link to a message or a forum topic in a chat

    :param chat_id: If found, identifier of the chat to which the link points, 0 otherwise
    :type chat_id: :class:`Int53`
    :param message_thread_id: If found, identifier of the message thread in which to open the message, or a forum topic to open if the message is missing
    :type message_thread_id: :class:`Int53`
    :param media_timestamp: Timestamp from which the video/audio/video note/voice note playing must start, in seconds; 0 if not specified. The media can be in the message content or in its web page preview
    :type media_timestamp: :class:`Int32`
    :param message: If found, the linked message; may be null, defaults to None
    :type message: :class:`Message`, optional
    :param is_public: True, if the link is a public link for a message or a forum topic in a chat
    :type is_public: :class:`Bool`
    :param for_album: True, if the whole media album to which the message belongs is linked
    :type for_album: :class:`Bool`
    """

    ID: typing.Literal["messageLinkInfo"] = "messageLinkInfo"
    chat_id: Int53
    message_thread_id: Int53
    media_timestamp: Int32
    message: typing.Optional[Message] = None
    is_public: Bool = False
    for_album: Bool = False


class MessagePosition(BaseObject):
    """
    Contains information about a message in a specific position

    :param position: 0-based message position in the full list of suitable messages
    :type position: :class:`Int32`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) when the message was sent
    :type date: :class:`Int32`
    """

    ID: typing.Literal["messagePosition"] = "messagePosition"
    position: Int32
    message_id: Int53
    date: Int32


class MessagePositions(BaseObject):
    """
    Contains a list of message positions

    :param total_count: Total number of messages found
    :type total_count: :class:`Int32`
    :param positions: List of message positions
    :type positions: :class:`Vector[MessagePosition]`
    """

    ID: typing.Literal["messagePositions"] = "messagePositions"
    total_count: Int32
    positions: Vector[MessagePosition]


class MessageReaction(BaseObject):
    """
    Contains information about a reaction to a message

    :param type_: Type of the reaction
    :type type_: :class:`ReactionType`
    :param total_count: Number of times the reaction was added
    :type total_count: :class:`Int32`
    :param recent_sender_ids: Identifiers of at most 3 recent message senders, added the reaction; available in private, basic group and supergroup chats
    :type recent_sender_ids: :class:`Vector[MessageSender]`
    :param is_chosen: True, if the reaction is chosen by the current user
    :type is_chosen: :class:`Bool`
    """

    ID: typing.Literal["messageReaction"] = "messageReaction"
    type_: ReactionType = Field(..., alias="type")
    total_count: Int32
    recent_sender_ids: Vector[MessageSender]
    is_chosen: Bool = False


class MessageReplyInfo(BaseObject):
    """
    Contains information about replies to a message

    :param reply_count: Number of times the message was directly or indirectly replied
    :type reply_count: :class:`Int32`
    :param recent_replier_ids: Identifiers of at most 3 recent repliers to the message; available in channels with a discussion supergroup. The users and chats are expected to be inaccessible: only their photo and name will be available
    :type recent_replier_ids: :class:`Vector[MessageSender]`
    :param last_read_inbox_message_id: Identifier of the last read incoming reply to the message
    :type last_read_inbox_message_id: :class:`Int53`
    :param last_read_outbox_message_id: Identifier of the last read outgoing reply to the message
    :type last_read_outbox_message_id: :class:`Int53`
    :param last_message_id: Identifier of the last reply to the message
    :type last_message_id: :class:`Int53`
    """

    ID: typing.Literal["messageReplyInfo"] = "messageReplyInfo"
    reply_count: Int32
    recent_replier_ids: Vector[MessageSender]
    last_read_inbox_message_id: Int53
    last_read_outbox_message_id: Int53
    last_message_id: Int53


class MessageReplyToMessage(BaseObject):
    """
    Describes a replied message

    :param chat_id: The identifier of the chat to which the replied message belongs; ignored for outgoing replies. For example, messages in the Replies chat are replies to messages in different chats
    :type chat_id: :class:`Int53`
    :param message_id: The identifier of the replied message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["messageReplyToMessage"] = "messageReplyToMessage"
    chat_id: Int53
    message_id: Int53


class MessageReplyToStory(BaseObject):
    """
    Describes a replied story

    :param story_sender_chat_id: The identifier of the sender of the replied story. Currently, stories can be replied only in the sender's chat
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: The identifier of the replied story
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["messageReplyToStory"] = "messageReplyToStory"
    story_sender_chat_id: Int53
    story_id: Int32


MessageReplyTo = typing.Union[
    MessageReplyToMessage,
    MessageReplyToStory,
]


class MessageSchedulingStateSendAtDate(BaseObject):
    """
    The message will be sent at the specified date

    :param send_date: Point in time (Unix timestamp) when the message will be sent. The date must be within 367 days in the future
    :type send_date: :class:`Int32`
    """

    ID: typing.Literal["messageSchedulingStateSendAtDate"] = "messageSchedulingStateSendAtDate"
    send_date: Int32


class MessageSchedulingStateSendWhenOnline(BaseObject):
    """
    The message will be sent when the peer will be online. Applicable to private chats only and when the exact online status of the peer is known
    """

    ID: typing.Literal["messageSchedulingStateSendWhenOnline"] = "messageSchedulingStateSendWhenOnline"


MessageSchedulingState = typing.Union[
    MessageSchedulingStateSendAtDate,
    MessageSchedulingStateSendWhenOnline,
]


class MessageSelfDestructTypeImmediately(BaseObject):
    """
    The message can be opened only once and will be self-destructed once closed
    """

    ID: typing.Literal["messageSelfDestructTypeImmediately"] = "messageSelfDestructTypeImmediately"


class MessageSelfDestructTypeTimer(BaseObject):
    """
    The message will be self-destructed in the specified time after its content was opened

    :param self_destruct_time: The message's self-destruct time, in seconds; must be between 0 and 60 in private chats
    :type self_destruct_time: :class:`Int32`
    """

    ID: typing.Literal["messageSelfDestructTypeTimer"] = "messageSelfDestructTypeTimer"
    self_destruct_time: Int32


MessageSelfDestructType = typing.Union[
    MessageSelfDestructTypeImmediately,
    MessageSelfDestructTypeTimer,
]


class MessageSendOptions(BaseObject):
    """
    Options to be used when a message is sent

    :param sending_id: Non-persistent identifier, which will be returned back in messageSendingStatePending object and can be used to match sent messages and corresponding updateNewMessage updates
    :type sending_id: :class:`Int32`
    :param disable_notification: Pass true to disable notification for the message
    :type disable_notification: :class:`Bool`
    :param from_background: Pass true if the message is sent from the background
    :type from_background: :class:`Bool`
    :param protect_content: Pass true if the content of the message must be protected from forwarding and saving; for bots only
    :type protect_content: :class:`Bool`
    :param update_order_of_installed_sticker_sets: Pass true if the user explicitly chosen a sticker or a custom emoji from an installed sticker set; applicable only to sendMessage and sendMessageAlbum
    :type update_order_of_installed_sticker_sets: :class:`Bool`
    :param scheduling_state: Message scheduling state; pass null to send message immediately. Messages sent to a secret chat, live location messages and self-destructing messages can't be scheduled, defaults to None
    :type scheduling_state: :class:`MessageSchedulingState`, optional
    """

    ID: typing.Literal["messageSendOptions"] = "messageSendOptions"
    sending_id: Int32
    disable_notification: Bool = False
    from_background: Bool = False
    protect_content: Bool = False
    update_order_of_installed_sticker_sets: Bool = False
    scheduling_state: typing.Optional[MessageSchedulingState] = None


class MessageSenderChat(BaseObject):
    """
    The message was sent on behalf of a chat

    :param chat_id: Identifier of the chat that sent the message
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["messageSenderChat"] = "messageSenderChat"
    chat_id: Int53


class MessageSenderUser(BaseObject):
    """
    The message was sent by a known user

    :param user_id: Identifier of the user that sent the message
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["messageSenderUser"] = "messageSenderUser"
    user_id: Int53


MessageSender = typing.Union[
    MessageSenderChat,
    MessageSenderUser,
]


class MessageSenders(BaseObject):
    """
    Represents a list of message senders

    :param total_count: Approximate total number of messages senders found
    :type total_count: :class:`Int32`
    :param senders: List of message senders
    :type senders: :class:`Vector[MessageSender]`
    """

    ID: typing.Literal["messageSenders"] = "messageSenders"
    total_count: Int32
    senders: Vector[MessageSender]


class MessageSendingStateFailed(BaseObject):
    """
    The message failed to be sent

    :param error_message: Error message
    :type error_message: :class:`String`
    :param retry_after: Time left before the message can be re-sent, in seconds. No update is sent when this field changes
    :type retry_after: :class:`Double`
    :param can_retry: True, if the message can be re-sent
    :type can_retry: :class:`Bool`
    :param need_another_sender: True, if the message can be re-sent only on behalf of a different sender
    :type need_another_sender: :class:`Bool`
    :param error_code: An error code; 0 if unknown, defaults to None
    :type error_code: :class:`Int32`, optional
    """

    ID: typing.Literal["messageSendingStateFailed"] = "messageSendingStateFailed"
    error_message: String
    retry_after: Double
    can_retry: Bool = False
    need_another_sender: Bool = False
    error_code: typing.Optional[Int32] = 0


class MessageSendingStatePending(BaseObject):
    """
    The message is being sent now, but has not yet been delivered to the server

    :param sending_id: Non-persistent message sending identifier, specified by the application
    :type sending_id: :class:`Int32`
    """

    ID: typing.Literal["messageSendingStatePending"] = "messageSendingStatePending"
    sending_id: Int32


MessageSendingState = typing.Union[
    MessageSendingStateFailed,
    MessageSendingStatePending,
]


class MessageSourceChatEventLog(BaseObject):
    """
    The message is from a chat event log
    """

    ID: typing.Literal["messageSourceChatEventLog"] = "messageSourceChatEventLog"


class MessageSourceChatHistory(BaseObject):
    """
    The message is from a chat history
    """

    ID: typing.Literal["messageSourceChatHistory"] = "messageSourceChatHistory"


class MessageSourceChatList(BaseObject):
    """
    The message is from a chat list or a forum topic list
    """

    ID: typing.Literal["messageSourceChatList"] = "messageSourceChatList"


class MessageSourceForumTopicHistory(BaseObject):
    """
    The message is from a forum topic history
    """

    ID: typing.Literal["messageSourceForumTopicHistory"] = "messageSourceForumTopicHistory"


class MessageSourceHistoryPreview(BaseObject):
    """
    The message is from chat, message thread or forum topic history preview
    """

    ID: typing.Literal["messageSourceHistoryPreview"] = "messageSourceHistoryPreview"


class MessageSourceMessageThreadHistory(BaseObject):
    """
    The message is from a message thread history
    """

    ID: typing.Literal["messageSourceMessageThreadHistory"] = "messageSourceMessageThreadHistory"


class MessageSourceNotification(BaseObject):
    """
    The message is from a notification
    """

    ID: typing.Literal["messageSourceNotification"] = "messageSourceNotification"


class MessageSourceOther(BaseObject):
    """
    The message is from some other source
    """

    ID: typing.Literal["messageSourceOther"] = "messageSourceOther"


class MessageSourceScreenshot(BaseObject):
    """
    The message was screenshotted; the source must be used only if the message content was visible during the screenshot
    """

    ID: typing.Literal["messageSourceScreenshot"] = "messageSourceScreenshot"


class MessageSourceSearch(BaseObject):
    """
    The message is from search results, including file downloads, local file list, outgoing document messages, calendar
    """

    ID: typing.Literal["messageSourceSearch"] = "messageSourceSearch"


MessageSource = typing.Union[
    MessageSourceChatEventLog,
    MessageSourceChatHistory,
    MessageSourceChatList,
    MessageSourceForumTopicHistory,
    MessageSourceHistoryPreview,
    MessageSourceMessageThreadHistory,
    MessageSourceNotification,
    MessageSourceOther,
    MessageSourceScreenshot,
    MessageSourceSearch,
]


class MessageSponsor(BaseObject):
    """
    Information about the sponsor of a message

    :param type_: Type of the sponsor
    :type type_: :class:`MessageSponsorType`
    :param info: Additional optional information about the sponsor to be shown along with the message
    :type info: :class:`String`
    :param photo: Photo of the sponsor; may be null if must not be shown, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    """

    ID: typing.Literal["messageSponsor"] = "messageSponsor"
    type_: MessageSponsorType = Field(..., alias="type")
    info: String
    photo: typing.Optional[ChatPhotoInfo] = None


class MessageSponsorTypeBot(BaseObject):
    """
    The sponsor is a bot

    :param bot_user_id: User identifier of the bot
    :type bot_user_id: :class:`Int53`
    :param link: An internal link to be opened when the sponsored message is clicked
    :type link: :class:`InternalLinkType`
    """

    ID: typing.Literal["messageSponsorTypeBot"] = "messageSponsorTypeBot"
    bot_user_id: Int53
    link: InternalLinkType


class MessageSponsorTypePrivateChannel(BaseObject):
    """
    The sponsor is a private channel chat

    :param title: Title of the chat
    :type title: :class:`String`
    :param invite_link: Invite link for the channel
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["messageSponsorTypePrivateChannel"] = "messageSponsorTypePrivateChannel"
    title: String
    invite_link: String


class MessageSponsorTypePublicChannel(BaseObject):
    """
    The sponsor is a public channel chat

    :param chat_id: Sponsor chat identifier
    :type chat_id: :class:`Int53`
    :param link: An internal link to be opened when the sponsored message is clicked; may be null if the sponsor chat needs to be opened instead, defaults to None
    :type link: :class:`InternalLinkType`, optional
    """

    ID: typing.Literal["messageSponsorTypePublicChannel"] = "messageSponsorTypePublicChannel"
    chat_id: Int53
    link: typing.Optional[InternalLinkType] = None


class MessageSponsorTypeWebsite(BaseObject):
    """
    The sponsor is a website

    :param url: URL of the website
    :type url: :class:`String`
    :param name: Name of the website
    :type name: :class:`String`
    """

    ID: typing.Literal["messageSponsorTypeWebsite"] = "messageSponsorTypeWebsite"
    url: String
    name: String


MessageSponsorType = typing.Union[
    MessageSponsorTypeBot,
    MessageSponsorTypePrivateChannel,
    MessageSponsorTypePublicChannel,
    MessageSponsorTypeWebsite,
]


class MessageStatistics(BaseObject):
    """
    A detailed statistics about a message

    :param message_interaction_graph: A graph containing number of message views and shares
    :type message_interaction_graph: :class:`StatisticalGraph`
    """

    ID: typing.Literal["messageStatistics"] = "messageStatistics"
    message_interaction_graph: StatisticalGraph


class MessageThreadInfo(BaseObject):
    """
    Contains information about a message thread

    :param chat_id: Identifier of the chat to which the message thread belongs
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier, unique within the chat
    :type message_thread_id: :class:`Int53`
    :param unread_message_count: Approximate number of unread messages in the message thread
    :type unread_message_count: :class:`Int32`
    :param messages: The messages from which the thread starts. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)
    :type messages: :class:`Vector[Message]`
    :param reply_info: Information about the message thread; may be null for forum topic threads, defaults to None
    :type reply_info: :class:`MessageReplyInfo`, optional
    :param draft_message: A draft of a message in the message thread; may be null if none, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    """

    ID: typing.Literal["messageThreadInfo"] = "messageThreadInfo"
    chat_id: Int53
    message_thread_id: Int53
    unread_message_count: Int32
    messages: Vector[Message]
    reply_info: typing.Optional[MessageReplyInfo] = None
    draft_message: typing.Optional[DraftMessage] = None


class MessageViewer(BaseObject):
    """
    Represents a viewer of a message

    :param user_id: User identifier of the viewer
    :type user_id: :class:`Int53`
    :param view_date: Approximate point in time (Unix timestamp) when the message was viewed
    :type view_date: :class:`Int32`
    """

    ID: typing.Literal["messageViewer"] = "messageViewer"
    user_id: Int53
    view_date: Int32


class MessageViewers(BaseObject):
    """
    Represents a list of message viewers

    :param viewers: List of message viewers
    :type viewers: :class:`Vector[MessageViewer]`
    """

    ID: typing.Literal["messageViewers"] = "messageViewers"
    viewers: Vector[MessageViewer]


class Messages(BaseObject):
    """
    Contains a list of messages

    :param total_count: Approximate total number of messages found
    :type total_count: :class:`Int32`
    :param messages: List of messages; messages may be null, defaults to None
    :type messages: :class:`Vector[Message]`, optional
    """

    ID: typing.Literal["messages"] = "messages"
    total_count: Int32
    messages: Vector[typing.Optional[Message]] = None


class Minithumbnail(BaseObject):
    """
    Thumbnail image of a very poor quality and low resolution

    :param width: Thumbnail width, usually doesn't exceed 40
    :type width: :class:`Int32`
    :param height: Thumbnail height, usually doesn't exceed 40
    :type height: :class:`Int32`
    :param data: The thumbnail in JPEG format
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["minithumbnail"] = "minithumbnail"
    width: Int32
    height: Int32
    data: Bytes


class NetworkStatistics(BaseObject):
    """
    A full list of available network statistic entries

    :param since_date: Point in time (Unix timestamp) from which the statistics are collected
    :type since_date: :class:`Int32`
    :param entries: Network statistics entries
    :type entries: :class:`Vector[NetworkStatisticsEntry]`
    """

    ID: typing.Literal["networkStatistics"] = "networkStatistics"
    since_date: Int32
    entries: Vector[NetworkStatisticsEntry]


class NetworkStatisticsEntryCall(BaseObject):
    """
    Contains information about the total amount of data that was used for calls

    :param network_type: Type of the network the data was sent through. Call setNetworkType to maintain the actual network type
    :type network_type: :class:`NetworkType`
    :param sent_bytes: Total number of bytes sent
    :type sent_bytes: :class:`Int53`
    :param received_bytes: Total number of bytes received
    :type received_bytes: :class:`Int53`
    :param duration: Total call duration, in seconds
    :type duration: :class:`Double`
    """

    ID: typing.Literal["networkStatisticsEntryCall"] = "networkStatisticsEntryCall"
    network_type: NetworkType
    sent_bytes: Int53
    received_bytes: Int53
    duration: Double


class NetworkStatisticsEntryFile(BaseObject):
    """
    Contains information about the total amount of data that was used to send and receive files

    :param network_type: Type of the network the data was sent through. Call setNetworkType to maintain the actual network type
    :type network_type: :class:`NetworkType`
    :param sent_bytes: Total number of bytes sent
    :type sent_bytes: :class:`Int53`
    :param received_bytes: Total number of bytes received
    :type received_bytes: :class:`Int53`
    :param file_type: Type of the file the data is part of; pass null if the data isn't related to files, defaults to None
    :type file_type: :class:`FileType`, optional
    """

    ID: typing.Literal["networkStatisticsEntryFile"] = "networkStatisticsEntryFile"
    network_type: NetworkType
    sent_bytes: Int53
    received_bytes: Int53
    file_type: typing.Optional[FileType] = None


NetworkStatisticsEntry = typing.Union[
    NetworkStatisticsEntryCall,
    NetworkStatisticsEntryFile,
]


class NetworkTypeMobile(BaseObject):
    """
    A mobile network
    """

    ID: typing.Literal["networkTypeMobile"] = "networkTypeMobile"


class NetworkTypeMobileRoaming(BaseObject):
    """
    A mobile roaming network
    """

    ID: typing.Literal["networkTypeMobileRoaming"] = "networkTypeMobileRoaming"


class NetworkTypeNone(BaseObject):
    """
    The network is not available
    """

    ID: typing.Literal["networkTypeNone"] = "networkTypeNone"


class NetworkTypeOther(BaseObject):
    """
    A different network type (e.g., Ethernet network)
    """

    ID: typing.Literal["networkTypeOther"] = "networkTypeOther"


class NetworkTypeWiFi(BaseObject):
    """
    A Wi-Fi network
    """

    ID: typing.Literal["networkTypeWiFi"] = "networkTypeWiFi"


NetworkType = typing.Union[
    NetworkTypeMobile,
    NetworkTypeMobileRoaming,
    NetworkTypeNone,
    NetworkTypeOther,
    NetworkTypeWiFi,
]


class Notification(BaseObject):
    """
    Contains information about a notification

    :param id: Unique persistent identifier of this notification
    :type id: :class:`Int32`
    :param date: Notification date
    :type date: :class:`Int32`
    :param type_: Notification type
    :type type_: :class:`NotificationType`
    :param is_silent: True, if the notification was explicitly sent without sound
    :type is_silent: :class:`Bool`
    """

    ID: typing.Literal["notification"] = "notification"
    id: Int32
    date: Int32
    type_: NotificationType = Field(..., alias="type")
    is_silent: Bool = False


class NotificationGroup(BaseObject):
    """
    Describes a group of notifications

    :param id: Unique persistent auto-incremented from 1 identifier of the notification group
    :type id: :class:`Int32`
    :param type_: Type of the group
    :type type_: :class:`NotificationGroupType`
    :param chat_id: Identifier of a chat to which all notifications in the group belong
    :type chat_id: :class:`Int53`
    :param total_count: Total number of active notifications in the group
    :type total_count: :class:`Int32`
    :param notifications: The list of active notifications
    :type notifications: :class:`Vector[Notification]`
    """

    ID: typing.Literal["notificationGroup"] = "notificationGroup"
    id: Int32
    type_: NotificationGroupType = Field(..., alias="type")
    chat_id: Int53
    total_count: Int32
    notifications: Vector[Notification]


class NotificationGroupTypeCalls(BaseObject):
    """
    A group containing notifications of type notificationTypeNewCall
    """

    ID: typing.Literal["notificationGroupTypeCalls"] = "notificationGroupTypeCalls"


class NotificationGroupTypeMentions(BaseObject):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with unread mentions of the current user, replies to their messages, or a pinned message
    """

    ID: typing.Literal["notificationGroupTypeMentions"] = "notificationGroupTypeMentions"


class NotificationGroupTypeMessages(BaseObject):
    """
    A group containing notifications of type notificationTypeNewMessage and notificationTypeNewPushMessage with ordinary unread messages
    """

    ID: typing.Literal["notificationGroupTypeMessages"] = "notificationGroupTypeMessages"


class NotificationGroupTypeSecretChat(BaseObject):
    """
    A group containing a notification of type notificationTypeNewSecretChat
    """

    ID: typing.Literal["notificationGroupTypeSecretChat"] = "notificationGroupTypeSecretChat"


NotificationGroupType = typing.Union[
    NotificationGroupTypeCalls,
    NotificationGroupTypeMentions,
    NotificationGroupTypeMessages,
    NotificationGroupTypeSecretChat,
]


class NotificationSettingsScopeChannelChats(BaseObject):
    """
    Notification settings applied to all channel chats when the corresponding chat setting has a default value
    """

    ID: typing.Literal["notificationSettingsScopeChannelChats"] = "notificationSettingsScopeChannelChats"


class NotificationSettingsScopeGroupChats(BaseObject):
    """
    Notification settings applied to all basic group and supergroup chats when the corresponding chat setting has a default value
    """

    ID: typing.Literal["notificationSettingsScopeGroupChats"] = "notificationSettingsScopeGroupChats"


class NotificationSettingsScopePrivateChats(BaseObject):
    """
    Notification settings applied to all private and secret chats when the corresponding chat setting has a default value
    """

    ID: typing.Literal["notificationSettingsScopePrivateChats"] = "notificationSettingsScopePrivateChats"


NotificationSettingsScope = typing.Union[
    NotificationSettingsScopeChannelChats,
    NotificationSettingsScopeGroupChats,
    NotificationSettingsScopePrivateChats,
]


class NotificationSound(BaseObject):
    """
    Describes a notification sound in MP3 format

    :param id: Unique identifier of the notification sound
    :type id: :class:`Int64`
    :param duration: Duration of the sound, in seconds
    :type duration: :class:`Int32`
    :param date: Point in time (Unix timestamp) when the sound was created
    :type date: :class:`Int32`
    :param title: Title of the notification sound
    :type title: :class:`String`
    :param data: Arbitrary data, defined while the sound was uploaded
    :type data: :class:`String`
    :param sound: File containing the sound
    :type sound: :class:`File`
    """

    ID: typing.Literal["notificationSound"] = "notificationSound"
    id: Int64
    duration: Int32
    date: Int32
    title: String
    data: String
    sound: File


class NotificationSounds(BaseObject):
    """
    Contains a list of notification sounds

    :param notification_sounds: A list of notification sounds
    :type notification_sounds: :class:`Vector[NotificationSound]`
    """

    ID: typing.Literal["notificationSounds"] = "notificationSounds"
    notification_sounds: Vector[NotificationSound]


class NotificationTypeNewCall(BaseObject):
    """
    New call was received

    :param call_id: Call identifier
    :type call_id: :class:`Int32`
    """

    ID: typing.Literal["notificationTypeNewCall"] = "notificationTypeNewCall"
    call_id: Int32


class NotificationTypeNewMessage(BaseObject):
    """
    New message was received

    :param message: The message
    :type message: :class:`Message`
    :param show_preview: True, if message content must be displayed in notifications
    :type show_preview: :class:`Bool`
    """

    ID: typing.Literal["notificationTypeNewMessage"] = "notificationTypeNewMessage"
    message: Message
    show_preview: Bool = False


class NotificationTypeNewPushMessage(BaseObject):
    """
    New message was received through a push notification

    :param message_id: The message identifier. The message will not be available in the chat history, but the identifier can be used in viewMessages, or as a message to reply
    :type message_id: :class:`Int53`
    :param sender_id: Identifier of the sender of the message. Corresponding user or chat may be inaccessible
    :type sender_id: :class:`MessageSender`
    :param sender_name: Name of the sender
    :type sender_name: :class:`String`
    :param content: Push message content
    :type content: :class:`PushMessageContent`
    :param is_outgoing: True, if the message is outgoing
    :type is_outgoing: :class:`Bool`
    """

    ID: typing.Literal["notificationTypeNewPushMessage"] = "notificationTypeNewPushMessage"
    message_id: Int53
    sender_id: MessageSender
    sender_name: String
    content: PushMessageContent
    is_outgoing: Bool = False


class NotificationTypeNewSecretChat(BaseObject):
    """
    New secret chat was created
    """

    ID: typing.Literal["notificationTypeNewSecretChat"] = "notificationTypeNewSecretChat"


NotificationType = typing.Union[
    NotificationTypeNewCall,
    NotificationTypeNewMessage,
    NotificationTypeNewPushMessage,
    NotificationTypeNewSecretChat,
]


class Ok(BaseObject):
    """
    An object of this type is returned on a successful function call for certain functions
    """

    ID: typing.Literal["ok"] = "ok"


class OptionValueBoolean(BaseObject):
    """
    Represents a boolean option

    :param value: The value of the option
    :type value: :class:`Bool`
    """

    ID: typing.Literal["optionValueBoolean"] = "optionValueBoolean"
    value: Bool


class OptionValueEmpty(BaseObject):
    """
    Represents an unknown option or an option which has a default value
    """

    ID: typing.Literal["optionValueEmpty"] = "optionValueEmpty"


class OptionValueInteger(BaseObject):
    """
    Represents an integer option

    :param value: The value of the option
    :type value: :class:`Int64`
    """

    ID: typing.Literal["optionValueInteger"] = "optionValueInteger"
    value: Int64


class OptionValueString(BaseObject):
    """
    Represents a string option

    :param value: The value of the option
    :type value: :class:`String`
    """

    ID: typing.Literal["optionValueString"] = "optionValueString"
    value: String


OptionValue = typing.Union[
    OptionValueBoolean,
    OptionValueEmpty,
    OptionValueInteger,
    OptionValueString,
]


class OrderInfo(BaseObject):
    """
    Order information

    :param name: Name of the user
    :type name: :class:`String`
    :param phone_number: Phone number of the user
    :type phone_number: :class:`String`
    :param email_address: Email address of the user
    :type email_address: :class:`String`
    :param shipping_address: Shipping address for this order; may be null, defaults to None
    :type shipping_address: :class:`Address`, optional
    """

    ID: typing.Literal["orderInfo"] = "orderInfo"
    name: String
    phone_number: String
    email_address: String
    shipping_address: typing.Optional[Address] = None


class PageBlockAnchor(BaseObject):
    """
    An invisible anchor on a page, which can be used in a URL to open the page from the specified anchor

    :param name: Name of the anchor
    :type name: :class:`String`
    """

    ID: typing.Literal["pageBlockAnchor"] = "pageBlockAnchor"
    name: String


class PageBlockAnimation(BaseObject):
    """
    An animation

    :param caption: Animation caption
    :type caption: :class:`PageBlockCaption`
    :param animation: Animation file; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    :param need_autoplay: True, if the animation must be played automatically
    :type need_autoplay: :class:`Bool`
    """

    ID: typing.Literal["pageBlockAnimation"] = "pageBlockAnimation"
    caption: PageBlockCaption
    animation: typing.Optional[Animation] = None
    need_autoplay: Bool = False


class PageBlockAudio(BaseObject):
    """
    An audio file

    :param caption: Audio file caption
    :type caption: :class:`PageBlockCaption`
    :param audio: Audio file; may be null, defaults to None
    :type audio: :class:`Audio`, optional
    """

    ID: typing.Literal["pageBlockAudio"] = "pageBlockAudio"
    caption: PageBlockCaption
    audio: typing.Optional[Audio] = None


class PageBlockAuthorDate(BaseObject):
    """
    The author and publishing date of a page

    :param author: Author
    :type author: :class:`RichText`
    :param publish_date: Point in time (Unix timestamp) when the article was published; 0 if unknown, defaults to None
    :type publish_date: :class:`Int32`, optional
    """

    ID: typing.Literal["pageBlockAuthorDate"] = "pageBlockAuthorDate"
    author: RichText
    publish_date: typing.Optional[Int32] = 0


class PageBlockBlockQuote(BaseObject):
    """
    A block quote

    :param text: Quote text
    :type text: :class:`RichText`
    :param credit: Quote credit
    :type credit: :class:`RichText`
    """

    ID: typing.Literal["pageBlockBlockQuote"] = "pageBlockBlockQuote"
    text: RichText
    credit: RichText


class PageBlockChatLink(BaseObject):
    """
    A link to a chat

    :param title: Chat title
    :type title: :class:`String`
    :param username: Chat username by which all other information about the chat can be resolved
    :type username: :class:`String`
    :param photo: Chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    """

    ID: typing.Literal["pageBlockChatLink"] = "pageBlockChatLink"
    title: String
    username: String
    photo: typing.Optional[ChatPhotoInfo] = None


class PageBlockCollage(BaseObject):
    """
    A collage

    :param page_blocks: Collage item contents
    :type page_blocks: :class:`Vector[PageBlock]`
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    """

    ID: typing.Literal["pageBlockCollage"] = "pageBlockCollage"
    page_blocks: Vector[PageBlock]
    caption: PageBlockCaption


class PageBlockCover(BaseObject):
    """
    A page cover

    :param cover: Cover
    :type cover: :class:`PageBlock`
    """

    ID: typing.Literal["pageBlockCover"] = "pageBlockCover"
    cover: PageBlock


class PageBlockDetails(BaseObject):
    """
    A collapsible block

    :param header: Always visible heading for the block
    :type header: :class:`RichText`
    :param page_blocks: Block contents
    :type page_blocks: :class:`Vector[PageBlock]`
    :param is_open: True, if the block is open by default
    :type is_open: :class:`Bool`
    """

    ID: typing.Literal["pageBlockDetails"] = "pageBlockDetails"
    header: RichText
    page_blocks: Vector[PageBlock]
    is_open: Bool = False


class PageBlockDivider(BaseObject):
    """
    An empty block separating a page
    """

    ID: typing.Literal["pageBlockDivider"] = "pageBlockDivider"


class PageBlockEmbedded(BaseObject):
    """
    An embedded web page

    :param url: Web page URL, if available
    :type url: :class:`String`
    :param html: HTML-markup of the embedded page
    :type html: :class:`String`
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    :param poster_photo: Poster photo, if available; may be null, defaults to None
    :type poster_photo: :class:`Photo`, optional
    :param is_full_width: True, if the block must be full width
    :type is_full_width: :class:`Bool`
    :param allow_scrolling: True, if scrolling needs to be allowed
    :type allow_scrolling: :class:`Bool`
    :param width: Block width; 0 if unknown, defaults to None
    :type width: :class:`Int32`, optional
    :param height: Block height; 0 if unknown, defaults to None
    :type height: :class:`Int32`, optional
    """

    ID: typing.Literal["pageBlockEmbedded"] = "pageBlockEmbedded"
    url: String
    html: String
    caption: PageBlockCaption
    poster_photo: typing.Optional[Photo] = None
    is_full_width: Bool = False
    allow_scrolling: Bool = False
    width: typing.Optional[Int32] = 0
    height: typing.Optional[Int32] = 0


class PageBlockEmbeddedPost(BaseObject):
    """
    An embedded post

    :param url: Web page URL
    :type url: :class:`String`
    :param author: Post author
    :type author: :class:`String`
    :param page_blocks: Post content
    :type page_blocks: :class:`Vector[PageBlock]`
    :param caption: Post caption
    :type caption: :class:`PageBlockCaption`
    :param author_photo: Post author photo; may be null, defaults to None
    :type author_photo: :class:`Photo`, optional
    :param date: Point in time (Unix timestamp) when the post was created; 0 if unknown, defaults to None
    :type date: :class:`Int32`, optional
    """

    ID: typing.Literal["pageBlockEmbeddedPost"] = "pageBlockEmbeddedPost"
    url: String
    author: String
    page_blocks: Vector[PageBlock]
    caption: PageBlockCaption
    author_photo: typing.Optional[Photo] = None
    date: typing.Optional[Int32] = 0


class PageBlockFooter(BaseObject):
    """
    The footer of a page

    :param footer: Footer
    :type footer: :class:`RichText`
    """

    ID: typing.Literal["pageBlockFooter"] = "pageBlockFooter"
    footer: RichText


class PageBlockHeader(BaseObject):
    """
    A header

    :param header: Header
    :type header: :class:`RichText`
    """

    ID: typing.Literal["pageBlockHeader"] = "pageBlockHeader"
    header: RichText


class PageBlockKicker(BaseObject):
    """
    A kicker

    :param kicker: Kicker
    :type kicker: :class:`RichText`
    """

    ID: typing.Literal["pageBlockKicker"] = "pageBlockKicker"
    kicker: RichText


class PageBlockList(BaseObject):
    """
    A list of data blocks

    :param items: The items of the list
    :type items: :class:`Vector[PageBlockListItem]`
    """

    ID: typing.Literal["pageBlockList"] = "pageBlockList"
    items: Vector[PageBlockListItem]


class PageBlockMap(BaseObject):
    """
    A map

    :param location: Location of the map center
    :type location: :class:`Location`
    :param zoom: Map zoom level
    :type zoom: :class:`Int32`
    :param width: Map width
    :type width: :class:`Int32`
    :param height: Map height
    :type height: :class:`Int32`
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    """

    ID: typing.Literal["pageBlockMap"] = "pageBlockMap"
    location: Location
    zoom: Int32
    width: Int32
    height: Int32
    caption: PageBlockCaption


class PageBlockParagraph(BaseObject):
    """
    A text paragraph

    :param text: Paragraph text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["pageBlockParagraph"] = "pageBlockParagraph"
    text: RichText


class PageBlockPhoto(BaseObject):
    """
    A photo

    :param caption: Photo caption
    :type caption: :class:`PageBlockCaption`
    :param url: URL that needs to be opened when the photo is clicked
    :type url: :class:`String`
    :param photo: Photo file; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    """

    ID: typing.Literal["pageBlockPhoto"] = "pageBlockPhoto"
    caption: PageBlockCaption
    url: String
    photo: typing.Optional[Photo] = None


class PageBlockPreformatted(BaseObject):
    """
    A preformatted text paragraph

    :param text: Paragraph text
    :type text: :class:`RichText`
    :param language: Programming language for which the text needs to be formatted
    :type language: :class:`String`
    """

    ID: typing.Literal["pageBlockPreformatted"] = "pageBlockPreformatted"
    text: RichText
    language: String


class PageBlockPullQuote(BaseObject):
    """
    A pull quote

    :param text: Quote text
    :type text: :class:`RichText`
    :param credit: Quote credit
    :type credit: :class:`RichText`
    """

    ID: typing.Literal["pageBlockPullQuote"] = "pageBlockPullQuote"
    text: RichText
    credit: RichText


class PageBlockRelatedArticles(BaseObject):
    """
    Related articles

    :param header: Block header
    :type header: :class:`RichText`
    :param articles: List of related articles
    :type articles: :class:`Vector[PageBlockRelatedArticle]`
    """

    ID: typing.Literal["pageBlockRelatedArticles"] = "pageBlockRelatedArticles"
    header: RichText
    articles: Vector[PageBlockRelatedArticle]


class PageBlockSlideshow(BaseObject):
    """
    A slideshow

    :param page_blocks: Slideshow item contents
    :type page_blocks: :class:`Vector[PageBlock]`
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    """

    ID: typing.Literal["pageBlockSlideshow"] = "pageBlockSlideshow"
    page_blocks: Vector[PageBlock]
    caption: PageBlockCaption


class PageBlockSubheader(BaseObject):
    """
    A subheader

    :param subheader: Subheader
    :type subheader: :class:`RichText`
    """

    ID: typing.Literal["pageBlockSubheader"] = "pageBlockSubheader"
    subheader: RichText


class PageBlockSubtitle(BaseObject):
    """
    The subtitle of a page

    :param subtitle: Subtitle
    :type subtitle: :class:`RichText`
    """

    ID: typing.Literal["pageBlockSubtitle"] = "pageBlockSubtitle"
    subtitle: RichText


class PageBlockTable(BaseObject):
    """
    A table

    :param caption: Table caption
    :type caption: :class:`RichText`
    :param cells: Table cells
    :type cells: :class:`Vector[Vector[PageBlockTableCell]]`
    :param is_bordered: True, if the table is bordered
    :type is_bordered: :class:`Bool`
    :param is_striped: True, if the table is striped
    :type is_striped: :class:`Bool`
    """

    ID: typing.Literal["pageBlockTable"] = "pageBlockTable"
    caption: RichText
    cells: Vector[Vector[PageBlockTableCell]]
    is_bordered: Bool = False
    is_striped: Bool = False


class PageBlockTitle(BaseObject):
    """
    The title of a page

    :param title: Title
    :type title: :class:`RichText`
    """

    ID: typing.Literal["pageBlockTitle"] = "pageBlockTitle"
    title: RichText


class PageBlockVideo(BaseObject):
    """
    A video

    :param caption: Video caption
    :type caption: :class:`PageBlockCaption`
    :param video: Video file; may be null, defaults to None
    :type video: :class:`Video`, optional
    :param need_autoplay: True, if the video must be played automatically
    :type need_autoplay: :class:`Bool`
    :param is_looped: True, if the video must be looped
    :type is_looped: :class:`Bool`
    """

    ID: typing.Literal["pageBlockVideo"] = "pageBlockVideo"
    caption: PageBlockCaption
    video: typing.Optional[Video] = None
    need_autoplay: Bool = False
    is_looped: Bool = False


class PageBlockVoiceNote(BaseObject):
    """
    A voice note

    :param caption: Voice note caption
    :type caption: :class:`PageBlockCaption`
    :param voice_note: Voice note; may be null, defaults to None
    :type voice_note: :class:`VoiceNote`, optional
    """

    ID: typing.Literal["pageBlockVoiceNote"] = "pageBlockVoiceNote"
    caption: PageBlockCaption
    voice_note: typing.Optional[VoiceNote] = None


PageBlock = typing.Union[
    PageBlockAnchor,
    PageBlockAnimation,
    PageBlockAudio,
    PageBlockAuthorDate,
    PageBlockBlockQuote,
    PageBlockChatLink,
    PageBlockCollage,
    PageBlockCover,
    PageBlockDetails,
    PageBlockDivider,
    PageBlockEmbedded,
    PageBlockEmbeddedPost,
    PageBlockFooter,
    PageBlockHeader,
    PageBlockKicker,
    PageBlockList,
    PageBlockMap,
    PageBlockParagraph,
    PageBlockPhoto,
    PageBlockPreformatted,
    PageBlockPullQuote,
    PageBlockRelatedArticles,
    PageBlockSlideshow,
    PageBlockSubheader,
    PageBlockSubtitle,
    PageBlockTable,
    PageBlockTitle,
    PageBlockVideo,
    PageBlockVoiceNote,
]


class PageBlockListItem(BaseObject):
    """
    Describes an item of a list page block

    :param label: Item label
    :type label: :class:`String`
    :param page_blocks: Item blocks
    :type page_blocks: :class:`Vector[PageBlock]`
    """

    ID: typing.Literal["pageBlockListItem"] = "pageBlockListItem"
    label: String
    page_blocks: Vector[PageBlock]


class PageBlockCaption(BaseObject):
    """
    Contains a caption of an instant view web page block, consisting of a text and a trailing credit

    :param text: Content of the caption
    :type text: :class:`RichText`
    :param credit: Block credit (like HTML tag <cite>)
    :type credit: :class:`RichText`
    """

    ID: typing.Literal["pageBlockCaption"] = "pageBlockCaption"
    text: RichText
    credit: RichText


class PageBlockHorizontalAlignmentCenter(BaseObject):
    """
    The content must be center-aligned
    """

    ID: typing.Literal["pageBlockHorizontalAlignmentCenter"] = "pageBlockHorizontalAlignmentCenter"


class PageBlockHorizontalAlignmentLeft(BaseObject):
    """
    The content must be left-aligned
    """

    ID: typing.Literal["pageBlockHorizontalAlignmentLeft"] = "pageBlockHorizontalAlignmentLeft"


class PageBlockHorizontalAlignmentRight(BaseObject):
    """
    The content must be right-aligned
    """

    ID: typing.Literal["pageBlockHorizontalAlignmentRight"] = "pageBlockHorizontalAlignmentRight"


PageBlockHorizontalAlignment = typing.Union[
    PageBlockHorizontalAlignmentCenter,
    PageBlockHorizontalAlignmentLeft,
    PageBlockHorizontalAlignmentRight,
]


class PageBlockRelatedArticle(BaseObject):
    """
    Contains information about a related article

    :param url: Related article URL
    :type url: :class:`String`
    :param photo: Article photo; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    :param title: Article title; may be empty
    :type title: :class:`String`
    :param description: Article description; may be empty
    :type description: :class:`String`
    :param author: Article author; may be empty
    :type author: :class:`String`
    :param publish_date: Point in time (Unix timestamp) when the article was published; 0 if unknown, defaults to None
    :type publish_date: :class:`Int32`, optional
    """

    ID: typing.Literal["pageBlockRelatedArticle"] = "pageBlockRelatedArticle"
    url: String
    photo: typing.Optional[Photo] = None
    title: String = ""
    description: String = ""
    author: String = ""
    publish_date: typing.Optional[Int32] = 0


class PageBlockTableCell(BaseObject):
    """
    Represents a cell of a table

    :param colspan: The number of columns the cell spans
    :type colspan: :class:`Int32`
    :param rowspan: The number of rows the cell spans
    :type rowspan: :class:`Int32`
    :param align: Horizontal cell content alignment
    :type align: :class:`PageBlockHorizontalAlignment`
    :param valign: Vertical cell content alignment
    :type valign: :class:`PageBlockVerticalAlignment`
    :param text: Cell text; may be null. If the text is null, then the cell must be invisible, defaults to None
    :type text: :class:`RichText`, optional
    :param is_header: True, if it is a header cell
    :type is_header: :class:`Bool`
    """

    ID: typing.Literal["pageBlockTableCell"] = "pageBlockTableCell"
    colspan: Int32
    rowspan: Int32
    align: PageBlockHorizontalAlignment
    valign: PageBlockVerticalAlignment
    text: typing.Optional[RichText] = None
    is_header: Bool = False


class PageBlockVerticalAlignmentBottom(BaseObject):
    """
    The content must be bottom-aligned
    """

    ID: typing.Literal["pageBlockVerticalAlignmentBottom"] = "pageBlockVerticalAlignmentBottom"


class PageBlockVerticalAlignmentMiddle(BaseObject):
    """
    The content must be middle-aligned
    """

    ID: typing.Literal["pageBlockVerticalAlignmentMiddle"] = "pageBlockVerticalAlignmentMiddle"


class PageBlockVerticalAlignmentTop(BaseObject):
    """
    The content must be top-aligned
    """

    ID: typing.Literal["pageBlockVerticalAlignmentTop"] = "pageBlockVerticalAlignmentTop"


PageBlockVerticalAlignment = typing.Union[
    PageBlockVerticalAlignmentBottom,
    PageBlockVerticalAlignmentMiddle,
    PageBlockVerticalAlignmentTop,
]


class PassportAuthorizationForm(BaseObject):
    """
    Contains information about a Telegram Passport authorization form that was requested

    :param id: Unique identifier of the authorization form
    :type id: :class:`Int32`
    :param required_elements: Telegram Passport elements that must be provided to complete the form
    :type required_elements: :class:`Vector[PassportRequiredElement]`
    :param privacy_policy_url: URL for the privacy policy of the service; may be empty
    :type privacy_policy_url: :class:`String`
    """

    ID: typing.Literal["passportAuthorizationForm"] = "passportAuthorizationForm"
    id: Int32
    required_elements: Vector[PassportRequiredElement]
    privacy_policy_url: String = ""


class PassportElementAddress(BaseObject):
    """
    A Telegram Passport element containing the user's address

    :param address: Address
    :type address: :class:`Address`
    """

    ID: typing.Literal["passportElementAddress"] = "passportElementAddress"
    address: Address


class PassportElementBankStatement(BaseObject):
    """
    A Telegram Passport element containing the user's bank statement

    :param bank_statement: Bank statement
    :type bank_statement: :class:`PersonalDocument`
    """

    ID: typing.Literal["passportElementBankStatement"] = "passportElementBankStatement"
    bank_statement: PersonalDocument


class PassportElementDriverLicense(BaseObject):
    """
    A Telegram Passport element containing the user's driver license

    :param driver_license: Driver license
    :type driver_license: :class:`IdentityDocument`
    """

    ID: typing.Literal["passportElementDriverLicense"] = "passportElementDriverLicense"
    driver_license: IdentityDocument


class PassportElementEmailAddress(BaseObject):
    """
    A Telegram Passport element containing the user's email address

    :param email_address: Email address
    :type email_address: :class:`String`
    """

    ID: typing.Literal["passportElementEmailAddress"] = "passportElementEmailAddress"
    email_address: String


class PassportElementIdentityCard(BaseObject):
    """
    A Telegram Passport element containing the user's identity card

    :param identity_card: Identity card
    :type identity_card: :class:`IdentityDocument`
    """

    ID: typing.Literal["passportElementIdentityCard"] = "passportElementIdentityCard"
    identity_card: IdentityDocument


class PassportElementInternalPassport(BaseObject):
    """
    A Telegram Passport element containing the user's internal passport

    :param internal_passport: Internal passport
    :type internal_passport: :class:`IdentityDocument`
    """

    ID: typing.Literal["passportElementInternalPassport"] = "passportElementInternalPassport"
    internal_passport: IdentityDocument


class PassportElementPassport(BaseObject):
    """
    A Telegram Passport element containing the user's passport

    :param passport: Passport
    :type passport: :class:`IdentityDocument`
    """

    ID: typing.Literal["passportElementPassport"] = "passportElementPassport"
    passport: IdentityDocument


class PassportElementPassportRegistration(BaseObject):
    """
    A Telegram Passport element containing the user's passport registration pages

    :param passport_registration: Passport registration pages
    :type passport_registration: :class:`PersonalDocument`
    """

    ID: typing.Literal["passportElementPassportRegistration"] = "passportElementPassportRegistration"
    passport_registration: PersonalDocument


class PassportElementPersonalDetails(BaseObject):
    """
    A Telegram Passport element containing the user's personal details

    :param personal_details: Personal details of the user
    :type personal_details: :class:`PersonalDetails`
    """

    ID: typing.Literal["passportElementPersonalDetails"] = "passportElementPersonalDetails"
    personal_details: PersonalDetails


class PassportElementPhoneNumber(BaseObject):
    """
    A Telegram Passport element containing the user's phone number

    :param phone_number: Phone number
    :type phone_number: :class:`String`
    """

    ID: typing.Literal["passportElementPhoneNumber"] = "passportElementPhoneNumber"
    phone_number: String


class PassportElementRentalAgreement(BaseObject):
    """
    A Telegram Passport element containing the user's rental agreement

    :param rental_agreement: Rental agreement
    :type rental_agreement: :class:`PersonalDocument`
    """

    ID: typing.Literal["passportElementRentalAgreement"] = "passportElementRentalAgreement"
    rental_agreement: PersonalDocument


class PassportElementTemporaryRegistration(BaseObject):
    """
    A Telegram Passport element containing the user's temporary registration

    :param temporary_registration: Temporary registration
    :type temporary_registration: :class:`PersonalDocument`
    """

    ID: typing.Literal["passportElementTemporaryRegistration"] = "passportElementTemporaryRegistration"
    temporary_registration: PersonalDocument


class PassportElementUtilityBill(BaseObject):
    """
    A Telegram Passport element containing the user's utility bill

    :param utility_bill: Utility bill
    :type utility_bill: :class:`PersonalDocument`
    """

    ID: typing.Literal["passportElementUtilityBill"] = "passportElementUtilityBill"
    utility_bill: PersonalDocument


PassportElement = typing.Union[
    PassportElementAddress,
    PassportElementBankStatement,
    PassportElementDriverLicense,
    PassportElementEmailAddress,
    PassportElementIdentityCard,
    PassportElementInternalPassport,
    PassportElementPassport,
    PassportElementPassportRegistration,
    PassportElementPersonalDetails,
    PassportElementPhoneNumber,
    PassportElementRentalAgreement,
    PassportElementTemporaryRegistration,
    PassportElementUtilityBill,
]


class PassportElementError(BaseObject):
    """
    Contains the description of an error in a Telegram Passport element

    :param type_: Type of the Telegram Passport element which has the error
    :type type_: :class:`PassportElementType`
    :param message: Error message
    :type message: :class:`String`
    :param source: Error source
    :type source: :class:`PassportElementErrorSource`
    """

    ID: typing.Literal["passportElementError"] = "passportElementError"
    type_: PassportElementType = Field(..., alias="type")
    message: String
    source: PassportElementErrorSource


class PassportElementErrorSourceDataField(BaseObject):
    """
    One of the data fields contains an error. The error will be considered resolved when the value of the field changes

    :param field_name: Field name
    :type field_name: :class:`String`
    """

    ID: typing.Literal["passportElementErrorSourceDataField"] = "passportElementErrorSourceDataField"
    field_name: String


class PassportElementErrorSourceFile(BaseObject):
    """
    The file contains an error. The error will be considered resolved when the file changes

    :param file_index: Index of a file with the error
    :type file_index: :class:`Int32`
    """

    ID: typing.Literal["passportElementErrorSourceFile"] = "passportElementErrorSourceFile"
    file_index: Int32


class PassportElementErrorSourceFiles(BaseObject):
    """
    The list of attached files contains an error. The error will be considered resolved when the list of files changes
    """

    ID: typing.Literal["passportElementErrorSourceFiles"] = "passportElementErrorSourceFiles"


class PassportElementErrorSourceFrontSide(BaseObject):
    """
    The front side of the document contains an error. The error will be considered resolved when the file with the front side changes
    """

    ID: typing.Literal["passportElementErrorSourceFrontSide"] = "passportElementErrorSourceFrontSide"


class PassportElementErrorSourceReverseSide(BaseObject):
    """
    The reverse side of the document contains an error. The error will be considered resolved when the file with the reverse side changes
    """

    ID: typing.Literal["passportElementErrorSourceReverseSide"] = "passportElementErrorSourceReverseSide"


class PassportElementErrorSourceSelfie(BaseObject):
    """
    The selfie with the document contains an error. The error will be considered resolved when the file with the selfie changes
    """

    ID: typing.Literal["passportElementErrorSourceSelfie"] = "passportElementErrorSourceSelfie"


class PassportElementErrorSourceTranslationFile(BaseObject):
    """
    One of files with the translation of the document contains an error. The error will be considered resolved when the file changes

    :param file_index: Index of a file with the error
    :type file_index: :class:`Int32`
    """

    ID: typing.Literal["passportElementErrorSourceTranslationFile"] = "passportElementErrorSourceTranslationFile"
    file_index: Int32


class PassportElementErrorSourceTranslationFiles(BaseObject):
    """
    The translation of the document contains an error. The error will be considered resolved when the list of translation files changes
    """

    ID: typing.Literal["passportElementErrorSourceTranslationFiles"] = "passportElementErrorSourceTranslationFiles"


class PassportElementErrorSourceUnspecified(BaseObject):
    """
    The element contains an error in an unspecified place. The error will be considered resolved when new data is added
    """

    ID: typing.Literal["passportElementErrorSourceUnspecified"] = "passportElementErrorSourceUnspecified"


PassportElementErrorSource = typing.Union[
    PassportElementErrorSourceDataField,
    PassportElementErrorSourceFile,
    PassportElementErrorSourceFiles,
    PassportElementErrorSourceFrontSide,
    PassportElementErrorSourceReverseSide,
    PassportElementErrorSourceSelfie,
    PassportElementErrorSourceTranslationFile,
    PassportElementErrorSourceTranslationFiles,
    PassportElementErrorSourceUnspecified,
]


class PassportElementTypeAddress(BaseObject):
    """
    A Telegram Passport element containing the user's address
    """

    ID: typing.Literal["passportElementTypeAddress"] = "passportElementTypeAddress"


class PassportElementTypeBankStatement(BaseObject):
    """
    A Telegram Passport element containing the user's bank statement
    """

    ID: typing.Literal["passportElementTypeBankStatement"] = "passportElementTypeBankStatement"


class PassportElementTypeDriverLicense(BaseObject):
    """
    A Telegram Passport element containing the user's driver license
    """

    ID: typing.Literal["passportElementTypeDriverLicense"] = "passportElementTypeDriverLicense"


class PassportElementTypeEmailAddress(BaseObject):
    """
    A Telegram Passport element containing the user's email address
    """

    ID: typing.Literal["passportElementTypeEmailAddress"] = "passportElementTypeEmailAddress"


class PassportElementTypeIdentityCard(BaseObject):
    """
    A Telegram Passport element containing the user's identity card
    """

    ID: typing.Literal["passportElementTypeIdentityCard"] = "passportElementTypeIdentityCard"


class PassportElementTypeInternalPassport(BaseObject):
    """
    A Telegram Passport element containing the user's internal passport
    """

    ID: typing.Literal["passportElementTypeInternalPassport"] = "passportElementTypeInternalPassport"


class PassportElementTypePassport(BaseObject):
    """
    A Telegram Passport element containing the user's passport
    """

    ID: typing.Literal["passportElementTypePassport"] = "passportElementTypePassport"


class PassportElementTypePassportRegistration(BaseObject):
    """
    A Telegram Passport element containing the registration page of the user's passport
    """

    ID: typing.Literal["passportElementTypePassportRegistration"] = "passportElementTypePassportRegistration"


class PassportElementTypePersonalDetails(BaseObject):
    """
    A Telegram Passport element containing the user's personal details
    """

    ID: typing.Literal["passportElementTypePersonalDetails"] = "passportElementTypePersonalDetails"


class PassportElementTypePhoneNumber(BaseObject):
    """
    A Telegram Passport element containing the user's phone number
    """

    ID: typing.Literal["passportElementTypePhoneNumber"] = "passportElementTypePhoneNumber"


class PassportElementTypeRentalAgreement(BaseObject):
    """
    A Telegram Passport element containing the user's rental agreement
    """

    ID: typing.Literal["passportElementTypeRentalAgreement"] = "passportElementTypeRentalAgreement"


class PassportElementTypeTemporaryRegistration(BaseObject):
    """
    A Telegram Passport element containing the user's temporary registration
    """

    ID: typing.Literal["passportElementTypeTemporaryRegistration"] = "passportElementTypeTemporaryRegistration"


class PassportElementTypeUtilityBill(BaseObject):
    """
    A Telegram Passport element containing the user's utility bill
    """

    ID: typing.Literal["passportElementTypeUtilityBill"] = "passportElementTypeUtilityBill"


PassportElementType = typing.Union[
    PassportElementTypeAddress,
    PassportElementTypeBankStatement,
    PassportElementTypeDriverLicense,
    PassportElementTypeEmailAddress,
    PassportElementTypeIdentityCard,
    PassportElementTypeInternalPassport,
    PassportElementTypePassport,
    PassportElementTypePassportRegistration,
    PassportElementTypePersonalDetails,
    PassportElementTypePhoneNumber,
    PassportElementTypeRentalAgreement,
    PassportElementTypeTemporaryRegistration,
    PassportElementTypeUtilityBill,
]


class PassportElements(BaseObject):
    """
    Contains information about saved Telegram Passport elements

    :param elements: Telegram Passport elements
    :type elements: :class:`Vector[PassportElement]`
    """

    ID: typing.Literal["passportElements"] = "passportElements"
    elements: Vector[PassportElement]


class PassportElementsWithErrors(BaseObject):
    """
    Contains information about a Telegram Passport elements and corresponding errors

    :param elements: Telegram Passport elements
    :type elements: :class:`Vector[PassportElement]`
    :param errors: Errors in the elements that are already available
    :type errors: :class:`Vector[PassportElementError]`
    """

    ID: typing.Literal["passportElementsWithErrors"] = "passportElementsWithErrors"
    elements: Vector[PassportElement]
    errors: Vector[PassportElementError]


class PassportRequiredElement(BaseObject):
    """
    Contains a description of the required Telegram Passport element that was requested by a service

    :param suitable_elements: List of Telegram Passport elements any of which is enough to provide
    :type suitable_elements: :class:`Vector[PassportSuitableElement]`
    """

    ID: typing.Literal["passportRequiredElement"] = "passportRequiredElement"
    suitable_elements: Vector[PassportSuitableElement]


class PassportSuitableElement(BaseObject):
    """
    Contains information about a Telegram Passport element that was requested by a service

    :param type_: Type of the element
    :type type_: :class:`PassportElementType`
    :param is_selfie_required: True, if a selfie is required with the identity document
    :type is_selfie_required: :class:`Bool`
    :param is_translation_required: True, if a certified English translation is required with the document
    :type is_translation_required: :class:`Bool`
    :param is_native_name_required: True, if personal details must include the user's name in the language of their country of residence
    :type is_native_name_required: :class:`Bool`
    """

    ID: typing.Literal["passportSuitableElement"] = "passportSuitableElement"
    type_: PassportElementType = Field(..., alias="type")
    is_selfie_required: Bool = False
    is_translation_required: Bool = False
    is_native_name_required: Bool = False


class PasswordState(BaseObject):
    """
    Represents the current state of 2-step verification

    :param login_email_address_pattern: Pattern of the email address set up for logging in
    :type login_email_address_pattern: :class:`String`
    :param recovery_email_address_code_info: Information about the recovery email address to which the confirmation email was sent; may be null, defaults to None
    :type recovery_email_address_code_info: :class:`EmailAddressAuthenticationCodeInfo`, optional
    :param has_password: True, if a 2-step verification password is set
    :type has_password: :class:`Bool`
    :param password_hint: Hint for the password; may be empty
    :type password_hint: :class:`String`
    :param has_recovery_email_address: True, if a recovery email is set
    :type has_recovery_email_address: :class:`Bool`
    :param has_passport_data: True, if some Telegram Passport elements were saved
    :type has_passport_data: :class:`Bool`
    :param pending_reset_date: If not 0, point in time (Unix timestamp) after which the 2-step verification password can be reset immediately using resetPassword
    :type pending_reset_date: :class:`Int32`
    """

    ID: typing.Literal["passwordState"] = "passwordState"
    login_email_address_pattern: String
    recovery_email_address_code_info: typing.Optional[EmailAddressAuthenticationCodeInfo] = None
    has_password: Bool = False
    password_hint: String = ""
    has_recovery_email_address: Bool = False
    has_passport_data: Bool = False
    pending_reset_date: Int32 = 0


class PaymentForm(BaseObject):
    """
    Contains information about an invoice payment form

    :param id: The payment form identifier
    :type id: :class:`Int64`
    :param invoice: Full information about the invoice
    :type invoice: :class:`Invoice`
    :param seller_bot_user_id: User identifier of the seller bot
    :type seller_bot_user_id: :class:`Int53`
    :param payment_provider_user_id: User identifier of the payment provider bot
    :type payment_provider_user_id: :class:`Int53`
    :param payment_provider: Information about the payment provider
    :type payment_provider: :class:`PaymentProvider`
    :param additional_payment_options: The list of additional payment options
    :type additional_payment_options: :class:`Vector[PaymentOption]`
    :param saved_credentials: The list of saved payment credentials
    :type saved_credentials: :class:`Vector[SavedCredentials]`
    :param product_title: Product title
    :type product_title: :class:`String`
    :param product_description: Product description
    :type product_description: :class:`FormattedText`
    :param saved_order_info: Saved server-side order information; may be null, defaults to None
    :type saved_order_info: :class:`OrderInfo`, optional
    :param product_photo: Product photo; may be null, defaults to None
    :type product_photo: :class:`Photo`, optional
    :param can_save_credentials: True, if the user can choose to save credentials
    :type can_save_credentials: :class:`Bool`
    :param need_password: True, if the user will be able to save credentials, if sets up a 2-step verification password
    :type need_password: :class:`Bool`
    """

    ID: typing.Literal["paymentForm"] = "paymentForm"
    id: Int64
    invoice: Invoice
    seller_bot_user_id: Int53
    payment_provider_user_id: Int53
    payment_provider: PaymentProvider
    additional_payment_options: Vector[PaymentOption]
    saved_credentials: Vector[SavedCredentials]
    product_title: String
    product_description: FormattedText
    saved_order_info: typing.Optional[OrderInfo] = None
    product_photo: typing.Optional[Photo] = None
    can_save_credentials: Bool = False
    need_password: Bool = False


class PaymentOption(BaseObject):
    """
    Describes an additional payment option

    :param title: Title for the payment option
    :type title: :class:`String`
    :param url: Payment form URL to be opened in a web view
    :type url: :class:`String`
    """

    ID: typing.Literal["paymentOption"] = "paymentOption"
    title: String
    url: String


class PaymentProviderOther(BaseObject):
    """
    Some other payment provider, for which a web payment form must be shown

    :param url: Payment form URL
    :type url: :class:`String`
    """

    ID: typing.Literal["paymentProviderOther"] = "paymentProviderOther"
    url: String


class PaymentProviderSmartGlocal(BaseObject):
    """
    Smart Glocal payment provider

    :param public_token: Public payment token
    :type public_token: :class:`String`
    """

    ID: typing.Literal["paymentProviderSmartGlocal"] = "paymentProviderSmartGlocal"
    public_token: String


class PaymentProviderStripe(BaseObject):
    """
    Stripe payment provider

    :param publishable_key: Stripe API publishable key
    :type publishable_key: :class:`String`
    :param need_country: True, if the user country must be provided
    :type need_country: :class:`Bool`
    :param need_postal_code: True, if the user ZIP/postal code must be provided
    :type need_postal_code: :class:`Bool`
    :param need_cardholder_name: True, if the cardholder name must be provided
    :type need_cardholder_name: :class:`Bool`
    """

    ID: typing.Literal["paymentProviderStripe"] = "paymentProviderStripe"
    publishable_key: String
    need_country: Bool = False
    need_postal_code: Bool = False
    need_cardholder_name: Bool = False


PaymentProvider = typing.Union[
    PaymentProviderOther,
    PaymentProviderSmartGlocal,
    PaymentProviderStripe,
]


class PaymentReceipt(BaseObject):
    """
    Contains information about a successful payment

    :param title: Product title
    :type title: :class:`String`
    :param description: Product description
    :type description: :class:`FormattedText`
    :param date: Point in time (Unix timestamp) when the payment was made
    :type date: :class:`Int32`
    :param seller_bot_user_id: User identifier of the seller bot
    :type seller_bot_user_id: :class:`Int53`
    :param payment_provider_user_id: User identifier of the payment provider bot
    :type payment_provider_user_id: :class:`Int53`
    :param invoice: Information about the invoice
    :type invoice: :class:`Invoice`
    :param credentials_title: Title of the saved credentials chosen by the buyer
    :type credentials_title: :class:`String`
    :param tip_amount: The amount of tip chosen by the buyer in the smallest units of the currency
    :type tip_amount: :class:`Int53`
    :param photo: Product photo; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    :param order_info: Order information; may be null, defaults to None
    :type order_info: :class:`OrderInfo`, optional
    :param shipping_option: Chosen shipping option; may be null, defaults to None
    :type shipping_option: :class:`ShippingOption`, optional
    """

    ID: typing.Literal["paymentReceipt"] = "paymentReceipt"
    title: String
    description: FormattedText
    date: Int32
    seller_bot_user_id: Int53
    payment_provider_user_id: Int53
    invoice: Invoice
    credentials_title: String
    tip_amount: Int53
    photo: typing.Optional[Photo] = None
    order_info: typing.Optional[OrderInfo] = None
    shipping_option: typing.Optional[ShippingOption] = None


class PaymentResult(BaseObject):
    """
    Contains the result of a payment request

    :param verification_url: URL for additional payment credentials verification
    :type verification_url: :class:`String`
    :param success: True, if the payment request was successful; otherwise, the verification_url will be non-empty
    :type success: :class:`Bool`
    """

    ID: typing.Literal["paymentResult"] = "paymentResult"
    verification_url: String
    success: Bool = False


class PersonalDetails(BaseObject):
    """
    Contains the user's personal details

    :param first_name: First name of the user written in English; 1-255 characters
    :type first_name: :class:`String`
    :param last_name: Last name of the user written in English; 1-255 characters
    :type last_name: :class:`String`
    :param native_first_name: Native first name of the user; 1-255 characters
    :type native_first_name: :class:`String`
    :param native_last_name: Native last name of the user; 1-255 characters
    :type native_last_name: :class:`String`
    :param birthdate: Birthdate of the user
    :type birthdate: :class:`Date`
    :param gender: Gender of the user, "male" or "female"
    :type gender: :class:`String`
    :param country_code: A two-letter ISO 3166-1 alpha-2 country code of the user's country
    :type country_code: :class:`String`
    :param residence_country_code: A two-letter ISO 3166-1 alpha-2 country code of the user's residence country
    :type residence_country_code: :class:`String`
    :param middle_name: Middle name of the user written in English; 0-255 characters
    :type middle_name: :class:`String`
    :param native_middle_name: Native middle name of the user; 0-255 characters
    :type native_middle_name: :class:`String`
    """

    ID: typing.Literal["personalDetails"] = "personalDetails"
    first_name: String = Field(..., min_length=1, max_length=255)
    last_name: String = Field(..., min_length=1, max_length=255)
    native_first_name: String = Field(..., min_length=1, max_length=255)
    native_last_name: String = Field(..., min_length=1, max_length=255)
    birthdate: Date
    gender: String
    country_code: String
    residence_country_code: String
    middle_name: String = Field("", max_length=255)
    native_middle_name: String = Field("", max_length=255)


class PersonalDocument(BaseObject):
    """
    A personal document, containing some information about a user

    :param files: List of files containing the pages of the document
    :type files: :class:`Vector[DatedFile]`
    :param translation: List of files containing a certified English translation of the document
    :type translation: :class:`Vector[DatedFile]`
    """

    ID: typing.Literal["personalDocument"] = "personalDocument"
    files: Vector[DatedFile]
    translation: Vector[DatedFile]


class PhoneNumberAuthenticationSettings(BaseObject):
    """
    Contains settings for the authentication of the user's phone number

    :param authentication_tokens: List of up to 20 authentication tokens, recently received in updateOption("authentication_token") in previously logged out sessions
    :type authentication_tokens: :class:`Vector[String]`
    :param allow_flash_call: Pass true if the authentication code may be sent via a flash call to the specified phone number
    :type allow_flash_call: :class:`Bool`
    :param allow_missed_call: Pass true if the authentication code may be sent via a missed call to the specified phone number
    :type allow_missed_call: :class:`Bool`
    :param is_current_phone_number: Pass true if the authenticated phone number is used on the current device
    :type is_current_phone_number: :class:`Bool`
    :param allow_sms_retriever_api: For official applications only. True, if the application can use Android SMS Retriever API (requires Google Play Services >= 10.2) to automatically receive the authentication code from the SMS. See https://developers.google.com/identity/sms-retriever/ for more details
    :type allow_sms_retriever_api: :class:`Bool`
    :param firebase_authentication_settings: For official Android and iOS applications only; pass null otherwise. Settings for Firebase Authentication, defaults to None
    :type firebase_authentication_settings: :class:`FirebaseAuthenticationSettings`, optional
    """

    ID: typing.Literal["phoneNumberAuthenticationSettings"] = "phoneNumberAuthenticationSettings"
    authentication_tokens: Vector[String]
    allow_flash_call: Bool = False
    allow_missed_call: Bool = False
    is_current_phone_number: Bool = False
    allow_sms_retriever_api: Bool = False
    firebase_authentication_settings: typing.Optional[FirebaseAuthenticationSettings] = None


class PhoneNumberInfo(BaseObject):
    """
    Contains information about a phone number

    :param country_calling_code: The part of the phone number denoting country calling code or its part
    :type country_calling_code: :class:`String`
    :param formatted_phone_number: The phone number without country calling code formatted accordingly to local rules. Expected digits are returned as '-', but even more digits might be entered by the user
    :type formatted_phone_number: :class:`String`
    :param country: Information about the country to which the phone number belongs; may be null, defaults to None
    :type country: :class:`CountryInfo`, optional
    :param is_anonymous: True, if the phone number was bought on Fragment and isn't tied to a SIM card
    :type is_anonymous: :class:`Bool`
    """

    ID: typing.Literal["phoneNumberInfo"] = "phoneNumberInfo"
    country_calling_code: String
    formatted_phone_number: String
    country: typing.Optional[CountryInfo] = None
    is_anonymous: Bool = False


class Photo(BaseObject):
    """
    Describes a photo

    :param sizes: Available variants of the photo, in different sizes
    :type sizes: :class:`Vector[PhotoSize]`
    :param minithumbnail: Photo minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param has_stickers: True, if stickers were added to the photo. The list of corresponding sticker sets can be received using getAttachedStickerSets
    :type has_stickers: :class:`Bool`
    """

    ID: typing.Literal["photo"] = "photo"
    sizes: Vector[PhotoSize]
    minithumbnail: typing.Optional[Minithumbnail] = None
    has_stickers: Bool = False


class PhotoSize(BaseObject):
    """
    Describes an image in JPEG format

    :param type_: Image type (see https://core.telegram.org/constructor/photoSize)
    :type type_: :class:`String`
    :param photo: Information about the image file
    :type photo: :class:`File`
    :param width: Image width
    :type width: :class:`Int32`
    :param height: Image height
    :type height: :class:`Int32`
    :param progressive_sizes: Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image; in bytes
    :type progressive_sizes: :class:`Vector[Int32]`
    """

    ID: typing.Literal["photoSize"] = "photoSize"
    type_: String = Field(..., alias="type")
    photo: File
    width: Int32
    height: Int32
    progressive_sizes: Vector[Int32]


class Point(BaseObject):
    """
    A point on a Cartesian plane

    :param x: The point's first coordinate
    :type x: :class:`Double`
    :param y: The point's second coordinate
    :type y: :class:`Double`
    """

    ID: typing.Literal["point"] = "point"
    x: Double
    y: Double


class Poll(BaseObject):
    """
    Describes a poll

    :param id: Unique poll identifier
    :type id: :class:`Int64`
    :param question: Poll question; 1-300 characters
    :type question: :class:`String`
    :param options: List of poll answer options
    :type options: :class:`Vector[PollOption]`
    :param total_voter_count: Total number of voters, participating in the poll
    :type total_voter_count: :class:`Int32`
    :param recent_voter_ids: Identifiers of recent voters, if the poll is non-anonymous
    :type recent_voter_ids: :class:`Vector[MessageSender]`
    :param type_: Type of the poll
    :type type_: :class:`PollType`
    :param open_period: Amount of time the poll will be active after creation, in seconds
    :type open_period: :class:`Int32`
    :param close_date: Point in time (Unix timestamp) when the poll will automatically be closed
    :type close_date: :class:`Int32`
    :param is_anonymous: True, if the poll is anonymous
    :type is_anonymous: :class:`Bool`
    :param is_closed: True, if the poll is closed
    :type is_closed: :class:`Bool`
    """

    ID: typing.Literal["poll"] = "poll"
    id: Int64
    question: String = Field(..., min_length=1, max_length=300)
    options: Vector[PollOption]
    total_voter_count: Int32
    recent_voter_ids: Vector[MessageSender]
    type_: PollType = Field(..., alias="type")
    open_period: Int32
    close_date: Int32
    is_anonymous: Bool = False
    is_closed: Bool = False


class PollOption(BaseObject):
    """
    Describes one answer option of a poll

    :param text: Option text; 1-100 characters
    :type text: :class:`String`
    :param voter_count: Number of voters for this option, available only for closed or voted polls
    :type voter_count: :class:`Int32`
    :param vote_percentage: The percentage of votes for this option; 0-100
    :type vote_percentage: :class:`Int32`
    :param is_chosen: True, if the option was chosen by the user
    :type is_chosen: :class:`Bool`
    :param is_being_chosen: True, if the option is being chosen by a pending setPollAnswer request
    :type is_being_chosen: :class:`Bool`
    """

    ID: typing.Literal["pollOption"] = "pollOption"
    text: String = Field(..., min_length=1, max_length=100)
    voter_count: Int32
    vote_percentage: Int32
    is_chosen: Bool = False
    is_being_chosen: Bool = False


class PollTypeQuiz(BaseObject):
    """
    A poll in quiz mode, which has exactly one correct answer option and can be answered only once

    :param correct_option_id: 0-based identifier of the correct answer option; -1 for a yet unanswered poll
    :type correct_option_id: :class:`Int32`
    :param explanation: Text that is shown when the user chooses an incorrect answer or taps on the lamp icon; 0-200 characters with at most 2 line feeds; empty for a yet unanswered poll
    :type explanation: :class:`FormattedText`
    """

    ID: typing.Literal["pollTypeQuiz"] = "pollTypeQuiz"
    correct_option_id: Int32
    explanation: FormattedText = ""


class PollTypeRegular(BaseObject):
    """
    A regular poll

    :param allow_multiple_answers: True, if multiple answer options can be chosen simultaneously
    :type allow_multiple_answers: :class:`Bool`
    """

    ID: typing.Literal["pollTypeRegular"] = "pollTypeRegular"
    allow_multiple_answers: Bool = False


PollType = typing.Union[
    PollTypeQuiz,
    PollTypeRegular,
]


class PremiumFeatureAdvancedChatManagement(BaseObject):
    """
    Ability to change position of the main chat list, archive and mute all new chats from non-contacts, and completely disable notifications about the user's contacts joined Telegram
    """

    ID: typing.Literal["premiumFeatureAdvancedChatManagement"] = "premiumFeatureAdvancedChatManagement"


class PremiumFeatureAnimatedProfilePhoto(BaseObject):
    """
    Profile photo animation on message and chat screens
    """

    ID: typing.Literal["premiumFeatureAnimatedProfilePhoto"] = "premiumFeatureAnimatedProfilePhoto"


class PremiumFeatureAppIcons(BaseObject):
    """
    Allowed to set a premium application icons
    """

    ID: typing.Literal["premiumFeatureAppIcons"] = "premiumFeatureAppIcons"


class PremiumFeatureCustomEmoji(BaseObject):
    """
    Allowed to use custom emoji stickers in message texts and captions
    """

    ID: typing.Literal["premiumFeatureCustomEmoji"] = "premiumFeatureCustomEmoji"


class PremiumFeatureDisabledAds(BaseObject):
    """
    Disabled ads
    """

    ID: typing.Literal["premiumFeatureDisabledAds"] = "premiumFeatureDisabledAds"


class PremiumFeatureEmojiStatus(BaseObject):
    """
    An emoji status shown along with the user's name
    """

    ID: typing.Literal["premiumFeatureEmojiStatus"] = "premiumFeatureEmojiStatus"


class PremiumFeatureForumTopicIcon(BaseObject):
    """
    The ability to set a custom emoji as a forum topic icon
    """

    ID: typing.Literal["premiumFeatureForumTopicIcon"] = "premiumFeatureForumTopicIcon"


class PremiumFeatureImprovedDownloadSpeed(BaseObject):
    """
    Improved download speed
    """

    ID: typing.Literal["premiumFeatureImprovedDownloadSpeed"] = "premiumFeatureImprovedDownloadSpeed"


class PremiumFeatureIncreasedLimits(BaseObject):
    """
    Increased limits
    """

    ID: typing.Literal["premiumFeatureIncreasedLimits"] = "premiumFeatureIncreasedLimits"


class PremiumFeatureIncreasedUploadFileSize(BaseObject):
    """
    Increased maximum upload file size
    """

    ID: typing.Literal["premiumFeatureIncreasedUploadFileSize"] = "premiumFeatureIncreasedUploadFileSize"


class PremiumFeatureProfileBadge(BaseObject):
    """
    A badge in the user's profile
    """

    ID: typing.Literal["premiumFeatureProfileBadge"] = "premiumFeatureProfileBadge"


class PremiumFeatureRealTimeChatTranslation(BaseObject):
    """
    Allowed to translate chat messages real-time
    """

    ID: typing.Literal["premiumFeatureRealTimeChatTranslation"] = "premiumFeatureRealTimeChatTranslation"


class PremiumFeatureUniqueReactions(BaseObject):
    """
    Allowed to use more reactions
    """

    ID: typing.Literal["premiumFeatureUniqueReactions"] = "premiumFeatureUniqueReactions"


class PremiumFeatureUniqueStickers(BaseObject):
    """
    Allowed to use premium stickers with unique effects
    """

    ID: typing.Literal["premiumFeatureUniqueStickers"] = "premiumFeatureUniqueStickers"


class PremiumFeatureUpgradedStories(BaseObject):
    """
    Allowed to use many additional features for stories
    """

    ID: typing.Literal["premiumFeatureUpgradedStories"] = "premiumFeatureUpgradedStories"


class PremiumFeatureVoiceRecognition(BaseObject):
    """
    The ability to convert voice notes to text
    """

    ID: typing.Literal["premiumFeatureVoiceRecognition"] = "premiumFeatureVoiceRecognition"


PremiumFeature = typing.Union[
    PremiumFeatureAdvancedChatManagement,
    PremiumFeatureAnimatedProfilePhoto,
    PremiumFeatureAppIcons,
    PremiumFeatureCustomEmoji,
    PremiumFeatureDisabledAds,
    PremiumFeatureEmojiStatus,
    PremiumFeatureForumTopicIcon,
    PremiumFeatureImprovedDownloadSpeed,
    PremiumFeatureIncreasedLimits,
    PremiumFeatureIncreasedUploadFileSize,
    PremiumFeatureProfileBadge,
    PremiumFeatureRealTimeChatTranslation,
    PremiumFeatureUniqueReactions,
    PremiumFeatureUniqueStickers,
    PremiumFeatureUpgradedStories,
    PremiumFeatureVoiceRecognition,
]


class PremiumFeaturePromotionAnimation(BaseObject):
    """
    Describes a promotion animation for a Premium feature

    :param feature: Premium feature
    :type feature: :class:`PremiumFeature`
    :param animation: Promotion animation for the feature
    :type animation: :class:`Animation`
    """

    ID: typing.Literal["premiumFeaturePromotionAnimation"] = "premiumFeaturePromotionAnimation"
    feature: PremiumFeature
    animation: Animation


class PremiumFeatures(BaseObject):
    """
    Contains information about features, available to Premium users

    :param features: The list of available features
    :type features: :class:`Vector[PremiumFeature]`
    :param limits: The list of limits, increased for Premium users
    :type limits: :class:`Vector[PremiumLimit]`
    :param payment_link: An internal link to be opened to pay for Telegram Premium if store payment isn't possible; may be null if direct payment isn't available, defaults to None
    :type payment_link: :class:`InternalLinkType`, optional
    """

    ID: typing.Literal["premiumFeatures"] = "premiumFeatures"
    features: Vector[PremiumFeature]
    limits: Vector[PremiumLimit]
    payment_link: typing.Optional[InternalLinkType] = None


class PremiumLimit(BaseObject):
    """
    Contains information about a limit, increased for Premium users

    :param type_: The type of the limit
    :type type_: :class:`PremiumLimitType`
    :param default_value: Default value of the limit
    :type default_value: :class:`Int32`
    :param premium_value: Value of the limit for Premium users
    :type premium_value: :class:`Int32`
    """

    ID: typing.Literal["premiumLimit"] = "premiumLimit"
    type_: PremiumLimitType = Field(..., alias="type")
    default_value: Int32
    premium_value: Int32


class PremiumLimitTypeActiveStoryCount(BaseObject):
    """
    The maximum number of active stories
    """

    ID: typing.Literal["premiumLimitTypeActiveStoryCount"] = "premiumLimitTypeActiveStoryCount"


class PremiumLimitTypeBioLength(BaseObject):
    """
    The maximum length of the user's bio
    """

    ID: typing.Literal["premiumLimitTypeBioLength"] = "premiumLimitTypeBioLength"


class PremiumLimitTypeCaptionLength(BaseObject):
    """
    The maximum length of sent media caption
    """

    ID: typing.Literal["premiumLimitTypeCaptionLength"] = "premiumLimitTypeCaptionLength"


class PremiumLimitTypeChatFolderChosenChatCount(BaseObject):
    """
    The maximum number of pinned and always included, or always excluded chats in a chat folder
    """

    ID: typing.Literal["premiumLimitTypeChatFolderChosenChatCount"] = "premiumLimitTypeChatFolderChosenChatCount"


class PremiumLimitTypeChatFolderCount(BaseObject):
    """
    The maximum number of chat folders
    """

    ID: typing.Literal["premiumLimitTypeChatFolderCount"] = "premiumLimitTypeChatFolderCount"


class PremiumLimitTypeChatFolderInviteLinkCount(BaseObject):
    """
    The maximum number of invite links for a chat folder
    """

    ID: typing.Literal["premiumLimitTypeChatFolderInviteLinkCount"] = "premiumLimitTypeChatFolderInviteLinkCount"


class PremiumLimitTypeCreatedPublicChatCount(BaseObject):
    """
    The maximum number of created public chats
    """

    ID: typing.Literal["premiumLimitTypeCreatedPublicChatCount"] = "premiumLimitTypeCreatedPublicChatCount"


class PremiumLimitTypeFavoriteStickerCount(BaseObject):
    """
    The maximum number of favorite stickers
    """

    ID: typing.Literal["premiumLimitTypeFavoriteStickerCount"] = "premiumLimitTypeFavoriteStickerCount"


class PremiumLimitTypeMonthlySentStoryCount(BaseObject):
    """
    The maximum number of stories sent per month
    """

    ID: typing.Literal["premiumLimitTypeMonthlySentStoryCount"] = "premiumLimitTypeMonthlySentStoryCount"


class PremiumLimitTypePinnedArchivedChatCount(BaseObject):
    """
    The maximum number of pinned chats in the archive chat list
    """

    ID: typing.Literal["premiumLimitTypePinnedArchivedChatCount"] = "premiumLimitTypePinnedArchivedChatCount"


class PremiumLimitTypePinnedChatCount(BaseObject):
    """
    The maximum number of pinned chats in the main chat list
    """

    ID: typing.Literal["premiumLimitTypePinnedChatCount"] = "premiumLimitTypePinnedChatCount"


class PremiumLimitTypeSavedAnimationCount(BaseObject):
    """
    The maximum number of saved animations
    """

    ID: typing.Literal["premiumLimitTypeSavedAnimationCount"] = "premiumLimitTypeSavedAnimationCount"


class PremiumLimitTypeShareableChatFolderCount(BaseObject):
    """
    The maximum number of added shareable chat folders
    """

    ID: typing.Literal["premiumLimitTypeShareableChatFolderCount"] = "premiumLimitTypeShareableChatFolderCount"


class PremiumLimitTypeStoryCaptionLength(BaseObject):
    """
    The maximum length of captions of sent stories
    """

    ID: typing.Literal["premiumLimitTypeStoryCaptionLength"] = "premiumLimitTypeStoryCaptionLength"


class PremiumLimitTypeSupergroupCount(BaseObject):
    """
    The maximum number of joined supergroups and channels
    """

    ID: typing.Literal["premiumLimitTypeSupergroupCount"] = "premiumLimitTypeSupergroupCount"


class PremiumLimitTypeWeeklySentStoryCount(BaseObject):
    """
    The maximum number of stories sent per week
    """

    ID: typing.Literal["premiumLimitTypeWeeklySentStoryCount"] = "premiumLimitTypeWeeklySentStoryCount"


PremiumLimitType = typing.Union[
    PremiumLimitTypeActiveStoryCount,
    PremiumLimitTypeBioLength,
    PremiumLimitTypeCaptionLength,
    PremiumLimitTypeChatFolderChosenChatCount,
    PremiumLimitTypeChatFolderCount,
    PremiumLimitTypeChatFolderInviteLinkCount,
    PremiumLimitTypeCreatedPublicChatCount,
    PremiumLimitTypeFavoriteStickerCount,
    PremiumLimitTypeMonthlySentStoryCount,
    PremiumLimitTypePinnedArchivedChatCount,
    PremiumLimitTypePinnedChatCount,
    PremiumLimitTypeSavedAnimationCount,
    PremiumLimitTypeShareableChatFolderCount,
    PremiumLimitTypeStoryCaptionLength,
    PremiumLimitTypeSupergroupCount,
    PremiumLimitTypeWeeklySentStoryCount,
]


class PremiumPaymentOption(BaseObject):
    """
    Describes an option for buying Telegram Premium to a user

    :param currency: ISO 4217 currency code for Telegram Premium subscription payment
    :type currency: :class:`String`
    :param amount: The amount to pay, in the smallest units of the currency
    :type amount: :class:`Int53`
    :param discount_percentage: The discount associated with this option, as a percentage
    :type discount_percentage: :class:`Int32`
    :param month_count: Number of month the Telegram Premium subscription will be active
    :type month_count: :class:`Int32`
    :param store_product_id: Identifier of the store product associated with the option
    :type store_product_id: :class:`String`
    :param payment_link: An internal link to be opened for buying Telegram Premium to the user if store payment isn't possible; may be null if direct payment isn't available, defaults to None
    :type payment_link: :class:`InternalLinkType`, optional
    """

    ID: typing.Literal["premiumPaymentOption"] = "premiumPaymentOption"
    currency: String
    amount: Int53
    discount_percentage: Int32
    month_count: Int32
    store_product_id: String
    payment_link: typing.Optional[InternalLinkType] = None


class PremiumSourceFeature(BaseObject):
    """
    A user tried to use a Premium feature

    :param feature: The used feature
    :type feature: :class:`PremiumFeature`
    """

    ID: typing.Literal["premiumSourceFeature"] = "premiumSourceFeature"
    feature: PremiumFeature


class PremiumSourceLimitExceeded(BaseObject):
    """
    A limit was exceeded

    :param limit_type: Type of the exceeded limit
    :type limit_type: :class:`PremiumLimitType`
    """

    ID: typing.Literal["premiumSourceLimitExceeded"] = "premiumSourceLimitExceeded"
    limit_type: PremiumLimitType


class PremiumSourceLink(BaseObject):
    """
    A user opened an internal link of the type internalLinkTypePremiumFeatures

    :param referrer: The referrer from the link
    :type referrer: :class:`String`
    """

    ID: typing.Literal["premiumSourceLink"] = "premiumSourceLink"
    referrer: String


class PremiumSourceSettings(BaseObject):
    """
    A user opened the Premium features screen from settings
    """

    ID: typing.Literal["premiumSourceSettings"] = "premiumSourceSettings"


class PremiumSourceStoryFeature(BaseObject):
    """
    A user tried to use a Premium story feature

    :param feature: The used feature
    :type feature: :class:`PremiumStoryFeature`
    """

    ID: typing.Literal["premiumSourceStoryFeature"] = "premiumSourceStoryFeature"
    feature: PremiumStoryFeature


PremiumSource = typing.Union[
    PremiumSourceFeature,
    PremiumSourceLimitExceeded,
    PremiumSourceLink,
    PremiumSourceSettings,
    PremiumSourceStoryFeature,
]


class PremiumState(BaseObject):
    """
    Contains state of Telegram Premium subscription and promotion videos for Premium features

    :param state: Text description of the state of the current Premium subscription; may be empty if the current user has no Telegram Premium subscription
    :type state: :class:`FormattedText`
    :param payment_options: The list of available options for buying Telegram Premium
    :type payment_options: :class:`Vector[PremiumStatePaymentOption]`
    :param animations: The list of available promotion animations for Premium features
    :type animations: :class:`Vector[PremiumFeaturePromotionAnimation]`
    """

    ID: typing.Literal["premiumState"] = "premiumState"
    state: FormattedText
    payment_options: Vector[PremiumStatePaymentOption]
    animations: Vector[PremiumFeaturePromotionAnimation]


class PremiumStatePaymentOption(BaseObject):
    """
    Describes an option for buying or upgrading Telegram Premium for self

    :param payment_option: Information about the payment option
    :type payment_option: :class:`PremiumPaymentOption`
    :param last_transaction_id: Identifier of the last in-store transaction for the currently used option
    :type last_transaction_id: :class:`String`
    :param is_current: True, if this is the currently used Telegram Premium subscription option
    :type is_current: :class:`Bool`
    :param is_upgrade: True, if the payment option can be used to upgrade the existing Telegram Premium subscription
    :type is_upgrade: :class:`Bool`
    """

    ID: typing.Literal["premiumStatePaymentOption"] = "premiumStatePaymentOption"
    payment_option: PremiumPaymentOption
    last_transaction_id: String
    is_current: Bool = False
    is_upgrade: Bool = False


class PremiumStoryFeatureCustomExpirationDuration(BaseObject):
    """
    The ability to set custom expiration duration for stories
    """

    ID: typing.Literal["premiumStoryFeatureCustomExpirationDuration"] = "premiumStoryFeatureCustomExpirationDuration"


class PremiumStoryFeatureLinksAndFormatting(BaseObject):
    """
    The ability to use links and formatting in story caption
    """

    ID: typing.Literal["premiumStoryFeatureLinksAndFormatting"] = "premiumStoryFeatureLinksAndFormatting"


class PremiumStoryFeaturePermanentViewsHistory(BaseObject):
    """
    The ability to check who opened the current user's stories after they expire
    """

    ID: typing.Literal["premiumStoryFeaturePermanentViewsHistory"] = "premiumStoryFeaturePermanentViewsHistory"


class PremiumStoryFeaturePriorityOrder(BaseObject):
    """
    User stories are displayed before stories of non-premium contacts
    """

    ID: typing.Literal["premiumStoryFeaturePriorityOrder"] = "premiumStoryFeaturePriorityOrder"


class PremiumStoryFeatureSaveStories(BaseObject):
    """
    The ability to save other's unprotected stories
    """

    ID: typing.Literal["premiumStoryFeatureSaveStories"] = "premiumStoryFeatureSaveStories"


class PremiumStoryFeatureStealthMode(BaseObject):
    """
    The ability to hide the fact that the user viewed other's stories
    """

    ID: typing.Literal["premiumStoryFeatureStealthMode"] = "premiumStoryFeatureStealthMode"


PremiumStoryFeature = typing.Union[
    PremiumStoryFeatureCustomExpirationDuration,
    PremiumStoryFeatureLinksAndFormatting,
    PremiumStoryFeaturePermanentViewsHistory,
    PremiumStoryFeaturePriorityOrder,
    PremiumStoryFeatureSaveStories,
    PremiumStoryFeatureStealthMode,
]


class ProfilePhoto(BaseObject):
    """
    Describes a user profile photo

    :param id: Photo identifier; 0 for an empty photo. Can be used to find a photo in a list of user profile photos
    :type id: :class:`Int64`
    :param small: A small (160x160) user profile photo. The file can be downloaded only before the photo is changed
    :type small: :class:`File`
    :param big: A big (640x640) user profile photo. The file can be downloaded only before the photo is changed
    :type big: :class:`File`
    :param minithumbnail: User profile photo minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param has_animation: True, if the photo has animated variant
    :type has_animation: :class:`Bool`
    :param is_personal: True, if the photo is visible only for the current user
    :type is_personal: :class:`Bool`
    """

    ID: typing.Literal["profilePhoto"] = "profilePhoto"
    id: Int64
    small: File
    big: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    has_animation: Bool = False
    is_personal: Bool = False


class Proxies(BaseObject):
    """
    Represents a list of proxy servers

    :param proxies: List of proxy servers
    :type proxies: :class:`Vector[Proxy]`
    """

    ID: typing.Literal["proxies"] = "proxies"
    proxies: Vector[Proxy]


class Proxy(BaseObject):
    """
    Contains information about a proxy server

    :param id: Unique identifier of the proxy
    :type id: :class:`Int32`
    :param server: Proxy server domain or IP address
    :type server: :class:`String`
    :param port: Proxy server port
    :type port: :class:`Int32`
    :param last_used_date: Point in time (Unix timestamp) when the proxy was last used; 0 if never
    :type last_used_date: :class:`Int32`
    :param type_: Type of the proxy
    :type type_: :class:`ProxyType`
    :param is_enabled: True, if the proxy is enabled now
    :type is_enabled: :class:`Bool`
    """

    ID: typing.Literal["proxy"] = "proxy"
    id: Int32
    server: String
    port: Int32
    last_used_date: Int32
    type_: ProxyType = Field(..., alias="type")
    is_enabled: Bool = False


class ProxyTypeHttp(BaseObject):
    """
    A HTTP transparent proxy server

    :param username: Username for logging in; may be empty
    :type username: :class:`String`
    :param password: Password for logging in; may be empty
    :type password: :class:`String`
    :param http_only: Pass true if the proxy supports only HTTP requests and doesn't support transparent TCP connections via HTTP CONNECT method
    :type http_only: :class:`Bool`
    """

    ID: typing.Literal["proxyTypeHttp"] = "proxyTypeHttp"
    username: String = ""
    password: String = ""
    http_only: Bool = False


class ProxyTypeMtproto(BaseObject):
    """
    An MTProto proxy server

    :param secret: The proxy's secret in hexadecimal encoding
    :type secret: :class:`String`
    """

    ID: typing.Literal["proxyTypeMtproto"] = "proxyTypeMtproto"
    secret: String


class ProxyTypeSocks5(BaseObject):
    """
    A SOCKS5 proxy server

    :param username: Username for logging in; may be empty
    :type username: :class:`String`
    :param password: Password for logging in; may be empty
    :type password: :class:`String`
    """

    ID: typing.Literal["proxyTypeSocks5"] = "proxyTypeSocks5"
    username: String = ""
    password: String = ""


ProxyType = typing.Union[
    ProxyTypeHttp,
    ProxyTypeMtproto,
    ProxyTypeSocks5,
]


class PublicChatTypeHasUsername(BaseObject):
    """
    The chat is public, because it has an active username
    """

    ID: typing.Literal["publicChatTypeHasUsername"] = "publicChatTypeHasUsername"


class PublicChatTypeIsLocationBased(BaseObject):
    """
    The chat is public, because it is a location-based supergroup
    """

    ID: typing.Literal["publicChatTypeIsLocationBased"] = "publicChatTypeIsLocationBased"


PublicChatType = typing.Union[
    PublicChatTypeHasUsername,
    PublicChatTypeIsLocationBased,
]


class PushMessageContentAnimation(BaseObject):
    """
    An animation message (GIF-style).

    :param caption: Animation caption
    :type caption: :class:`String`
    :param animation: Message content; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentAnimation"] = "pushMessageContentAnimation"
    caption: String
    animation: typing.Optional[Animation] = None
    is_pinned: Bool = False


class PushMessageContentAudio(BaseObject):
    """
    An audio message

    :param audio: Message content; may be null, defaults to None
    :type audio: :class:`Audio`, optional
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentAudio"] = "pushMessageContentAudio"
    audio: typing.Optional[Audio] = None
    is_pinned: Bool = False


class PushMessageContentBasicGroupChatCreate(BaseObject):
    """
    A newly created basic group
    """

    ID: typing.Literal["pushMessageContentBasicGroupChatCreate"] = "pushMessageContentBasicGroupChatCreate"


class PushMessageContentChatAddMembers(BaseObject):
    """
    New chat members were invited to a group

    :param member_name: Name of the added member
    :type member_name: :class:`String`
    :param is_current_user: True, if the current user was added to the group
    :type is_current_user: :class:`Bool`
    :param is_returned: True, if the user has returned to the group themselves
    :type is_returned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentChatAddMembers"] = "pushMessageContentChatAddMembers"
    member_name: String
    is_current_user: Bool = False
    is_returned: Bool = False


class PushMessageContentChatChangePhoto(BaseObject):
    """
    A chat photo was edited
    """

    ID: typing.Literal["pushMessageContentChatChangePhoto"] = "pushMessageContentChatChangePhoto"


class PushMessageContentChatChangeTitle(BaseObject):
    """
    A chat title was edited

    :param title: New chat title
    :type title: :class:`String`
    """

    ID: typing.Literal["pushMessageContentChatChangeTitle"] = "pushMessageContentChatChangeTitle"
    title: String


class PushMessageContentChatDeleteMember(BaseObject):
    """
    A chat member was deleted

    :param member_name: Name of the deleted member
    :type member_name: :class:`String`
    :param is_current_user: True, if the current user was deleted from the group
    :type is_current_user: :class:`Bool`
    :param is_left: True, if the user has left the group themselves
    :type is_left: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentChatDeleteMember"] = "pushMessageContentChatDeleteMember"
    member_name: String
    is_current_user: Bool = False
    is_left: Bool = False


class PushMessageContentChatJoinByLink(BaseObject):
    """
    A new member joined the chat via an invite link
    """

    ID: typing.Literal["pushMessageContentChatJoinByLink"] = "pushMessageContentChatJoinByLink"


class PushMessageContentChatJoinByRequest(BaseObject):
    """
    A new member was accepted to the chat by an administrator
    """

    ID: typing.Literal["pushMessageContentChatJoinByRequest"] = "pushMessageContentChatJoinByRequest"


class PushMessageContentChatSetBackground(BaseObject):
    """
    A chat background was edited

    :param is_same: True, if the set background is the same as the background of the current user
    :type is_same: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentChatSetBackground"] = "pushMessageContentChatSetBackground"
    is_same: Bool = False


class PushMessageContentChatSetTheme(BaseObject):
    """
    A chat theme was edited

    :param theme_name: If non-empty, name of a new theme, set for the chat. Otherwise, the chat theme was reset to the default one
    :type theme_name: :class:`String`
    """

    ID: typing.Literal["pushMessageContentChatSetTheme"] = "pushMessageContentChatSetTheme"
    theme_name: String


class PushMessageContentContact(BaseObject):
    """
    A message with a user contact

    :param name: Contact's name
    :type name: :class:`String`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentContact"] = "pushMessageContentContact"
    name: String
    is_pinned: Bool = False


class PushMessageContentContactRegistered(BaseObject):
    """
    A contact has registered with Telegram
    """

    ID: typing.Literal["pushMessageContentContactRegistered"] = "pushMessageContentContactRegistered"


class PushMessageContentDocument(BaseObject):
    """
    A document message (a general file)

    :param document: Message content; may be null, defaults to None
    :type document: :class:`Document`, optional
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentDocument"] = "pushMessageContentDocument"
    document: typing.Optional[Document] = None
    is_pinned: Bool = False


class PushMessageContentGame(BaseObject):
    """
    A message with a game

    :param title: Game title, empty for pinned game message
    :type title: :class:`String`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentGame"] = "pushMessageContentGame"
    title: String
    is_pinned: Bool = False


class PushMessageContentGameScore(BaseObject):
    """
    A new high score was achieved in a game

    :param title: Game title, empty for pinned message
    :type title: :class:`String`
    :param score: New score, 0 for pinned message
    :type score: :class:`Int32`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentGameScore"] = "pushMessageContentGameScore"
    title: String
    score: Int32
    is_pinned: Bool = False


class PushMessageContentHidden(BaseObject):
    """
    A general message with hidden content

    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentHidden"] = "pushMessageContentHidden"
    is_pinned: Bool = False


class PushMessageContentInvoice(BaseObject):
    """
    A message with an invoice from a bot

    :param price: Product price
    :type price: :class:`String`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentInvoice"] = "pushMessageContentInvoice"
    price: String
    is_pinned: Bool = False


class PushMessageContentLocation(BaseObject):
    """
    A message with a location

    :param is_live: True, if the location is live
    :type is_live: :class:`Bool`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentLocation"] = "pushMessageContentLocation"
    is_live: Bool = False
    is_pinned: Bool = False


class PushMessageContentMediaAlbum(BaseObject):
    """
    A media album

    :param total_count: Number of messages in the album
    :type total_count: :class:`Int32`
    :param has_photos: True, if the album has at least one photo
    :type has_photos: :class:`Bool`
    :param has_videos: True, if the album has at least one video file
    :type has_videos: :class:`Bool`
    :param has_audios: True, if the album has at least one audio file
    :type has_audios: :class:`Bool`
    :param has_documents: True, if the album has at least one document
    :type has_documents: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentMediaAlbum"] = "pushMessageContentMediaAlbum"
    total_count: Int32
    has_photos: Bool = False
    has_videos: Bool = False
    has_audios: Bool = False
    has_documents: Bool = False


class PushMessageContentMessageForwards(BaseObject):
    """
    A forwarded messages

    :param total_count: Number of forwarded messages
    :type total_count: :class:`Int32`
    """

    ID: typing.Literal["pushMessageContentMessageForwards"] = "pushMessageContentMessageForwards"
    total_count: Int32


class PushMessageContentPhoto(BaseObject):
    """
    A photo message

    :param caption: Photo caption
    :type caption: :class:`String`
    :param photo: Message content; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    :param is_secret: True, if the photo is secret
    :type is_secret: :class:`Bool`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentPhoto"] = "pushMessageContentPhoto"
    caption: String
    photo: typing.Optional[Photo] = None
    is_secret: Bool = False
    is_pinned: Bool = False


class PushMessageContentPoll(BaseObject):
    """
    A message with a poll

    :param question: Poll question
    :type question: :class:`String`
    :param is_regular: True, if the poll is regular and not in quiz mode
    :type is_regular: :class:`Bool`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentPoll"] = "pushMessageContentPoll"
    question: String
    is_regular: Bool = False
    is_pinned: Bool = False


class PushMessageContentRecurringPayment(BaseObject):
    """
    A new recurring payment was made by the current user

    :param amount: The paid amount
    :type amount: :class:`String`
    """

    ID: typing.Literal["pushMessageContentRecurringPayment"] = "pushMessageContentRecurringPayment"
    amount: String


class PushMessageContentScreenshotTaken(BaseObject):
    """
    A screenshot of a message in the chat has been taken
    """

    ID: typing.Literal["pushMessageContentScreenshotTaken"] = "pushMessageContentScreenshotTaken"


class PushMessageContentSticker(BaseObject):
    """
    A message with a sticker

    :param sticker: Message content; may be null, defaults to None
    :type sticker: :class:`Sticker`, optional
    :param emoji: Emoji corresponding to the sticker; may be empty
    :type emoji: :class:`String`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentSticker"] = "pushMessageContentSticker"
    sticker: typing.Optional[Sticker] = None
    emoji: String = ""
    is_pinned: Bool = False


class PushMessageContentStory(BaseObject):
    """
    A message with a story

    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentStory"] = "pushMessageContentStory"
    is_pinned: Bool = False


class PushMessageContentSuggestProfilePhoto(BaseObject):
    """
    A profile photo was suggested to the user
    """

    ID: typing.Literal["pushMessageContentSuggestProfilePhoto"] = "pushMessageContentSuggestProfilePhoto"


class PushMessageContentText(BaseObject):
    """
    A text message

    :param text: Message text
    :type text: :class:`String`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentText"] = "pushMessageContentText"
    text: String
    is_pinned: Bool = False


class PushMessageContentVideo(BaseObject):
    """
    A video message

    :param caption: Video caption
    :type caption: :class:`String`
    :param video: Message content; may be null, defaults to None
    :type video: :class:`Video`, optional
    :param is_secret: True, if the video is secret
    :type is_secret: :class:`Bool`
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentVideo"] = "pushMessageContentVideo"
    caption: String
    video: typing.Optional[Video] = None
    is_secret: Bool = False
    is_pinned: Bool = False


class PushMessageContentVideoNote(BaseObject):
    """
    A video note message

    :param video_note: Message content; may be null, defaults to None
    :type video_note: :class:`VideoNote`, optional
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentVideoNote"] = "pushMessageContentVideoNote"
    video_note: typing.Optional[VideoNote] = None
    is_pinned: Bool = False


class PushMessageContentVoiceNote(BaseObject):
    """
    A voice note message

    :param voice_note: Message content; may be null, defaults to None
    :type voice_note: :class:`VoiceNote`, optional
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["pushMessageContentVoiceNote"] = "pushMessageContentVoiceNote"
    voice_note: typing.Optional[VoiceNote] = None
    is_pinned: Bool = False


PushMessageContent = typing.Union[
    PushMessageContentAnimation,
    PushMessageContentAudio,
    PushMessageContentBasicGroupChatCreate,
    PushMessageContentChatAddMembers,
    PushMessageContentChatChangePhoto,
    PushMessageContentChatChangeTitle,
    PushMessageContentChatDeleteMember,
    PushMessageContentChatJoinByLink,
    PushMessageContentChatJoinByRequest,
    PushMessageContentChatSetBackground,
    PushMessageContentChatSetTheme,
    PushMessageContentContact,
    PushMessageContentContactRegistered,
    PushMessageContentDocument,
    PushMessageContentGame,
    PushMessageContentGameScore,
    PushMessageContentHidden,
    PushMessageContentInvoice,
    PushMessageContentLocation,
    PushMessageContentMediaAlbum,
    PushMessageContentMessageForwards,
    PushMessageContentPhoto,
    PushMessageContentPoll,
    PushMessageContentRecurringPayment,
    PushMessageContentScreenshotTaken,
    PushMessageContentSticker,
    PushMessageContentStory,
    PushMessageContentSuggestProfilePhoto,
    PushMessageContentText,
    PushMessageContentVideo,
    PushMessageContentVideoNote,
    PushMessageContentVoiceNote,
]


class PushReceiverId(BaseObject):
    """
    Contains a globally unique push receiver identifier, which can be used to identify which account has received a push notification

    :param id: The globally unique identifier of push notification subscription
    :type id: :class:`Int64`
    """

    ID: typing.Literal["pushReceiverId"] = "pushReceiverId"
    id: Int64


class ReactionTypeCustomEmoji(BaseObject):
    """
    A reaction with a custom emoji

    :param custom_emoji_id: Unique identifier of the custom emoji
    :type custom_emoji_id: :class:`Int64`
    """

    ID: typing.Literal["reactionTypeCustomEmoji"] = "reactionTypeCustomEmoji"
    custom_emoji_id: Int64


class ReactionTypeEmoji(BaseObject):
    """
    A reaction with an emoji

    :param emoji: Text representation of the reaction
    :type emoji: :class:`String`
    """

    ID: typing.Literal["reactionTypeEmoji"] = "reactionTypeEmoji"
    emoji: String


ReactionType = typing.Union[
    ReactionTypeCustomEmoji,
    ReactionTypeEmoji,
]


class RecommendedChatFolder(BaseObject):
    """
    Describes a recommended chat folder

    :param folder: The chat folder
    :type folder: :class:`ChatFolder`
    :param description: Chat folder description
    :type description: :class:`String`
    """

    ID: typing.Literal["recommendedChatFolder"] = "recommendedChatFolder"
    folder: ChatFolder
    description: String


class RecommendedChatFolders(BaseObject):
    """
    Contains a list of recommended chat folders

    :param chat_folders: List of recommended chat folders
    :type chat_folders: :class:`Vector[RecommendedChatFolder]`
    """

    ID: typing.Literal["recommendedChatFolders"] = "recommendedChatFolders"
    chat_folders: Vector[RecommendedChatFolder]


class RecoveryEmailAddress(BaseObject):
    """
    Contains information about the current recovery email address

    :param recovery_email_address: Recovery email address
    :type recovery_email_address: :class:`String`
    """

    ID: typing.Literal["recoveryEmailAddress"] = "recoveryEmailAddress"
    recovery_email_address: String


class RemoteFile(BaseObject):
    """
    Represents a remote file

    :param id: Remote file identifier; may be empty. Can be used by the current user across application restarts or even from other devices. Uniquely identifies a file, but a file can have a lot of different valid identifiers. If the identifier starts with "http://" or "https://", it represents the HTTP URL of the file. TDLib is currently unable to download files if only their URL is known. If downloadFile/addFileToDownloads is called on such a file or if it is sent to a secret chat, TDLib starts a file generation process by sending updateFileGenerationStart to the application with the HTTP URL in the original_path and "#url#" as the conversion string. Application must generate the file by downloading it to the specified location
    :type id: :class:`String`
    :param unique_id: Unique file identifier; may be empty if unknown. The unique file identifier which is the same for the same file even for different users and is persistent over time
    :type unique_id: :class:`String`
    :param is_uploading_active: True, if the file is currently being uploaded (or a remote copy is being generated by some other means)
    :type is_uploading_active: :class:`Bool`
    :param is_uploading_completed: True, if a remote copy is fully available
    :type is_uploading_completed: :class:`Bool`
    :param uploaded_size: Size of the remote available part of the file, in bytes; 0 if unknown, defaults to None
    :type uploaded_size: :class:`Int53`, optional
    """

    ID: typing.Literal["remoteFile"] = "remoteFile"
    id: String = ""
    unique_id: String = ""
    is_uploading_active: Bool = False
    is_uploading_completed: Bool = False
    uploaded_size: typing.Optional[Int53] = 0


class ReplyMarkupForceReply(BaseObject):
    """
    Instructs application to force a reply to this message

    :param is_personal: True, if a forced reply must automatically be shown to the current user. For outgoing messages, specify true to show the forced reply only for the mentioned users and for the target user of a reply
    :type is_personal: :class:`Bool`
    :param input_field_placeholder: If non-empty, the placeholder to be shown in the input field when the reply is active; 0-64 characters
    :type input_field_placeholder: :class:`String`
    """

    ID: typing.Literal["replyMarkupForceReply"] = "replyMarkupForceReply"
    is_personal: Bool = False
    input_field_placeholder: String = Field("", max_length=64)


class ReplyMarkupInlineKeyboard(BaseObject):
    """
    Contains an inline keyboard layout

    :param rows: A list of rows of inline keyboard buttons
    :type rows: :class:`Vector[Vector[InlineKeyboardButton]]`
    """

    ID: typing.Literal["replyMarkupInlineKeyboard"] = "replyMarkupInlineKeyboard"
    rows: Vector[Vector[InlineKeyboardButton]]


class ReplyMarkupRemoveKeyboard(BaseObject):
    """
    Instructs application to remove the keyboard once this message has been received. This kind of keyboard can't be received in an incoming message; instead, updateChatReplyMarkup with message_id == 0 will be sent

    :param is_personal: True, if the keyboard is removed only for the mentioned users or the target user of a reply
    :type is_personal: :class:`Bool`
    """

    ID: typing.Literal["replyMarkupRemoveKeyboard"] = "replyMarkupRemoveKeyboard"
    is_personal: Bool = False


class ReplyMarkupShowKeyboard(BaseObject):
    """
    Contains a custom keyboard layout to quickly reply to bots

    :param rows: A list of rows of bot keyboard buttons
    :type rows: :class:`Vector[Vector[KeyboardButton]]`
    :param is_persistent: True, if the keyboard is supposed to always be shown when the ordinary keyboard is hidden
    :type is_persistent: :class:`Bool`
    :param resize_keyboard: True, if the application needs to resize the keyboard vertically
    :type resize_keyboard: :class:`Bool`
    :param one_time: True, if the application needs to hide the keyboard after use
    :type one_time: :class:`Bool`
    :param is_personal: True, if the keyboard must automatically be shown to the current user. For outgoing messages, specify true to show the keyboard only for the mentioned users and for the target user of a reply
    :type is_personal: :class:`Bool`
    :param input_field_placeholder: If non-empty, the placeholder to be shown in the input field when the keyboard is active; 0-64 characters
    :type input_field_placeholder: :class:`String`
    """

    ID: typing.Literal["replyMarkupShowKeyboard"] = "replyMarkupShowKeyboard"
    rows: Vector[Vector[KeyboardButton]]
    is_persistent: Bool = False
    resize_keyboard: Bool = False
    one_time: Bool = False
    is_personal: Bool = False
    input_field_placeholder: String = Field("", max_length=64)


ReplyMarkup = typing.Union[
    ReplyMarkupForceReply,
    ReplyMarkupInlineKeyboard,
    ReplyMarkupRemoveKeyboard,
    ReplyMarkupShowKeyboard,
]


class ReportReasonChildAbuse(BaseObject):
    """
    The chat has child abuse related content
    """

    ID: typing.Literal["reportReasonChildAbuse"] = "reportReasonChildAbuse"


class ReportReasonCopyright(BaseObject):
    """
    The chat contains copyrighted content
    """

    ID: typing.Literal["reportReasonCopyright"] = "reportReasonCopyright"


class ReportReasonCustom(BaseObject):
    """
    A custom reason provided by the user
    """

    ID: typing.Literal["reportReasonCustom"] = "reportReasonCustom"


class ReportReasonFake(BaseObject):
    """
    The chat represents a fake account
    """

    ID: typing.Literal["reportReasonFake"] = "reportReasonFake"


class ReportReasonIllegalDrugs(BaseObject):
    """
    The chat has illegal drugs related content
    """

    ID: typing.Literal["reportReasonIllegalDrugs"] = "reportReasonIllegalDrugs"


class ReportReasonPersonalDetails(BaseObject):
    """
    The chat contains messages with personal details
    """

    ID: typing.Literal["reportReasonPersonalDetails"] = "reportReasonPersonalDetails"


class ReportReasonPornography(BaseObject):
    """
    The chat contains pornographic messages
    """

    ID: typing.Literal["reportReasonPornography"] = "reportReasonPornography"


class ReportReasonSpam(BaseObject):
    """
    The chat contains spam messages
    """

    ID: typing.Literal["reportReasonSpam"] = "reportReasonSpam"


class ReportReasonUnrelatedLocation(BaseObject):
    """
    The location-based chat is unrelated to its stated location
    """

    ID: typing.Literal["reportReasonUnrelatedLocation"] = "reportReasonUnrelatedLocation"


class ReportReasonViolence(BaseObject):
    """
    The chat promotes violence
    """

    ID: typing.Literal["reportReasonViolence"] = "reportReasonViolence"


ReportReason = typing.Union[
    ReportReasonChildAbuse,
    ReportReasonCopyright,
    ReportReasonCustom,
    ReportReasonFake,
    ReportReasonIllegalDrugs,
    ReportReasonPersonalDetails,
    ReportReasonPornography,
    ReportReasonSpam,
    ReportReasonUnrelatedLocation,
    ReportReasonViolence,
]


class ResetPasswordResultDeclined(BaseObject):
    """
    The password reset request was declined

    :param retry_date: Point in time (Unix timestamp) when the password reset can be retried
    :type retry_date: :class:`Int32`
    """

    ID: typing.Literal["resetPasswordResultDeclined"] = "resetPasswordResultDeclined"
    retry_date: Int32


class ResetPasswordResultOk(BaseObject):
    """
    The password was reset
    """

    ID: typing.Literal["resetPasswordResultOk"] = "resetPasswordResultOk"


class ResetPasswordResultPending(BaseObject):
    """
    The password reset request is pending

    :param pending_reset_date: Point in time (Unix timestamp) after which the password can be reset immediately using resetPassword
    :type pending_reset_date: :class:`Int32`
    """

    ID: typing.Literal["resetPasswordResultPending"] = "resetPasswordResultPending"
    pending_reset_date: Int32


ResetPasswordResult = typing.Union[
    ResetPasswordResultDeclined,
    ResetPasswordResultOk,
    ResetPasswordResultPending,
]


class RichTextAnchor(BaseObject):
    """
    An anchor

    :param name: Anchor name
    :type name: :class:`String`
    """

    ID: typing.Literal["richTextAnchor"] = "richTextAnchor"
    name: String


class RichTextAnchorLink(BaseObject):
    """
    A link to an anchor on the same web page

    :param text: The link text
    :type text: :class:`RichText`
    :param anchor_name: The anchor name. If the name is empty, the link must bring back to top
    :type anchor_name: :class:`String`
    :param url: An HTTP URL, opening the anchor
    :type url: :class:`String`
    """

    ID: typing.Literal["richTextAnchorLink"] = "richTextAnchorLink"
    text: RichText
    anchor_name: String
    url: String


class RichTextBold(BaseObject):
    """
    A bold rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextBold"] = "richTextBold"
    text: RichText


class RichTextEmailAddress(BaseObject):
    """
    A rich text email link

    :param text: Text
    :type text: :class:`RichText`
    :param email_address: Email address
    :type email_address: :class:`String`
    """

    ID: typing.Literal["richTextEmailAddress"] = "richTextEmailAddress"
    text: RichText
    email_address: String


class RichTextFixed(BaseObject):
    """
    A fixed-width rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextFixed"] = "richTextFixed"
    text: RichText


class RichTextIcon(BaseObject):
    """
    A small image inside the text

    :param document: The image represented as a document. The image can be in GIF, JPEG or PNG format
    :type document: :class:`Document`
    :param width: Width of a bounding box in which the image must be shown; 0 if unknown, defaults to None
    :type width: :class:`Int32`, optional
    :param height: Height of a bounding box in which the image must be shown; 0 if unknown, defaults to None
    :type height: :class:`Int32`, optional
    """

    ID: typing.Literal["richTextIcon"] = "richTextIcon"
    document: Document
    width: typing.Optional[Int32] = 0
    height: typing.Optional[Int32] = 0


class RichTextItalic(BaseObject):
    """
    An italicized rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextItalic"] = "richTextItalic"
    text: RichText


class RichTextMarked(BaseObject):
    """
    A marked rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextMarked"] = "richTextMarked"
    text: RichText


class RichTextPhoneNumber(BaseObject):
    """
    A rich text phone number

    :param text: Text
    :type text: :class:`RichText`
    :param phone_number: Phone number
    :type phone_number: :class:`String`
    """

    ID: typing.Literal["richTextPhoneNumber"] = "richTextPhoneNumber"
    text: RichText
    phone_number: String


class RichTextPlain(BaseObject):
    """
    A plain text

    :param text: Text
    :type text: :class:`String`
    """

    ID: typing.Literal["richTextPlain"] = "richTextPlain"
    text: String


class RichTextReference(BaseObject):
    """
    A reference to a richTexts object on the same web page

    :param text: The text
    :type text: :class:`RichText`
    :param anchor_name: The name of a richTextAnchor object, which is the first element of the target richTexts object
    :type anchor_name: :class:`String`
    :param url: An HTTP URL, opening the reference
    :type url: :class:`String`
    """

    ID: typing.Literal["richTextReference"] = "richTextReference"
    text: RichText
    anchor_name: String
    url: String


class RichTextStrikethrough(BaseObject):
    """
    A strikethrough rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextStrikethrough"] = "richTextStrikethrough"
    text: RichText


class RichTextSubscript(BaseObject):
    """
    A subscript rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextSubscript"] = "richTextSubscript"
    text: RichText


class RichTextSuperscript(BaseObject):
    """
    A superscript rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextSuperscript"] = "richTextSuperscript"
    text: RichText


class RichTextUnderline(BaseObject):
    """
    An underlined rich text

    :param text: Text
    :type text: :class:`RichText`
    """

    ID: typing.Literal["richTextUnderline"] = "richTextUnderline"
    text: RichText


class RichTextUrl(BaseObject):
    """
    A rich text URL link

    :param text: Text
    :type text: :class:`RichText`
    :param url: URL
    :type url: :class:`String`
    :param is_cached: True, if the URL has cached instant view server-side
    :type is_cached: :class:`Bool`
    """

    ID: typing.Literal["richTextUrl"] = "richTextUrl"
    text: RichText
    url: String
    is_cached: Bool = False


class RichTexts(BaseObject):
    """
    A concatenation of rich texts

    :param texts: Texts
    :type texts: :class:`Vector[RichText]`
    """

    ID: typing.Literal["richTexts"] = "richTexts"
    texts: Vector[RichText]


RichText = typing.Union[
    RichTextAnchor,
    RichTextAnchorLink,
    RichTextBold,
    RichTextEmailAddress,
    RichTextFixed,
    RichTextIcon,
    RichTextItalic,
    RichTextMarked,
    RichTextPhoneNumber,
    RichTextPlain,
    RichTextReference,
    RichTextStrikethrough,
    RichTextSubscript,
    RichTextSuperscript,
    RichTextUnderline,
    RichTextUrl,
    RichTexts,
]


class RtmpUrl(BaseObject):
    """
    Represents an RTMP URL

    :param url: The URL
    :type url: :class:`String`
    :param stream_key: Stream key
    :type stream_key: :class:`String`
    """

    ID: typing.Literal["rtmpUrl"] = "rtmpUrl"
    url: String
    stream_key: String


class SavedCredentials(BaseObject):
    """
    Contains information about saved payment credentials

    :param id: Unique identifier of the saved credentials
    :type id: :class:`String`
    :param title: Title of the saved credentials
    :type title: :class:`String`
    """

    ID: typing.Literal["savedCredentials"] = "savedCredentials"
    id: String
    title: String


class ScopeAutosaveSettings(BaseObject):
    """
    Contains autosave settings for an autosave settings scope

    :param max_video_file_size: The maximum size of a video file to be autosaved, in bytes; 512 KB - 4000 MB
    :type max_video_file_size: :class:`Int53`
    :param autosave_photos: True, if photo autosave is enabled
    :type autosave_photos: :class:`Bool`
    :param autosave_videos: True, if video autosave is enabled
    :type autosave_videos: :class:`Bool`
    """

    ID: typing.Literal["scopeAutosaveSettings"] = "scopeAutosaveSettings"
    max_video_file_size: Int53
    autosave_photos: Bool = False
    autosave_videos: Bool = False


class ScopeNotificationSettings(BaseObject):
    """
    Contains information about notification settings for several chats

    :param mute_for: Time left before notifications will be unmuted, in seconds
    :type mute_for: :class:`Int32`
    :param sound_id: Identifier of the notification sound to be played; 0 if sound is disabled
    :type sound_id: :class:`Int64`
    :param use_default_mute_stories: If true, mute_stories is ignored and story notifications are received only for the first 5 chats from topChatCategoryUsers
    :type use_default_mute_stories: :class:`Bool`
    :param story_sound_id: Identifier of the notification sound to be played for stories; 0 if sound is disabled
    :type story_sound_id: :class:`Int64`
    :param show_preview: True, if message content must be displayed in notifications
    :type show_preview: :class:`Bool`
    :param mute_stories: True, if story notifications are disabled for the chat
    :type mute_stories: :class:`Bool`
    :param show_story_sender: True, if the sender of stories must be displayed in notifications
    :type show_story_sender: :class:`Bool`
    :param disable_pinned_message_notifications: True, if notifications for incoming pinned messages will be created as for an ordinary unread message
    :type disable_pinned_message_notifications: :class:`Bool`
    :param disable_mention_notifications: True, if notifications for messages with mentions will be created as for an ordinary unread message
    :type disable_mention_notifications: :class:`Bool`
    """

    ID: typing.Literal["scopeNotificationSettings"] = "scopeNotificationSettings"
    mute_for: Int32
    sound_id: Int64
    use_default_mute_stories: Bool
    story_sound_id: Int64
    show_preview: Bool = False
    mute_stories: Bool = False
    show_story_sender: Bool = False
    disable_pinned_message_notifications: Bool = False
    disable_mention_notifications: Bool = False


class SearchMessagesFilterAnimation(BaseObject):
    """
    Returns only animation messages
    """

    ID: typing.Literal["searchMessagesFilterAnimation"] = "searchMessagesFilterAnimation"


class SearchMessagesFilterAudio(BaseObject):
    """
    Returns only audio messages
    """

    ID: typing.Literal["searchMessagesFilterAudio"] = "searchMessagesFilterAudio"


class SearchMessagesFilterChatPhoto(BaseObject):
    """
    Returns only messages containing chat photos
    """

    ID: typing.Literal["searchMessagesFilterChatPhoto"] = "searchMessagesFilterChatPhoto"


class SearchMessagesFilterDocument(BaseObject):
    """
    Returns only document messages
    """

    ID: typing.Literal["searchMessagesFilterDocument"] = "searchMessagesFilterDocument"


class SearchMessagesFilterEmpty(BaseObject):
    """
    Returns all found messages, no filter is applied
    """

    ID: typing.Literal["searchMessagesFilterEmpty"] = "searchMessagesFilterEmpty"


class SearchMessagesFilterFailedToSend(BaseObject):
    """
    Returns only failed to send messages. This filter can be used only if the message database is used
    """

    ID: typing.Literal["searchMessagesFilterFailedToSend"] = "searchMessagesFilterFailedToSend"


class SearchMessagesFilterMention(BaseObject):
    """
    Returns only messages with mentions of the current user, or messages that are replies to their messages
    """

    ID: typing.Literal["searchMessagesFilterMention"] = "searchMessagesFilterMention"


class SearchMessagesFilterPhoto(BaseObject):
    """
    Returns only photo messages
    """

    ID: typing.Literal["searchMessagesFilterPhoto"] = "searchMessagesFilterPhoto"


class SearchMessagesFilterPhotoAndVideo(BaseObject):
    """
    Returns only photo and video messages
    """

    ID: typing.Literal["searchMessagesFilterPhotoAndVideo"] = "searchMessagesFilterPhotoAndVideo"


class SearchMessagesFilterPinned(BaseObject):
    """
    Returns only pinned messages
    """

    ID: typing.Literal["searchMessagesFilterPinned"] = "searchMessagesFilterPinned"


class SearchMessagesFilterUnreadMention(BaseObject):
    """
    Returns only messages with unread mentions of the current user, or messages that are replies to their messages. When using this filter the results can't be additionally filtered by a query, a message thread or by the sending user
    """

    ID: typing.Literal["searchMessagesFilterUnreadMention"] = "searchMessagesFilterUnreadMention"


class SearchMessagesFilterUnreadReaction(BaseObject):
    """
    Returns only messages with unread reactions for the current user. When using this filter the results can't be additionally filtered by a query, a message thread or by the sending user
    """

    ID: typing.Literal["searchMessagesFilterUnreadReaction"] = "searchMessagesFilterUnreadReaction"


class SearchMessagesFilterUrl(BaseObject):
    """
    Returns only messages containing URLs
    """

    ID: typing.Literal["searchMessagesFilterUrl"] = "searchMessagesFilterUrl"


class SearchMessagesFilterVideo(BaseObject):
    """
    Returns only video messages
    """

    ID: typing.Literal["searchMessagesFilterVideo"] = "searchMessagesFilterVideo"


class SearchMessagesFilterVideoNote(BaseObject):
    """
    Returns only video note messages
    """

    ID: typing.Literal["searchMessagesFilterVideoNote"] = "searchMessagesFilterVideoNote"


class SearchMessagesFilterVoiceAndVideoNote(BaseObject):
    """
    Returns only voice and video note messages
    """

    ID: typing.Literal["searchMessagesFilterVoiceAndVideoNote"] = "searchMessagesFilterVoiceAndVideoNote"


class SearchMessagesFilterVoiceNote(BaseObject):
    """
    Returns only voice note messages
    """

    ID: typing.Literal["searchMessagesFilterVoiceNote"] = "searchMessagesFilterVoiceNote"


SearchMessagesFilter = typing.Union[
    SearchMessagesFilterAnimation,
    SearchMessagesFilterAudio,
    SearchMessagesFilterChatPhoto,
    SearchMessagesFilterDocument,
    SearchMessagesFilterEmpty,
    SearchMessagesFilterFailedToSend,
    SearchMessagesFilterMention,
    SearchMessagesFilterPhoto,
    SearchMessagesFilterPhotoAndVideo,
    SearchMessagesFilterPinned,
    SearchMessagesFilterUnreadMention,
    SearchMessagesFilterUnreadReaction,
    SearchMessagesFilterUrl,
    SearchMessagesFilterVideo,
    SearchMessagesFilterVideoNote,
    SearchMessagesFilterVoiceAndVideoNote,
    SearchMessagesFilterVoiceNote,
]


class Seconds(BaseObject):
    """
    Contains a value representing a number of seconds

    :param seconds: Number of seconds
    :type seconds: :class:`Double`
    """

    ID: typing.Literal["seconds"] = "seconds"
    seconds: Double


class SecretChat(BaseObject):
    """
    Represents a secret chat

    :param id: Secret chat identifier
    :type id: :class:`Int32`
    :param user_id: Identifier of the chat partner
    :type user_id: :class:`Int53`
    :param state: State of the secret chat
    :type state: :class:`SecretChatState`
    :param key_hash: Hash of the currently used key for comparison with the hash of the chat partner's key. This is a string of 36 little-endian bytes, which must be split into groups of 2 bits, each denoting a pixel of one of 4 colors FFFFFF, D5E6F3, 2D5775, and 2F99C9. The pixels must be used to make a 12x12 square image filled from left to right, top to bottom. Alternatively, the first 32 bytes of the hash can be converted to the hexadecimal format and printed as 32 2-digit hex numbers
    :type key_hash: :class:`Bytes`
    :param layer: Secret chat layer; determines features supported by the chat partner's application. Nested text entities and underline and strikethrough entities are supported if the layer >= 101, files bigger than 2000MB are supported if the layer >= 143, spoiler and custom emoji text entities are supported if the layer >= 144
    :type layer: :class:`Int32`
    :param is_outbound: True, if the chat was created by the current user; false otherwise
    :type is_outbound: :class:`Bool`
    """

    ID: typing.Literal["secretChat"] = "secretChat"
    id: Int32
    user_id: Int53
    state: SecretChatState
    key_hash: Bytes
    layer: Int32
    is_outbound: Bool = False


class SecretChatStateClosed(BaseObject):
    """
    The secret chat is closed
    """

    ID: typing.Literal["secretChatStateClosed"] = "secretChatStateClosed"


class SecretChatStatePending(BaseObject):
    """
    The secret chat is not yet created; waiting for the other user to get online
    """

    ID: typing.Literal["secretChatStatePending"] = "secretChatStatePending"


class SecretChatStateReady(BaseObject):
    """
    The secret chat is ready to use
    """

    ID: typing.Literal["secretChatStateReady"] = "secretChatStateReady"


SecretChatState = typing.Union[
    SecretChatStateClosed,
    SecretChatStatePending,
    SecretChatStateReady,
]


class SentWebAppMessage(BaseObject):
    """
    Information about the message sent by answerWebAppQuery

    :param inline_message_id: Identifier of the sent inline message, if known
    :type inline_message_id: :class:`String`
    """

    ID: typing.Literal["sentWebAppMessage"] = "sentWebAppMessage"
    inline_message_id: String


class Session(BaseObject):
    """
    Contains information about one session in a Telegram application used by the current user. Sessions must be shown to the user in the returned order

    :param id: Session identifier
    :type id: :class:`Int64`
    :param type_: Session type based on the system and application version, which can be used to display a corresponding icon
    :type type_: :class:`SessionType`
    :param api_id: Telegram API identifier, as provided by the application
    :type api_id: :class:`Int32`
    :param application_name: Name of the application, as provided by the application
    :type application_name: :class:`String`
    :param application_version: The version of the application, as provided by the application
    :type application_version: :class:`String`
    :param device_model: Model of the device the application has been run or is running on, as provided by the application
    :type device_model: :class:`String`
    :param platform: Operating system the application has been run or is running on, as provided by the application
    :type platform: :class:`String`
    :param system_version: Version of the operating system the application has been run or is running on, as provided by the application
    :type system_version: :class:`String`
    :param log_in_date: Point in time (Unix timestamp) when the user has logged in
    :type log_in_date: :class:`Int32`
    :param last_active_date: Point in time (Unix timestamp) when the session was last used
    :type last_active_date: :class:`Int32`
    :param ip_address: IP address from which the session was created, in human-readable format
    :type ip_address: :class:`String`
    :param location: A human-readable description of the location from which the session was created, based on the IP address
    :type location: :class:`String`
    :param is_current: True, if this session is the current session
    :type is_current: :class:`Bool`
    :param is_password_pending: True, if a 2-step verification password is needed to complete authorization of the session
    :type is_password_pending: :class:`Bool`
    :param is_unconfirmed: True, if the session wasn't confirmed from another session
    :type is_unconfirmed: :class:`Bool`
    :param can_accept_secret_chats: True, if incoming secret chats can be accepted by the session
    :type can_accept_secret_chats: :class:`Bool`
    :param can_accept_calls: True, if incoming calls can be accepted by the session
    :type can_accept_calls: :class:`Bool`
    :param is_official_application: True, if the application is an official application or uses the api_id of an official application
    :type is_official_application: :class:`Bool`
    """

    ID: typing.Literal["session"] = "session"
    id: Int64
    type_: SessionType = Field(..., alias="type")
    api_id: Int32
    application_name: String
    application_version: String
    device_model: String
    platform: String
    system_version: String
    log_in_date: Int32
    last_active_date: Int32
    ip_address: String
    location: String
    is_current: Bool = False
    is_password_pending: Bool = False
    is_unconfirmed: Bool = False
    can_accept_secret_chats: Bool = False
    can_accept_calls: Bool = False
    is_official_application: Bool = False


class SessionTypeAndroid(BaseObject):
    """
    The session is running on an Android device
    """

    ID: typing.Literal["sessionTypeAndroid"] = "sessionTypeAndroid"


class SessionTypeApple(BaseObject):
    """
    The session is running on a generic Apple device
    """

    ID: typing.Literal["sessionTypeApple"] = "sessionTypeApple"


class SessionTypeBrave(BaseObject):
    """
    The session is running on the Brave browser
    """

    ID: typing.Literal["sessionTypeBrave"] = "sessionTypeBrave"


class SessionTypeChrome(BaseObject):
    """
    The session is running on the Chrome browser
    """

    ID: typing.Literal["sessionTypeChrome"] = "sessionTypeChrome"


class SessionTypeEdge(BaseObject):
    """
    The session is running on the Edge browser
    """

    ID: typing.Literal["sessionTypeEdge"] = "sessionTypeEdge"


class SessionTypeFirefox(BaseObject):
    """
    The session is running on the Firefox browser
    """

    ID: typing.Literal["sessionTypeFirefox"] = "sessionTypeFirefox"


class SessionTypeIpad(BaseObject):
    """
    The session is running on an iPad device
    """

    ID: typing.Literal["sessionTypeIpad"] = "sessionTypeIpad"


class SessionTypeIphone(BaseObject):
    """
    The session is running on an iPhone device
    """

    ID: typing.Literal["sessionTypeIphone"] = "sessionTypeIphone"


class SessionTypeLinux(BaseObject):
    """
    The session is running on a Linux device
    """

    ID: typing.Literal["sessionTypeLinux"] = "sessionTypeLinux"


class SessionTypeMac(BaseObject):
    """
    The session is running on a Mac device
    """

    ID: typing.Literal["sessionTypeMac"] = "sessionTypeMac"


class SessionTypeOpera(BaseObject):
    """
    The session is running on the Opera browser
    """

    ID: typing.Literal["sessionTypeOpera"] = "sessionTypeOpera"


class SessionTypeSafari(BaseObject):
    """
    The session is running on the Safari browser
    """

    ID: typing.Literal["sessionTypeSafari"] = "sessionTypeSafari"


class SessionTypeUbuntu(BaseObject):
    """
    The session is running on an Ubuntu device
    """

    ID: typing.Literal["sessionTypeUbuntu"] = "sessionTypeUbuntu"


class SessionTypeUnknown(BaseObject):
    """
    The session is running on an unknown type of device
    """

    ID: typing.Literal["sessionTypeUnknown"] = "sessionTypeUnknown"


class SessionTypeVivaldi(BaseObject):
    """
    The session is running on the Vivaldi browser
    """

    ID: typing.Literal["sessionTypeVivaldi"] = "sessionTypeVivaldi"


class SessionTypeWindows(BaseObject):
    """
    The session is running on a Windows device
    """

    ID: typing.Literal["sessionTypeWindows"] = "sessionTypeWindows"


class SessionTypeXbox(BaseObject):
    """
    The session is running on an Xbox console
    """

    ID: typing.Literal["sessionTypeXbox"] = "sessionTypeXbox"


SessionType = typing.Union[
    SessionTypeAndroid,
    SessionTypeApple,
    SessionTypeBrave,
    SessionTypeChrome,
    SessionTypeEdge,
    SessionTypeFirefox,
    SessionTypeIpad,
    SessionTypeIphone,
    SessionTypeLinux,
    SessionTypeMac,
    SessionTypeOpera,
    SessionTypeSafari,
    SessionTypeUbuntu,
    SessionTypeUnknown,
    SessionTypeVivaldi,
    SessionTypeWindows,
    SessionTypeXbox,
]


class Sessions(BaseObject):
    """
    Contains a list of sessions

    :param sessions: List of sessions
    :type sessions: :class:`Vector[Session]`
    :param inactive_session_ttl_days: Number of days of inactivity before sessions will automatically be terminated; 1-366 days
    :type inactive_session_ttl_days: :class:`Int32`
    """

    ID: typing.Literal["sessions"] = "sessions"
    sessions: Vector[Session]
    inactive_session_ttl_days: Int32


class ShippingOption(BaseObject):
    """
    One shipping option

    :param id: Shipping option identifier
    :type id: :class:`String`
    :param title: Option title
    :type title: :class:`String`
    :param price_parts: A list of objects used to calculate the total shipping costs
    :type price_parts: :class:`Vector[LabeledPricePart]`
    """

    ID: typing.Literal["shippingOption"] = "shippingOption"
    id: String
    title: String
    price_parts: Vector[LabeledPricePart]


class SpeechRecognitionResultError(BaseObject):
    """
    The speech recognition failed

    :param error: Recognition error
    :type error: :class:`Error`
    """

    ID: typing.Literal["speechRecognitionResultError"] = "speechRecognitionResultError"
    error: Error


class SpeechRecognitionResultPending(BaseObject):
    """
    The speech recognition is ongoing

    :param partial_text: Partially recognized text
    :type partial_text: :class:`String`
    """

    ID: typing.Literal["speechRecognitionResultPending"] = "speechRecognitionResultPending"
    partial_text: String


class SpeechRecognitionResultText(BaseObject):
    """
    The speech recognition successfully finished

    :param text: Recognized text
    :type text: :class:`String`
    """

    ID: typing.Literal["speechRecognitionResultText"] = "speechRecognitionResultText"
    text: String


SpeechRecognitionResult = typing.Union[
    SpeechRecognitionResultError,
    SpeechRecognitionResultPending,
    SpeechRecognitionResultText,
]


class SponsoredMessage(BaseObject):
    """
    Describes a sponsored message

    :param message_id: Message identifier; unique for the chat to which the sponsored message belongs among both ordinary and sponsored messages
    :type message_id: :class:`Int53`
    :param content: Content of the message. Currently, can be only of the type messageText
    :type content: :class:`MessageContent`
    :param sponsor: Information about the sponsor of the message
    :type sponsor: :class:`MessageSponsor`
    :param additional_info: If non-empty, additional information about the sponsored message to be shown along with the message
    :type additional_info: :class:`String`
    :param is_recommended: True, if the message needs to be labeled as "recommended" instead of "sponsored"
    :type is_recommended: :class:`Bool`
    """

    ID: typing.Literal["sponsoredMessage"] = "sponsoredMessage"
    message_id: Int53
    content: MessageContent
    sponsor: MessageSponsor
    additional_info: String
    is_recommended: Bool = False


class SponsoredMessages(BaseObject):
    """
    Contains a list of sponsored messages

    :param messages: List of sponsored messages
    :type messages: :class:`Vector[SponsoredMessage]`
    :param messages_between: The minimum number of messages between shown sponsored messages, or 0 if only one sponsored message must be shown after all ordinary messages
    :type messages_between: :class:`Int32`
    """

    ID: typing.Literal["sponsoredMessages"] = "sponsoredMessages"
    messages: Vector[SponsoredMessage]
    messages_between: Int32


class StatisticalGraphAsync(BaseObject):
    """
    The graph data to be asynchronously loaded through getStatisticalGraph

    :param token: The token to use for data loading
    :type token: :class:`String`
    """

    ID: typing.Literal["statisticalGraphAsync"] = "statisticalGraphAsync"
    token: String


class StatisticalGraphData(BaseObject):
    """
    A graph data

    :param json_data: Graph data in JSON format
    :type json_data: :class:`String`
    :param zoom_token: If non-empty, a token which can be used to receive a zoomed in graph
    :type zoom_token: :class:`String`
    """

    ID: typing.Literal["statisticalGraphData"] = "statisticalGraphData"
    json_data: String
    zoom_token: String


class StatisticalGraphError(BaseObject):
    """
    An error message to be shown to the user instead of the graph

    :param error_message: The error message
    :type error_message: :class:`String`
    """

    ID: typing.Literal["statisticalGraphError"] = "statisticalGraphError"
    error_message: String


StatisticalGraph = typing.Union[
    StatisticalGraphAsync,
    StatisticalGraphData,
    StatisticalGraphError,
]


class StatisticalValue(BaseObject):
    """
    A value with information about its recent changes

    :param value: The current value
    :type value: :class:`Double`
    :param previous_value: The value for the previous day
    :type previous_value: :class:`Double`
    :param growth_rate_percentage: The growth rate of the value, as a percentage
    :type growth_rate_percentage: :class:`Double`
    """

    ID: typing.Literal["statisticalValue"] = "statisticalValue"
    value: Double
    previous_value: Double
    growth_rate_percentage: Double


class Sticker(BaseObject):
    """
    Describes a sticker

    :param width: Sticker width; as defined by the sender
    :type width: :class:`Int32`
    :param height: Sticker height; as defined by the sender
    :type height: :class:`Int32`
    :param emoji: Emoji corresponding to the sticker
    :type emoji: :class:`String`
    :param format: Sticker format
    :type format: :class:`StickerFormat`
    :param full_type: Sticker's full type
    :type full_type: :class:`StickerFullType`
    :param sticker: File containing the sticker
    :type sticker: :class:`File`
    :param thumbnail: Sticker thumbnail in WEBP or JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param outline: Sticker's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
    :type outline: :class:`Vector[ClosedVectorPath]`
    :param id: Unique sticker identifier within the set; 0 if none, defaults to None
    :type id: :class:`Int64`, optional
    :param set_id: Identifier of the sticker set to which the sticker belongs; 0 if none, defaults to None
    :type set_id: :class:`Int64`, optional
    """

    ID: typing.Literal["sticker"] = "sticker"
    width: Int32
    height: Int32
    emoji: String
    format: StickerFormat
    full_type: StickerFullType
    sticker: File
    thumbnail: typing.Optional[Thumbnail] = None
    outline: Vector[ClosedVectorPath] = []
    id: typing.Optional[Int64] = 0
    set_id: typing.Optional[Int64] = 0


class StickerFormatTgs(BaseObject):
    """
    The sticker is an animation in TGS format
    """

    ID: typing.Literal["stickerFormatTgs"] = "stickerFormatTgs"


class StickerFormatWebm(BaseObject):
    """
    The sticker is a video in WEBM format
    """

    ID: typing.Literal["stickerFormatWebm"] = "stickerFormatWebm"


class StickerFormatWebp(BaseObject):
    """
    The sticker is an image in WEBP format
    """

    ID: typing.Literal["stickerFormatWebp"] = "stickerFormatWebp"


StickerFormat = typing.Union[
    StickerFormatTgs,
    StickerFormatWebm,
    StickerFormatWebp,
]


class StickerFullTypeCustomEmoji(BaseObject):
    """
    The sticker is a custom emoji to be used inside message text and caption. Currently, only Telegram Premium users can use custom emoji

    :param custom_emoji_id: Identifier of the custom emoji
    :type custom_emoji_id: :class:`Int64`
    :param needs_repainting: True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places
    :type needs_repainting: :class:`Bool`
    """

    ID: typing.Literal["stickerFullTypeCustomEmoji"] = "stickerFullTypeCustomEmoji"
    custom_emoji_id: Int64
    needs_repainting: Bool = False


class StickerFullTypeMask(BaseObject):
    """
    The sticker is a mask in WEBP format to be placed on photos or videos

    :param mask_position: Position where the mask is placed; may be null, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    """

    ID: typing.Literal["stickerFullTypeMask"] = "stickerFullTypeMask"
    mask_position: typing.Optional[MaskPosition] = None


class StickerFullTypeRegular(BaseObject):
    """
    The sticker is a regular sticker

    :param premium_animation: Premium animation of the sticker; may be null. If present, only Telegram Premium users can use the sticker, defaults to None
    :type premium_animation: :class:`File`, optional
    """

    ID: typing.Literal["stickerFullTypeRegular"] = "stickerFullTypeRegular"
    premium_animation: typing.Optional[File] = None


StickerFullType = typing.Union[
    StickerFullTypeCustomEmoji,
    StickerFullTypeMask,
    StickerFullTypeRegular,
]


class StickerSet(BaseObject):
    """
    Represents a sticker set

    :param id: Identifier of the sticker set
    :type id: :class:`Int64`
    :param title: Title of the sticker set
    :type title: :class:`String`
    :param name: Name of the sticker set
    :type name: :class:`String`
    :param sticker_format: Format of the stickers in the set
    :type sticker_format: :class:`StickerFormat`
    :param sticker_type: Type of the stickers in the set
    :type sticker_type: :class:`StickerType`
    :param is_viewed: True for already viewed trending sticker sets
    :type is_viewed: :class:`Bool`
    :param stickers: List of stickers in this set
    :type stickers: :class:`Vector[Sticker]`
    :param emojis: A list of emoji corresponding to the stickers in the same order. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
    :type emojis: :class:`Vector[Emojis]`
    :param thumbnail: Sticker set thumbnail in WEBP, TGS, or WEBM format with width and height 100; may be null. The file can be downloaded only before the thumbnail is changed, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param thumbnail_outline: Sticker set thumbnail's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
    :type thumbnail_outline: :class:`Vector[ClosedVectorPath]`
    :param is_installed: True, if the sticker set has been installed by the current user
    :type is_installed: :class:`Bool`
    :param is_archived: True, if the sticker set has been archived. A sticker set can't be installed and archived simultaneously
    :type is_archived: :class:`Bool`
    :param is_official: True, if the sticker set is official
    :type is_official: :class:`Bool`
    """

    ID: typing.Literal["stickerSet"] = "stickerSet"
    id: Int64
    title: String
    name: String
    sticker_format: StickerFormat
    sticker_type: StickerType
    is_viewed: Bool
    stickers: Vector[Sticker]
    emojis: Vector[Emojis]
    thumbnail: typing.Optional[Thumbnail] = None
    thumbnail_outline: Vector[ClosedVectorPath] = []
    is_installed: Bool = False
    is_archived: Bool = False
    is_official: Bool = False


class StickerSetInfo(BaseObject):
    """
    Represents short information about a sticker set

    :param id: Identifier of the sticker set
    :type id: :class:`Int64`
    :param title: Title of the sticker set
    :type title: :class:`String`
    :param name: Name of the sticker set
    :type name: :class:`String`
    :param sticker_format: Format of the stickers in the set
    :type sticker_format: :class:`StickerFormat`
    :param sticker_type: Type of the stickers in the set
    :type sticker_type: :class:`StickerType`
    :param is_viewed: True for already viewed trending sticker sets
    :type is_viewed: :class:`Bool`
    :param size: Total number of stickers in the set
    :type size: :class:`Int32`
    :param covers: Up to the first 5 stickers from the set, depending on the context. If the application needs more stickers the full sticker set needs to be requested
    :type covers: :class:`Vector[Sticker]`
    :param thumbnail: Sticker set thumbnail in WEBP, TGS, or WEBM format with width and height 100; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param thumbnail_outline: Sticker set thumbnail's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
    :type thumbnail_outline: :class:`Vector[ClosedVectorPath]`
    :param is_installed: True, if the sticker set has been installed by the current user
    :type is_installed: :class:`Bool`
    :param is_archived: True, if the sticker set has been archived. A sticker set can't be installed and archived simultaneously
    :type is_archived: :class:`Bool`
    :param is_official: True, if the sticker set is official
    :type is_official: :class:`Bool`
    """

    ID: typing.Literal["stickerSetInfo"] = "stickerSetInfo"
    id: Int64
    title: String
    name: String
    sticker_format: StickerFormat
    sticker_type: StickerType
    is_viewed: Bool
    size: Int32
    covers: Vector[Sticker]
    thumbnail: typing.Optional[Thumbnail] = None
    thumbnail_outline: Vector[ClosedVectorPath] = []
    is_installed: Bool = False
    is_archived: Bool = False
    is_official: Bool = False


class StickerSets(BaseObject):
    """
    Represents a list of sticker sets

    :param total_count: Approximate total number of sticker sets found
    :type total_count: :class:`Int32`
    :param sets: List of sticker sets
    :type sets: :class:`Vector[StickerSetInfo]`
    """

    ID: typing.Literal["stickerSets"] = "stickerSets"
    total_count: Int32
    sets: Vector[StickerSetInfo]


class StickerTypeCustomEmoji(BaseObject):
    """
    The sticker is a custom emoji to be used inside message text and caption
    """

    ID: typing.Literal["stickerTypeCustomEmoji"] = "stickerTypeCustomEmoji"


class StickerTypeMask(BaseObject):
    """
    The sticker is a mask in WEBP format to be placed on photos or videos
    """

    ID: typing.Literal["stickerTypeMask"] = "stickerTypeMask"


class StickerTypeRegular(BaseObject):
    """
    The sticker is a regular sticker
    """

    ID: typing.Literal["stickerTypeRegular"] = "stickerTypeRegular"


StickerType = typing.Union[
    StickerTypeCustomEmoji,
    StickerTypeMask,
    StickerTypeRegular,
]


class Stickers(BaseObject):
    """
    Represents a list of stickers

    :param stickers: List of stickers
    :type stickers: :class:`Vector[Sticker]`
    """

    ID: typing.Literal["stickers"] = "stickers"
    stickers: Vector[Sticker]


class StorageStatistics(BaseObject):
    """
    Contains the exact storage usage statistics split by chats and file type

    :param size: Total size of files, in bytes
    :type size: :class:`Int53`
    :param count: Total number of files
    :type count: :class:`Int32`
    :param by_chat: Statistics split by chats
    :type by_chat: :class:`Vector[StorageStatisticsByChat]`
    """

    ID: typing.Literal["storageStatistics"] = "storageStatistics"
    size: Int53
    count: Int32
    by_chat: Vector[StorageStatisticsByChat]


class StorageStatisticsByChat(BaseObject):
    """
    Contains the storage usage statistics for a specific chat

    :param size: Total size of the files in the chat, in bytes
    :type size: :class:`Int53`
    :param count: Total number of files in the chat
    :type count: :class:`Int32`
    :param by_file_type: Statistics split by file types
    :type by_file_type: :class:`Vector[StorageStatisticsByFileType]`
    :param chat_id: Chat identifier; 0 if none, defaults to None
    :type chat_id: :class:`Int53`, optional
    """

    ID: typing.Literal["storageStatisticsByChat"] = "storageStatisticsByChat"
    size: Int53
    count: Int32
    by_file_type: Vector[StorageStatisticsByFileType]
    chat_id: typing.Optional[Int53] = 0


class StorageStatisticsByFileType(BaseObject):
    """
    Contains the storage usage statistics for a specific file type

    :param file_type: File type
    :type file_type: :class:`FileType`
    :param size: Total size of the files, in bytes
    :type size: :class:`Int53`
    :param count: Total number of files
    :type count: :class:`Int32`
    """

    ID: typing.Literal["storageStatisticsByFileType"] = "storageStatisticsByFileType"
    file_type: FileType
    size: Int53
    count: Int32


class StorageStatisticsFast(BaseObject):
    """
    Contains approximate storage usage statistics, excluding files of unknown file type

    :param files_size: Approximate total size of files, in bytes
    :type files_size: :class:`Int53`
    :param file_count: Approximate number of files
    :type file_count: :class:`Int32`
    :param database_size: Size of the database
    :type database_size: :class:`Int53`
    :param language_pack_database_size: Size of the language pack database
    :type language_pack_database_size: :class:`Int53`
    :param log_size: Size of the TDLib internal log
    :type log_size: :class:`Int53`
    """

    ID: typing.Literal["storageStatisticsFast"] = "storageStatisticsFast"
    files_size: Int53
    file_count: Int32
    database_size: Int53
    language_pack_database_size: Int53
    log_size: Int53


class StorePaymentPurposeGiftedPremium(BaseObject):
    """
    The user gifted Telegram Premium to another user

    :param user_id: Identifier of the user for which Premium was gifted
    :type user_id: :class:`Int53`
    :param currency: ISO 4217 currency code of the payment currency
    :type currency: :class:`String`
    :param amount: Paid amount, in the smallest units of the currency
    :type amount: :class:`Int53`
    """

    ID: typing.Literal["storePaymentPurposeGiftedPremium"] = "storePaymentPurposeGiftedPremium"
    user_id: Int53
    currency: String
    amount: Int53


class StorePaymentPurposePremiumSubscription(BaseObject):
    """
    The user subscribed to Telegram Premium

    :param is_restore: Pass true if this is a restore of a Telegram Premium purchase; only for App Store
    :type is_restore: :class:`Bool`
    :param is_upgrade: Pass true if this is an upgrade from a monthly subscription to early subscription; only for App Store
    :type is_upgrade: :class:`Bool`
    """

    ID: typing.Literal["storePaymentPurposePremiumSubscription"] = "storePaymentPurposePremiumSubscription"
    is_restore: Bool = False
    is_upgrade: Bool = False


StorePaymentPurpose = typing.Union[
    StorePaymentPurposeGiftedPremium,
    StorePaymentPurposePremiumSubscription,
]


class Stories(BaseObject):
    """
    Represents a list of stories

    :param total_count: Approximate total number of stories found
    :type total_count: :class:`Int32`
    :param stories: The list of stories
    :type stories: :class:`Vector[Story]`
    """

    ID: typing.Literal["stories"] = "stories"
    total_count: Int32
    stories: Vector[Story]


class Story(BaseObject):
    """
    Represents a story

    :param id: Unique story identifier among stories of the given sender
    :type id: :class:`Int32`
    :param sender_chat_id: Identifier of the chat that posted the story
    :type sender_chat_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) when the story was published
    :type date: :class:`Int32`
    :param privacy_settings: Privacy rules affecting story visibility; may be approximate for non-owned stories
    :type privacy_settings: :class:`StoryPrivacySettings`
    :param content: Content of the story
    :type content: :class:`StoryContent`
    :param areas: Clickable areas to be shown on the story content
    :type areas: :class:`Vector[StoryArea]`
    :param caption: Caption of the story
    :type caption: :class:`FormattedText`
    :param interaction_info: Information about interactions with the story; may be null if the story isn't owned or there were no interactions, defaults to None
    :type interaction_info: :class:`StoryInteractionInfo`, optional
    :param chosen_reaction_type: Type of the chosen reaction; may be null if none, defaults to None
    :type chosen_reaction_type: :class:`ReactionType`, optional
    :param is_being_sent: True, if the story is being sent by the current user
    :type is_being_sent: :class:`Bool`
    :param is_being_edited: True, if the story is being edited by the current user
    :type is_being_edited: :class:`Bool`
    :param is_edited: True, if the story was edited
    :type is_edited: :class:`Bool`
    :param is_pinned: True, if the story is saved in the sender's profile and will be available there after expiration
    :type is_pinned: :class:`Bool`
    :param is_visible_only_for_self: True, if the story is visible only for the current user
    :type is_visible_only_for_self: :class:`Bool`
    :param can_be_forwarded: True, if the story can be forwarded as a message. Otherwise, screenshots and saving of the story content must be also forbidden
    :type can_be_forwarded: :class:`Bool`
    :param can_be_replied: True, if the story can be replied in the chat with the story sender
    :type can_be_replied: :class:`Bool`
    :param can_get_viewers: True, if users viewed the story can be received through getStoryViewers
    :type can_get_viewers: :class:`Bool`
    :param has_expired_viewers: True, if users viewed the story can't be received, because the story has expired more than getOption("story_viewers_expiration_delay") seconds ago
    :type has_expired_viewers: :class:`Bool`
    """

    ID: typing.Literal["story"] = "story"
    id: Int32
    sender_chat_id: Int53
    date: Int32
    privacy_settings: StoryPrivacySettings
    content: StoryContent
    areas: Vector[StoryArea]
    caption: FormattedText
    interaction_info: typing.Optional[StoryInteractionInfo] = None
    chosen_reaction_type: typing.Optional[ReactionType] = None
    is_being_sent: Bool = False
    is_being_edited: Bool = False
    is_edited: Bool = False
    is_pinned: Bool = False
    is_visible_only_for_self: Bool = False
    can_be_forwarded: Bool = False
    can_be_replied: Bool = False
    can_get_viewers: Bool = False
    has_expired_viewers: Bool = False


class StoryArea(BaseObject):
    """
    Describes a clickable rectangle area on a story media

    :param position: Position of the area
    :type position: :class:`StoryAreaPosition`
    :param type_: Type of the area
    :type type_: :class:`StoryAreaType`
    """

    ID: typing.Literal["storyArea"] = "storyArea"
    position: StoryAreaPosition
    type_: StoryAreaType = Field(..., alias="type")


class StoryAreaPosition(BaseObject):
    """
    Describes position of a clickable rectangle area on a story media

    :param x_percentage: The abscissa of the rectangle's center, as a percentage of the media width
    :type x_percentage: :class:`Double`
    :param y_percentage: The ordinate of the rectangle's center, as a percentage of the media height
    :type y_percentage: :class:`Double`
    :param width_percentage: The width of the rectangle, as a percentage of the media width
    :type width_percentage: :class:`Double`
    :param height_percentage: The ordinate of the rectangle's center, as a percentage of the media height
    :type height_percentage: :class:`Double`
    :param rotation_angle: Clockwise rotation angle of the rectangle, in degrees; 0-360
    :type rotation_angle: :class:`Double`
    """

    ID: typing.Literal["storyAreaPosition"] = "storyAreaPosition"
    x_percentage: Double
    y_percentage: Double
    width_percentage: Double
    height_percentage: Double
    rotation_angle: Double


class StoryAreaTypeLocation(BaseObject):
    """
    An area pointing to a location

    :param location: The location
    :type location: :class:`Location`
    """

    ID: typing.Literal["storyAreaTypeLocation"] = "storyAreaTypeLocation"
    location: Location


class StoryAreaTypeVenue(BaseObject):
    """
    An area pointing to a venue

    :param venue: Information about the venue
    :type venue: :class:`Venue`
    """

    ID: typing.Literal["storyAreaTypeVenue"] = "storyAreaTypeVenue"
    venue: Venue


StoryAreaType = typing.Union[
    StoryAreaTypeLocation,
    StoryAreaTypeVenue,
]


class StoryContentPhoto(BaseObject):
    """
    A photo story

    :param photo: The photo
    :type photo: :class:`Photo`
    """

    ID: typing.Literal["storyContentPhoto"] = "storyContentPhoto"
    photo: Photo


class StoryContentUnsupported(BaseObject):
    """
    A story content that is not supported in the current TDLib version
    """

    ID: typing.Literal["storyContentUnsupported"] = "storyContentUnsupported"


class StoryContentVideo(BaseObject):
    """
    A video story

    :param video: The video in MPEG4 format
    :type video: :class:`StoryVideo`
    :param alternative_video: Alternative version of the video in MPEG4 format, encoded by x264 codec; may be null, defaults to None
    :type alternative_video: :class:`StoryVideo`, optional
    """

    ID: typing.Literal["storyContentVideo"] = "storyContentVideo"
    video: StoryVideo
    alternative_video: typing.Optional[StoryVideo] = None


StoryContent = typing.Union[
    StoryContentPhoto,
    StoryContentUnsupported,
    StoryContentVideo,
]


class StoryInfo(BaseObject):
    """
    Contains basic information about a story

    :param story_id: Unique story identifier among stories of the given sender
    :type story_id: :class:`Int32`
    :param date: Point in time (Unix timestamp) when the story was published
    :type date: :class:`Int32`
    :param is_for_close_friends: True, if the story is available only to close friends
    :type is_for_close_friends: :class:`Bool`
    """

    ID: typing.Literal["storyInfo"] = "storyInfo"
    story_id: Int32
    date: Int32
    is_for_close_friends: Bool = False


class StoryInteractionInfo(BaseObject):
    """
    Contains information about interactions with a story

    :param view_count: Number of times the story was viewed
    :type view_count: :class:`Int32`
    :param reaction_count: Number of reactions added to the story
    :type reaction_count: :class:`Int32`
    :param recent_viewer_user_ids: Identifiers of at most 3 recent viewers of the story
    :type recent_viewer_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["storyInteractionInfo"] = "storyInteractionInfo"
    view_count: Int32
    reaction_count: Int32
    recent_viewer_user_ids: Vector[Int53]


class StoryListArchive(BaseObject):
    """
    The list of stories, shown in the Arvhive chat list
    """

    ID: typing.Literal["storyListArchive"] = "storyListArchive"


class StoryListMain(BaseObject):
    """
    The list of stories, shown in the main chat list and folder chat lists
    """

    ID: typing.Literal["storyListMain"] = "storyListMain"


StoryList = typing.Union[
    StoryListArchive,
    StoryListMain,
]


class StoryPrivacySettingsCloseFriends(BaseObject):
    """
    The story can be viewed by all close friends
    """

    ID: typing.Literal["storyPrivacySettingsCloseFriends"] = "storyPrivacySettingsCloseFriends"


class StoryPrivacySettingsContacts(BaseObject):
    """
    The story can be viewed by all contacts except chosen users

    :param except_user_ids: User identifiers of the contacts that can't see the story; always unknown and empty for non-owned stories
    :type except_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["storyPrivacySettingsContacts"] = "storyPrivacySettingsContacts"
    except_user_ids: Vector[Int53]


class StoryPrivacySettingsEveryone(BaseObject):
    """
    The story can be viewed by everyone

    :param except_user_ids: Identifiers of the users that can't see the story; always unknown and empty for non-owned stories
    :type except_user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["storyPrivacySettingsEveryone"] = "storyPrivacySettingsEveryone"
    except_user_ids: Vector[Int53]


class StoryPrivacySettingsSelectedUsers(BaseObject):
    """
    The story can be viewed by certain specified users

    :param user_ids: Identifiers of the users; always unknown and empty for non-owned stories
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["storyPrivacySettingsSelectedUsers"] = "storyPrivacySettingsSelectedUsers"
    user_ids: Vector[Int53]


StoryPrivacySettings = typing.Union[
    StoryPrivacySettingsCloseFriends,
    StoryPrivacySettingsContacts,
    StoryPrivacySettingsEveryone,
    StoryPrivacySettingsSelectedUsers,
]


class StoryVideo(BaseObject):
    """
    Describes a video file sent in a story

    :param duration: Duration of the video, in seconds
    :type duration: :class:`Double`
    :param width: Video width
    :type width: :class:`Int32`
    :param height: Video height
    :type height: :class:`Int32`
    :param preload_prefix_size: Size of file prefix, which is supposed to be preloaded, in bytes
    :type preload_prefix_size: :class:`Int32`
    :param video: File containing the video
    :type video: :class:`File`
    :param minithumbnail: Video minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param thumbnail: Video thumbnail in JPEG or MPEG4 format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param has_stickers: True, if stickers were added to the video. The list of corresponding sticker sets can be received using getAttachedStickerSets
    :type has_stickers: :class:`Bool`
    :param is_animation: True, if the video has no sound
    :type is_animation: :class:`Bool`
    """

    ID: typing.Literal["storyVideo"] = "storyVideo"
    duration: Double
    width: Int32
    height: Int32
    preload_prefix_size: Int32
    video: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    has_stickers: Bool = False
    is_animation: Bool = False


class StoryViewer(BaseObject):
    """
    Represents a viewer of a story

    :param user_id: User identifier of the viewer
    :type user_id: :class:`Int53`
    :param view_date: Approximate point in time (Unix timestamp) when the story was viewed
    :type view_date: :class:`Int32`
    :param block_list: Block list to which the user is added; may be null if none, defaults to None
    :type block_list: :class:`BlockList`, optional
    :param chosen_reaction_type: Type of the reaction that was chosen by the user; may be null if none, defaults to None
    :type chosen_reaction_type: :class:`ReactionType`, optional
    """

    ID: typing.Literal["storyViewer"] = "storyViewer"
    user_id: Int53
    view_date: Int32
    block_list: typing.Optional[BlockList] = None
    chosen_reaction_type: typing.Optional[ReactionType] = None


class StoryViewers(BaseObject):
    """
    Represents a list of story viewers

    :param total_count: Approximate total number of story viewers found
    :type total_count: :class:`Int32`
    :param total_reaction_count: Approximate total number of reactions set by found story viewers
    :type total_reaction_count: :class:`Int32`
    :param viewers: List of story viewers
    :type viewers: :class:`Vector[StoryViewer]`
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`String`
    """

    ID: typing.Literal["storyViewers"] = "storyViewers"
    total_count: Int32
    total_reaction_count: Int32
    viewers: Vector[StoryViewer]
    next_offset: String


class SuggestedActionCheckPassword(BaseObject):
    """
    Suggests the user to check whether they still remember their 2-step verification password
    """

    ID: typing.Literal["suggestedActionCheckPassword"] = "suggestedActionCheckPassword"


class SuggestedActionCheckPhoneNumber(BaseObject):
    """
    Suggests the user to check whether authorization phone number is correct and change the phone number if it is inaccessible
    """

    ID: typing.Literal["suggestedActionCheckPhoneNumber"] = "suggestedActionCheckPhoneNumber"


class SuggestedActionConvertToBroadcastGroup(BaseObject):
    """
    Suggests the user to convert specified supergroup to a broadcast group

    :param supergroup_id: Supergroup identifier
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["suggestedActionConvertToBroadcastGroup"] = "suggestedActionConvertToBroadcastGroup"
    supergroup_id: Int53


class SuggestedActionEnableArchiveAndMuteNewChats(BaseObject):
    """
    Suggests the user to enable archive_and_mute_new_chats_from_unknown_users setting in archiveChatListSettings
    """

    ID: typing.Literal["suggestedActionEnableArchiveAndMuteNewChats"] = "suggestedActionEnableArchiveAndMuteNewChats"


class SuggestedActionRestorePremium(BaseObject):
    """
    Suggests the user to restore a recently expired Premium subscription
    """

    ID: typing.Literal["suggestedActionRestorePremium"] = "suggestedActionRestorePremium"


class SuggestedActionSetPassword(BaseObject):
    """
    Suggests the user to set a 2-step verification password to be able to log in again

    :param authorization_delay: The number of days to pass between consecutive authorizations if the user declines to set password; if 0, then the user is advised to set the password for security reasons
    :type authorization_delay: :class:`Int32`
    """

    ID: typing.Literal["suggestedActionSetPassword"] = "suggestedActionSetPassword"
    authorization_delay: Int32 = 0


class SuggestedActionSubscribeToAnnualPremium(BaseObject):
    """
    Suggests the user to subscribe to the Premium subscription with annual payments
    """

    ID: typing.Literal["suggestedActionSubscribeToAnnualPremium"] = "suggestedActionSubscribeToAnnualPremium"


class SuggestedActionUpgradePremium(BaseObject):
    """
    Suggests the user to upgrade the Premium subscription from monthly payments to annual payments
    """

    ID: typing.Literal["suggestedActionUpgradePremium"] = "suggestedActionUpgradePremium"


class SuggestedActionViewChecksHint(BaseObject):
    """
    Suggests the user to view a hint about the meaning of one and two check marks on sent messages
    """

    ID: typing.Literal["suggestedActionViewChecksHint"] = "suggestedActionViewChecksHint"


SuggestedAction = typing.Union[
    SuggestedActionCheckPassword,
    SuggestedActionCheckPhoneNumber,
    SuggestedActionConvertToBroadcastGroup,
    SuggestedActionEnableArchiveAndMuteNewChats,
    SuggestedActionRestorePremium,
    SuggestedActionSetPassword,
    SuggestedActionSubscribeToAnnualPremium,
    SuggestedActionUpgradePremium,
    SuggestedActionViewChecksHint,
]


class Supergroup(BaseObject):
    """
    Represents a supergroup or channel with zero or more members (subscribers in the case of channels). From the point of view of the system, a channel is a special kind of a supergroup: only administrators can post and see the list of members, and posts from all administrators use the name and photo of the channel instead of individual names and profile photos. Unlike supergroups, channels can have an unlimited number of subscribers

    :param id: Supergroup or channel identifier
    :type id: :class:`Int53`
    :param date: Point in time (Unix timestamp) when the current user joined, or the point in time when the supergroup or channel was created, in case the user is not a member
    :type date: :class:`Int32`
    :param status: Status of the current user in the supergroup or channel; custom title will always be empty
    :type status: :class:`ChatMemberStatus`
    :param restriction_reason: If non-empty, contains a human-readable description of the reason why access to this supergroup or channel must be restricted
    :type restriction_reason: :class:`String`
    :param usernames: Usernames of the supergroup or channel; may be null, defaults to None
    :type usernames: :class:`Usernames`, optional
    :param has_linked_chat: True, if the channel has a discussion group, or the supergroup is the designated discussion group for a channel
    :type has_linked_chat: :class:`Bool`
    :param has_location: True, if the supergroup is connected to a location, i.e. the supergroup is a location-based supergroup
    :type has_location: :class:`Bool`
    :param sign_messages: True, if messages sent to the channel need to contain information about the sender. This field is only applicable to channels
    :type sign_messages: :class:`Bool`
    :param join_to_send_messages: True, if users need to join the supergroup before they can send messages. Always true for channels and non-discussion supergroups
    :type join_to_send_messages: :class:`Bool`
    :param join_by_request: True, if all users directly joining the supergroup need to be approved by supergroup administrators. Always false for channels and supergroups without username, location, or a linked chat
    :type join_by_request: :class:`Bool`
    :param is_slow_mode_enabled: True, if the slow mode is enabled in the supergroup
    :type is_slow_mode_enabled: :class:`Bool`
    :param is_channel: True, if the supergroup is a channel
    :type is_channel: :class:`Bool`
    :param is_broadcast_group: True, if the supergroup is a broadcast group, i.e. only administrators can send messages and there is no limit on the number of members
    :type is_broadcast_group: :class:`Bool`
    :param is_forum: True, if the supergroup must be shown as a forum by default
    :type is_forum: :class:`Bool`
    :param is_verified: True, if the supergroup or channel is verified
    :type is_verified: :class:`Bool`
    :param is_scam: True, if many users reported this supergroup or channel as a scam
    :type is_scam: :class:`Bool`
    :param is_fake: True, if many users reported this supergroup or channel as a fake account
    :type is_fake: :class:`Bool`
    :param member_count: Number of members in the supergroup or channel; 0 if unknown. Currently, it is guaranteed to be known only if the supergroup or channel was received through searchPublicChats, searchChatsNearby, getInactiveSupergroupChats, getSuitableDiscussionChats, getGroupsInCommon, getUserPrivacySettingRules, or in chatFolderInviteLinkInfo.missing_chat_ids, defaults to None
    :type member_count: :class:`Int32`, optional
    """

    ID: typing.Literal["supergroup"] = "supergroup"
    id: Int53
    date: Int32
    status: ChatMemberStatus
    restriction_reason: String
    usernames: typing.Optional[Usernames] = None
    has_linked_chat: Bool = False
    has_location: Bool = False
    sign_messages: Bool = False
    join_to_send_messages: Bool = False
    join_by_request: Bool = False
    is_slow_mode_enabled: Bool = False
    is_channel: Bool = False
    is_broadcast_group: Bool = False
    is_forum: Bool = False
    is_verified: Bool = False
    is_scam: Bool = False
    is_fake: Bool = False
    member_count: typing.Optional[Int32] = 0


class SupergroupFullInfo(BaseObject):
    """
    Contains full information about a supergroup or channel

    :param description: Supergroup or channel description
    :type description: :class:`String`
    :param slow_mode_delay: Delay between consecutive sent messages for non-administrator supergroup members, in seconds
    :type slow_mode_delay: :class:`Int32`
    :param slow_mode_delay_expires_in: Time left before next message can be sent in the supergroup, in seconds. An updateSupergroupFullInfo update is not triggered when value of this field changes, but both new and old values are non-zero
    :type slow_mode_delay_expires_in: :class:`Double`
    :param bot_commands: List of commands of bots in the group
    :type bot_commands: :class:`Vector[BotCommands]`
    :param photo: Chat photo; may be null if empty or unknown. If non-null, then it is the same photo as in chat.photo, defaults to None
    :type photo: :class:`ChatPhoto`, optional
    :param location: Location to which the supergroup is connected; may be null if none, defaults to None
    :type location: :class:`ChatLocation`, optional
    :param invite_link: Primary invite link for the chat; may be null. For chat administrators with can_invite_users right only, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    :param can_get_members: True, if members of the chat can be retrieved via getSupergroupMembers or searchChatMembers
    :type can_get_members: :class:`Bool`
    :param has_hidden_members: True, if non-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers
    :type has_hidden_members: :class:`Bool`
    :param can_hide_members: True, if non-administrators and non-bots can be hidden in responses to getSupergroupMembers and searchChatMembers for non-administrators
    :type can_hide_members: :class:`Bool`
    :param can_set_sticker_set: True, if the supergroup sticker set can be changed
    :type can_set_sticker_set: :class:`Bool`
    :param can_set_location: True, if the supergroup location can be changed
    :type can_set_location: :class:`Bool`
    :param can_get_statistics: True, if the supergroup or channel statistics are available
    :type can_get_statistics: :class:`Bool`
    :param can_toggle_aggressive_anti_spam: True, if aggressive anti-spam checks can be enabled or disabled in the supergroup
    :type can_toggle_aggressive_anti_spam: :class:`Bool`
    :param is_all_history_available: True, if new chat members will have access to old messages. In public, discussion, of forum groups and all channels, old messages are always available, so this option affects only private non-forum supergroups without a linked chat. The value of this field is only available to chat administrators
    :type is_all_history_available: :class:`Bool`
    :param has_aggressive_anti_spam_enabled: True, if aggressive anti-spam checks are enabled in the supergroup. The value of this field is only available to chat administrators
    :type has_aggressive_anti_spam_enabled: :class:`Bool`
    :param member_count: Number of members in the supergroup or channel; 0 if unknown, defaults to None
    :type member_count: :class:`Int32`, optional
    :param administrator_count: Number of privileged users in the supergroup or channel; 0 if unknown, defaults to None
    :type administrator_count: :class:`Int32`, optional
    :param restricted_count: Number of restricted users in the supergroup; 0 if unknown, defaults to None
    :type restricted_count: :class:`Int32`, optional
    :param banned_count: Number of users banned from chat; 0 if unknown, defaults to None
    :type banned_count: :class:`Int32`, optional
    :param linked_chat_id: Chat identifier of a discussion group for the channel, or a channel, for which the supergroup is the designated discussion group; 0 if none or unknown, defaults to None
    :type linked_chat_id: :class:`Int53`, optional
    :param sticker_set_id: Identifier of the supergroup sticker set; 0 if none, defaults to None
    :type sticker_set_id: :class:`Int64`, optional
    :param upgraded_from_basic_group_id: Identifier of the basic group from which supergroup was upgraded; 0 if none, defaults to None
    :type upgraded_from_basic_group_id: :class:`Int53`, optional
    :param upgraded_from_max_message_id: Identifier of the last message in the basic group from which supergroup was upgraded; 0 if none, defaults to None
    :type upgraded_from_max_message_id: :class:`Int53`, optional
    """

    ID: typing.Literal["supergroupFullInfo"] = "supergroupFullInfo"
    description: String
    slow_mode_delay: Int32
    slow_mode_delay_expires_in: Double
    bot_commands: Vector[BotCommands]
    photo: typing.Optional[ChatPhoto] = None
    location: typing.Optional[ChatLocation] = None
    invite_link: typing.Optional[ChatInviteLink] = None
    can_get_members: Bool = False
    has_hidden_members: Bool = False
    can_hide_members: Bool = False
    can_set_sticker_set: Bool = False
    can_set_location: Bool = False
    can_get_statistics: Bool = False
    can_toggle_aggressive_anti_spam: Bool = False
    is_all_history_available: Bool = False
    has_aggressive_anti_spam_enabled: Bool = False
    member_count: typing.Optional[Int32] = 0
    administrator_count: typing.Optional[Int32] = 0
    restricted_count: typing.Optional[Int32] = 0
    banned_count: typing.Optional[Int32] = 0
    linked_chat_id: typing.Optional[Int53] = 0
    sticker_set_id: typing.Optional[Int64] = 0
    upgraded_from_basic_group_id: typing.Optional[Int53] = 0
    upgraded_from_max_message_id: typing.Optional[Int53] = 0


class SupergroupMembersFilterAdministrators(BaseObject):
    """
    Returns the owner and administrators
    """

    ID: typing.Literal["supergroupMembersFilterAdministrators"] = "supergroupMembersFilterAdministrators"


class SupergroupMembersFilterBanned(BaseObject):
    """
    Returns users banned from the supergroup or channel; can be used only by administrators

    :param query: Query to search for
    :type query: :class:`String`
    """

    ID: typing.Literal["supergroupMembersFilterBanned"] = "supergroupMembersFilterBanned"
    query: String


class SupergroupMembersFilterBots(BaseObject):
    """
    Returns bot members of the supergroup or channel
    """

    ID: typing.Literal["supergroupMembersFilterBots"] = "supergroupMembersFilterBots"


class SupergroupMembersFilterContacts(BaseObject):
    """
    Returns contacts of the user, which are members of the supergroup or channel

    :param query: Query to search for
    :type query: :class:`String`
    """

    ID: typing.Literal["supergroupMembersFilterContacts"] = "supergroupMembersFilterContacts"
    query: String


class SupergroupMembersFilterMention(BaseObject):
    """
    Returns users which can be mentioned in the supergroup

    :param query: Query to search for
    :type query: :class:`String`
    :param message_thread_id: If non-zero, the identifier of the current message thread
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["supergroupMembersFilterMention"] = "supergroupMembersFilterMention"
    query: String
    message_thread_id: Int53


class SupergroupMembersFilterRecent(BaseObject):
    """
    Returns recently active users in reverse chronological order
    """

    ID: typing.Literal["supergroupMembersFilterRecent"] = "supergroupMembersFilterRecent"


class SupergroupMembersFilterRestricted(BaseObject):
    """
    Returns restricted supergroup members; can be used only by administrators

    :param query: Query to search for
    :type query: :class:`String`
    """

    ID: typing.Literal["supergroupMembersFilterRestricted"] = "supergroupMembersFilterRestricted"
    query: String


class SupergroupMembersFilterSearch(BaseObject):
    """
    Used to search for supergroup or channel members via a (string) query

    :param query: Query to search for
    :type query: :class:`String`
    """

    ID: typing.Literal["supergroupMembersFilterSearch"] = "supergroupMembersFilterSearch"
    query: String


SupergroupMembersFilter = typing.Union[
    SupergroupMembersFilterAdministrators,
    SupergroupMembersFilterBanned,
    SupergroupMembersFilterBots,
    SupergroupMembersFilterContacts,
    SupergroupMembersFilterMention,
    SupergroupMembersFilterRecent,
    SupergroupMembersFilterRestricted,
    SupergroupMembersFilterSearch,
]


class TMeUrl(BaseObject):
    """
    Represents a URL linking to an internal Telegram entity

    :param url: URL
    :type url: :class:`String`
    :param type_: Type of the URL
    :type type_: :class:`TMeUrlType`
    """

    ID: typing.Literal["tMeUrl"] = "tMeUrl"
    url: String
    type_: TMeUrlType = Field(..., alias="type")


class TMeUrlTypeChatInvite(BaseObject):
    """
    A chat invite link

    :param info: Information about the chat invite link
    :type info: :class:`ChatInviteLinkInfo`
    """

    ID: typing.Literal["tMeUrlTypeChatInvite"] = "tMeUrlTypeChatInvite"
    info: ChatInviteLinkInfo


class TMeUrlTypeStickerSet(BaseObject):
    """
    A URL linking to a sticker set

    :param sticker_set_id: Identifier of the sticker set
    :type sticker_set_id: :class:`Int64`
    """

    ID: typing.Literal["tMeUrlTypeStickerSet"] = "tMeUrlTypeStickerSet"
    sticker_set_id: Int64


class TMeUrlTypeSupergroup(BaseObject):
    """
    A URL linking to a public supergroup or channel

    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["tMeUrlTypeSupergroup"] = "tMeUrlTypeSupergroup"
    supergroup_id: Int53


class TMeUrlTypeUser(BaseObject):
    """
    A URL linking to a user

    :param user_id: Identifier of the user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["tMeUrlTypeUser"] = "tMeUrlTypeUser"
    user_id: Int53


TMeUrlType = typing.Union[
    TMeUrlTypeChatInvite,
    TMeUrlTypeStickerSet,
    TMeUrlTypeSupergroup,
    TMeUrlTypeUser,
]


class TMeUrls(BaseObject):
    """
    Contains a list of t.me URLs

    :param urls: List of URLs
    :type urls: :class:`Vector[TMeUrl]`
    """

    ID: typing.Literal["tMeUrls"] = "tMeUrls"
    urls: Vector[TMeUrl]


class TargetChatChosen(BaseObject):
    """
    The chat needs to be chosen by the user among chats of the specified types

    :param allow_user_chats: True, if private chats with ordinary users are allowed
    :type allow_user_chats: :class:`Bool`
    :param allow_bot_chats: True, if private chats with other bots are allowed
    :type allow_bot_chats: :class:`Bool`
    :param allow_group_chats: True, if basic group and supergroup chats are allowed
    :type allow_group_chats: :class:`Bool`
    :param allow_channel_chats: True, if channel chats are allowed
    :type allow_channel_chats: :class:`Bool`
    """

    ID: typing.Literal["targetChatChosen"] = "targetChatChosen"
    allow_user_chats: Bool = False
    allow_bot_chats: Bool = False
    allow_group_chats: Bool = False
    allow_channel_chats: Bool = False


class TargetChatCurrent(BaseObject):
    """
    The currently opened chat needs to be kept
    """

    ID: typing.Literal["targetChatCurrent"] = "targetChatCurrent"


class TargetChatInternalLink(BaseObject):
    """
    The chat needs to be open with the provided internal link

    :param link: An internal link pointing to the chat
    :type link: :class:`InternalLinkType`
    """

    ID: typing.Literal["targetChatInternalLink"] = "targetChatInternalLink"
    link: InternalLinkType


TargetChat = typing.Union[
    TargetChatChosen,
    TargetChatCurrent,
    TargetChatInternalLink,
]


class TemporaryPasswordState(BaseObject):
    """
    Returns information about the availability of a temporary password, which can be used for payments

    :param valid_for: Time left before the temporary password expires, in seconds
    :type valid_for: :class:`Int32`
    :param has_password: True, if a temporary password is available
    :type has_password: :class:`Bool`
    """

    ID: typing.Literal["temporaryPasswordState"] = "temporaryPasswordState"
    valid_for: Int32
    has_password: Bool = False


class TermsOfService(BaseObject):
    """
    Contains Telegram terms of service

    :param text: Text of the terms of service
    :type text: :class:`FormattedText`
    :param min_user_age: The minimum age of a user to be able to accept the terms; 0 if age isn't restricted
    :type min_user_age: :class:`Int32`
    :param show_popup: True, if a blocking popup with terms of service must be shown to the user
    :type show_popup: :class:`Bool`
    """

    ID: typing.Literal["termsOfService"] = "termsOfService"
    text: FormattedText
    min_user_age: Int32
    show_popup: Bool = False


class TestBytes(BaseObject):
    """
    A simple object containing a sequence of bytes; for testing only

    :param value: Bytes
    :type value: :class:`Bytes`
    """

    ID: typing.Literal["testBytes"] = "testBytes"
    value: Bytes


class TestInt(BaseObject):
    """
    A simple object containing a number; for testing only

    :param value: Number
    :type value: :class:`Int32`
    """

    ID: typing.Literal["testInt"] = "testInt"
    value: Int32


class TestString(BaseObject):
    """
    A simple object containing a string; for testing only

    :param value: String
    :type value: :class:`String`
    """

    ID: typing.Literal["testString"] = "testString"
    value: String


class TestVectorInt(BaseObject):
    """
    A simple object containing a vector of numbers; for testing only

    :param value: Vector of numbers
    :type value: :class:`Vector[Int32]`
    """

    ID: typing.Literal["testVectorInt"] = "testVectorInt"
    value: Vector[Int32]


class TestVectorIntObject(BaseObject):
    """
    A simple object containing a vector of objects that hold a number; for testing only

    :param value: Vector of objects
    :type value: :class:`Vector[TestInt]`
    """

    ID: typing.Literal["testVectorIntObject"] = "testVectorIntObject"
    value: Vector[TestInt]


class TestVectorString(BaseObject):
    """
    A simple object containing a vector of strings; for testing only

    :param value: Vector of strings
    :type value: :class:`Vector[String]`
    """

    ID: typing.Literal["testVectorString"] = "testVectorString"
    value: Vector[String]


class TestVectorStringObject(BaseObject):
    """
    A simple object containing a vector of objects that hold a string; for testing only

    :param value: Vector of objects
    :type value: :class:`Vector[TestString]`
    """

    ID: typing.Literal["testVectorStringObject"] = "testVectorStringObject"
    value: Vector[TestString]


class Text(BaseObject):
    """
    Contains some text

    :param text: Text
    :type text: :class:`String`
    """

    ID: typing.Literal["text"] = "text"
    text: String


class TextEntities(BaseObject):
    """
    Contains a list of text entities

    :param entities: List of text entities
    :type entities: :class:`Vector[TextEntity]`
    """

    ID: typing.Literal["textEntities"] = "textEntities"
    entities: Vector[TextEntity]


class TextEntity(BaseObject):
    """
    Represents a part of the text that needs to be formatted in some unusual way

    :param offset: Offset of the entity, in UTF-16 code units
    :type offset: :class:`Int32`
    :param length: Length of the entity, in UTF-16 code units
    :type length: :class:`Int32`
    :param type_: Type of the entity
    :type type_: :class:`TextEntityType`
    """

    ID: typing.Literal["textEntity"] = "textEntity"
    offset: Int32
    length: Int32
    type_: TextEntityType = Field(..., alias="type")


class TextEntityTypeBankCardNumber(BaseObject):
    """
    A bank card number. The getBankCardInfo method can be used to get information about the bank card
    """

    ID: typing.Literal["textEntityTypeBankCardNumber"] = "textEntityTypeBankCardNumber"


class TextEntityTypeBold(BaseObject):
    """
    A bold text
    """

    ID: typing.Literal["textEntityTypeBold"] = "textEntityTypeBold"


class TextEntityTypeBotCommand(BaseObject):
    """
    A bot command, beginning with "/"
    """

    ID: typing.Literal["textEntityTypeBotCommand"] = "textEntityTypeBotCommand"


class TextEntityTypeCashtag(BaseObject):
    """
    A cashtag text, beginning with "$" and consisting of capital English letters (e.g., "$USD")
    """

    ID: typing.Literal["textEntityTypeCashtag"] = "textEntityTypeCashtag"


class TextEntityTypeCode(BaseObject):
    """
    Text that must be formatted as if inside a code HTML tag
    """

    ID: typing.Literal["textEntityTypeCode"] = "textEntityTypeCode"


class TextEntityTypeCustomEmoji(BaseObject):
    """
    A custom emoji. The text behind a custom emoji must be an emoji. Only premium users can use premium custom emoji

    :param custom_emoji_id: Unique identifier of the custom emoji
    :type custom_emoji_id: :class:`Int64`
    """

    ID: typing.Literal["textEntityTypeCustomEmoji"] = "textEntityTypeCustomEmoji"
    custom_emoji_id: Int64


class TextEntityTypeEmailAddress(BaseObject):
    """
    An email address
    """

    ID: typing.Literal["textEntityTypeEmailAddress"] = "textEntityTypeEmailAddress"


class TextEntityTypeHashtag(BaseObject):
    """
    A hashtag text, beginning with "#"
    """

    ID: typing.Literal["textEntityTypeHashtag"] = "textEntityTypeHashtag"


class TextEntityTypeItalic(BaseObject):
    """
    An italic text
    """

    ID: typing.Literal["textEntityTypeItalic"] = "textEntityTypeItalic"


class TextEntityTypeMediaTimestamp(BaseObject):
    """
    A media timestamp

    :param media_timestamp: Timestamp from which a video/audio/video note/voice note playing must start, in seconds. The media can be in the content or the web page preview of the current message, or in the same places in the replied message
    :type media_timestamp: :class:`Int32`
    """

    ID: typing.Literal["textEntityTypeMediaTimestamp"] = "textEntityTypeMediaTimestamp"
    media_timestamp: Int32


class TextEntityTypeMention(BaseObject):
    """
    A mention of a user, a supergroup, or a channel by their username
    """

    ID: typing.Literal["textEntityTypeMention"] = "textEntityTypeMention"


class TextEntityTypeMentionName(BaseObject):
    """
    A text shows instead of a raw mention of the user (e.g., when the user has no username)

    :param user_id: Identifier of the mentioned user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["textEntityTypeMentionName"] = "textEntityTypeMentionName"
    user_id: Int53


class TextEntityTypePhoneNumber(BaseObject):
    """
    A phone number
    """

    ID: typing.Literal["textEntityTypePhoneNumber"] = "textEntityTypePhoneNumber"


class TextEntityTypePre(BaseObject):
    """
    Text that must be formatted as if inside a pre HTML tag
    """

    ID: typing.Literal["textEntityTypePre"] = "textEntityTypePre"


class TextEntityTypePreCode(BaseObject):
    """
    Text that must be formatted as if inside pre, and code HTML tags

    :param language: Programming language of the code; as defined by the sender
    :type language: :class:`String`
    """

    ID: typing.Literal["textEntityTypePreCode"] = "textEntityTypePreCode"
    language: String


class TextEntityTypeSpoiler(BaseObject):
    """
    A spoiler text
    """

    ID: typing.Literal["textEntityTypeSpoiler"] = "textEntityTypeSpoiler"


class TextEntityTypeStrikethrough(BaseObject):
    """
    A strikethrough text
    """

    ID: typing.Literal["textEntityTypeStrikethrough"] = "textEntityTypeStrikethrough"


class TextEntityTypeTextUrl(BaseObject):
    """
    A text description shown instead of a raw URL

    :param url: HTTP or tg:// URL to be opened when the link is clicked
    :type url: :class:`String`
    """

    ID: typing.Literal["textEntityTypeTextUrl"] = "textEntityTypeTextUrl"
    url: String


class TextEntityTypeUnderline(BaseObject):
    """
    An underlined text
    """

    ID: typing.Literal["textEntityTypeUnderline"] = "textEntityTypeUnderline"


class TextEntityTypeUrl(BaseObject):
    """
    An HTTP URL
    """

    ID: typing.Literal["textEntityTypeUrl"] = "textEntityTypeUrl"


TextEntityType = typing.Union[
    TextEntityTypeBankCardNumber,
    TextEntityTypeBold,
    TextEntityTypeBotCommand,
    TextEntityTypeCashtag,
    TextEntityTypeCode,
    TextEntityTypeCustomEmoji,
    TextEntityTypeEmailAddress,
    TextEntityTypeHashtag,
    TextEntityTypeItalic,
    TextEntityTypeMediaTimestamp,
    TextEntityTypeMention,
    TextEntityTypeMentionName,
    TextEntityTypePhoneNumber,
    TextEntityTypePre,
    TextEntityTypePreCode,
    TextEntityTypeSpoiler,
    TextEntityTypeStrikethrough,
    TextEntityTypeTextUrl,
    TextEntityTypeUnderline,
    TextEntityTypeUrl,
]


class TextParseModeHTML(BaseObject):
    """
    The text uses HTML-style formatting. The same as Telegram Bot API "HTML" parse mode
    """

    ID: typing.Literal["textParseModeHTML"] = "textParseModeHTML"


class TextParseModeMarkdown(BaseObject):
    """
    The text uses Markdown-style formatting

    :param version: Version of the parser: 0 or 1 - Telegram Bot API "Markdown" parse mode, 2 - Telegram Bot API "MarkdownV2" parse mode
    :type version: :class:`Int32`
    """

    ID: typing.Literal["textParseModeMarkdown"] = "textParseModeMarkdown"
    version: Int32


TextParseMode = typing.Union[
    TextParseModeHTML,
    TextParseModeMarkdown,
]


class ThemeParameters(BaseObject):
    """
    Contains parameters of the application theme

    :param background_color: A color of the background in the RGB24 format
    :type background_color: :class:`Int32`
    :param secondary_background_color: A secondary color for the background in the RGB24 format
    :type secondary_background_color: :class:`Int32`
    :param text_color: A color of text in the RGB24 format
    :type text_color: :class:`Int32`
    :param hint_color: A color of hints in the RGB24 format
    :type hint_color: :class:`Int32`
    :param link_color: A color of links in the RGB24 format
    :type link_color: :class:`Int32`
    :param button_color: A color of the buttons in the RGB24 format
    :type button_color: :class:`Int32`
    :param button_text_color: A color of text on the buttons in the RGB24 format
    :type button_text_color: :class:`Int32`
    """

    ID: typing.Literal["themeParameters"] = "themeParameters"
    background_color: Int32
    secondary_background_color: Int32
    text_color: Int32
    hint_color: Int32
    link_color: Int32
    button_color: Int32
    button_text_color: Int32


class ThemeSettings(BaseObject):
    """
    Describes theme settings

    :param accent_color: Theme accent color in ARGB format
    :type accent_color: :class:`Int32`
    :param outgoing_message_fill: The fill to be used as a background for outgoing messages
    :type outgoing_message_fill: :class:`BackgroundFill`
    :param animate_outgoing_message_fill: If true, the freeform gradient fill needs to be animated on every sent message
    :type animate_outgoing_message_fill: :class:`Bool`
    :param outgoing_message_accent_color: Accent color of outgoing messages in ARGB format
    :type outgoing_message_accent_color: :class:`Int32`
    :param background: The background to be used in chats; may be null, defaults to None
    :type background: :class:`Background`, optional
    """

    ID: typing.Literal["themeSettings"] = "themeSettings"
    accent_color: Int32
    outgoing_message_fill: BackgroundFill
    animate_outgoing_message_fill: Bool
    outgoing_message_accent_color: Int32
    background: typing.Optional[Background] = None


class Thumbnail(BaseObject):
    """
    Represents a thumbnail

    :param format: Thumbnail format
    :type format: :class:`ThumbnailFormat`
    :param width: Thumbnail width
    :type width: :class:`Int32`
    :param height: Thumbnail height
    :type height: :class:`Int32`
    :param file: The thumbnail
    :type file: :class:`File`
    """

    ID: typing.Literal["thumbnail"] = "thumbnail"
    format: ThumbnailFormat
    width: Int32
    height: Int32
    file: File


class ThumbnailFormatGif(BaseObject):
    """
    The thumbnail is in static GIF format. It will be used only for some bot inline query results
    """

    ID: typing.Literal["thumbnailFormatGif"] = "thumbnailFormatGif"


class ThumbnailFormatJpeg(BaseObject):
    """
    The thumbnail is in JPEG format
    """

    ID: typing.Literal["thumbnailFormatJpeg"] = "thumbnailFormatJpeg"


class ThumbnailFormatMpeg4(BaseObject):
    """
    The thumbnail is in MPEG4 format. It will be used only for some animations and videos
    """

    ID: typing.Literal["thumbnailFormatMpeg4"] = "thumbnailFormatMpeg4"


class ThumbnailFormatPng(BaseObject):
    """
    The thumbnail is in PNG format. It will be used only for background patterns
    """

    ID: typing.Literal["thumbnailFormatPng"] = "thumbnailFormatPng"


class ThumbnailFormatTgs(BaseObject):
    """
    The thumbnail is in TGS format. It will be used only for TGS sticker sets
    """

    ID: typing.Literal["thumbnailFormatTgs"] = "thumbnailFormatTgs"


class ThumbnailFormatWebm(BaseObject):
    """
    The thumbnail is in WEBM format. It will be used only for WEBM sticker sets
    """

    ID: typing.Literal["thumbnailFormatWebm"] = "thumbnailFormatWebm"


class ThumbnailFormatWebp(BaseObject):
    """
    The thumbnail is in WEBP format. It will be used only for some stickers
    """

    ID: typing.Literal["thumbnailFormatWebp"] = "thumbnailFormatWebp"


ThumbnailFormat = typing.Union[
    ThumbnailFormatGif,
    ThumbnailFormatJpeg,
    ThumbnailFormatMpeg4,
    ThumbnailFormatPng,
    ThumbnailFormatTgs,
    ThumbnailFormatWebm,
    ThumbnailFormatWebp,
]


class TopChatCategoryBots(BaseObject):
    """
    A category containing frequently used private chats with bot users
    """

    ID: typing.Literal["topChatCategoryBots"] = "topChatCategoryBots"


class TopChatCategoryCalls(BaseObject):
    """
    A category containing frequently used chats used for calls
    """

    ID: typing.Literal["topChatCategoryCalls"] = "topChatCategoryCalls"


class TopChatCategoryChannels(BaseObject):
    """
    A category containing frequently used channels
    """

    ID: typing.Literal["topChatCategoryChannels"] = "topChatCategoryChannels"


class TopChatCategoryForwardChats(BaseObject):
    """
    A category containing frequently used chats used to forward messages
    """

    ID: typing.Literal["topChatCategoryForwardChats"] = "topChatCategoryForwardChats"


class TopChatCategoryGroups(BaseObject):
    """
    A category containing frequently used basic groups and supergroups
    """

    ID: typing.Literal["topChatCategoryGroups"] = "topChatCategoryGroups"


class TopChatCategoryInlineBots(BaseObject):
    """
    A category containing frequently used chats with inline bots sorted by their usage in inline mode
    """

    ID: typing.Literal["topChatCategoryInlineBots"] = "topChatCategoryInlineBots"


class TopChatCategoryUsers(BaseObject):
    """
    A category containing frequently used private chats with non-bot users
    """

    ID: typing.Literal["topChatCategoryUsers"] = "topChatCategoryUsers"


TopChatCategory = typing.Union[
    TopChatCategoryBots,
    TopChatCategoryCalls,
    TopChatCategoryChannels,
    TopChatCategoryForwardChats,
    TopChatCategoryGroups,
    TopChatCategoryInlineBots,
    TopChatCategoryUsers,
]


class TrendingStickerSets(BaseObject):
    """
    Represents a list of trending sticker sets

    :param total_count: Approximate total number of trending sticker sets
    :type total_count: :class:`Int32`
    :param sets: List of trending sticker sets
    :type sets: :class:`Vector[StickerSetInfo]`
    :param is_premium: True, if the list contains sticker sets with premium stickers
    :type is_premium: :class:`Bool`
    """

    ID: typing.Literal["trendingStickerSets"] = "trendingStickerSets"
    total_count: Int32
    sets: Vector[StickerSetInfo]
    is_premium: Bool = False


class UnconfirmedSession(BaseObject):
    """
    Contains information about an unconfirmed session

    :param id: Session identifier
    :type id: :class:`Int64`
    :param log_in_date: Point in time (Unix timestamp) when the user has logged in
    :type log_in_date: :class:`Int32`
    :param device_model: Model of the device that was used for the session creation, as provided by the application
    :type device_model: :class:`String`
    :param location: A human-readable description of the location from which the session was created, based on the IP address
    :type location: :class:`String`
    """

    ID: typing.Literal["unconfirmedSession"] = "unconfirmedSession"
    id: Int64
    log_in_date: Int32
    device_model: String
    location: String


class UnreadReaction(BaseObject):
    """
    Contains information about an unread reaction to a message

    :param type_: Type of the reaction
    :type type_: :class:`ReactionType`
    :param sender_id: Identifier of the sender, added the reaction
    :type sender_id: :class:`MessageSender`
    :param is_big: True, if the reaction was added with a big animation
    :type is_big: :class:`Bool`
    """

    ID: typing.Literal["unreadReaction"] = "unreadReaction"
    type_: ReactionType = Field(..., alias="type")
    sender_id: MessageSender
    is_big: Bool = False


class UpdateActiveEmojiReactions(BaseObject):
    """
    The list of active emoji reactions has changed

    :param emojis: The new list of active emoji reactions
    :type emojis: :class:`Vector[String]`
    """

    ID: typing.Literal["updateActiveEmojiReactions"] = "updateActiveEmojiReactions"
    emojis: Vector[String]


class UpdateActiveNotifications(BaseObject):
    """
    Contains active notifications that was shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any updateNotification and updateNotificationGroup update

    :param groups: Lists of active notification groups
    :type groups: :class:`Vector[NotificationGroup]`
    """

    ID: typing.Literal["updateActiveNotifications"] = "updateActiveNotifications"
    groups: Vector[NotificationGroup]


class UpdateAddChatMembersPrivacyForbidden(BaseObject):
    """
    Adding users to a chat has failed because of their privacy settings. An invite link can be shared with the users if appropriate

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param user_ids: Identifiers of users, which weren't added because of their privacy settings
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["updateAddChatMembersPrivacyForbidden"] = "updateAddChatMembersPrivacyForbidden"
    chat_id: Int53
    user_ids: Vector[Int53]


class UpdateAnimatedEmojiMessageClicked(BaseObject):
    """
    Some animated emoji message was clicked and a big animated sticker must be played if the message is visible on the screen. chatActionWatchingAnimations with the text of the message needs to be sent if the sticker is played

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param sticker: The animated sticker to be played
    :type sticker: :class:`Sticker`
    """

    ID: typing.Literal["updateAnimatedEmojiMessageClicked"] = "updateAnimatedEmojiMessageClicked"
    chat_id: Int53
    message_id: Int53
    sticker: Sticker


class UpdateAnimationSearchParameters(BaseObject):
    """
    The parameters of animation search through getOption("animation_search_bot_username") bot has changed

    :param provider: Name of the animation search provider
    :type provider: :class:`String`
    :param emojis: The new list of emojis suggested for searching
    :type emojis: :class:`Vector[String]`
    """

    ID: typing.Literal["updateAnimationSearchParameters"] = "updateAnimationSearchParameters"
    provider: String
    emojis: Vector[String]


class UpdateAttachmentMenuBots(BaseObject):
    """
    The list of bots added to attachment or side menu has changed

    :param bots: The new list of bots. The bots must not be shown on scheduled messages screen
    :type bots: :class:`Vector[AttachmentMenuBot]`
    """

    ID: typing.Literal["updateAttachmentMenuBots"] = "updateAttachmentMenuBots"
    bots: Vector[AttachmentMenuBot]


class UpdateAuthorizationState(BaseObject):
    """
    The user authorization state has changed

    :param authorization_state: New authorization state
    :type authorization_state: :class:`AuthorizationState`
    """

    ID: typing.Literal["updateAuthorizationState"] = "updateAuthorizationState"
    authorization_state: AuthorizationState


class UpdateAutosaveSettings(BaseObject):
    """
    Autosave settings for some type of chats were updated

    :param scope: Type of chats for which autosave settings were updated
    :type scope: :class:`AutosaveSettingsScope`
    :param settings: The new autosave settings; may be null if the settings are reset to default, defaults to None
    :type settings: :class:`ScopeAutosaveSettings`, optional
    """

    ID: typing.Literal["updateAutosaveSettings"] = "updateAutosaveSettings"
    scope: AutosaveSettingsScope
    settings: typing.Optional[ScopeAutosaveSettings] = None


class UpdateBasicGroup(BaseObject):
    """
    Some data of a basic group has changed. This update is guaranteed to come before the basic group identifier is returned to the application

    :param basic_group: New data about the group
    :type basic_group: :class:`BasicGroup`
    """

    ID: typing.Literal["updateBasicGroup"] = "updateBasicGroup"
    basic_group: BasicGroup


class UpdateBasicGroupFullInfo(BaseObject):
    """
    Some data in basicGroupFullInfo has been changed

    :param basic_group_id: Identifier of a basic group
    :type basic_group_id: :class:`Int53`
    :param basic_group_full_info: New full information about the group
    :type basic_group_full_info: :class:`BasicGroupFullInfo`
    """

    ID: typing.Literal["updateBasicGroupFullInfo"] = "updateBasicGroupFullInfo"
    basic_group_id: Int53
    basic_group_full_info: BasicGroupFullInfo


class UpdateCall(BaseObject):
    """
    New call was created or information about a call was updated

    :param call: New data about a call
    :type call: :class:`Call`
    """

    ID: typing.Literal["updateCall"] = "updateCall"
    call: Call


class UpdateChatAction(BaseObject):
    """
    A message sender activity in the chat has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param sender_id: Identifier of a message sender performing the action
    :type sender_id: :class:`MessageSender`
    :param action: The action
    :type action: :class:`ChatAction`
    :param message_thread_id: If not 0, a message thread identifier in which the action was performed
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["updateChatAction"] = "updateChatAction"
    chat_id: Int53
    sender_id: MessageSender
    action: ChatAction
    message_thread_id: Int53 = 0


class UpdateChatActionBar(BaseObject):
    """
    The chat action bar was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param action_bar: The new value of the action bar; may be null, defaults to None
    :type action_bar: :class:`ChatActionBar`, optional
    """

    ID: typing.Literal["updateChatActionBar"] = "updateChatActionBar"
    chat_id: Int53
    action_bar: typing.Optional[ChatActionBar] = None


class UpdateChatActiveStories(BaseObject):
    """
    The list of active stories posted by a specific chat has changed

    :param active_stories: The new list of active stories
    :type active_stories: :class:`ChatActiveStories`
    """

    ID: typing.Literal["updateChatActiveStories"] = "updateChatActiveStories"
    active_stories: ChatActiveStories


class UpdateChatAvailableReactions(BaseObject):
    """
    The chat available reactions were changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param available_reactions: The new reactions, available in the chat
    :type available_reactions: :class:`ChatAvailableReactions`
    """

    ID: typing.Literal["updateChatAvailableReactions"] = "updateChatAvailableReactions"
    chat_id: Int53
    available_reactions: ChatAvailableReactions


class UpdateChatBackground(BaseObject):
    """
    The chat background was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param background: The new chat background; may be null if background was reset to default, defaults to None
    :type background: :class:`ChatBackground`, optional
    """

    ID: typing.Literal["updateChatBackground"] = "updateChatBackground"
    chat_id: Int53
    background: typing.Optional[ChatBackground] = None


class UpdateChatBlockList(BaseObject):
    """
    A chat was blocked or unblocked

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param block_list: Block list to which the chat is added; may be null if none, defaults to None
    :type block_list: :class:`BlockList`, optional
    """

    ID: typing.Literal["updateChatBlockList"] = "updateChatBlockList"
    chat_id: Int53
    block_list: typing.Optional[BlockList] = None


class UpdateChatDefaultDisableNotification(BaseObject):
    """
    The value of the default disable_notification parameter, used when a message is sent to the chat, was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param default_disable_notification: The new default_disable_notification value
    :type default_disable_notification: :class:`Bool`
    """

    ID: typing.Literal["updateChatDefaultDisableNotification"] = "updateChatDefaultDisableNotification"
    chat_id: Int53
    default_disable_notification: Bool


class UpdateChatDraftMessage(BaseObject):
    """
    A chat draft has changed. Be aware that the update may come in the currently opened chat but with old content of the draft. If the user has changed the content of the draft, this update mustn't be applied

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param positions: The new chat positions in the chat lists
    :type positions: :class:`Vector[ChatPosition]`
    :param draft_message: The new draft message; may be null, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    """

    ID: typing.Literal["updateChatDraftMessage"] = "updateChatDraftMessage"
    chat_id: Int53
    positions: Vector[ChatPosition]
    draft_message: typing.Optional[DraftMessage] = None


class UpdateChatFolders(BaseObject):
    """
    The list of chat folders or a chat folder has changed

    :param chat_folders: The new list of chat folders
    :type chat_folders: :class:`Vector[ChatFolderInfo]`
    :param main_chat_list_position: Position of the main chat list among chat folders, 0-based
    :type main_chat_list_position: :class:`Int32`
    """

    ID: typing.Literal["updateChatFolders"] = "updateChatFolders"
    chat_folders: Vector[ChatFolderInfo]
    main_chat_list_position: Int32


class UpdateChatHasProtectedContent(BaseObject):
    """
    A chat content was allowed or restricted for saving

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param has_protected_content: New value of has_protected_content
    :type has_protected_content: :class:`Bool`
    """

    ID: typing.Literal["updateChatHasProtectedContent"] = "updateChatHasProtectedContent"
    chat_id: Int53
    has_protected_content: Bool


class UpdateChatHasScheduledMessages(BaseObject):
    """
    A chat's has_scheduled_messages field has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param has_scheduled_messages: New value of has_scheduled_messages
    :type has_scheduled_messages: :class:`Bool`
    """

    ID: typing.Literal["updateChatHasScheduledMessages"] = "updateChatHasScheduledMessages"
    chat_id: Int53
    has_scheduled_messages: Bool


class UpdateChatIsMarkedAsUnread(BaseObject):
    """
    A chat was marked as unread or was read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_marked_as_unread: New value of is_marked_as_unread
    :type is_marked_as_unread: :class:`Bool`
    """

    ID: typing.Literal["updateChatIsMarkedAsUnread"] = "updateChatIsMarkedAsUnread"
    chat_id: Int53
    is_marked_as_unread: Bool


class UpdateChatIsTranslatable(BaseObject):
    """
    Translation of chat messages was enabled or disabled

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_translatable: New value of is_translatable
    :type is_translatable: :class:`Bool`
    """

    ID: typing.Literal["updateChatIsTranslatable"] = "updateChatIsTranslatable"
    chat_id: Int53
    is_translatable: Bool


class UpdateChatLastMessage(BaseObject):
    """
    The last message of a chat was changed. If last_message is null, then the last message in the chat became unknown. Some new unknown messages might be added to the chat in this case

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param positions: The new chat positions in the chat lists
    :type positions: :class:`Vector[ChatPosition]`
    :param last_message: The new last message in the chat; may be null, defaults to None
    :type last_message: :class:`Message`, optional
    """

    ID: typing.Literal["updateChatLastMessage"] = "updateChatLastMessage"
    chat_id: Int53
    positions: Vector[ChatPosition]
    last_message: typing.Optional[Message] = None


class UpdateChatMember(BaseObject):
    """
    User rights changed in a chat; for bots only

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param actor_user_id: Identifier of the user, changing the rights
    :type actor_user_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) when the user rights was changed
    :type date: :class:`Int32`
    :param old_chat_member: Previous chat member
    :type old_chat_member: :class:`ChatMember`
    :param new_chat_member: New chat member
    :type new_chat_member: :class:`ChatMember`
    :param invite_link: If user has joined the chat using an invite link, the invite link; may be null, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    :param via_chat_folder_invite_link: True, if the user has joined the chat using an invite link for a chat folder
    :type via_chat_folder_invite_link: :class:`Bool`
    """

    ID: typing.Literal["updateChatMember"] = "updateChatMember"
    chat_id: Int53
    actor_user_id: Int53
    date: Int32
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: typing.Optional[ChatInviteLink] = None
    via_chat_folder_invite_link: Bool = False


class UpdateChatMessageAutoDeleteTime(BaseObject):
    """
    The message auto-delete or self-destruct timer setting for a chat was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_auto_delete_time: New value of message_auto_delete_time
    :type message_auto_delete_time: :class:`Int32`
    """

    ID: typing.Literal["updateChatMessageAutoDeleteTime"] = "updateChatMessageAutoDeleteTime"
    chat_id: Int53
    message_auto_delete_time: Int32


class UpdateChatMessageSender(BaseObject):
    """
    The message sender that is selected to send messages in a chat has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_sender_id: New value of message_sender_id; may be null if the user can't change message sender, defaults to None
    :type message_sender_id: :class:`MessageSender`, optional
    """

    ID: typing.Literal["updateChatMessageSender"] = "updateChatMessageSender"
    chat_id: Int53
    message_sender_id: typing.Optional[MessageSender] = None


class UpdateChatNotificationSettings(BaseObject):
    """
    Notification settings for a chat were changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param notification_settings: The new notification settings
    :type notification_settings: :class:`ChatNotificationSettings`
    """

    ID: typing.Literal["updateChatNotificationSettings"] = "updateChatNotificationSettings"
    chat_id: Int53
    notification_settings: ChatNotificationSettings


class UpdateChatOnlineMemberCount(BaseObject):
    """
    The number of online group members has changed. This update with non-zero number of online group members is sent only for currently opened chats. There is no guarantee that it will be sent just after the number of online users has changed

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param online_member_count: New number of online members in the chat, or 0 if unknown
    :type online_member_count: :class:`Int32`
    """

    ID: typing.Literal["updateChatOnlineMemberCount"] = "updateChatOnlineMemberCount"
    chat_id: Int53
    online_member_count: Int32


class UpdateChatPendingJoinRequests(BaseObject):
    """
    The chat pending join requests were changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param pending_join_requests: The new data about pending join requests; may be null, defaults to None
    :type pending_join_requests: :class:`ChatJoinRequestsInfo`, optional
    """

    ID: typing.Literal["updateChatPendingJoinRequests"] = "updateChatPendingJoinRequests"
    chat_id: Int53
    pending_join_requests: typing.Optional[ChatJoinRequestsInfo] = None


class UpdateChatPermissions(BaseObject):
    """
    Chat permissions was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param permissions: The new chat permissions
    :type permissions: :class:`ChatPermissions`
    """

    ID: typing.Literal["updateChatPermissions"] = "updateChatPermissions"
    chat_id: Int53
    permissions: ChatPermissions


class UpdateChatPhoto(BaseObject):
    """
    A chat photo was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param photo: The new chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    """

    ID: typing.Literal["updateChatPhoto"] = "updateChatPhoto"
    chat_id: Int53
    photo: typing.Optional[ChatPhotoInfo] = None


class UpdateChatPosition(BaseObject):
    """
    The position of a chat in a chat list has changed. An updateChatLastMessage or updateChatDraftMessage update might be sent instead of the update

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param position: New chat position. If new order is 0, then the chat needs to be removed from the list
    :type position: :class:`ChatPosition`
    """

    ID: typing.Literal["updateChatPosition"] = "updateChatPosition"
    chat_id: Int53
    position: ChatPosition


class UpdateChatReadInbox(BaseObject):
    """
    Incoming messages were read or the number of unread messages has been changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :type last_read_inbox_message_id: :class:`Int53`
    :param unread_count: The number of unread messages left in the chat
    :type unread_count: :class:`Int32`
    """

    ID: typing.Literal["updateChatReadInbox"] = "updateChatReadInbox"
    chat_id: Int53
    last_read_inbox_message_id: Int53
    unread_count: Int32


class UpdateChatReadOutbox(BaseObject):
    """
    Outgoing messages were read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param last_read_outbox_message_id: Identifier of last read outgoing message
    :type last_read_outbox_message_id: :class:`Int53`
    """

    ID: typing.Literal["updateChatReadOutbox"] = "updateChatReadOutbox"
    chat_id: Int53
    last_read_outbox_message_id: Int53


class UpdateChatReplyMarkup(BaseObject):
    """
    The default chat reply markup was changed. Can occur because new messages with reply markup were received or because an old reply markup was hidden by the user

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param reply_markup_message_id: Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
    :type reply_markup_message_id: :class:`Int53`
    """

    ID: typing.Literal["updateChatReplyMarkup"] = "updateChatReplyMarkup"
    chat_id: Int53
    reply_markup_message_id: Int53


class UpdateChatTheme(BaseObject):
    """
    The chat theme was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param theme_name: The new name of the chat theme; may be empty if theme was reset to default
    :type theme_name: :class:`String`
    """

    ID: typing.Literal["updateChatTheme"] = "updateChatTheme"
    chat_id: Int53
    theme_name: String = ""


class UpdateChatThemes(BaseObject):
    """
    The list of available chat themes has changed

    :param chat_themes: The new list of chat themes
    :type chat_themes: :class:`Vector[ChatTheme]`
    """

    ID: typing.Literal["updateChatThemes"] = "updateChatThemes"
    chat_themes: Vector[ChatTheme]


class UpdateChatTitle(BaseObject):
    """
    The title of a chat was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param title: The new chat title
    :type title: :class:`String`
    """

    ID: typing.Literal["updateChatTitle"] = "updateChatTitle"
    chat_id: Int53
    title: String


class UpdateChatUnreadMentionCount(BaseObject):
    """
    The chat unread_mention_count has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param unread_mention_count: The number of unread mention messages left in the chat
    :type unread_mention_count: :class:`Int32`
    """

    ID: typing.Literal["updateChatUnreadMentionCount"] = "updateChatUnreadMentionCount"
    chat_id: Int53
    unread_mention_count: Int32


class UpdateChatUnreadReactionCount(BaseObject):
    """
    The chat unread_reaction_count has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param unread_reaction_count: The number of messages with unread reactions left in the chat
    :type unread_reaction_count: :class:`Int32`
    """

    ID: typing.Literal["updateChatUnreadReactionCount"] = "updateChatUnreadReactionCount"
    chat_id: Int53
    unread_reaction_count: Int32


class UpdateChatVideoChat(BaseObject):
    """
    A chat video chat state has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param video_chat: New value of video_chat
    :type video_chat: :class:`VideoChat`
    """

    ID: typing.Literal["updateChatVideoChat"] = "updateChatVideoChat"
    chat_id: Int53
    video_chat: VideoChat


class UpdateConnectionState(BaseObject):
    """
    The connection state has changed. This update must be used only to show a human-readable description of the connection state

    :param state: The new connection state
    :type state: :class:`ConnectionState`
    """

    ID: typing.Literal["updateConnectionState"] = "updateConnectionState"
    state: ConnectionState


class UpdateDefaultReactionType(BaseObject):
    """
    The type of default reaction has changed

    :param reaction_type: The new type of the default reaction
    :type reaction_type: :class:`ReactionType`
    """

    ID: typing.Literal["updateDefaultReactionType"] = "updateDefaultReactionType"
    reaction_type: ReactionType


class UpdateDeleteMessages(BaseObject):
    """
    Some messages were deleted

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_ids: Identifiers of the deleted messages
    :type message_ids: :class:`Vector[Int53]`
    :param is_permanent: True, if the messages are permanently deleted by a user (as opposed to just becoming inaccessible)
    :type is_permanent: :class:`Bool`
    :param from_cache: True, if the messages are deleted only from the cache and can possibly be retrieved again in the future
    :type from_cache: :class:`Bool`
    """

    ID: typing.Literal["updateDeleteMessages"] = "updateDeleteMessages"
    chat_id: Int53
    message_ids: Vector[Int53]
    is_permanent: Bool = False
    from_cache: Bool = False


class UpdateDiceEmojis(BaseObject):
    """
    The list of supported dice emojis has changed

    :param emojis: The new list of supported dice emojis
    :type emojis: :class:`Vector[String]`
    """

    ID: typing.Literal["updateDiceEmojis"] = "updateDiceEmojis"
    emojis: Vector[String]


class UpdateFavoriteStickers(BaseObject):
    """
    The list of favorite stickers was updated

    :param sticker_ids: The new list of file identifiers of favorite stickers
    :type sticker_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["updateFavoriteStickers"] = "updateFavoriteStickers"
    sticker_ids: Vector[Int32]


class UpdateFile(BaseObject):
    """
    Information about a file was updated

    :param file: New data about the file
    :type file: :class:`File`
    """

    ID: typing.Literal["updateFile"] = "updateFile"
    file: File


class UpdateFileAddedToDownloads(BaseObject):
    """
    A file was added to the file download list. This update is sent only after file download list is loaded for the first time

    :param file_download: The added file download
    :type file_download: :class:`FileDownload`
    :param counts: New number of being downloaded and recently downloaded files found
    :type counts: :class:`DownloadedFileCounts`
    """

    ID: typing.Literal["updateFileAddedToDownloads"] = "updateFileAddedToDownloads"
    file_download: FileDownload
    counts: DownloadedFileCounts


class UpdateFileDownload(BaseObject):
    """
    A file download was changed. This update is sent only after file download list is loaded for the first time

    :param file_id: File identifier
    :type file_id: :class:`Int32`
    :param complete_date: Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed
    :type complete_date: :class:`Int32`
    :param counts: New number of being downloaded and recently downloaded files found
    :type counts: :class:`DownloadedFileCounts`
    :param is_paused: True, if downloading of the file is paused
    :type is_paused: :class:`Bool`
    """

    ID: typing.Literal["updateFileDownload"] = "updateFileDownload"
    file_id: Int32
    complete_date: Int32
    counts: DownloadedFileCounts
    is_paused: Bool = False


class UpdateFileDownloads(BaseObject):
    """
    The state of the file download list has changed

    :param total_size: Total size of files in the file download list, in bytes
    :type total_size: :class:`Int53`
    :param total_count: Total number of files in the file download list
    :type total_count: :class:`Int32`
    :param downloaded_size: Total downloaded size of files in the file download list, in bytes
    :type downloaded_size: :class:`Int53`
    """

    ID: typing.Literal["updateFileDownloads"] = "updateFileDownloads"
    total_size: Int53
    total_count: Int32
    downloaded_size: Int53


class UpdateFileGenerationStart(BaseObject):
    """
    The file generation process needs to be started by the application

    :param generation_id: Unique identifier for the generation process
    :type generation_id: :class:`Int64`
    :param destination_path: The path to a file that must be created and where the new file is generated
    :type destination_path: :class:`String`
    :param conversion: String specifying the conversion applied to the original file. If conversion is "#url#" than original_path contains an HTTP/HTTPS URL of a file, which must be downloaded by the application
    :type conversion: :class:`String`
    :param original_path: The path to a file from which a new file is generated; may be empty
    :type original_path: :class:`String`
    """

    ID: typing.Literal["updateFileGenerationStart"] = "updateFileGenerationStart"
    generation_id: Int64
    destination_path: String
    conversion: String
    original_path: String = ""


class UpdateFileGenerationStop(BaseObject):
    """
    File generation is no longer needed

    :param generation_id: Unique identifier for the generation process
    :type generation_id: :class:`Int64`
    """

    ID: typing.Literal["updateFileGenerationStop"] = "updateFileGenerationStop"
    generation_id: Int64


class UpdateFileRemovedFromDownloads(BaseObject):
    """
    A file was removed from the file download list. This update is sent only after file download list is loaded for the first time

    :param file_id: File identifier
    :type file_id: :class:`Int32`
    :param counts: New number of being downloaded and recently downloaded files found
    :type counts: :class:`DownloadedFileCounts`
    """

    ID: typing.Literal["updateFileRemovedFromDownloads"] = "updateFileRemovedFromDownloads"
    file_id: Int32
    counts: DownloadedFileCounts


class UpdateForumTopicInfo(BaseObject):
    """
    Basic information about a topic in a forum chat was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param info: New information about the topic
    :type info: :class:`ForumTopicInfo`
    """

    ID: typing.Literal["updateForumTopicInfo"] = "updateForumTopicInfo"
    chat_id: Int53
    info: ForumTopicInfo


class UpdateGroupCall(BaseObject):
    """
    Information about a group call was updated

    :param group_call: New data about a group call
    :type group_call: :class:`GroupCall`
    """

    ID: typing.Literal["updateGroupCall"] = "updateGroupCall"
    group_call: GroupCall


class UpdateGroupCallParticipant(BaseObject):
    """
    Information about a group call participant was changed. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined

    :param group_call_id: Identifier of group call
    :type group_call_id: :class:`Int32`
    :param participant: New data about a participant
    :type participant: :class:`GroupCallParticipant`
    """

    ID: typing.Literal["updateGroupCallParticipant"] = "updateGroupCallParticipant"
    group_call_id: Int32
    participant: GroupCallParticipant


class UpdateHavePendingNotifications(BaseObject):
    """
    Describes whether there are some pending notification updates. Can be used to prevent application from killing, while there are some pending notifications

    :param have_delayed_notifications: True, if there are some delayed notification updates, which will be sent soon
    :type have_delayed_notifications: :class:`Bool`
    :param have_unreceived_notifications: True, if there can be some yet unreceived notifications, which are being fetched from the server
    :type have_unreceived_notifications: :class:`Bool`
    """

    ID: typing.Literal["updateHavePendingNotifications"] = "updateHavePendingNotifications"
    have_delayed_notifications: Bool = False
    have_unreceived_notifications: Bool = False


class UpdateInstalledStickerSets(BaseObject):
    """
    The list of installed sticker sets was updated

    :param sticker_type: Type of the affected stickers
    :type sticker_type: :class:`StickerType`
    :param sticker_set_ids: The new list of installed ordinary sticker sets
    :type sticker_set_ids: :class:`Vector[Int64]`
    """

    ID: typing.Literal["updateInstalledStickerSets"] = "updateInstalledStickerSets"
    sticker_type: StickerType
    sticker_set_ids: Vector[Int64]


class UpdateLanguagePackStrings(BaseObject):
    """
    Some language pack strings have been updated

    :param localization_target: Localization target to which the language pack belongs
    :type localization_target: :class:`String`
    :param language_pack_id: Identifier of the updated language pack
    :type language_pack_id: :class:`String`
    :param strings: List of changed language pack strings; empty if all strings have changed
    :type strings: :class:`Vector[LanguagePackString]`
    """

    ID: typing.Literal["updateLanguagePackStrings"] = "updateLanguagePackStrings"
    localization_target: String
    language_pack_id: String
    strings: Vector[LanguagePackString]


class UpdateMessageContent(BaseObject):
    """
    The message content has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param new_content: New message content
    :type new_content: :class:`MessageContent`
    """

    ID: typing.Literal["updateMessageContent"] = "updateMessageContent"
    chat_id: Int53
    message_id: Int53
    new_content: MessageContent


class UpdateMessageContentOpened(BaseObject):
    """
    The message content was opened. Updates voice note messages to "listened", video note messages to "viewed" and starts the self-destruct timer

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["updateMessageContentOpened"] = "updateMessageContentOpened"
    chat_id: Int53
    message_id: Int53


class UpdateMessageEdited(BaseObject):
    """
    A message was edited. Changes in the message content will come in a separate updateMessageContent

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param edit_date: Point in time (Unix timestamp) when the message was edited
    :type edit_date: :class:`Int32`
    :param reply_markup: New message reply markup; may be null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["updateMessageEdited"] = "updateMessageEdited"
    chat_id: Int53
    message_id: Int53
    edit_date: Int32
    reply_markup: typing.Optional[ReplyMarkup] = None


class UpdateMessageInteractionInfo(BaseObject):
    """
    The information about interactions with a message has changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param interaction_info: New information about interactions with the message; may be null, defaults to None
    :type interaction_info: :class:`MessageInteractionInfo`, optional
    """

    ID: typing.Literal["updateMessageInteractionInfo"] = "updateMessageInteractionInfo"
    chat_id: Int53
    message_id: Int53
    interaction_info: typing.Optional[MessageInteractionInfo] = None


class UpdateMessageIsPinned(BaseObject):
    """
    The message pinned state was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: The message identifier
    :type message_id: :class:`Int53`
    :param is_pinned: True, if the message is pinned
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["updateMessageIsPinned"] = "updateMessageIsPinned"
    chat_id: Int53
    message_id: Int53
    is_pinned: Bool = False


class UpdateMessageLiveLocationViewed(BaseObject):
    """
    A message with a live location was viewed. When the update is received, the application is supposed to update the live location

    :param chat_id: Identifier of the chat with the live location message
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message with live location
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["updateMessageLiveLocationViewed"] = "updateMessageLiveLocationViewed"
    chat_id: Int53
    message_id: Int53


class UpdateMessageMentionRead(BaseObject):
    """
    A message with an unread mention was read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param unread_mention_count: The new number of unread mention messages left in the chat
    :type unread_mention_count: :class:`Int32`
    """

    ID: typing.Literal["updateMessageMentionRead"] = "updateMessageMentionRead"
    chat_id: Int53
    message_id: Int53
    unread_mention_count: Int32


class UpdateMessageSendAcknowledged(BaseObject):
    """
    A request to send a message has reached the Telegram server. This doesn't mean that the message will be sent successfully or even that the send message request will be processed. This update will be sent only if the option "use_quick_ack" is set to true. This update may be sent multiple times for the same message

    :param chat_id: The chat identifier of the sent message
    :type chat_id: :class:`Int53`
    :param message_id: A temporary message identifier
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["updateMessageSendAcknowledged"] = "updateMessageSendAcknowledged"
    chat_id: Int53
    message_id: Int53


class UpdateMessageSendFailed(BaseObject):
    """
    A message failed to send. Be aware that some messages being sent can be irrecoverably deleted, in which case updateDeleteMessages will be received instead of this update

    :param message: The failed to send message
    :type message: :class:`Message`
    :param old_message_id: The previous temporary message identifier
    :type old_message_id: :class:`Int53`
    :param error_code: An error code
    :type error_code: :class:`Int32`
    :param error_message: Error message
    :type error_message: :class:`String`
    """

    ID: typing.Literal["updateMessageSendFailed"] = "updateMessageSendFailed"
    message: Message
    old_message_id: Int53
    error_code: Int32
    error_message: String


class UpdateMessageSendSucceeded(BaseObject):
    """
    A message has been successfully sent

    :param message: The sent message. Usually only the message identifier, date, and content are changed, but almost all other fields can also change
    :type message: :class:`Message`
    :param old_message_id: The previous temporary message identifier
    :type old_message_id: :class:`Int53`
    """

    ID: typing.Literal["updateMessageSendSucceeded"] = "updateMessageSendSucceeded"
    message: Message
    old_message_id: Int53


class UpdateMessageUnreadReactions(BaseObject):
    """
    The list of unread reactions added to a message was changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param unread_reactions: The new list of unread reactions
    :type unread_reactions: :class:`Vector[UnreadReaction]`
    :param unread_reaction_count: The new number of messages with unread reactions left in the chat
    :type unread_reaction_count: :class:`Int32`
    """

    ID: typing.Literal["updateMessageUnreadReactions"] = "updateMessageUnreadReactions"
    chat_id: Int53
    message_id: Int53
    unread_reactions: Vector[UnreadReaction]
    unread_reaction_count: Int32


class UpdateNewCallSignalingData(BaseObject):
    """
    New call signaling data arrived

    :param call_id: The call identifier
    :type call_id: :class:`Int32`
    :param data: The data
    :type data: :class:`Bytes`
    """

    ID: typing.Literal["updateNewCallSignalingData"] = "updateNewCallSignalingData"
    call_id: Int32
    data: Bytes


class UpdateNewCallbackQuery(BaseObject):
    """
    A new incoming callback query; for bots only

    :param id: Unique query identifier
    :type id: :class:`Int64`
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`Int53`
    :param chat_id: Identifier of the chat where the query was sent
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message from which the query originated
    :type message_id: :class:`Int53`
    :param chat_instance: Identifier that uniquely corresponds to the chat to which the message was sent
    :type chat_instance: :class:`Int64`
    :param payload: Query payload
    :type payload: :class:`CallbackQueryPayload`
    """

    ID: typing.Literal["updateNewCallbackQuery"] = "updateNewCallbackQuery"
    id: Int64
    sender_user_id: Int53
    chat_id: Int53
    message_id: Int53
    chat_instance: Int64
    payload: CallbackQueryPayload


class UpdateNewChat(BaseObject):
    """
    A new chat has been loaded/created. This update is guaranteed to come before the chat identifier is returned to the application. The chat field changes will be reported through separate updates

    :param chat: The chat
    :type chat: :class:`Chat`
    """

    ID: typing.Literal["updateNewChat"] = "updateNewChat"
    chat: Chat


class UpdateNewChatJoinRequest(BaseObject):
    """
    A user sent a join request to a chat; for bots only

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param request: Join request
    :type request: :class:`ChatJoinRequest`
    :param user_chat_id: Chat identifier of the private chat with the user
    :type user_chat_id: :class:`Int53`
    :param invite_link: The invite link, which was used to send join request; may be null, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    """

    ID: typing.Literal["updateNewChatJoinRequest"] = "updateNewChatJoinRequest"
    chat_id: Int53
    request: ChatJoinRequest
    user_chat_id: Int53
    invite_link: typing.Optional[ChatInviteLink] = None


class UpdateNewChosenInlineResult(BaseObject):
    """
    The user has chosen a result of an inline query; for bots only

    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`Int53`
    :param query: Text of the query
    :type query: :class:`String`
    :param result_id: Identifier of the chosen result
    :type result_id: :class:`String`
    :param inline_message_id: Identifier of the sent inline message, if known
    :type inline_message_id: :class:`String`
    :param user_location: User location; may be null, defaults to None
    :type user_location: :class:`Location`, optional
    """

    ID: typing.Literal["updateNewChosenInlineResult"] = "updateNewChosenInlineResult"
    sender_user_id: Int53
    query: String
    result_id: String
    inline_message_id: String
    user_location: typing.Optional[Location] = None


class UpdateNewCustomEvent(BaseObject):
    """
    A new incoming event; for bots only

    :param event: A JSON-serialized event
    :type event: :class:`String`
    """

    ID: typing.Literal["updateNewCustomEvent"] = "updateNewCustomEvent"
    event: String


class UpdateNewCustomQuery(BaseObject):
    """
    A new incoming query; for bots only

    :param id: The query identifier
    :type id: :class:`Int64`
    :param data: JSON-serialized query data
    :type data: :class:`String`
    :param timeout: Query timeout
    :type timeout: :class:`Int32`
    """

    ID: typing.Literal["updateNewCustomQuery"] = "updateNewCustomQuery"
    id: Int64
    data: String
    timeout: Int32


class UpdateNewInlineCallbackQuery(BaseObject):
    """
    A new incoming callback query from a message sent via a bot; for bots only

    :param id: Unique query identifier
    :type id: :class:`Int64`
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`Int53`
    :param inline_message_id: Identifier of the inline message from which the query originated
    :type inline_message_id: :class:`String`
    :param chat_instance: An identifier uniquely corresponding to the chat a message was sent to
    :type chat_instance: :class:`Int64`
    :param payload: Query payload
    :type payload: :class:`CallbackQueryPayload`
    """

    ID: typing.Literal["updateNewInlineCallbackQuery"] = "updateNewInlineCallbackQuery"
    id: Int64
    sender_user_id: Int53
    inline_message_id: String
    chat_instance: Int64
    payload: CallbackQueryPayload


class UpdateNewInlineQuery(BaseObject):
    """
    A new incoming inline query; for bots only

    :param id: Unique query identifier
    :type id: :class:`Int64`
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`Int53`
    :param query: Text of the query
    :type query: :class:`String`
    :param offset: Offset of the first entry to return
    :type offset: :class:`String`
    :param user_location: User location; may be null, defaults to None
    :type user_location: :class:`Location`, optional
    :param chat_type: The type of the chat from which the query originated; may be null if unknown, defaults to None
    :type chat_type: :class:`ChatType`, optional
    """

    ID: typing.Literal["updateNewInlineQuery"] = "updateNewInlineQuery"
    id: Int64
    sender_user_id: Int53
    query: String
    offset: String
    user_location: typing.Optional[Location] = None
    chat_type: typing.Optional[ChatType] = None


class UpdateNewMessage(BaseObject):
    """
    A new message was received; can also be an outgoing message

    :param message: The new message
    :type message: :class:`Message`
    """

    ID: typing.Literal["updateNewMessage"] = "updateNewMessage"
    message: Message


class UpdateNewPreCheckoutQuery(BaseObject):
    """
    A new incoming pre-checkout query; for bots only. Contains full information about a checkout

    :param id: Unique query identifier
    :type id: :class:`Int64`
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`Int53`
    :param currency: Currency for the product price
    :type currency: :class:`String`
    :param total_amount: Total price for the product, in the smallest units of the currency
    :type total_amount: :class:`Int53`
    :param invoice_payload: Invoice payload
    :type invoice_payload: :class:`Bytes`
    :param order_info: Information about the order; may be null, defaults to None
    :type order_info: :class:`OrderInfo`, optional
    :param shipping_option_id: Identifier of a shipping option chosen by the user; may be empty if not applicable
    :type shipping_option_id: :class:`String`
    """

    ID: typing.Literal["updateNewPreCheckoutQuery"] = "updateNewPreCheckoutQuery"
    id: Int64
    sender_user_id: Int53
    currency: String
    total_amount: Int53
    invoice_payload: Bytes
    order_info: typing.Optional[OrderInfo] = None
    shipping_option_id: String = ""


class UpdateNewShippingQuery(BaseObject):
    """
    A new incoming shipping query; for bots only. Only for invoices with flexible price

    :param id: Unique query identifier
    :type id: :class:`Int64`
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`Int53`
    :param invoice_payload: Invoice payload
    :type invoice_payload: :class:`String`
    :param shipping_address: User shipping address
    :type shipping_address: :class:`Address`
    """

    ID: typing.Literal["updateNewShippingQuery"] = "updateNewShippingQuery"
    id: Int64
    sender_user_id: Int53
    invoice_payload: String
    shipping_address: Address


class UpdateNotification(BaseObject):
    """
    A notification was changed

    :param notification_group_id: Unique notification group identifier
    :type notification_group_id: :class:`Int32`
    :param notification: Changed notification
    :type notification: :class:`Notification`
    """

    ID: typing.Literal["updateNotification"] = "updateNotification"
    notification_group_id: Int32
    notification: Notification


class UpdateNotificationGroup(BaseObject):
    """
    A list of active notifications in a notification group has changed

    :param notification_group_id: Unique notification group identifier
    :type notification_group_id: :class:`Int32`
    :param type_: New type of the notification group
    :type type_: :class:`NotificationGroupType`
    :param chat_id: Identifier of a chat to which all notifications in the group belong
    :type chat_id: :class:`Int53`
    :param notification_settings_chat_id: Chat identifier, which notification settings must be applied to the added notifications
    :type notification_settings_chat_id: :class:`Int53`
    :param notification_sound_id: Identifier of the notification sound to be played; 0 if sound is disabled
    :type notification_sound_id: :class:`Int64`
    :param total_count: Total number of unread notifications in the group, can be bigger than number of active notifications
    :type total_count: :class:`Int32`
    :param added_notifications: List of added group notifications, sorted by notification identifier
    :type added_notifications: :class:`Vector[Notification]`
    :param removed_notification_ids: Identifiers of removed group notifications, sorted by notification identifier
    :type removed_notification_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["updateNotificationGroup"] = "updateNotificationGroup"
    notification_group_id: Int32
    type_: NotificationGroupType = Field(..., alias="type")
    chat_id: Int53
    notification_settings_chat_id: Int53
    notification_sound_id: Int64
    total_count: Int32
    added_notifications: Vector[Notification]
    removed_notification_ids: Vector[Int32]


class UpdateOption(BaseObject):
    """
    An option changed its value

    :param name: The option name
    :type name: :class:`String`
    :param value: The new option value
    :type value: :class:`OptionValue`
    """

    ID: typing.Literal["updateOption"] = "updateOption"
    name: String
    value: OptionValue


class UpdatePoll(BaseObject):
    """
    A poll was updated; for bots only

    :param poll: New data about the poll
    :type poll: :class:`Poll`
    """

    ID: typing.Literal["updatePoll"] = "updatePoll"
    poll: Poll


class UpdatePollAnswer(BaseObject):
    """
    A user changed the answer to a poll; for bots only

    :param poll_id: Unique poll identifier
    :type poll_id: :class:`Int64`
    :param voter_id: Identifier of the message sender that changed the answer to the poll
    :type voter_id: :class:`MessageSender`
    :param option_ids: 0-based identifiers of answer options, chosen by the user
    :type option_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["updatePollAnswer"] = "updatePollAnswer"
    poll_id: Int64
    voter_id: MessageSender
    option_ids: Vector[Int32]


class UpdateRecentStickers(BaseObject):
    """
    The list of recently used stickers was updated

    :param sticker_ids: The new list of file identifiers of recently used stickers
    :type sticker_ids: :class:`Vector[Int32]`
    :param is_attached: True, if the list of stickers attached to photo or video files was updated; otherwise, the list of sent stickers is updated
    :type is_attached: :class:`Bool`
    """

    ID: typing.Literal["updateRecentStickers"] = "updateRecentStickers"
    sticker_ids: Vector[Int32]
    is_attached: Bool = False


class UpdateSavedAnimations(BaseObject):
    """
    The list of saved animations was updated

    :param animation_ids: The new list of file identifiers of saved animations
    :type animation_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["updateSavedAnimations"] = "updateSavedAnimations"
    animation_ids: Vector[Int32]


class UpdateSavedNotificationSounds(BaseObject):
    """
    The list of saved notifications sounds was updated. This update may not be sent until information about a notification sound was requested for the first time

    :param notification_sound_ids: The new list of identifiers of saved notification sounds
    :type notification_sound_ids: :class:`Vector[Int64]`
    """

    ID: typing.Literal["updateSavedNotificationSounds"] = "updateSavedNotificationSounds"
    notification_sound_ids: Vector[Int64]


class UpdateScopeNotificationSettings(BaseObject):
    """
    Notification settings for some type of chats were updated

    :param scope: Types of chats for which notification settings were updated
    :type scope: :class:`NotificationSettingsScope`
    :param notification_settings: The new notification settings
    :type notification_settings: :class:`ScopeNotificationSettings`
    """

    ID: typing.Literal["updateScopeNotificationSettings"] = "updateScopeNotificationSettings"
    scope: NotificationSettingsScope
    notification_settings: ScopeNotificationSettings


class UpdateSecretChat(BaseObject):
    """
    Some data of a secret chat has changed. This update is guaranteed to come before the secret chat identifier is returned to the application

    :param secret_chat: New data about the secret chat
    :type secret_chat: :class:`SecretChat`
    """

    ID: typing.Literal["updateSecretChat"] = "updateSecretChat"
    secret_chat: SecretChat


class UpdateSelectedBackground(BaseObject):
    """
    The selected background has changed

    :param background: The new selected background; may be null, defaults to None
    :type background: :class:`Background`, optional
    :param for_dark_theme: True, if background for dark theme has changed
    :type for_dark_theme: :class:`Bool`
    """

    ID: typing.Literal["updateSelectedBackground"] = "updateSelectedBackground"
    background: typing.Optional[Background] = None
    for_dark_theme: Bool = False


class UpdateServiceNotification(BaseObject):
    """
    A service notification from the server was received. Upon receiving this the application must show a popup with the content of the notification

    :param type_: Notification type. If type begins with "AUTH_KEY_DROP_", then two buttons "Cancel" and "Log out" must be shown under notification; if user presses the second, all local data must be destroyed using Destroy method
    :type type_: :class:`String`
    :param content: Notification content
    :type content: :class:`MessageContent`
    """

    ID: typing.Literal["updateServiceNotification"] = "updateServiceNotification"
    type_: String = Field(..., alias="type")
    content: MessageContent


class UpdateStickerSet(BaseObject):
    """
    A sticker set has changed

    :param sticker_set: The sticker set
    :type sticker_set: :class:`StickerSet`
    """

    ID: typing.Literal["updateStickerSet"] = "updateStickerSet"
    sticker_set: StickerSet


class UpdateStory(BaseObject):
    """
    A story was changed

    :param story: The new information about the story
    :type story: :class:`Story`
    """

    ID: typing.Literal["updateStory"] = "updateStory"
    story: Story


class UpdateStoryDeleted(BaseObject):
    """
    A story became inaccessible

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["updateStoryDeleted"] = "updateStoryDeleted"
    story_sender_chat_id: Int53
    story_id: Int32


class UpdateStoryListChatCount(BaseObject):
    """
    Number of chats in a story list has changed

    :param story_list: The story list
    :type story_list: :class:`StoryList`
    :param chat_count: Approximate total number of chats with active stories in the list
    :type chat_count: :class:`Int32`
    """

    ID: typing.Literal["updateStoryListChatCount"] = "updateStoryListChatCount"
    story_list: StoryList
    chat_count: Int32


class UpdateStorySendFailed(BaseObject):
    """
    A story failed to send. If the story sending is canceled, then updateStoryDeleted will be received instead of this update

    :param story: The failed to send story
    :type story: :class:`Story`
    :param error_code: An error code
    :type error_code: :class:`Int32`
    :param error_message: Error message
    :type error_message: :class:`String`
    :param error: The cause of the failure; may be null if unknown, defaults to None
    :type error: :class:`CanSendStoryResult`, optional
    """

    ID: typing.Literal["updateStorySendFailed"] = "updateStorySendFailed"
    story: Story
    error_code: Int32
    error_message: String
    error: typing.Optional[CanSendStoryResult] = None


class UpdateStorySendSucceeded(BaseObject):
    """
    A story has been successfully sent

    :param story: The sent story
    :type story: :class:`Story`
    :param old_story_id: The previous temporary story identifier
    :type old_story_id: :class:`Int32`
    """

    ID: typing.Literal["updateStorySendSucceeded"] = "updateStorySendSucceeded"
    story: Story
    old_story_id: Int32


class UpdateStoryStealthMode(BaseObject):
    """
    Story stealth mode settings have changed

    :param active_until_date: Point in time (Unix timestamp) until stealth mode is active; 0 if it is disabled
    :type active_until_date: :class:`Int32`
    :param cooldown_until_date: Point in time (Unix timestamp) when stealth mode can be enabled again; 0 if there is no active cooldown
    :type cooldown_until_date: :class:`Int32`
    """

    ID: typing.Literal["updateStoryStealthMode"] = "updateStoryStealthMode"
    active_until_date: Int32
    cooldown_until_date: Int32


class UpdateSuggestedActions(BaseObject):
    """
    The list of suggested to the user actions has changed

    :param added_actions: Added suggested actions
    :type added_actions: :class:`Vector[SuggestedAction]`
    :param removed_actions: Removed suggested actions
    :type removed_actions: :class:`Vector[SuggestedAction]`
    """

    ID: typing.Literal["updateSuggestedActions"] = "updateSuggestedActions"
    added_actions: Vector[SuggestedAction]
    removed_actions: Vector[SuggestedAction]


class UpdateSupergroup(BaseObject):
    """
    Some data of a supergroup or a channel has changed. This update is guaranteed to come before the supergroup identifier is returned to the application

    :param supergroup: New data about the supergroup
    :type supergroup: :class:`Supergroup`
    """

    ID: typing.Literal["updateSupergroup"] = "updateSupergroup"
    supergroup: Supergroup


class UpdateSupergroupFullInfo(BaseObject):
    """
    Some data in supergroupFullInfo has been changed

    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`Int53`
    :param supergroup_full_info: New full information about the supergroup
    :type supergroup_full_info: :class:`SupergroupFullInfo`
    """

    ID: typing.Literal["updateSupergroupFullInfo"] = "updateSupergroupFullInfo"
    supergroup_id: Int53
    supergroup_full_info: SupergroupFullInfo


class UpdateTermsOfService(BaseObject):
    """
    New terms of service must be accepted by the user. If the terms of service are declined, then the deleteAccount method must be called with the reason "Decline ToS update"

    :param terms_of_service_id: Identifier of the terms of service
    :type terms_of_service_id: :class:`String`
    :param terms_of_service: The new terms of service
    :type terms_of_service: :class:`TermsOfService`
    """

    ID: typing.Literal["updateTermsOfService"] = "updateTermsOfService"
    terms_of_service_id: String
    terms_of_service: TermsOfService


class UpdateTrendingStickerSets(BaseObject):
    """
    The list of trending sticker sets was updated or some of them were viewed

    :param sticker_type: Type of the affected stickers
    :type sticker_type: :class:`StickerType`
    :param sticker_sets: The prefix of the list of trending sticker sets with the newest trending sticker sets
    :type sticker_sets: :class:`TrendingStickerSets`
    """

    ID: typing.Literal["updateTrendingStickerSets"] = "updateTrendingStickerSets"
    sticker_type: StickerType
    sticker_sets: TrendingStickerSets


class UpdateUnconfirmedSession(BaseObject):
    """
    The first unconfirmed session has changed

    :param session: The unconfirmed session; may be null if none, defaults to None
    :type session: :class:`UnconfirmedSession`, optional
    """

    ID: typing.Literal["updateUnconfirmedSession"] = "updateUnconfirmedSession"
    session: typing.Optional[UnconfirmedSession] = None


class UpdateUnreadChatCount(BaseObject):
    """
    Number of unread chats, i.e. with unread messages or marked as unread, has changed. This update is sent only if the message database is used

    :param chat_list: The chat list with changed number of unread messages
    :type chat_list: :class:`ChatList`
    :param total_count: Approximate total number of chats in the chat list
    :type total_count: :class:`Int32`
    :param unread_count: Total number of unread chats
    :type unread_count: :class:`Int32`
    :param unread_unmuted_count: Total number of unread unmuted chats
    :type unread_unmuted_count: :class:`Int32`
    :param marked_as_unread_count: Total number of chats marked as unread
    :type marked_as_unread_count: :class:`Int32`
    :param marked_as_unread_unmuted_count: Total number of unmuted chats marked as unread
    :type marked_as_unread_unmuted_count: :class:`Int32`
    """

    ID: typing.Literal["updateUnreadChatCount"] = "updateUnreadChatCount"
    chat_list: ChatList
    total_count: Int32
    unread_count: Int32
    unread_unmuted_count: Int32
    marked_as_unread_count: Int32
    marked_as_unread_unmuted_count: Int32


class UpdateUnreadMessageCount(BaseObject):
    """
    Number of unread messages in a chat list has changed. This update is sent only if the message database is used

    :param chat_list: The chat list with changed number of unread messages
    :type chat_list: :class:`ChatList`
    :param unread_count: Total number of unread messages
    :type unread_count: :class:`Int32`
    :param unread_unmuted_count: Total number of unread messages in unmuted chats
    :type unread_unmuted_count: :class:`Int32`
    """

    ID: typing.Literal["updateUnreadMessageCount"] = "updateUnreadMessageCount"
    chat_list: ChatList
    unread_count: Int32
    unread_unmuted_count: Int32


class UpdateUser(BaseObject):
    """
    Some data of a user has changed. This update is guaranteed to come before the user identifier is returned to the application

    :param user: New data about the user
    :type user: :class:`User`
    """

    ID: typing.Literal["updateUser"] = "updateUser"
    user: User


class UpdateUserFullInfo(BaseObject):
    """
    Some data in userFullInfo has been changed

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param user_full_info: New full information about the user
    :type user_full_info: :class:`UserFullInfo`
    """

    ID: typing.Literal["updateUserFullInfo"] = "updateUserFullInfo"
    user_id: Int53
    user_full_info: UserFullInfo


class UpdateUserPrivacySettingRules(BaseObject):
    """
    Some privacy setting rules have been changed

    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    :param rules: New privacy rules
    :type rules: :class:`UserPrivacySettingRules`
    """

    ID: typing.Literal["updateUserPrivacySettingRules"] = "updateUserPrivacySettingRules"
    setting: UserPrivacySetting
    rules: UserPrivacySettingRules


class UpdateUserStatus(BaseObject):
    """
    The user went online or offline

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param status: New status of the user
    :type status: :class:`UserStatus`
    """

    ID: typing.Literal["updateUserStatus"] = "updateUserStatus"
    user_id: Int53
    status: UserStatus


class UpdateUsersNearby(BaseObject):
    """
    The list of users nearby has changed. The update is guaranteed to be sent only 60 seconds after a successful searchChatsNearby request

    :param users_nearby: The new list of users nearby
    :type users_nearby: :class:`Vector[ChatNearby]`
    """

    ID: typing.Literal["updateUsersNearby"] = "updateUsersNearby"
    users_nearby: Vector[ChatNearby]


class UpdateWebAppMessageSent(BaseObject):
    """
    A message was sent by an opened Web App, so the Web App needs to be closed

    :param web_app_launch_id: Identifier of Web App launch
    :type web_app_launch_id: :class:`Int64`
    """

    ID: typing.Literal["updateWebAppMessageSent"] = "updateWebAppMessageSent"
    web_app_launch_id: Int64


Update = typing.Union[
    UpdateActiveEmojiReactions,
    UpdateActiveNotifications,
    UpdateAddChatMembersPrivacyForbidden,
    UpdateAnimatedEmojiMessageClicked,
    UpdateAnimationSearchParameters,
    UpdateAttachmentMenuBots,
    UpdateAuthorizationState,
    UpdateAutosaveSettings,
    UpdateBasicGroup,
    UpdateBasicGroupFullInfo,
    UpdateCall,
    UpdateChatAction,
    UpdateChatActionBar,
    UpdateChatActiveStories,
    UpdateChatAvailableReactions,
    UpdateChatBackground,
    UpdateChatBlockList,
    UpdateChatDefaultDisableNotification,
    UpdateChatDraftMessage,
    UpdateChatFolders,
    UpdateChatHasProtectedContent,
    UpdateChatHasScheduledMessages,
    UpdateChatIsMarkedAsUnread,
    UpdateChatIsTranslatable,
    UpdateChatLastMessage,
    UpdateChatMember,
    UpdateChatMessageAutoDeleteTime,
    UpdateChatMessageSender,
    UpdateChatNotificationSettings,
    UpdateChatOnlineMemberCount,
    UpdateChatPendingJoinRequests,
    UpdateChatPermissions,
    UpdateChatPhoto,
    UpdateChatPosition,
    UpdateChatReadInbox,
    UpdateChatReadOutbox,
    UpdateChatReplyMarkup,
    UpdateChatTheme,
    UpdateChatThemes,
    UpdateChatTitle,
    UpdateChatUnreadMentionCount,
    UpdateChatUnreadReactionCount,
    UpdateChatVideoChat,
    UpdateConnectionState,
    UpdateDefaultReactionType,
    UpdateDeleteMessages,
    UpdateDiceEmojis,
    UpdateFavoriteStickers,
    UpdateFile,
    UpdateFileAddedToDownloads,
    UpdateFileDownload,
    UpdateFileDownloads,
    UpdateFileGenerationStart,
    UpdateFileGenerationStop,
    UpdateFileRemovedFromDownloads,
    UpdateForumTopicInfo,
    UpdateGroupCall,
    UpdateGroupCallParticipant,
    UpdateHavePendingNotifications,
    UpdateInstalledStickerSets,
    UpdateLanguagePackStrings,
    UpdateMessageContent,
    UpdateMessageContentOpened,
    UpdateMessageEdited,
    UpdateMessageInteractionInfo,
    UpdateMessageIsPinned,
    UpdateMessageLiveLocationViewed,
    UpdateMessageMentionRead,
    UpdateMessageSendAcknowledged,
    UpdateMessageSendFailed,
    UpdateMessageSendSucceeded,
    UpdateMessageUnreadReactions,
    UpdateNewCallSignalingData,
    UpdateNewCallbackQuery,
    UpdateNewChat,
    UpdateNewChatJoinRequest,
    UpdateNewChosenInlineResult,
    UpdateNewCustomEvent,
    UpdateNewCustomQuery,
    UpdateNewInlineCallbackQuery,
    UpdateNewInlineQuery,
    UpdateNewMessage,
    UpdateNewPreCheckoutQuery,
    UpdateNewShippingQuery,
    UpdateNotification,
    UpdateNotificationGroup,
    UpdateOption,
    UpdatePoll,
    UpdatePollAnswer,
    UpdateRecentStickers,
    UpdateSavedAnimations,
    UpdateSavedNotificationSounds,
    UpdateScopeNotificationSettings,
    UpdateSecretChat,
    UpdateSelectedBackground,
    UpdateServiceNotification,
    UpdateStickerSet,
    UpdateStory,
    UpdateStoryDeleted,
    UpdateStoryListChatCount,
    UpdateStorySendFailed,
    UpdateStorySendSucceeded,
    UpdateStoryStealthMode,
    UpdateSuggestedActions,
    UpdateSupergroup,
    UpdateSupergroupFullInfo,
    UpdateTermsOfService,
    UpdateTrendingStickerSets,
    UpdateUnconfirmedSession,
    UpdateUnreadChatCount,
    UpdateUnreadMessageCount,
    UpdateUser,
    UpdateUserFullInfo,
    UpdateUserPrivacySettingRules,
    UpdateUserStatus,
    UpdateUsersNearby,
    UpdateWebAppMessageSent,
]


class Updates(BaseObject):
    """
    Contains a list of updates

    :param updates: List of updates
    :type updates: :class:`Vector[Update]`
    """

    ID: typing.Literal["updates"] = "updates"
    updates: Vector[Update]


class User(BaseObject):
    """
    Represents a user

    :param id: User identifier
    :type id: :class:`Int53`
    :param first_name: First name of the user
    :type first_name: :class:`String`
    :param last_name: Last name of the user
    :type last_name: :class:`String`
    :param phone_number: Phone number of the user
    :type phone_number: :class:`String`
    :param status: Current online status of the user
    :type status: :class:`UserStatus`
    :param is_contact: The user is a contact of the current user
    :type is_contact: :class:`Bool`
    :param is_mutual_contact: The user is a contact of the current user and the current user is a contact of the user
    :type is_mutual_contact: :class:`Bool`
    :param is_close_friend: The user is a close friend of the current user; implies that the user is a contact
    :type is_close_friend: :class:`Bool`
    :param restriction_reason: If non-empty, it contains a human-readable description of the reason why access to this user must be restricted
    :type restriction_reason: :class:`String`
    :param have_access: If false, the user is inaccessible, and the only information known about the user is inside this class. Identifier of the user can't be passed to any method
    :type have_access: :class:`Bool`
    :param type_: Type of the user
    :type type_: :class:`UserType`
    :param language_code: IETF language tag of the user's language; only available to bots
    :type language_code: :class:`String`
    :param usernames: Usernames of the user; may be null, defaults to None
    :type usernames: :class:`Usernames`, optional
    :param profile_photo: Profile photo of the user; may be null, defaults to None
    :type profile_photo: :class:`ProfilePhoto`, optional
    :param emoji_status: Emoji status to be shown instead of the default Telegram Premium badge; may be null. For Telegram Premium users only, defaults to None
    :type emoji_status: :class:`EmojiStatus`, optional
    :param is_verified: True, if the user is verified
    :type is_verified: :class:`Bool`
    :param is_premium: True, if the user is a Telegram Premium user
    :type is_premium: :class:`Bool`
    :param is_support: True, if the user is Telegram support account
    :type is_support: :class:`Bool`
    :param is_scam: True, if many users reported this user as a scam
    :type is_scam: :class:`Bool`
    :param is_fake: True, if many users reported this user as a fake account
    :type is_fake: :class:`Bool`
    :param has_active_stories: True, if the user has non-expired stories available to the current user
    :type has_active_stories: :class:`Bool`
    :param has_unread_active_stories: True, if the user has unread non-expired stories available to the current user
    :type has_unread_active_stories: :class:`Bool`
    :param added_to_attachment_menu: True, if the user added the current bot to attachment menu; only available to bots
    :type added_to_attachment_menu: :class:`Bool`
    """

    ID: typing.Literal["user"] = "user"
    id: Int53
    first_name: String
    last_name: String
    phone_number: String
    status: UserStatus
    is_contact: Bool
    is_mutual_contact: Bool
    is_close_friend: Bool
    restriction_reason: String
    have_access: Bool
    type_: UserType = Field(..., alias="type")
    language_code: String
    usernames: typing.Optional[Usernames] = None
    profile_photo: typing.Optional[ProfilePhoto] = None
    emoji_status: typing.Optional[EmojiStatus] = None
    is_verified: Bool = False
    is_premium: Bool = False
    is_support: Bool = False
    is_scam: Bool = False
    is_fake: Bool = False
    has_active_stories: Bool = False
    has_unread_active_stories: Bool = False
    added_to_attachment_menu: Bool = False


class UserFullInfo(BaseObject):
    """
    Contains full information about a user

    :param premium_gift_options: The list of available options for gifting Telegram Premium to the user
    :type premium_gift_options: :class:`Vector[PremiumPaymentOption]`
    :param group_in_common_count: Number of group chats where both the other user and the current user are a member; 0 for the current user
    :type group_in_common_count: :class:`Int32`
    :param personal_photo: User profile photo set by the current user for the contact; may be null. If null and user.profile_photo is null, then the photo is empty; otherwise, it is unknown. If non-null, then it is the same photo as in user.profile_photo and chat.photo. This photo isn't returned in the list of user photos, defaults to None
    :type personal_photo: :class:`ChatPhoto`, optional
    :param photo: User profile photo; may be null. If null and user.profile_photo is null, then the photo is empty; otherwise, it is unknown. If non-null and personal_photo is null, then it is the same photo as in user.profile_photo and chat.photo, defaults to None
    :type photo: :class:`ChatPhoto`, optional
    :param public_photo: User profile photo visible if the main photo is hidden by privacy settings; may be null. If null and user.profile_photo is null, then the photo is empty; otherwise, it is unknown. If non-null and both photo and personal_photo are null, then it is the same photo as in user.profile_photo and chat.photo. This photo isn't returned in the list of user photos, defaults to None
    :type public_photo: :class:`ChatPhoto`, optional
    :param block_list: Block list to which the user is added; may be null if none, defaults to None
    :type block_list: :class:`BlockList`, optional
    :param bio: A short user bio; may be null for bots, defaults to None
    :type bio: :class:`FormattedText`, optional
    :param bot_info: For bots, information about the bot; may be null if the user isn't a bot, defaults to None
    :type bot_info: :class:`BotInfo`, optional
    :param can_be_called: True, if the user can be called
    :type can_be_called: :class:`Bool`
    :param supports_video_calls: True, if a video call can be created with the user
    :type supports_video_calls: :class:`Bool`
    :param has_private_calls: True, if the user can't be called due to their privacy settings
    :type has_private_calls: :class:`Bool`
    :param has_private_forwards: True, if the user can't be linked in forwarded messages due to their privacy settings
    :type has_private_forwards: :class:`Bool`
    :param has_restricted_voice_and_video_note_messages: True, if voice and video notes can't be sent or forwarded to the user
    :type has_restricted_voice_and_video_note_messages: :class:`Bool`
    :param has_pinned_stories: True, if the user has pinned stories
    :type has_pinned_stories: :class:`Bool`
    :param need_phone_number_privacy_exception: True, if the current user needs to explicitly allow to share their phone number with the user when the method addContact is used
    :type need_phone_number_privacy_exception: :class:`Bool`
    """

    ID: typing.Literal["userFullInfo"] = "userFullInfo"
    premium_gift_options: Vector[PremiumPaymentOption]
    group_in_common_count: Int32
    personal_photo: typing.Optional[ChatPhoto] = None
    photo: typing.Optional[ChatPhoto] = None
    public_photo: typing.Optional[ChatPhoto] = None
    block_list: typing.Optional[BlockList] = None
    bio: typing.Optional[FormattedText] = None
    bot_info: typing.Optional[BotInfo] = None
    can_be_called: Bool = False
    supports_video_calls: Bool = False
    has_private_calls: Bool = False
    has_private_forwards: Bool = False
    has_restricted_voice_and_video_note_messages: Bool = False
    has_pinned_stories: Bool = False
    need_phone_number_privacy_exception: Bool = False


class UserLink(BaseObject):
    """
    Contains an HTTPS URL, which can be used to get information about a user

    :param url: The URL
    :type url: :class:`String`
    :param expires_in: Left time for which the link is valid, in seconds; 0 if the link is a public username link
    :type expires_in: :class:`Int32`
    """

    ID: typing.Literal["userLink"] = "userLink"
    url: String
    expires_in: Int32


class UserPrivacySettingAllowCalls(BaseObject):
    """
    A privacy setting for managing whether the user can be called
    """

    ID: typing.Literal["userPrivacySettingAllowCalls"] = "userPrivacySettingAllowCalls"


class UserPrivacySettingAllowChatInvites(BaseObject):
    """
    A privacy setting for managing whether the user can be invited to chats
    """

    ID: typing.Literal["userPrivacySettingAllowChatInvites"] = "userPrivacySettingAllowChatInvites"


class UserPrivacySettingAllowFindingByPhoneNumber(BaseObject):
    """
    A privacy setting for managing whether the user can be found by their phone number. Checked only if the phone number is not known to the other user. Can be set only to "Allow contacts" or "Allow all"
    """

    ID: typing.Literal["userPrivacySettingAllowFindingByPhoneNumber"] = "userPrivacySettingAllowFindingByPhoneNumber"


class UserPrivacySettingAllowPeerToPeerCalls(BaseObject):
    """
    A privacy setting for managing whether peer-to-peer connections can be used for calls
    """

    ID: typing.Literal["userPrivacySettingAllowPeerToPeerCalls"] = "userPrivacySettingAllowPeerToPeerCalls"


class UserPrivacySettingAllowPrivateVoiceAndVideoNoteMessages(BaseObject):
    """
    A privacy setting for managing whether the user can receive voice and video messages in private chats
    """

    ID: typing.Literal[
        "userPrivacySettingAllowPrivateVoiceAndVideoNoteMessages"
    ] = "userPrivacySettingAllowPrivateVoiceAndVideoNoteMessages"


class UserPrivacySettingShowBio(BaseObject):
    """
    A privacy setting for managing whether the user's bio is visible
    """

    ID: typing.Literal["userPrivacySettingShowBio"] = "userPrivacySettingShowBio"


class UserPrivacySettingShowLinkInForwardedMessages(BaseObject):
    """
    A privacy setting for managing whether a link to the user's account is included in forwarded messages
    """

    ID: typing.Literal[
        "userPrivacySettingShowLinkInForwardedMessages"
    ] = "userPrivacySettingShowLinkInForwardedMessages"


class UserPrivacySettingShowPhoneNumber(BaseObject):
    """
    A privacy setting for managing whether the user's phone number is visible
    """

    ID: typing.Literal["userPrivacySettingShowPhoneNumber"] = "userPrivacySettingShowPhoneNumber"


class UserPrivacySettingShowProfilePhoto(BaseObject):
    """
    A privacy setting for managing whether the user's profile photo is visible
    """

    ID: typing.Literal["userPrivacySettingShowProfilePhoto"] = "userPrivacySettingShowProfilePhoto"


class UserPrivacySettingShowStatus(BaseObject):
    """
    A privacy setting for managing whether the user's online status is visible
    """

    ID: typing.Literal["userPrivacySettingShowStatus"] = "userPrivacySettingShowStatus"


UserPrivacySetting = typing.Union[
    UserPrivacySettingAllowCalls,
    UserPrivacySettingAllowChatInvites,
    UserPrivacySettingAllowFindingByPhoneNumber,
    UserPrivacySettingAllowPeerToPeerCalls,
    UserPrivacySettingAllowPrivateVoiceAndVideoNoteMessages,
    UserPrivacySettingShowBio,
    UserPrivacySettingShowLinkInForwardedMessages,
    UserPrivacySettingShowPhoneNumber,
    UserPrivacySettingShowProfilePhoto,
    UserPrivacySettingShowStatus,
]


class UserPrivacySettingRuleAllowAll(BaseObject):
    """
    A rule to allow all users to do something
    """

    ID: typing.Literal["userPrivacySettingRuleAllowAll"] = "userPrivacySettingRuleAllowAll"


class UserPrivacySettingRuleAllowChatMembers(BaseObject):
    """
    A rule to allow all members of certain specified basic groups and supergroups to doing something

    :param chat_ids: The chat identifiers, total number of chats in all rules must not exceed 20
    :type chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["userPrivacySettingRuleAllowChatMembers"] = "userPrivacySettingRuleAllowChatMembers"
    chat_ids: Vector[Int53]


class UserPrivacySettingRuleAllowContacts(BaseObject):
    """
    A rule to allow all contacts of the user to do something
    """

    ID: typing.Literal["userPrivacySettingRuleAllowContacts"] = "userPrivacySettingRuleAllowContacts"


class UserPrivacySettingRuleAllowUsers(BaseObject):
    """
    A rule to allow certain specified users to do something

    :param user_ids: The user identifiers, total number of users in all rules must not exceed 1000
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["userPrivacySettingRuleAllowUsers"] = "userPrivacySettingRuleAllowUsers"
    user_ids: Vector[Int53]


class UserPrivacySettingRuleRestrictAll(BaseObject):
    """
    A rule to restrict all users from doing something
    """

    ID: typing.Literal["userPrivacySettingRuleRestrictAll"] = "userPrivacySettingRuleRestrictAll"


class UserPrivacySettingRuleRestrictChatMembers(BaseObject):
    """
    A rule to restrict all members of specified basic groups and supergroups from doing something

    :param chat_ids: The chat identifiers, total number of chats in all rules must not exceed 20
    :type chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["userPrivacySettingRuleRestrictChatMembers"] = "userPrivacySettingRuleRestrictChatMembers"
    chat_ids: Vector[Int53]


class UserPrivacySettingRuleRestrictContacts(BaseObject):
    """
    A rule to restrict all contacts of the user from doing something
    """

    ID: typing.Literal["userPrivacySettingRuleRestrictContacts"] = "userPrivacySettingRuleRestrictContacts"


class UserPrivacySettingRuleRestrictUsers(BaseObject):
    """
    A rule to restrict all specified users from doing something

    :param user_ids: The user identifiers, total number of users in all rules must not exceed 1000
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["userPrivacySettingRuleRestrictUsers"] = "userPrivacySettingRuleRestrictUsers"
    user_ids: Vector[Int53]


UserPrivacySettingRule = typing.Union[
    UserPrivacySettingRuleAllowAll,
    UserPrivacySettingRuleAllowChatMembers,
    UserPrivacySettingRuleAllowContacts,
    UserPrivacySettingRuleAllowUsers,
    UserPrivacySettingRuleRestrictAll,
    UserPrivacySettingRuleRestrictChatMembers,
    UserPrivacySettingRuleRestrictContacts,
    UserPrivacySettingRuleRestrictUsers,
]


class UserPrivacySettingRules(BaseObject):
    """
    A list of privacy rules. Rules are matched in the specified order. The first matched rule defines the privacy setting for a given user. If no rule matches, the action is not allowed

    :param rules: A list of rules
    :type rules: :class:`Vector[UserPrivacySettingRule]`
    """

    ID: typing.Literal["userPrivacySettingRules"] = "userPrivacySettingRules"
    rules: Vector[UserPrivacySettingRule]


class UserStatusEmpty(BaseObject):
    """
    The user status was never changed
    """

    ID: typing.Literal["userStatusEmpty"] = "userStatusEmpty"


class UserStatusLastMonth(BaseObject):
    """
    The user is offline, but was online last month
    """

    ID: typing.Literal["userStatusLastMonth"] = "userStatusLastMonth"


class UserStatusLastWeek(BaseObject):
    """
    The user is offline, but was online last week
    """

    ID: typing.Literal["userStatusLastWeek"] = "userStatusLastWeek"


class UserStatusOffline(BaseObject):
    """
    The user is offline

    :param was_online: Point in time (Unix timestamp) when the user was last online
    :type was_online: :class:`Int32`
    """

    ID: typing.Literal["userStatusOffline"] = "userStatusOffline"
    was_online: Int32


class UserStatusOnline(BaseObject):
    """
    The user is online

    :param expires: Point in time (Unix timestamp) when the user's online status will expire
    :type expires: :class:`Int32`
    """

    ID: typing.Literal["userStatusOnline"] = "userStatusOnline"
    expires: Int32


class UserStatusRecently(BaseObject):
    """
    The user was online recently
    """

    ID: typing.Literal["userStatusRecently"] = "userStatusRecently"


UserStatus = typing.Union[
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
]


class UserSupportInfo(BaseObject):
    """
    Contains custom information about the user

    :param message: Information message
    :type message: :class:`FormattedText`
    :param author: Information author
    :type author: :class:`String`
    :param date: Information change date
    :type date: :class:`Int32`
    """

    ID: typing.Literal["userSupportInfo"] = "userSupportInfo"
    message: FormattedText
    author: String
    date: Int32


class UserTypeBot(BaseObject):
    """
    A bot (see https://core.telegram.org/bots)

    :param inline_query_placeholder: Placeholder for inline queries (displayed on the application input field)
    :type inline_query_placeholder: :class:`String`
    :param can_be_edited: True, if the bot is owned by the current user and can be edited using the methods toggleBotUsernameIsActive, reorderBotActiveUsernames, setBotProfilePhoto, setBotName, setBotInfoDescription, and setBotInfoShortDescription
    :type can_be_edited: :class:`Bool`
    :param can_join_groups: True, if the bot can be invited to basic group and supergroup chats
    :type can_join_groups: :class:`Bool`
    :param can_read_all_group_messages: True, if the bot can read all messages in basic group or supergroup chats and not just those addressed to the bot. In private and channel chats a bot can always read all messages
    :type can_read_all_group_messages: :class:`Bool`
    :param is_inline: True, if the bot supports inline queries
    :type is_inline: :class:`Bool`
    :param need_location: True, if the location of the user is expected to be sent with every inline query to this bot
    :type need_location: :class:`Bool`
    :param can_be_added_to_attachment_menu: True, if the bot can be added to attachment or side menu
    :type can_be_added_to_attachment_menu: :class:`Bool`
    """

    ID: typing.Literal["userTypeBot"] = "userTypeBot"
    inline_query_placeholder: String
    can_be_edited: Bool = False
    can_join_groups: Bool = False
    can_read_all_group_messages: Bool = False
    is_inline: Bool = False
    need_location: Bool = False
    can_be_added_to_attachment_menu: Bool = False


class UserTypeDeleted(BaseObject):
    """
    A deleted user or deleted bot. No information on the user besides the user identifier is available. It is not possible to perform any active actions on this type of user
    """

    ID: typing.Literal["userTypeDeleted"] = "userTypeDeleted"


class UserTypeRegular(BaseObject):
    """
    A regular user
    """

    ID: typing.Literal["userTypeRegular"] = "userTypeRegular"


class UserTypeUnknown(BaseObject):
    """
    No information on the user besides the user identifier is available, yet this user has not been deleted. This object is extremely rare and must be handled like a deleted user. It is not possible to perform any actions on users of this type
    """

    ID: typing.Literal["userTypeUnknown"] = "userTypeUnknown"


UserType = typing.Union[
    UserTypeBot,
    UserTypeDeleted,
    UserTypeRegular,
    UserTypeUnknown,
]


class Usernames(BaseObject):
    """
    Describes usernames assigned to a user, a supergroup, or a channel

    :param active_usernames: List of active usernames; the first one must be shown as the primary username. The order of active usernames can be changed with reorderActiveUsernames, reorderBotActiveUsernames or reorderSupergroupActiveUsernames
    :type active_usernames: :class:`Vector[String]`
    :param disabled_usernames: List of currently disabled usernames; the username can be activated with toggleUsernameIsActive, toggleBotUsernameIsActive, or toggleSupergroupUsernameIsActive
    :type disabled_usernames: :class:`Vector[String]`
    :param editable_username: The active username, which can be changed with setUsername or setSupergroupUsername
    :type editable_username: :class:`String`
    """

    ID: typing.Literal["usernames"] = "usernames"
    active_usernames: Vector[String]
    disabled_usernames: Vector[String]
    editable_username: String


class Users(BaseObject):
    """
    Represents a list of users

    :param total_count: Approximate total number of users found
    :type total_count: :class:`Int32`
    :param user_ids: A list of user identifiers
    :type user_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["users"] = "users"
    total_count: Int32
    user_ids: Vector[Int53]


class ValidatedOrderInfo(BaseObject):
    """
    Contains a temporary identifier of validated order information, which is stored for one hour, and the available shipping options

    :param order_info_id: Temporary identifier of the order information
    :type order_info_id: :class:`String`
    :param shipping_options: Available shipping options
    :type shipping_options: :class:`Vector[ShippingOption]`
    """

    ID: typing.Literal["validatedOrderInfo"] = "validatedOrderInfo"
    order_info_id: String
    shipping_options: Vector[ShippingOption]


class VectorPathCommandCubicBezierCurve(BaseObject):
    """
    A cubic Bézier curve to a given point

    :param start_control_point: The start control point of the curve
    :type start_control_point: :class:`Point`
    :param end_control_point: The end control point of the curve
    :type end_control_point: :class:`Point`
    :param end_point: The end point of the curve
    :type end_point: :class:`Point`
    """

    ID: typing.Literal["vectorPathCommandCubicBezierCurve"] = "vectorPathCommandCubicBezierCurve"
    start_control_point: Point
    end_control_point: Point
    end_point: Point


class VectorPathCommandLine(BaseObject):
    """
    A straight line to a given point

    :param end_point: The end point of the straight line
    :type end_point: :class:`Point`
    """

    ID: typing.Literal["vectorPathCommandLine"] = "vectorPathCommandLine"
    end_point: Point


VectorPathCommand = typing.Union[
    VectorPathCommandCubicBezierCurve,
    VectorPathCommandLine,
]


class Venue(BaseObject):
    """
    Describes a venue

    :param location: Venue location; as defined by the sender
    :type location: :class:`Location`
    :param title: Venue name; as defined by the sender
    :type title: :class:`String`
    :param address: Venue address; as defined by the sender
    :type address: :class:`String`
    :param provider: Provider of the venue database; as defined by the sender. Currently, only "foursquare" and "gplaces" (Google Places) need to be supported
    :type provider: :class:`String`
    :param id: Identifier of the venue in the provider database; as defined by the sender
    :type id: :class:`String`
    :param type_: Type of the venue in the provider database; as defined by the sender
    :type type_: :class:`String`
    """

    ID: typing.Literal["venue"] = "venue"
    location: Location
    title: String
    address: String
    provider: String
    id: String
    type_: String = Field(..., alias="type")


class Video(BaseObject):
    """
    Describes a video file

    :param duration: Duration of the video, in seconds; as defined by the sender
    :type duration: :class:`Int32`
    :param width: Video width; as defined by the sender
    :type width: :class:`Int32`
    :param height: Video height; as defined by the sender
    :type height: :class:`Int32`
    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`String`
    :param mime_type: MIME type of the file; as defined by the sender
    :type mime_type: :class:`String`
    :param video: File containing the video
    :type video: :class:`File`
    :param minithumbnail: Video minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param thumbnail: Video thumbnail in JPEG or MPEG4 format; as defined by the sender; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param has_stickers: True, if stickers were added to the video. The list of corresponding sticker sets can be received using getAttachedStickerSets
    :type has_stickers: :class:`Bool`
    :param supports_streaming: True, if the video is supposed to be streamed
    :type supports_streaming: :class:`Bool`
    """

    ID: typing.Literal["video"] = "video"
    duration: Int32
    width: Int32
    height: Int32
    file_name: String
    mime_type: String
    video: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    has_stickers: Bool = False
    supports_streaming: Bool = False


class VideoChat(BaseObject):
    """
    Describes a video chat

    :param default_participant_id: Default group call participant identifier to join the video chat; may be null, defaults to None
    :type default_participant_id: :class:`MessageSender`, optional
    :param has_participants: True, if the video chat has participants
    :type has_participants: :class:`Bool`
    :param group_call_id: Group call identifier of an active video chat; 0 if none. Full information about the video chat can be received through the method getGroupCall, defaults to None
    :type group_call_id: :class:`Int32`, optional
    """

    ID: typing.Literal["videoChat"] = "videoChat"
    default_participant_id: typing.Optional[MessageSender] = None
    has_participants: Bool = False
    group_call_id: typing.Optional[Int32] = 0


class VideoNote(BaseObject):
    """
    Describes a video note. The video must be equal in width and height, cropped to a circle, and stored in MPEG4 format

    :param duration: Duration of the video, in seconds; as defined by the sender
    :type duration: :class:`Int32`
    :param length: Video width and height; as defined by the sender
    :type length: :class:`Int32`
    :param video: File containing the video
    :type video: :class:`File`
    :param minithumbnail: Video minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    :param thumbnail: Video thumbnail in JPEG format; as defined by the sender; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    :param speech_recognition_result: Result of speech recognition in the video note; may be null, defaults to None
    :type speech_recognition_result: :class:`SpeechRecognitionResult`, optional
    :param waveform: A waveform representation of the video note's audio in 5-bit format; may be empty if unknown
    :type waveform: :class:`Bytes`
    """

    ID: typing.Literal["videoNote"] = "videoNote"
    duration: Int32
    length: Int32
    video: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    speech_recognition_result: typing.Optional[SpeechRecognitionResult] = None
    waveform: Bytes = b""


class VoiceNote(BaseObject):
    """
    Describes a voice note. The voice note must be encoded with the Opus codec, and stored inside an OGG container. Voice notes can have only a single audio channel

    :param duration: Duration of the voice note, in seconds; as defined by the sender
    :type duration: :class:`Int32`
    :param waveform: A waveform representation of the voice note in 5-bit format
    :type waveform: :class:`Bytes`
    :param mime_type: MIME type of the file; as defined by the sender
    :type mime_type: :class:`String`
    :param voice: File containing the voice note
    :type voice: :class:`File`
    :param speech_recognition_result: Result of speech recognition in the voice note; may be null, defaults to None
    :type speech_recognition_result: :class:`SpeechRecognitionResult`, optional
    """

    ID: typing.Literal["voiceNote"] = "voiceNote"
    duration: Int32
    waveform: Bytes
    mime_type: String
    voice: File
    speech_recognition_result: typing.Optional[SpeechRecognitionResult] = None


class WebApp(BaseObject):
    """
    Describes a Web App. Use getInternalLink with internalLinkTypeWebApp to share the Web App

    :param short_name: Web App short name
    :type short_name: :class:`String`
    :param title: Web App title
    :type title: :class:`String`
    :param description: Web App description
    :type description: :class:`String`
    :param photo: Web App photo
    :type photo: :class:`Photo`
    :param animation: Web App animation; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    """

    ID: typing.Literal["webApp"] = "webApp"
    short_name: String
    title: String
    description: String
    photo: Photo
    animation: typing.Optional[Animation] = None


class WebAppInfo(BaseObject):
    """
    Contains information about a Web App

    :param launch_id: Unique identifier for the Web App launch
    :type launch_id: :class:`Int64`
    :param url: A Web App URL to open in a web view
    :type url: :class:`String`
    """

    ID: typing.Literal["webAppInfo"] = "webAppInfo"
    launch_id: Int64
    url: String


class WebPage(BaseObject):
    """
    Describes a web page preview

    :param url: Original URL of the link
    :type url: :class:`String`
    :param display_url: URL to display
    :type display_url: :class:`String`
    :param type_: Type of the web page. Can be: article, photo, audio, video, document, profile, app, or something else
    :type type_: :class:`String`
    :param site_name: Short name of the site (e.g., Google Docs, App Store)
    :type site_name: :class:`String`
    :param title: Title of the content
    :type title: :class:`String`
    :param description: Description of the content
    :type description: :class:`FormattedText`
    :param embed_url: URL to show in the embedded preview
    :type embed_url: :class:`String`
    :param embed_type: MIME type of the embedded preview, (e.g., text/html or video/mp4)
    :type embed_type: :class:`String`
    :param embed_width: Width of the embedded preview
    :type embed_width: :class:`Int32`
    :param embed_height: Height of the embedded preview
    :type embed_height: :class:`Int32`
    :param duration: Duration of the content, in seconds
    :type duration: :class:`Int32`
    :param author: Author of the content
    :type author: :class:`String`
    :param photo: Image representing the content; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    :param animation: Preview of the content as an animation, if available; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    :param audio: Preview of the content as an audio file, if available; may be null, defaults to None
    :type audio: :class:`Audio`, optional
    :param document: Preview of the content as a document, if available; may be null, defaults to None
    :type document: :class:`Document`, optional
    :param sticker: Preview of the content as a sticker for small WEBP files, if available; may be null, defaults to None
    :type sticker: :class:`Sticker`, optional
    :param video: Preview of the content as a video, if available; may be null, defaults to None
    :type video: :class:`Video`, optional
    :param video_note: Preview of the content as a video note, if available; may be null, defaults to None
    :type video_note: :class:`VideoNote`, optional
    :param voice_note: Preview of the content as a voice note, if available; may be null, defaults to None
    :type voice_note: :class:`VoiceNote`, optional
    :param story_sender_chat_id: The identifier of the sender of the previewed story; 0 if none, defaults to None
    :type story_sender_chat_id: :class:`Int53`, optional
    :param story_id: The identifier of the previewed story; 0 if none, defaults to None
    :type story_id: :class:`Int32`, optional
    :param instant_view_version: Version of web page instant view (currently, can be 1 or 2); 0 if none, defaults to None
    :type instant_view_version: :class:`Int32`, optional
    """

    ID: typing.Literal["webPage"] = "webPage"
    url: String
    display_url: String
    type_: String = Field(..., alias="type")
    site_name: String
    title: String
    description: FormattedText
    embed_url: String
    embed_type: String
    embed_width: Int32
    embed_height: Int32
    duration: Int32
    author: String
    photo: typing.Optional[Photo] = None
    animation: typing.Optional[Animation] = None
    audio: typing.Optional[Audio] = None
    document: typing.Optional[Document] = None
    sticker: typing.Optional[Sticker] = None
    video: typing.Optional[Video] = None
    video_note: typing.Optional[VideoNote] = None
    voice_note: typing.Optional[VoiceNote] = None
    story_sender_chat_id: typing.Optional[Int53] = 0
    story_id: typing.Optional[Int32] = 0
    instant_view_version: typing.Optional[Int32] = 0


class WebPageInstantView(BaseObject):
    """
    Describes an instant view page for a web page

    :param page_blocks: Content of the web page
    :type page_blocks: :class:`Vector[PageBlock]`
    :param version: Version of the instant view; currently, can be 1 or 2
    :type version: :class:`Int32`
    :param feedback_link: An internal link to be opened to leave feedback about the instant view
    :type feedback_link: :class:`InternalLinkType`
    :param is_rtl: True, if the instant view must be shown from right to left
    :type is_rtl: :class:`Bool`
    :param is_full: True, if the instant view contains the full page. A network request might be needed to get the full web page instant view
    :type is_full: :class:`Bool`
    :param view_count: Number of the instant view views; 0 if unknown, defaults to None
    :type view_count: :class:`Int32`, optional
    """

    ID: typing.Literal["webPageInstantView"] = "webPageInstantView"
    page_blocks: Vector[PageBlock]
    version: Int32
    feedback_link: InternalLinkType
    is_rtl: Bool = False
    is_full: Bool = False
    view_count: typing.Optional[Int32] = 0


AddedReaction.update_forward_refs()
AddedReactions.update_forward_refs()
AnimatedChatPhoto.update_forward_refs()
AnimatedEmoji.update_forward_refs()
Animation.update_forward_refs()
Animations.update_forward_refs()
AttachmentMenuBot.update_forward_refs()
Audio.update_forward_refs()
AuthenticationCodeInfo.update_forward_refs()
AuthorizationStateWaitCode.update_forward_refs()
AuthorizationStateWaitEmailCode.update_forward_refs()
AuthorizationStateWaitRegistration.update_forward_refs()
AutoDownloadSettingsPresets.update_forward_refs()
AutosaveSettings.update_forward_refs()
AutosaveSettingsException.update_forward_refs()
AvailableReaction.update_forward_refs()
AvailableReactions.update_forward_refs()
Background.update_forward_refs()
BackgroundTypeFill.update_forward_refs()
BackgroundTypePattern.update_forward_refs()
Backgrounds.update_forward_refs()
BankCardInfo.update_forward_refs()
BasicGroup.update_forward_refs()
BasicGroupFullInfo.update_forward_refs()
BotCommands.update_forward_refs()
BotInfo.update_forward_refs()
Call.update_forward_refs()
CallServer.update_forward_refs()
CallStateDiscarded.update_forward_refs()
CallStateError.update_forward_refs()
CallStateReady.update_forward_refs()
Chat.update_forward_refs()
ChatActiveStories.update_forward_refs()
ChatAdministrators.update_forward_refs()
ChatAvailableReactionsSome.update_forward_refs()
ChatBackground.update_forward_refs()
ChatEvent.update_forward_refs()
ChatEventAvailableReactionsChanged.update_forward_refs()
ChatEventForumTopicCreated.update_forward_refs()
ChatEventForumTopicDeleted.update_forward_refs()
ChatEventForumTopicEdited.update_forward_refs()
ChatEventForumTopicPinned.update_forward_refs()
ChatEventForumTopicToggleIsClosed.update_forward_refs()
ChatEventForumTopicToggleIsHidden.update_forward_refs()
ChatEventInviteLinkDeleted.update_forward_refs()
ChatEventInviteLinkEdited.update_forward_refs()
ChatEventInviteLinkRevoked.update_forward_refs()
ChatEventLocationChanged.update_forward_refs()
ChatEventMemberInvited.update_forward_refs()
ChatEventMemberJoinedByInviteLink.update_forward_refs()
ChatEventMemberJoinedByRequest.update_forward_refs()
ChatEventMemberPromoted.update_forward_refs()
ChatEventMemberRestricted.update_forward_refs()
ChatEventMessageDeleted.update_forward_refs()
ChatEventMessageEdited.update_forward_refs()
ChatEventMessagePinned.update_forward_refs()
ChatEventMessageUnpinned.update_forward_refs()
ChatEventPermissionsChanged.update_forward_refs()
ChatEventPhotoChanged.update_forward_refs()
ChatEventPollStopped.update_forward_refs()
ChatEventVideoChatParticipantIsMutedToggled.update_forward_refs()
ChatEventVideoChatParticipantVolumeLevelChanged.update_forward_refs()
ChatEvents.update_forward_refs()
ChatFolder.update_forward_refs()
ChatFolderInfo.update_forward_refs()
ChatFolderInviteLinkInfo.update_forward_refs()
ChatFolderInviteLinks.update_forward_refs()
ChatInviteLinkCounts.update_forward_refs()
ChatInviteLinkInfo.update_forward_refs()
ChatInviteLinkMembers.update_forward_refs()
ChatInviteLinks.update_forward_refs()
ChatJoinRequests.update_forward_refs()
ChatLists.update_forward_refs()
ChatLocation.update_forward_refs()
ChatMember.update_forward_refs()
ChatMemberStatusAdministrator.update_forward_refs()
ChatMemberStatusRestricted.update_forward_refs()
ChatMembers.update_forward_refs()
ChatMessageSender.update_forward_refs()
ChatMessageSenders.update_forward_refs()
ChatPhoto.update_forward_refs()
ChatPhotoInfo.update_forward_refs()
ChatPhotoSticker.update_forward_refs()
ChatPhotos.update_forward_refs()
ChatPosition.update_forward_refs()
ChatStatisticsChannel.update_forward_refs()
ChatStatisticsSupergroup.update_forward_refs()
ChatTheme.update_forward_refs()
ChatsNearby.update_forward_refs()
ClosedVectorPath.update_forward_refs()
ConnectedWebsites.update_forward_refs()
Countries.update_forward_refs()
DatedFile.update_forward_refs()
DeepLinkInfo.update_forward_refs()
DiceStickersRegular.update_forward_refs()
DiceStickersSlotMachine.update_forward_refs()
Document.update_forward_refs()
DraftMessage.update_forward_refs()
EmojiCategories.update_forward_refs()
EmojiCategory.update_forward_refs()
EmojiReaction.update_forward_refs()
EncryptedPassportElement.update_forward_refs()
File.update_forward_refs()
FileDownload.update_forward_refs()
FormattedText.update_forward_refs()
ForumTopic.update_forward_refs()
ForumTopicInfo.update_forward_refs()
ForumTopics.update_forward_refs()
FoundChatMessages.update_forward_refs()
FoundFileDownloads.update_forward_refs()
FoundMessages.update_forward_refs()
FoundWebApp.update_forward_refs()
Game.update_forward_refs()
GameHighScores.update_forward_refs()
GroupCall.update_forward_refs()
GroupCallParticipant.update_forward_refs()
GroupCallParticipantVideoInfo.update_forward_refs()
GroupCallRecentSpeaker.update_forward_refs()
GroupCallStreams.update_forward_refs()
IdentityDocument.update_forward_refs()
InlineKeyboardButton.update_forward_refs()
InlineKeyboardButtonTypeSwitchInline.update_forward_refs()
InlineQueryResultAnimation.update_forward_refs()
InlineQueryResultArticle.update_forward_refs()
InlineQueryResultAudio.update_forward_refs()
InlineQueryResultContact.update_forward_refs()
InlineQueryResultDocument.update_forward_refs()
InlineQueryResultGame.update_forward_refs()
InlineQueryResultLocation.update_forward_refs()
InlineQueryResultPhoto.update_forward_refs()
InlineQueryResultSticker.update_forward_refs()
InlineQueryResultVenue.update_forward_refs()
InlineQueryResultVideo.update_forward_refs()
InlineQueryResultVoiceNote.update_forward_refs()
InlineQueryResults.update_forward_refs()
InlineQueryResultsButton.update_forward_refs()
InputBackgroundLocal.update_forward_refs()
InputChatPhotoAnimation.update_forward_refs()
InputChatPhotoStatic.update_forward_refs()
InputChatPhotoSticker.update_forward_refs()
InputIdentityDocument.update_forward_refs()
InputInlineQueryResultAnimation.update_forward_refs()
InputInlineQueryResultArticle.update_forward_refs()
InputInlineQueryResultAudio.update_forward_refs()
InputInlineQueryResultContact.update_forward_refs()
InputInlineQueryResultDocument.update_forward_refs()
InputInlineQueryResultGame.update_forward_refs()
InputInlineQueryResultLocation.update_forward_refs()
InputInlineQueryResultPhoto.update_forward_refs()
InputInlineQueryResultSticker.update_forward_refs()
InputInlineQueryResultVenue.update_forward_refs()
InputInlineQueryResultVideo.update_forward_refs()
InputInlineQueryResultVoiceNote.update_forward_refs()
InputMessageAnimation.update_forward_refs()
InputMessageAudio.update_forward_refs()
InputMessageContact.update_forward_refs()
InputMessageDocument.update_forward_refs()
InputMessageForwarded.update_forward_refs()
InputMessageInvoice.update_forward_refs()
InputMessageLocation.update_forward_refs()
InputMessagePhoto.update_forward_refs()
InputMessagePoll.update_forward_refs()
InputMessageSticker.update_forward_refs()
InputMessageText.update_forward_refs()
InputMessageVenue.update_forward_refs()
InputMessageVideo.update_forward_refs()
InputMessageVideoNote.update_forward_refs()
InputMessageVoiceNote.update_forward_refs()
InputPassportElementAddress.update_forward_refs()
InputPassportElementBankStatement.update_forward_refs()
InputPassportElementDriverLicense.update_forward_refs()
InputPassportElementIdentityCard.update_forward_refs()
InputPassportElementInternalPassport.update_forward_refs()
InputPassportElementPassport.update_forward_refs()
InputPassportElementPassportRegistration.update_forward_refs()
InputPassportElementPersonalDetails.update_forward_refs()
InputPassportElementRentalAgreement.update_forward_refs()
InputPassportElementTemporaryRegistration.update_forward_refs()
InputPassportElementUtilityBill.update_forward_refs()
InputPassportElementError.update_forward_refs()
InputPersonalDocument.update_forward_refs()
InputSticker.update_forward_refs()
InputStoryArea.update_forward_refs()
InputStoryAreaTypeLocation.update_forward_refs()
InputStoryAreas.update_forward_refs()
InputStoryContentPhoto.update_forward_refs()
InputStoryContentVideo.update_forward_refs()
InputThumbnail.update_forward_refs()
InternalLinkTypeAttachmentMenuBot.update_forward_refs()
InternalLinkTypeBotAddToChannel.update_forward_refs()
InternalLinkTypeBotStartInGroup.update_forward_refs()
InternalLinkTypeMessageDraft.update_forward_refs()
InternalLinkTypeProxy.update_forward_refs()
Invoice.update_forward_refs()
JsonValueArray.update_forward_refs()
JsonValueObject.update_forward_refs()
JsonObjectMember.update_forward_refs()
KeyboardButton.update_forward_refs()
KeyboardButtonTypeRequestChat.update_forward_refs()
LanguagePackString.update_forward_refs()
LanguagePackStrings.update_forward_refs()
LocalizationTargetInfo.update_forward_refs()
MaskPosition.update_forward_refs()
Message.update_forward_refs()
MessageCalendar.update_forward_refs()
MessageCalendarDay.update_forward_refs()
MessageAnimatedEmoji.update_forward_refs()
MessageAnimation.update_forward_refs()
MessageAudio.update_forward_refs()
MessageBotWriteAccessAllowed.update_forward_refs()
MessageCall.update_forward_refs()
MessageChatChangePhoto.update_forward_refs()
MessageChatSetBackground.update_forward_refs()
MessageContact.update_forward_refs()
MessageDice.update_forward_refs()
MessageDocument.update_forward_refs()
MessageForumTopicCreated.update_forward_refs()
MessageGame.update_forward_refs()
MessageGiftedPremium.update_forward_refs()
MessageInvoice.update_forward_refs()
MessageLocation.update_forward_refs()
MessagePassportDataReceived.update_forward_refs()
MessagePassportDataSent.update_forward_refs()
MessagePaymentSuccessfulBot.update_forward_refs()
MessagePhoto.update_forward_refs()
MessagePoll.update_forward_refs()
MessageProximityAlertTriggered.update_forward_refs()
MessageSticker.update_forward_refs()
MessageSuggestProfilePhoto.update_forward_refs()
MessageText.update_forward_refs()
MessageVenue.update_forward_refs()
MessageVideo.update_forward_refs()
MessageVideoNote.update_forward_refs()
MessageVoiceNote.update_forward_refs()
MessageCopyOptions.update_forward_refs()
MessageExtendedMediaPhoto.update_forward_refs()
MessageExtendedMediaPreview.update_forward_refs()
MessageExtendedMediaUnsupported.update_forward_refs()
MessageExtendedMediaVideo.update_forward_refs()
MessageForwardInfo.update_forward_refs()
MessageInteractionInfo.update_forward_refs()
MessageLinkInfo.update_forward_refs()
MessagePositions.update_forward_refs()
MessageReaction.update_forward_refs()
MessageReplyInfo.update_forward_refs()
MessageSendOptions.update_forward_refs()
MessageSenders.update_forward_refs()
MessageSponsor.update_forward_refs()
MessageSponsorTypeBot.update_forward_refs()
MessageSponsorTypePublicChannel.update_forward_refs()
MessageStatistics.update_forward_refs()
MessageThreadInfo.update_forward_refs()
MessageViewers.update_forward_refs()
Messages.update_forward_refs()
NetworkStatistics.update_forward_refs()
NetworkStatisticsEntryCall.update_forward_refs()
NetworkStatisticsEntryFile.update_forward_refs()
Notification.update_forward_refs()
NotificationGroup.update_forward_refs()
NotificationSound.update_forward_refs()
NotificationSounds.update_forward_refs()
NotificationTypeNewMessage.update_forward_refs()
NotificationTypeNewPushMessage.update_forward_refs()
OrderInfo.update_forward_refs()
PageBlockAnimation.update_forward_refs()
PageBlockAudio.update_forward_refs()
PageBlockAuthorDate.update_forward_refs()
PageBlockBlockQuote.update_forward_refs()
PageBlockChatLink.update_forward_refs()
PageBlockCollage.update_forward_refs()
PageBlockCover.update_forward_refs()
PageBlockDetails.update_forward_refs()
PageBlockEmbedded.update_forward_refs()
PageBlockEmbeddedPost.update_forward_refs()
PageBlockFooter.update_forward_refs()
PageBlockHeader.update_forward_refs()
PageBlockKicker.update_forward_refs()
PageBlockList.update_forward_refs()
PageBlockMap.update_forward_refs()
PageBlockParagraph.update_forward_refs()
PageBlockPhoto.update_forward_refs()
PageBlockPreformatted.update_forward_refs()
PageBlockPullQuote.update_forward_refs()
PageBlockRelatedArticles.update_forward_refs()
PageBlockSlideshow.update_forward_refs()
PageBlockSubheader.update_forward_refs()
PageBlockSubtitle.update_forward_refs()
PageBlockTable.update_forward_refs()
PageBlockTitle.update_forward_refs()
PageBlockVideo.update_forward_refs()
PageBlockVoiceNote.update_forward_refs()
PageBlockListItem.update_forward_refs()
PageBlockCaption.update_forward_refs()
PageBlockRelatedArticle.update_forward_refs()
PageBlockTableCell.update_forward_refs()
PassportAuthorizationForm.update_forward_refs()
PassportElementAddress.update_forward_refs()
PassportElementBankStatement.update_forward_refs()
PassportElementDriverLicense.update_forward_refs()
PassportElementIdentityCard.update_forward_refs()
PassportElementInternalPassport.update_forward_refs()
PassportElementPassport.update_forward_refs()
PassportElementPassportRegistration.update_forward_refs()
PassportElementPersonalDetails.update_forward_refs()
PassportElementRentalAgreement.update_forward_refs()
PassportElementTemporaryRegistration.update_forward_refs()
PassportElementUtilityBill.update_forward_refs()
PassportElementError.update_forward_refs()
PassportElements.update_forward_refs()
PassportElementsWithErrors.update_forward_refs()
PassportRequiredElement.update_forward_refs()
PassportSuitableElement.update_forward_refs()
PasswordState.update_forward_refs()
PaymentForm.update_forward_refs()
PaymentReceipt.update_forward_refs()
PersonalDetails.update_forward_refs()
PersonalDocument.update_forward_refs()
PhoneNumberAuthenticationSettings.update_forward_refs()
PhoneNumberInfo.update_forward_refs()
Photo.update_forward_refs()
PhotoSize.update_forward_refs()
Poll.update_forward_refs()
PollTypeQuiz.update_forward_refs()
PremiumFeaturePromotionAnimation.update_forward_refs()
PremiumFeatures.update_forward_refs()
PremiumLimit.update_forward_refs()
PremiumPaymentOption.update_forward_refs()
PremiumSourceFeature.update_forward_refs()
PremiumSourceLimitExceeded.update_forward_refs()
PremiumSourceStoryFeature.update_forward_refs()
PremiumState.update_forward_refs()
PremiumStatePaymentOption.update_forward_refs()
ProfilePhoto.update_forward_refs()
Proxies.update_forward_refs()
Proxy.update_forward_refs()
PushMessageContentAnimation.update_forward_refs()
PushMessageContentAudio.update_forward_refs()
PushMessageContentDocument.update_forward_refs()
PushMessageContentPhoto.update_forward_refs()
PushMessageContentSticker.update_forward_refs()
PushMessageContentVideo.update_forward_refs()
PushMessageContentVideoNote.update_forward_refs()
PushMessageContentVoiceNote.update_forward_refs()
RecommendedChatFolder.update_forward_refs()
RecommendedChatFolders.update_forward_refs()
ReplyMarkupInlineKeyboard.update_forward_refs()
ReplyMarkupShowKeyboard.update_forward_refs()
RichTextAnchorLink.update_forward_refs()
RichTextBold.update_forward_refs()
RichTextEmailAddress.update_forward_refs()
RichTextFixed.update_forward_refs()
RichTextIcon.update_forward_refs()
RichTextItalic.update_forward_refs()
RichTextMarked.update_forward_refs()
RichTextPhoneNumber.update_forward_refs()
RichTextReference.update_forward_refs()
RichTextStrikethrough.update_forward_refs()
RichTextSubscript.update_forward_refs()
RichTextSuperscript.update_forward_refs()
RichTextUnderline.update_forward_refs()
RichTextUrl.update_forward_refs()
RichTexts.update_forward_refs()
SecretChat.update_forward_refs()
Session.update_forward_refs()
Sessions.update_forward_refs()
ShippingOption.update_forward_refs()
SpeechRecognitionResultError.update_forward_refs()
SponsoredMessage.update_forward_refs()
SponsoredMessages.update_forward_refs()
Sticker.update_forward_refs()
StickerFullTypeMask.update_forward_refs()
StickerFullTypeRegular.update_forward_refs()
StickerSet.update_forward_refs()
StickerSetInfo.update_forward_refs()
StickerSets.update_forward_refs()
Stickers.update_forward_refs()
StorageStatistics.update_forward_refs()
StorageStatisticsByChat.update_forward_refs()
StorageStatisticsByFileType.update_forward_refs()
Stories.update_forward_refs()
Story.update_forward_refs()
StoryArea.update_forward_refs()
StoryAreaTypeLocation.update_forward_refs()
StoryAreaTypeVenue.update_forward_refs()
StoryContentPhoto.update_forward_refs()
StoryContentVideo.update_forward_refs()
StoryVideo.update_forward_refs()
StoryViewer.update_forward_refs()
StoryViewers.update_forward_refs()
Supergroup.update_forward_refs()
SupergroupFullInfo.update_forward_refs()
TMeUrl.update_forward_refs()
TMeUrlTypeChatInvite.update_forward_refs()
TMeUrls.update_forward_refs()
TargetChatInternalLink.update_forward_refs()
TermsOfService.update_forward_refs()
TestVectorIntObject.update_forward_refs()
TestVectorStringObject.update_forward_refs()
TextEntities.update_forward_refs()
TextEntity.update_forward_refs()
ThemeSettings.update_forward_refs()
Thumbnail.update_forward_refs()
TrendingStickerSets.update_forward_refs()
UnreadReaction.update_forward_refs()
UpdateActiveNotifications.update_forward_refs()
UpdateAnimatedEmojiMessageClicked.update_forward_refs()
UpdateAttachmentMenuBots.update_forward_refs()
UpdateAuthorizationState.update_forward_refs()
UpdateAutosaveSettings.update_forward_refs()
UpdateBasicGroup.update_forward_refs()
UpdateBasicGroupFullInfo.update_forward_refs()
UpdateCall.update_forward_refs()
UpdateChatAction.update_forward_refs()
UpdateChatActionBar.update_forward_refs()
UpdateChatActiveStories.update_forward_refs()
UpdateChatAvailableReactions.update_forward_refs()
UpdateChatBackground.update_forward_refs()
UpdateChatBlockList.update_forward_refs()
UpdateChatDraftMessage.update_forward_refs()
UpdateChatFolders.update_forward_refs()
UpdateChatLastMessage.update_forward_refs()
UpdateChatMember.update_forward_refs()
UpdateChatMessageSender.update_forward_refs()
UpdateChatNotificationSettings.update_forward_refs()
UpdateChatPendingJoinRequests.update_forward_refs()
UpdateChatPermissions.update_forward_refs()
UpdateChatPhoto.update_forward_refs()
UpdateChatPosition.update_forward_refs()
UpdateChatThemes.update_forward_refs()
UpdateChatVideoChat.update_forward_refs()
UpdateConnectionState.update_forward_refs()
UpdateDefaultReactionType.update_forward_refs()
UpdateFile.update_forward_refs()
UpdateFileAddedToDownloads.update_forward_refs()
UpdateFileDownload.update_forward_refs()
UpdateFileRemovedFromDownloads.update_forward_refs()
UpdateForumTopicInfo.update_forward_refs()
UpdateGroupCall.update_forward_refs()
UpdateGroupCallParticipant.update_forward_refs()
UpdateInstalledStickerSets.update_forward_refs()
UpdateLanguagePackStrings.update_forward_refs()
UpdateMessageContent.update_forward_refs()
UpdateMessageEdited.update_forward_refs()
UpdateMessageInteractionInfo.update_forward_refs()
UpdateMessageSendFailed.update_forward_refs()
UpdateMessageSendSucceeded.update_forward_refs()
UpdateMessageUnreadReactions.update_forward_refs()
UpdateNewCallbackQuery.update_forward_refs()
UpdateNewChat.update_forward_refs()
UpdateNewChatJoinRequest.update_forward_refs()
UpdateNewChosenInlineResult.update_forward_refs()
UpdateNewInlineCallbackQuery.update_forward_refs()
UpdateNewInlineQuery.update_forward_refs()
UpdateNewMessage.update_forward_refs()
UpdateNewPreCheckoutQuery.update_forward_refs()
UpdateNewShippingQuery.update_forward_refs()
UpdateNotification.update_forward_refs()
UpdateNotificationGroup.update_forward_refs()
UpdateOption.update_forward_refs()
UpdatePoll.update_forward_refs()
UpdatePollAnswer.update_forward_refs()
UpdateScopeNotificationSettings.update_forward_refs()
UpdateSecretChat.update_forward_refs()
UpdateSelectedBackground.update_forward_refs()
UpdateServiceNotification.update_forward_refs()
UpdateStickerSet.update_forward_refs()
UpdateStory.update_forward_refs()
UpdateStoryListChatCount.update_forward_refs()
UpdateStorySendFailed.update_forward_refs()
UpdateStorySendSucceeded.update_forward_refs()
UpdateSuggestedActions.update_forward_refs()
UpdateSupergroup.update_forward_refs()
UpdateSupergroupFullInfo.update_forward_refs()
UpdateTermsOfService.update_forward_refs()
UpdateTrendingStickerSets.update_forward_refs()
UpdateUnconfirmedSession.update_forward_refs()
UpdateUnreadChatCount.update_forward_refs()
UpdateUnreadMessageCount.update_forward_refs()
UpdateUser.update_forward_refs()
UpdateUserFullInfo.update_forward_refs()
UpdateUserPrivacySettingRules.update_forward_refs()
UpdateUserStatus.update_forward_refs()
UpdateUsersNearby.update_forward_refs()
Updates.update_forward_refs()
User.update_forward_refs()
UserFullInfo.update_forward_refs()
UserPrivacySettingRules.update_forward_refs()
UserSupportInfo.update_forward_refs()
ValidatedOrderInfo.update_forward_refs()
VectorPathCommandCubicBezierCurve.update_forward_refs()
VectorPathCommandLine.update_forward_refs()
Venue.update_forward_refs()
Video.update_forward_refs()
VideoChat.update_forward_refs()
VideoNote.update_forward_refs()
VoiceNote.update_forward_refs()
WebApp.update_forward_refs()
WebPage.update_forward_refs()
WebPageInstantView.update_forward_refs()
