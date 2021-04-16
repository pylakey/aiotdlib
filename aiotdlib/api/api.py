# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #

import typing

from .functions import *
from .types import *
from .base_object import BaseObject

if typing.TYPE_CHECKING:
    from aiotdlib.client import Client

ReturnType = typing.TypeVar('ReturnType', bound=BaseObject)


class API:
    class Types:
        # Types and Functions
        ANY = '*'
        ACCEPT_CALL = 'acceptCall'
        ACCEPT_TERMS_OF_SERVICE = 'acceptTermsOfService'
        ACCOUNT_TTL = 'accountTtl'
        ADD_CHAT_MEMBER = 'addChatMember'
        ADD_CHAT_MEMBERS = 'addChatMembers'
        ADD_CHAT_TO_LIST = 'addChatToList'
        ADD_CONTACT = 'addContact'
        ADD_CUSTOM_SERVER_LANGUAGE_PACK = 'addCustomServerLanguagePack'
        ADD_FAVORITE_STICKER = 'addFavoriteSticker'
        ADD_LOCAL_MESSAGE = 'addLocalMessage'
        ADD_LOG_MESSAGE = 'addLogMessage'
        ADD_NETWORK_STATISTICS = 'addNetworkStatistics'
        ADD_PROXY = 'addProxy'
        ADD_RECENT_STICKER = 'addRecentSticker'
        ADD_RECENTLY_FOUND_CHAT = 'addRecentlyFoundChat'
        ADD_SAVED_ANIMATION = 'addSavedAnimation'
        ADD_STICKER_TO_SET = 'addStickerToSet'
        ADDRESS = 'address'
        ANIMATED_CHAT_PHOTO = 'animatedChatPhoto'
        ANIMATION = 'animation'
        ANIMATIONS = 'animations'
        ANSWER_CALLBACK_QUERY = 'answerCallbackQuery'
        ANSWER_CUSTOM_QUERY = 'answerCustomQuery'
        ANSWER_INLINE_QUERY = 'answerInlineQuery'
        ANSWER_PRE_CHECKOUT_QUERY = 'answerPreCheckoutQuery'
        ANSWER_SHIPPING_QUERY = 'answerShippingQuery'
        AUDIO = 'audio'
        AUTHENTICATION_CODE_INFO = 'authenticationCodeInfo'
        AUTHENTICATION_CODE_TYPE = 'authenticationCodeType'
        AUTHENTICATION_CODE_TYPE_CALL = 'authenticationCodeTypeCall'
        AUTHENTICATION_CODE_TYPE_FLASH_CALL = 'authenticationCodeTypeFlashCall'
        AUTHENTICATION_CODE_TYPE_SMS = 'authenticationCodeTypeSms'
        AUTHENTICATION_CODE_TYPE_TELEGRAM_MESSAGE = 'authenticationCodeTypeTelegramMessage'
        AUTHORIZATION_STATE = 'authorizationState'
        AUTHORIZATION_STATE_CLOSED = 'authorizationStateClosed'
        AUTHORIZATION_STATE_CLOSING = 'authorizationStateClosing'
        AUTHORIZATION_STATE_LOGGING_OUT = 'authorizationStateLoggingOut'
        AUTHORIZATION_STATE_READY = 'authorizationStateReady'
        AUTHORIZATION_STATE_WAIT_CODE = 'authorizationStateWaitCode'
        AUTHORIZATION_STATE_WAIT_ENCRYPTION_KEY = 'authorizationStateWaitEncryptionKey'
        AUTHORIZATION_STATE_WAIT_OTHER_DEVICE_CONFIRMATION = 'authorizationStateWaitOtherDeviceConfirmation'
        AUTHORIZATION_STATE_WAIT_PASSWORD = 'authorizationStateWaitPassword'
        AUTHORIZATION_STATE_WAIT_PHONE_NUMBER = 'authorizationStateWaitPhoneNumber'
        AUTHORIZATION_STATE_WAIT_REGISTRATION = 'authorizationStateWaitRegistration'
        AUTHORIZATION_STATE_WAIT_TDLIB_PARAMETERS = 'authorizationStateWaitTdlibParameters'
        AUTO_DOWNLOAD_SETTINGS = 'autoDownloadSettings'
        AUTO_DOWNLOAD_SETTINGS_PRESETS = 'autoDownloadSettingsPresets'
        BACKGROUND = 'background'
        BACKGROUND_FILL = 'backgroundFill'
        BACKGROUND_FILL_GRADIENT = 'backgroundFillGradient'
        BACKGROUND_FILL_SOLID = 'backgroundFillSolid'
        BACKGROUND_TYPE = 'backgroundType'
        BACKGROUND_TYPE_FILL = 'backgroundTypeFill'
        BACKGROUND_TYPE_PATTERN = 'backgroundTypePattern'
        BACKGROUND_TYPE_WALLPAPER = 'backgroundTypeWallpaper'
        BACKGROUNDS = 'backgrounds'
        BAN_CHAT_MEMBER = 'banChatMember'
        BANK_CARD_ACTION_OPEN_URL = 'bankCardActionOpenUrl'
        BANK_CARD_INFO = 'bankCardInfo'
        BASIC_GROUP = 'basicGroup'
        BASIC_GROUP_FULL_INFO = 'basicGroupFullInfo'
        BLOCK_MESSAGE_SENDER_FROM_REPLIES = 'blockMessageSenderFromReplies'
        BOT_COMMAND = 'botCommand'
        BOT_INFO = 'botInfo'
        CALL = 'call'
        CALL_DISCARD_REASON = 'callDiscardReason'
        CALL_DISCARD_REASON_DECLINED = 'callDiscardReasonDeclined'
        CALL_DISCARD_REASON_DISCONNECTED = 'callDiscardReasonDisconnected'
        CALL_DISCARD_REASON_EMPTY = 'callDiscardReasonEmpty'
        CALL_DISCARD_REASON_HUNG_UP = 'callDiscardReasonHungUp'
        CALL_DISCARD_REASON_MISSED = 'callDiscardReasonMissed'
        CALL_ID = 'callId'
        CALL_PROBLEM = 'callProblem'
        CALL_PROBLEM_DISTORTED_SPEECH = 'callProblemDistortedSpeech'
        CALL_PROBLEM_DISTORTED_VIDEO = 'callProblemDistortedVideo'
        CALL_PROBLEM_DROPPED = 'callProblemDropped'
        CALL_PROBLEM_ECHO = 'callProblemEcho'
        CALL_PROBLEM_INTERRUPTIONS = 'callProblemInterruptions'
        CALL_PROBLEM_NOISE = 'callProblemNoise'
        CALL_PROBLEM_PIXELATED_VIDEO = 'callProblemPixelatedVideo'
        CALL_PROBLEM_SILENT_LOCAL = 'callProblemSilentLocal'
        CALL_PROBLEM_SILENT_REMOTE = 'callProblemSilentRemote'
        CALL_PROTOCOL = 'callProtocol'
        CALL_SERVER = 'callServer'
        CALL_SERVER_TYPE = 'callServerType'
        CALL_SERVER_TYPE_TELEGRAM_REFLECTOR = 'callServerTypeTelegramReflector'
        CALL_SERVER_TYPE_WEBRTC = 'callServerTypeWebrtc'
        CALL_STATE = 'callState'
        CALL_STATE_DISCARDED = 'callStateDiscarded'
        CALL_STATE_ERROR = 'callStateError'
        CALL_STATE_EXCHANGING_KEYS = 'callStateExchangingKeys'
        CALL_STATE_HANGING_UP = 'callStateHangingUp'
        CALL_STATE_PENDING = 'callStatePending'
        CALL_STATE_READY = 'callStateReady'
        CALLBACK_QUERY_ANSWER = 'callbackQueryAnswer'
        CALLBACK_QUERY_PAYLOAD = 'callbackQueryPayload'
        CALLBACK_QUERY_PAYLOAD_DATA = 'callbackQueryPayloadData'
        CALLBACK_QUERY_PAYLOAD_DATA_WITH_PASSWORD = 'callbackQueryPayloadDataWithPassword'
        CALLBACK_QUERY_PAYLOAD_GAME = 'callbackQueryPayloadGame'
        CAN_TRANSFER_OWNERSHIP = 'canTransferOwnership'
        CAN_TRANSFER_OWNERSHIP_RESULT = 'canTransferOwnershipResult'
        CAN_TRANSFER_OWNERSHIP_RESULT_OK = 'canTransferOwnershipResultOk'
        CAN_TRANSFER_OWNERSHIP_RESULT_PASSWORD_NEEDED = 'canTransferOwnershipResultPasswordNeeded'
        CAN_TRANSFER_OWNERSHIP_RESULT_PASSWORD_TOO_FRESH = 'canTransferOwnershipResultPasswordTooFresh'
        CAN_TRANSFER_OWNERSHIP_RESULT_SESSION_TOO_FRESH = 'canTransferOwnershipResultSessionTooFresh'
        CANCEL_DOWNLOAD_FILE = 'cancelDownloadFile'
        CANCEL_UPLOAD_FILE = 'cancelUploadFile'
        CHANGE_IMPORTED_CONTACTS = 'changeImportedContacts'
        CHANGE_PHONE_NUMBER = 'changePhoneNumber'
        CHANGE_STICKER_SET = 'changeStickerSet'
        CHAT = 'chat'
        CHAT_ACTION = 'chatAction'
        CHAT_ACTION_CANCEL = 'chatActionCancel'
        CHAT_ACTION_CHOOSING_CONTACT = 'chatActionChoosingContact'
        CHAT_ACTION_CHOOSING_LOCATION = 'chatActionChoosingLocation'
        CHAT_ACTION_RECORDING_VIDEO = 'chatActionRecordingVideo'
        CHAT_ACTION_RECORDING_VIDEO_NOTE = 'chatActionRecordingVideoNote'
        CHAT_ACTION_RECORDING_VOICE_NOTE = 'chatActionRecordingVoiceNote'
        CHAT_ACTION_START_PLAYING_GAME = 'chatActionStartPlayingGame'
        CHAT_ACTION_TYPING = 'chatActionTyping'
        CHAT_ACTION_UPLOADING_DOCUMENT = 'chatActionUploadingDocument'
        CHAT_ACTION_UPLOADING_PHOTO = 'chatActionUploadingPhoto'
        CHAT_ACTION_UPLOADING_VIDEO = 'chatActionUploadingVideo'
        CHAT_ACTION_UPLOADING_VIDEO_NOTE = 'chatActionUploadingVideoNote'
        CHAT_ACTION_UPLOADING_VOICE_NOTE = 'chatActionUploadingVoiceNote'
        CHAT_ACTION_BAR = 'chatActionBar'
        CHAT_ACTION_BAR_ADD_CONTACT = 'chatActionBarAddContact'
        CHAT_ACTION_BAR_INVITE_MEMBERS = 'chatActionBarInviteMembers'
        CHAT_ACTION_BAR_REPORT_ADD_BLOCK = 'chatActionBarReportAddBlock'
        CHAT_ACTION_BAR_REPORT_SPAM = 'chatActionBarReportSpam'
        CHAT_ACTION_BAR_REPORT_UNRELATED_LOCATION = 'chatActionBarReportUnrelatedLocation'
        CHAT_ACTION_BAR_SHARE_PHONE_NUMBER = 'chatActionBarSharePhoneNumber'
        CHAT_ADMINISTRATOR = 'chatAdministrator'
        CHAT_ADMINISTRATORS = 'chatAdministrators'
        CHAT_EVENT = 'chatEvent'
        CHAT_EVENT_ACTION = 'chatEventAction'
        CHAT_EVENT_DESCRIPTION_CHANGED = 'chatEventDescriptionChanged'
        CHAT_EVENT_INVITE_LINK_DELETED = 'chatEventInviteLinkDeleted'
        CHAT_EVENT_INVITE_LINK_EDITED = 'chatEventInviteLinkEdited'
        CHAT_EVENT_INVITE_LINK_REVOKED = 'chatEventInviteLinkRevoked'
        CHAT_EVENT_INVITES_TOGGLED = 'chatEventInvitesToggled'
        CHAT_EVENT_IS_ALL_HISTORY_AVAILABLE_TOGGLED = 'chatEventIsAllHistoryAvailableToggled'
        CHAT_EVENT_LINKED_CHAT_CHANGED = 'chatEventLinkedChatChanged'
        CHAT_EVENT_LOCATION_CHANGED = 'chatEventLocationChanged'
        CHAT_EVENT_MEMBER_INVITED = 'chatEventMemberInvited'
        CHAT_EVENT_MEMBER_JOINED = 'chatEventMemberJoined'
        CHAT_EVENT_MEMBER_JOINED_BY_INVITE_LINK = 'chatEventMemberJoinedByInviteLink'
        CHAT_EVENT_MEMBER_LEFT = 'chatEventMemberLeft'
        CHAT_EVENT_MEMBER_PROMOTED = 'chatEventMemberPromoted'
        CHAT_EVENT_MEMBER_RESTRICTED = 'chatEventMemberRestricted'
        CHAT_EVENT_MESSAGE_DELETED = 'chatEventMessageDeleted'
        CHAT_EVENT_MESSAGE_EDITED = 'chatEventMessageEdited'
        CHAT_EVENT_MESSAGE_PINNED = 'chatEventMessagePinned'
        CHAT_EVENT_MESSAGE_TTL_SETTING_CHANGED = 'chatEventMessageTtlSettingChanged'
        CHAT_EVENT_MESSAGE_UNPINNED = 'chatEventMessageUnpinned'
        CHAT_EVENT_PERMISSIONS_CHANGED = 'chatEventPermissionsChanged'
        CHAT_EVENT_PHOTO_CHANGED = 'chatEventPhotoChanged'
        CHAT_EVENT_POLL_STOPPED = 'chatEventPollStopped'
        CHAT_EVENT_SIGN_MESSAGES_TOGGLED = 'chatEventSignMessagesToggled'
        CHAT_EVENT_SLOW_MODE_DELAY_CHANGED = 'chatEventSlowModeDelayChanged'
        CHAT_EVENT_STICKER_SET_CHANGED = 'chatEventStickerSetChanged'
        CHAT_EVENT_TITLE_CHANGED = 'chatEventTitleChanged'
        CHAT_EVENT_USERNAME_CHANGED = 'chatEventUsernameChanged'
        CHAT_EVENT_VOICE_CHAT_CREATED = 'chatEventVoiceChatCreated'
        CHAT_EVENT_VOICE_CHAT_DISCARDED = 'chatEventVoiceChatDiscarded'
        CHAT_EVENT_VOICE_CHAT_MUTE_NEW_PARTICIPANTS_TOGGLED = 'chatEventVoiceChatMuteNewParticipantsToggled'
        CHAT_EVENT_VOICE_CHAT_PARTICIPANT_IS_MUTED_TOGGLED = 'chatEventVoiceChatParticipantIsMutedToggled'
        CHAT_EVENT_VOICE_CHAT_PARTICIPANT_VOLUME_LEVEL_CHANGED = 'chatEventVoiceChatParticipantVolumeLevelChanged'
        CHAT_EVENT_LOG_FILTERS = 'chatEventLogFilters'
        CHAT_EVENTS = 'chatEvents'
        CHAT_FILTER = 'chatFilter'
        CHAT_FILTER_INFO = 'chatFilterInfo'
        CHAT_INVITE_LINK = 'chatInviteLink'
        CHAT_INVITE_LINK_COUNT = 'chatInviteLinkCount'
        CHAT_INVITE_LINK_COUNTS = 'chatInviteLinkCounts'
        CHAT_INVITE_LINK_INFO = 'chatInviteLinkInfo'
        CHAT_INVITE_LINK_MEMBER = 'chatInviteLinkMember'
        CHAT_INVITE_LINK_MEMBERS = 'chatInviteLinkMembers'
        CHAT_INVITE_LINKS = 'chatInviteLinks'
        CHAT_LIST = 'chatList'
        CHAT_LIST_ARCHIVE = 'chatListArchive'
        CHAT_LIST_FILTER = 'chatListFilter'
        CHAT_LIST_MAIN = 'chatListMain'
        CHAT_LISTS = 'chatLists'
        CHAT_LOCATION = 'chatLocation'
        CHAT_MEMBER = 'chatMember'
        CHAT_MEMBER_STATUS = 'chatMemberStatus'
        CHAT_MEMBER_STATUS_ADMINISTRATOR = 'chatMemberStatusAdministrator'
        CHAT_MEMBER_STATUS_BANNED = 'chatMemberStatusBanned'
        CHAT_MEMBER_STATUS_CREATOR = 'chatMemberStatusCreator'
        CHAT_MEMBER_STATUS_LEFT = 'chatMemberStatusLeft'
        CHAT_MEMBER_STATUS_MEMBER = 'chatMemberStatusMember'
        CHAT_MEMBER_STATUS_RESTRICTED = 'chatMemberStatusRestricted'
        CHAT_MEMBERS = 'chatMembers'
        CHAT_MEMBERS_FILTER = 'chatMembersFilter'
        CHAT_MEMBERS_FILTER_ADMINISTRATORS = 'chatMembersFilterAdministrators'
        CHAT_MEMBERS_FILTER_BANNED = 'chatMembersFilterBanned'
        CHAT_MEMBERS_FILTER_BOTS = 'chatMembersFilterBots'
        CHAT_MEMBERS_FILTER_CONTACTS = 'chatMembersFilterContacts'
        CHAT_MEMBERS_FILTER_MEMBERS = 'chatMembersFilterMembers'
        CHAT_MEMBERS_FILTER_MENTION = 'chatMembersFilterMention'
        CHAT_MEMBERS_FILTER_RESTRICTED = 'chatMembersFilterRestricted'
        CHAT_NEARBY = 'chatNearby'
        CHAT_NOTIFICATION_SETTINGS = 'chatNotificationSettings'
        CHAT_PERMISSIONS = 'chatPermissions'
        CHAT_PHOTO = 'chatPhoto'
        CHAT_PHOTO_INFO = 'chatPhotoInfo'
        CHAT_PHOTOS = 'chatPhotos'
        CHAT_POSITION = 'chatPosition'
        CHAT_REPORT_REASON = 'chatReportReason'
        CHAT_REPORT_REASON_CHILD_ABUSE = 'chatReportReasonChildAbuse'
        CHAT_REPORT_REASON_COPYRIGHT = 'chatReportReasonCopyright'
        CHAT_REPORT_REASON_CUSTOM = 'chatReportReasonCustom'
        CHAT_REPORT_REASON_FAKE = 'chatReportReasonFake'
        CHAT_REPORT_REASON_PORNOGRAPHY = 'chatReportReasonPornography'
        CHAT_REPORT_REASON_SPAM = 'chatReportReasonSpam'
        CHAT_REPORT_REASON_UNRELATED_LOCATION = 'chatReportReasonUnrelatedLocation'
        CHAT_REPORT_REASON_VIOLENCE = 'chatReportReasonViolence'
        CHAT_SOURCE = 'chatSource'
        CHAT_SOURCE_MTPROTO_PROXY = 'chatSourceMtprotoProxy'
        CHAT_SOURCE_PUBLIC_SERVICE_ANNOUNCEMENT = 'chatSourcePublicServiceAnnouncement'
        CHAT_STATISTICS = 'chatStatistics'
        CHAT_STATISTICS_CHANNEL = 'chatStatisticsChannel'
        CHAT_STATISTICS_SUPERGROUP = 'chatStatisticsSupergroup'
        CHAT_STATISTICS_ADMINISTRATOR_ACTIONS_INFO = 'chatStatisticsAdministratorActionsInfo'
        CHAT_STATISTICS_INVITER_INFO = 'chatStatisticsInviterInfo'
        CHAT_STATISTICS_MESSAGE_INTERACTION_INFO = 'chatStatisticsMessageInteractionInfo'
        CHAT_STATISTICS_MESSAGE_SENDER_INFO = 'chatStatisticsMessageSenderInfo'
        CHAT_TYPE = 'chatType'
        CHAT_TYPE_BASIC_GROUP = 'chatTypeBasicGroup'
        CHAT_TYPE_PRIVATE = 'chatTypePrivate'
        CHAT_TYPE_SECRET = 'chatTypeSecret'
        CHAT_TYPE_SUPERGROUP = 'chatTypeSupergroup'
        CHATS = 'chats'
        CHATS_NEARBY = 'chatsNearby'
        CHECK_AUTHENTICATION_BOT_TOKEN = 'checkAuthenticationBotToken'
        CHECK_AUTHENTICATION_CODE = 'checkAuthenticationCode'
        CHECK_AUTHENTICATION_PASSWORD = 'checkAuthenticationPassword'
        CHECK_CHANGE_PHONE_NUMBER_CODE = 'checkChangePhoneNumberCode'
        CHECK_CHAT_INVITE_LINK = 'checkChatInviteLink'
        CHECK_CHAT_USERNAME = 'checkChatUsername'
        CHECK_CHAT_USERNAME_RESULT = 'checkChatUsernameResult'
        CHECK_CHAT_USERNAME_RESULT_OK = 'checkChatUsernameResultOk'
        CHECK_CHAT_USERNAME_RESULT_PUBLIC_CHATS_TOO_MUCH = 'checkChatUsernameResultPublicChatsTooMuch'
        CHECK_CHAT_USERNAME_RESULT_PUBLIC_GROUPS_UNAVAILABLE = 'checkChatUsernameResultPublicGroupsUnavailable'
        CHECK_CHAT_USERNAME_RESULT_USERNAME_INVALID = 'checkChatUsernameResultUsernameInvalid'
        CHECK_CHAT_USERNAME_RESULT_USERNAME_OCCUPIED = 'checkChatUsernameResultUsernameOccupied'
        CHECK_CREATED_PUBLIC_CHATS_LIMIT = 'checkCreatedPublicChatsLimit'
        CHECK_DATABASE_ENCRYPTION_KEY = 'checkDatabaseEncryptionKey'
        CHECK_EMAIL_ADDRESS_VERIFICATION_CODE = 'checkEmailAddressVerificationCode'
        CHECK_PHONE_NUMBER_CONFIRMATION_CODE = 'checkPhoneNumberConfirmationCode'
        CHECK_PHONE_NUMBER_VERIFICATION_CODE = 'checkPhoneNumberVerificationCode'
        CHECK_RECOVERY_EMAIL_ADDRESS_CODE = 'checkRecoveryEmailAddressCode'
        CLEAN_FILE_NAME = 'cleanFileName'
        CLEAR_ALL_DRAFT_MESSAGES = 'clearAllDraftMessages'
        CLEAR_IMPORTED_CONTACTS = 'clearImportedContacts'
        CLEAR_RECENT_STICKERS = 'clearRecentStickers'
        CLEAR_RECENTLY_FOUND_CHATS = 'clearRecentlyFoundChats'
        CLOSE = 'close'
        CLOSE_CHAT = 'closeChat'
        CLOSE_SECRET_CHAT = 'closeSecretChat'
        CLOSED_VECTOR_PATH = 'closedVectorPath'
        CONFIRM_QR_CODE_AUTHENTICATION = 'confirmQrCodeAuthentication'
        CONNECTED_WEBSITE = 'connectedWebsite'
        CONNECTED_WEBSITES = 'connectedWebsites'
        CONNECTION_STATE = 'connectionState'
        CONNECTION_STATE_CONNECTING = 'connectionStateConnecting'
        CONNECTION_STATE_CONNECTING_TO_PROXY = 'connectionStateConnectingToProxy'
        CONNECTION_STATE_READY = 'connectionStateReady'
        CONNECTION_STATE_UPDATING = 'connectionStateUpdating'
        CONNECTION_STATE_WAITING_FOR_NETWORK = 'connectionStateWaitingForNetwork'
        CONTACT = 'contact'
        COUNT = 'count'
        COUNTRIES = 'countries'
        COUNTRY_INFO = 'countryInfo'
        CREATE_BASIC_GROUP_CHAT = 'createBasicGroupChat'
        CREATE_CALL = 'createCall'
        CREATE_CHAT_FILTER = 'createChatFilter'
        CREATE_CHAT_INVITE_LINK = 'createChatInviteLink'
        CREATE_NEW_BASIC_GROUP_CHAT = 'createNewBasicGroupChat'
        CREATE_NEW_SECRET_CHAT = 'createNewSecretChat'
        CREATE_NEW_STICKER_SET = 'createNewStickerSet'
        CREATE_NEW_SUPERGROUP_CHAT = 'createNewSupergroupChat'
        CREATE_PRIVATE_CHAT = 'createPrivateChat'
        CREATE_SECRET_CHAT = 'createSecretChat'
        CREATE_SUPERGROUP_CHAT = 'createSupergroupChat'
        CREATE_TEMPORARY_PASSWORD = 'createTemporaryPassword'
        CREATE_VOICE_CHAT = 'createVoiceChat'
        CUSTOM_REQUEST_RESULT = 'customRequestResult'
        DATABASE_STATISTICS = 'databaseStatistics'
        DATE = 'date'
        DATE_RANGE = 'dateRange'
        DATED_FILE = 'datedFile'
        DEEP_LINK_INFO = 'deepLinkInfo'
        DELETE_ACCOUNT = 'deleteAccount'
        DELETE_ALL_CALL_MESSAGES = 'deleteAllCallMessages'
        DELETE_ALL_REVOKED_CHAT_INVITE_LINKS = 'deleteAllRevokedChatInviteLinks'
        DELETE_CHAT = 'deleteChat'
        DELETE_CHAT_FILTER = 'deleteChatFilter'
        DELETE_CHAT_HISTORY = 'deleteChatHistory'
        DELETE_CHAT_MESSAGES_FROM_USER = 'deleteChatMessagesFromUser'
        DELETE_CHAT_REPLY_MARKUP = 'deleteChatReplyMarkup'
        DELETE_FILE = 'deleteFile'
        DELETE_LANGUAGE_PACK = 'deleteLanguagePack'
        DELETE_MESSAGES = 'deleteMessages'
        DELETE_PASSPORT_ELEMENT = 'deletePassportElement'
        DELETE_PROFILE_PHOTO = 'deleteProfilePhoto'
        DELETE_REVOKED_CHAT_INVITE_LINK = 'deleteRevokedChatInviteLink'
        DELETE_SAVED_CREDENTIALS = 'deleteSavedCredentials'
        DELETE_SAVED_ORDER_INFO = 'deleteSavedOrderInfo'
        DESTROY = 'destroy'
        DEVICE_TOKEN = 'deviceToken'
        DEVICE_TOKEN_APPLE_PUSH = 'deviceTokenApplePush'
        DEVICE_TOKEN_APPLE_PUSH_VO_IP = 'deviceTokenApplePushVoIP'
        DEVICE_TOKEN_BLACK_BERRY_PUSH = 'deviceTokenBlackBerryPush'
        DEVICE_TOKEN_FIREBASE_CLOUD_MESSAGING = 'deviceTokenFirebaseCloudMessaging'
        DEVICE_TOKEN_MICROSOFT_PUSH = 'deviceTokenMicrosoftPush'
        DEVICE_TOKEN_MICROSOFT_PUSH_VO_IP = 'deviceTokenMicrosoftPushVoIP'
        DEVICE_TOKEN_SIMPLE_PUSH = 'deviceTokenSimplePush'
        DEVICE_TOKEN_TIZEN_PUSH = 'deviceTokenTizenPush'
        DEVICE_TOKEN_UBUNTU_PUSH = 'deviceTokenUbuntuPush'
        DEVICE_TOKEN_WEB_PUSH = 'deviceTokenWebPush'
        DEVICE_TOKEN_WINDOWS_PUSH = 'deviceTokenWindowsPush'
        DICE_STICKERS = 'diceStickers'
        DICE_STICKERS_REGULAR = 'diceStickersRegular'
        DICE_STICKERS_SLOT_MACHINE = 'diceStickersSlotMachine'
        DISABLE_PROXY = 'disableProxy'
        DISCARD_CALL = 'discardCall'
        DISCARD_GROUP_CALL = 'discardGroupCall'
        DISCONNECT_ALL_WEBSITES = 'disconnectAllWebsites'
        DISCONNECT_WEBSITE = 'disconnectWebsite'
        DOCUMENT = 'document'
        DOWNLOAD_FILE = 'downloadFile'
        DRAFT_MESSAGE = 'draftMessage'
        EDIT_CHAT_FILTER = 'editChatFilter'
        EDIT_CHAT_INVITE_LINK = 'editChatInviteLink'
        EDIT_CUSTOM_LANGUAGE_PACK_INFO = 'editCustomLanguagePackInfo'
        EDIT_INLINE_MESSAGE_CAPTION = 'editInlineMessageCaption'
        EDIT_INLINE_MESSAGE_LIVE_LOCATION = 'editInlineMessageLiveLocation'
        EDIT_INLINE_MESSAGE_MEDIA = 'editInlineMessageMedia'
        EDIT_INLINE_MESSAGE_REPLY_MARKUP = 'editInlineMessageReplyMarkup'
        EDIT_INLINE_MESSAGE_TEXT = 'editInlineMessageText'
        EDIT_MESSAGE_CAPTION = 'editMessageCaption'
        EDIT_MESSAGE_LIVE_LOCATION = 'editMessageLiveLocation'
        EDIT_MESSAGE_MEDIA = 'editMessageMedia'
        EDIT_MESSAGE_REPLY_MARKUP = 'editMessageReplyMarkup'
        EDIT_MESSAGE_SCHEDULING_STATE = 'editMessageSchedulingState'
        EDIT_MESSAGE_TEXT = 'editMessageText'
        EDIT_PROXY = 'editProxy'
        EMAIL_ADDRESS_AUTHENTICATION_CODE_INFO = 'emailAddressAuthenticationCodeInfo'
        EMOJIS = 'emojis'
        ENABLE_PROXY = 'enableProxy'
        ENCRYPTED_CREDENTIALS = 'encryptedCredentials'
        ENCRYPTED_PASSPORT_ELEMENT = 'encryptedPassportElement'
        END_GROUP_CALL_RECORDING = 'endGroupCallRecording'
        ERROR = 'error'
        FILE = 'file'
        FILE_PART = 'filePart'
        FILE_TYPE = 'fileType'
        FILE_TYPE_ANIMATION = 'fileTypeAnimation'
        FILE_TYPE_AUDIO = 'fileTypeAudio'
        FILE_TYPE_DOCUMENT = 'fileTypeDocument'
        FILE_TYPE_NONE = 'fileTypeNone'
        FILE_TYPE_PHOTO = 'fileTypePhoto'
        FILE_TYPE_PROFILE_PHOTO = 'fileTypeProfilePhoto'
        FILE_TYPE_SECRET = 'fileTypeSecret'
        FILE_TYPE_SECRET_THUMBNAIL = 'fileTypeSecretThumbnail'
        FILE_TYPE_SECURE = 'fileTypeSecure'
        FILE_TYPE_STICKER = 'fileTypeSticker'
        FILE_TYPE_THUMBNAIL = 'fileTypeThumbnail'
        FILE_TYPE_UNKNOWN = 'fileTypeUnknown'
        FILE_TYPE_VIDEO = 'fileTypeVideo'
        FILE_TYPE_VIDEO_NOTE = 'fileTypeVideoNote'
        FILE_TYPE_VOICE_NOTE = 'fileTypeVoiceNote'
        FILE_TYPE_WALLPAPER = 'fileTypeWallpaper'
        FINISH_FILE_GENERATION = 'finishFileGeneration'
        FORMATTED_TEXT = 'formattedText'
        FORWARD_MESSAGES = 'forwardMessages'
        FOUND_MESSAGES = 'foundMessages'
        GAME = 'game'
        GAME_HIGH_SCORE = 'gameHighScore'
        GAME_HIGH_SCORES = 'gameHighScores'
        GET_ACCOUNT_TTL = 'getAccountTtl'
        GET_ACTIVE_LIVE_LOCATION_MESSAGES = 'getActiveLiveLocationMessages'
        GET_ACTIVE_SESSIONS = 'getActiveSessions'
        GET_ALL_PASSPORT_ELEMENTS = 'getAllPassportElements'
        GET_APPLICATION_CONFIG = 'getApplicationConfig'
        GET_ARCHIVED_STICKER_SETS = 'getArchivedStickerSets'
        GET_ATTACHED_STICKER_SETS = 'getAttachedStickerSets'
        GET_AUTHORIZATION_STATE = 'getAuthorizationState'
        GET_AUTO_DOWNLOAD_SETTINGS_PRESETS = 'getAutoDownloadSettingsPresets'
        GET_AVAILABLE_VOICE_CHAT_ALIASES = 'getAvailableVoiceChatAliases'
        GET_BACKGROUND_URL = 'getBackgroundUrl'
        GET_BACKGROUNDS = 'getBackgrounds'
        GET_BANK_CARD_INFO = 'getBankCardInfo'
        GET_BASIC_GROUP = 'getBasicGroup'
        GET_BASIC_GROUP_FULL_INFO = 'getBasicGroupFullInfo'
        GET_BLOCKED_MESSAGE_SENDERS = 'getBlockedMessageSenders'
        GET_CALLBACK_QUERY_ANSWER = 'getCallbackQueryAnswer'
        GET_CALLBACK_QUERY_MESSAGE = 'getCallbackQueryMessage'
        GET_CHAT = 'getChat'
        GET_CHAT_ADMINISTRATORS = 'getChatAdministrators'
        GET_CHAT_EVENT_LOG = 'getChatEventLog'
        GET_CHAT_FILTER = 'getChatFilter'
        GET_CHAT_FILTER_DEFAULT_ICON_NAME = 'getChatFilterDefaultIconName'
        GET_CHAT_HISTORY = 'getChatHistory'
        GET_CHAT_INVITE_LINK = 'getChatInviteLink'
        GET_CHAT_INVITE_LINK_COUNTS = 'getChatInviteLinkCounts'
        GET_CHAT_INVITE_LINK_MEMBERS = 'getChatInviteLinkMembers'
        GET_CHAT_INVITE_LINKS = 'getChatInviteLinks'
        GET_CHAT_LISTS_TO_ADD_CHAT = 'getChatListsToAddChat'
        GET_CHAT_MEMBER = 'getChatMember'
        GET_CHAT_MESSAGE_BY_DATE = 'getChatMessageByDate'
        GET_CHAT_MESSAGE_COUNT = 'getChatMessageCount'
        GET_CHAT_NOTIFICATION_SETTINGS_EXCEPTIONS = 'getChatNotificationSettingsExceptions'
        GET_CHAT_PINNED_MESSAGE = 'getChatPinnedMessage'
        GET_CHAT_SCHEDULED_MESSAGES = 'getChatScheduledMessages'
        GET_CHAT_STATISTICS = 'getChatStatistics'
        GET_CHAT_STATISTICS_URL = 'getChatStatisticsUrl'
        GET_CHATS = 'getChats'
        GET_CONNECTED_WEBSITES = 'getConnectedWebsites'
        GET_CONTACTS = 'getContacts'
        GET_COUNTRIES = 'getCountries'
        GET_COUNTRY_CODE = 'getCountryCode'
        GET_CREATED_PUBLIC_CHATS = 'getCreatedPublicChats'
        GET_CURRENT_STATE = 'getCurrentState'
        GET_DATABASE_STATISTICS = 'getDatabaseStatistics'
        GET_DEEP_LINK_INFO = 'getDeepLinkInfo'
        GET_EMOJI_SUGGESTIONS_URL = 'getEmojiSuggestionsUrl'
        GET_EXTERNAL_LINK = 'getExternalLink'
        GET_EXTERNAL_LINK_INFO = 'getExternalLinkInfo'
        GET_FAVORITE_STICKERS = 'getFavoriteStickers'
        GET_FILE = 'getFile'
        GET_FILE_DOWNLOADED_PREFIX_SIZE = 'getFileDownloadedPrefixSize'
        GET_FILE_EXTENSION = 'getFileExtension'
        GET_FILE_MIME_TYPE = 'getFileMimeType'
        GET_GAME_HIGH_SCORES = 'getGameHighScores'
        GET_GROUP_CALL = 'getGroupCall'
        GET_GROUP_CALL_INVITE_LINK = 'getGroupCallInviteLink'
        GET_GROUP_CALL_STREAM_SEGMENT = 'getGroupCallStreamSegment'
        GET_GROUPS_IN_COMMON = 'getGroupsInCommon'
        GET_IMPORTED_CONTACT_COUNT = 'getImportedContactCount'
        GET_INACTIVE_SUPERGROUP_CHATS = 'getInactiveSupergroupChats'
        GET_INLINE_GAME_HIGH_SCORES = 'getInlineGameHighScores'
        GET_INLINE_QUERY_RESULTS = 'getInlineQueryResults'
        GET_INSTALLED_STICKER_SETS = 'getInstalledStickerSets'
        GET_INVITE_TEXT = 'getInviteText'
        GET_JSON_STRING = 'getJsonString'
        GET_JSON_VALUE = 'getJsonValue'
        GET_LANGUAGE_PACK_INFO = 'getLanguagePackInfo'
        GET_LANGUAGE_PACK_STRING = 'getLanguagePackString'
        GET_LANGUAGE_PACK_STRINGS = 'getLanguagePackStrings'
        GET_LOCALIZATION_TARGET_INFO = 'getLocalizationTargetInfo'
        GET_LOG_STREAM = 'getLogStream'
        GET_LOG_TAG_VERBOSITY_LEVEL = 'getLogTagVerbosityLevel'
        GET_LOG_TAGS = 'getLogTags'
        GET_LOG_VERBOSITY_LEVEL = 'getLogVerbosityLevel'
        GET_LOGIN_URL = 'getLoginUrl'
        GET_LOGIN_URL_INFO = 'getLoginUrlInfo'
        GET_MAP_THUMBNAIL_FILE = 'getMapThumbnailFile'
        GET_MARKDOWN_TEXT = 'getMarkdownText'
        GET_ME = 'getMe'
        GET_MESSAGE = 'getMessage'
        GET_MESSAGE_EMBEDDING_CODE = 'getMessageEmbeddingCode'
        GET_MESSAGE_FILE_TYPE = 'getMessageFileType'
        GET_MESSAGE_IMPORT_CONFIRMATION_TEXT = 'getMessageImportConfirmationText'
        GET_MESSAGE_LINK = 'getMessageLink'
        GET_MESSAGE_LINK_INFO = 'getMessageLinkInfo'
        GET_MESSAGE_LOCALLY = 'getMessageLocally'
        GET_MESSAGE_PUBLIC_FORWARDS = 'getMessagePublicForwards'
        GET_MESSAGE_STATISTICS = 'getMessageStatistics'
        GET_MESSAGE_THREAD = 'getMessageThread'
        GET_MESSAGE_THREAD_HISTORY = 'getMessageThreadHistory'
        GET_MESSAGES = 'getMessages'
        GET_NETWORK_STATISTICS = 'getNetworkStatistics'
        GET_OPTION = 'getOption'
        GET_PASSPORT_AUTHORIZATION_FORM = 'getPassportAuthorizationForm'
        GET_PASSPORT_AUTHORIZATION_FORM_AVAILABLE_ELEMENTS = 'getPassportAuthorizationFormAvailableElements'
        GET_PASSPORT_ELEMENT = 'getPassportElement'
        GET_PASSWORD_STATE = 'getPasswordState'
        GET_PAYMENT_FORM = 'getPaymentForm'
        GET_PAYMENT_RECEIPT = 'getPaymentReceipt'
        GET_PHONE_NUMBER_INFO = 'getPhoneNumberInfo'
        GET_POLL_VOTERS = 'getPollVoters'
        GET_PREFERRED_COUNTRY_LANGUAGE = 'getPreferredCountryLanguage'
        GET_PROXIES = 'getProxies'
        GET_PROXY_LINK = 'getProxyLink'
        GET_PUSH_RECEIVER_ID = 'getPushReceiverId'
        GET_RECENT_INLINE_BOTS = 'getRecentInlineBots'
        GET_RECENT_STICKERS = 'getRecentStickers'
        GET_RECENTLY_VISITED_T_ME_URLS = 'getRecentlyVisitedTMeUrls'
        GET_RECOMMENDED_CHAT_FILTERS = 'getRecommendedChatFilters'
        GET_RECOVERY_EMAIL_ADDRESS = 'getRecoveryEmailAddress'
        GET_REMOTE_FILE = 'getRemoteFile'
        GET_REPLIED_MESSAGE = 'getRepliedMessage'
        GET_SAVED_ANIMATIONS = 'getSavedAnimations'
        GET_SAVED_ORDER_INFO = 'getSavedOrderInfo'
        GET_SCOPE_NOTIFICATION_SETTINGS = 'getScopeNotificationSettings'
        GET_SECRET_CHAT = 'getSecretChat'
        GET_STATISTICAL_GRAPH = 'getStatisticalGraph'
        GET_STICKER_EMOJIS = 'getStickerEmojis'
        GET_STICKER_SET = 'getStickerSet'
        GET_STICKERS = 'getStickers'
        GET_STORAGE_STATISTICS = 'getStorageStatistics'
        GET_STORAGE_STATISTICS_FAST = 'getStorageStatisticsFast'
        GET_SUITABLE_DISCUSSION_CHATS = 'getSuitableDiscussionChats'
        GET_SUPERGROUP = 'getSupergroup'
        GET_SUPERGROUP_FULL_INFO = 'getSupergroupFullInfo'
        GET_SUPERGROUP_MEMBERS = 'getSupergroupMembers'
        GET_SUPPORT_USER = 'getSupportUser'
        GET_TEMPORARY_PASSWORD_STATE = 'getTemporaryPasswordState'
        GET_TEXT_ENTITIES = 'getTextEntities'
        GET_TOP_CHATS = 'getTopChats'
        GET_TRENDING_STICKER_SETS = 'getTrendingStickerSets'
        GET_USER = 'getUser'
        GET_USER_FULL_INFO = 'getUserFullInfo'
        GET_USER_PRIVACY_SETTING_RULES = 'getUserPrivacySettingRules'
        GET_USER_PROFILE_PHOTOS = 'getUserProfilePhotos'
        GET_WEB_PAGE_INSTANT_VIEW = 'getWebPageInstantView'
        GET_WEB_PAGE_PREVIEW = 'getWebPagePreview'
        GROUP_CALL = 'groupCall'
        GROUP_CALL_ID = 'groupCallId'
        GROUP_CALL_JOIN_RESPONSE = 'groupCallJoinResponse'
        GROUP_CALL_JOIN_RESPONSE_STREAM = 'groupCallJoinResponseStream'
        GROUP_CALL_JOIN_RESPONSE_WEBRTC = 'groupCallJoinResponseWebrtc'
        GROUP_CALL_JOIN_RESPONSE_CANDIDATE = 'groupCallJoinResponseCandidate'
        GROUP_CALL_PARTICIPANT = 'groupCallParticipant'
        GROUP_CALL_PAYLOAD = 'groupCallPayload'
        GROUP_CALL_PAYLOAD_FINGERPRINT = 'groupCallPayloadFingerprint'
        GROUP_CALL_RECENT_SPEAKER = 'groupCallRecentSpeaker'
        HASHTAGS = 'hashtags'
        HIDE_SUGGESTED_ACTION = 'hideSuggestedAction'
        HTTP_URL = 'httpUrl'
        IDENTITY_DOCUMENT = 'identityDocument'
        IMPORT_CONTACTS = 'importContacts'
        IMPORT_MESSAGES = 'importMessages'
        IMPORTED_CONTACTS = 'importedContacts'
        INLINE_KEYBOARD_BUTTON = 'inlineKeyboardButton'
        INLINE_KEYBOARD_BUTTON_TYPE = 'inlineKeyboardButtonType'
        INLINE_KEYBOARD_BUTTON_TYPE_BUY = 'inlineKeyboardButtonTypeBuy'
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK = 'inlineKeyboardButtonTypeCallback'
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK_GAME = 'inlineKeyboardButtonTypeCallbackGame'
        INLINE_KEYBOARD_BUTTON_TYPE_CALLBACK_WITH_PASSWORD = 'inlineKeyboardButtonTypeCallbackWithPassword'
        INLINE_KEYBOARD_BUTTON_TYPE_LOGIN_URL = 'inlineKeyboardButtonTypeLoginUrl'
        INLINE_KEYBOARD_BUTTON_TYPE_SWITCH_INLINE = 'inlineKeyboardButtonTypeSwitchInline'
        INLINE_KEYBOARD_BUTTON_TYPE_URL = 'inlineKeyboardButtonTypeUrl'
        INLINE_QUERY_RESULT = 'inlineQueryResult'
        INLINE_QUERY_RESULT_ANIMATION = 'inlineQueryResultAnimation'
        INLINE_QUERY_RESULT_ARTICLE = 'inlineQueryResultArticle'
        INLINE_QUERY_RESULT_AUDIO = 'inlineQueryResultAudio'
        INLINE_QUERY_RESULT_CONTACT = 'inlineQueryResultContact'
        INLINE_QUERY_RESULT_DOCUMENT = 'inlineQueryResultDocument'
        INLINE_QUERY_RESULT_GAME = 'inlineQueryResultGame'
        INLINE_QUERY_RESULT_LOCATION = 'inlineQueryResultLocation'
        INLINE_QUERY_RESULT_PHOTO = 'inlineQueryResultPhoto'
        INLINE_QUERY_RESULT_STICKER = 'inlineQueryResultSticker'
        INLINE_QUERY_RESULT_VENUE = 'inlineQueryResultVenue'
        INLINE_QUERY_RESULT_VIDEO = 'inlineQueryResultVideo'
        INLINE_QUERY_RESULT_VOICE_NOTE = 'inlineQueryResultVoiceNote'
        INLINE_QUERY_RESULTS = 'inlineQueryResults'
        INPUT_BACKGROUND = 'inputBackground'
        INPUT_BACKGROUND_LOCAL = 'inputBackgroundLocal'
        INPUT_BACKGROUND_REMOTE = 'inputBackgroundRemote'
        INPUT_CHAT_PHOTO = 'inputChatPhoto'
        INPUT_CHAT_PHOTO_ANIMATION = 'inputChatPhotoAnimation'
        INPUT_CHAT_PHOTO_PREVIOUS = 'inputChatPhotoPrevious'
        INPUT_CHAT_PHOTO_STATIC = 'inputChatPhotoStatic'
        INPUT_CREDENTIALS = 'inputCredentials'
        INPUT_CREDENTIALS_APPLE_PAY = 'inputCredentialsApplePay'
        INPUT_CREDENTIALS_GOOGLE_PAY = 'inputCredentialsGooglePay'
        INPUT_CREDENTIALS_NEW = 'inputCredentialsNew'
        INPUT_CREDENTIALS_SAVED = 'inputCredentialsSaved'
        INPUT_FILE = 'inputFile'
        INPUT_FILE_GENERATED = 'inputFileGenerated'
        INPUT_FILE_ID = 'inputFileId'
        INPUT_FILE_LOCAL = 'inputFileLocal'
        INPUT_FILE_REMOTE = 'inputFileRemote'
        INPUT_IDENTITY_DOCUMENT = 'inputIdentityDocument'
        INPUT_INLINE_QUERY_RESULT = 'inputInlineQueryResult'
        INPUT_INLINE_QUERY_RESULT_ANIMATION = 'inputInlineQueryResultAnimation'
        INPUT_INLINE_QUERY_RESULT_ARTICLE = 'inputInlineQueryResultArticle'
        INPUT_INLINE_QUERY_RESULT_AUDIO = 'inputInlineQueryResultAudio'
        INPUT_INLINE_QUERY_RESULT_CONTACT = 'inputInlineQueryResultContact'
        INPUT_INLINE_QUERY_RESULT_DOCUMENT = 'inputInlineQueryResultDocument'
        INPUT_INLINE_QUERY_RESULT_GAME = 'inputInlineQueryResultGame'
        INPUT_INLINE_QUERY_RESULT_LOCATION = 'inputInlineQueryResultLocation'
        INPUT_INLINE_QUERY_RESULT_PHOTO = 'inputInlineQueryResultPhoto'
        INPUT_INLINE_QUERY_RESULT_STICKER = 'inputInlineQueryResultSticker'
        INPUT_INLINE_QUERY_RESULT_VENUE = 'inputInlineQueryResultVenue'
        INPUT_INLINE_QUERY_RESULT_VIDEO = 'inputInlineQueryResultVideo'
        INPUT_INLINE_QUERY_RESULT_VOICE_NOTE = 'inputInlineQueryResultVoiceNote'
        INPUT_MESSAGE_CONTENT = 'inputMessageContent'
        INPUT_MESSAGE_ANIMATION = 'inputMessageAnimation'
        INPUT_MESSAGE_AUDIO = 'inputMessageAudio'
        INPUT_MESSAGE_CONTACT = 'inputMessageContact'
        INPUT_MESSAGE_DICE = 'inputMessageDice'
        INPUT_MESSAGE_DOCUMENT = 'inputMessageDocument'
        INPUT_MESSAGE_FORWARDED = 'inputMessageForwarded'
        INPUT_MESSAGE_GAME = 'inputMessageGame'
        INPUT_MESSAGE_INVOICE = 'inputMessageInvoice'
        INPUT_MESSAGE_LOCATION = 'inputMessageLocation'
        INPUT_MESSAGE_PHOTO = 'inputMessagePhoto'
        INPUT_MESSAGE_POLL = 'inputMessagePoll'
        INPUT_MESSAGE_STICKER = 'inputMessageSticker'
        INPUT_MESSAGE_TEXT = 'inputMessageText'
        INPUT_MESSAGE_VENUE = 'inputMessageVenue'
        INPUT_MESSAGE_VIDEO = 'inputMessageVideo'
        INPUT_MESSAGE_VIDEO_NOTE = 'inputMessageVideoNote'
        INPUT_MESSAGE_VOICE_NOTE = 'inputMessageVoiceNote'
        INPUT_PASSPORT_ELEMENT = 'inputPassportElement'
        INPUT_PASSPORT_ELEMENT_ADDRESS = 'inputPassportElementAddress'
        INPUT_PASSPORT_ELEMENT_BANK_STATEMENT = 'inputPassportElementBankStatement'
        INPUT_PASSPORT_ELEMENT_DRIVER_LICENSE = 'inputPassportElementDriverLicense'
        INPUT_PASSPORT_ELEMENT_EMAIL_ADDRESS = 'inputPassportElementEmailAddress'
        INPUT_PASSPORT_ELEMENT_IDENTITY_CARD = 'inputPassportElementIdentityCard'
        INPUT_PASSPORT_ELEMENT_INTERNAL_PASSPORT = 'inputPassportElementInternalPassport'
        INPUT_PASSPORT_ELEMENT_PASSPORT = 'inputPassportElementPassport'
        INPUT_PASSPORT_ELEMENT_PASSPORT_REGISTRATION = 'inputPassportElementPassportRegistration'
        INPUT_PASSPORT_ELEMENT_PERSONAL_DETAILS = 'inputPassportElementPersonalDetails'
        INPUT_PASSPORT_ELEMENT_PHONE_NUMBER = 'inputPassportElementPhoneNumber'
        INPUT_PASSPORT_ELEMENT_RENTAL_AGREEMENT = 'inputPassportElementRentalAgreement'
        INPUT_PASSPORT_ELEMENT_TEMPORARY_REGISTRATION = 'inputPassportElementTemporaryRegistration'
        INPUT_PASSPORT_ELEMENT_UTILITY_BILL = 'inputPassportElementUtilityBill'
        INPUT_PASSPORT_ELEMENT_ERROR = 'inputPassportElementError'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE = 'inputPassportElementErrorSource'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_DATA_FIELD = 'inputPassportElementErrorSourceDataField'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FILE = 'inputPassportElementErrorSourceFile'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FILES = 'inputPassportElementErrorSourceFiles'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_FRONT_SIDE = 'inputPassportElementErrorSourceFrontSide'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_REVERSE_SIDE = 'inputPassportElementErrorSourceReverseSide'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_SELFIE = 'inputPassportElementErrorSourceSelfie'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILE = 'inputPassportElementErrorSourceTranslationFile'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILES = 'inputPassportElementErrorSourceTranslationFiles'
        INPUT_PASSPORT_ELEMENT_ERROR_SOURCE_UNSPECIFIED = 'inputPassportElementErrorSourceUnspecified'
        INPUT_PERSONAL_DOCUMENT = 'inputPersonalDocument'
        INPUT_STICKER = 'inputSticker'
        INPUT_STICKER_ANIMATED = 'inputStickerAnimated'
        INPUT_STICKER_STATIC = 'inputStickerStatic'
        INPUT_THUMBNAIL = 'inputThumbnail'
        INVITE_GROUP_CALL_PARTICIPANTS = 'inviteGroupCallParticipants'
        INVOICE = 'invoice'
        JOIN_CHAT = 'joinChat'
        JOIN_CHAT_BY_INVITE_LINK = 'joinChatByInviteLink'
        JOIN_GROUP_CALL = 'joinGroupCall'
        JSON_VALUE = 'jsonValue'
        JSON_VALUE_ARRAY = 'jsonValueArray'
        JSON_VALUE_BOOLEAN = 'jsonValueBoolean'
        JSON_VALUE_NULL = 'jsonValueNull'
        JSON_VALUE_NUMBER = 'jsonValueNumber'
        JSON_VALUE_OBJECT = 'jsonValueObject'
        JSON_VALUE_STRING = 'jsonValueString'
        KEYBOARD_BUTTON = 'keyboardButton'
        KEYBOARD_BUTTON_TYPE = 'keyboardButtonType'
        KEYBOARD_BUTTON_TYPE_REQUEST_LOCATION = 'keyboardButtonTypeRequestLocation'
        KEYBOARD_BUTTON_TYPE_REQUEST_PHONE_NUMBER = 'keyboardButtonTypeRequestPhoneNumber'
        KEYBOARD_BUTTON_TYPE_REQUEST_POLL = 'keyboardButtonTypeRequestPoll'
        KEYBOARD_BUTTON_TYPE_TEXT = 'keyboardButtonTypeText'
        LABELED_PRICE_PART = 'labeledPricePart'
        LANGUAGE_PACK_INFO = 'languagePackInfo'
        LANGUAGE_PACK_STRING = 'languagePackString'
        LANGUAGE_PACK_STRING_VALUE = 'languagePackStringValue'
        LANGUAGE_PACK_STRING_VALUE_DELETED = 'languagePackStringValueDeleted'
        LANGUAGE_PACK_STRING_VALUE_ORDINARY = 'languagePackStringValueOrdinary'
        LANGUAGE_PACK_STRING_VALUE_PLURALIZED = 'languagePackStringValuePluralized'
        LANGUAGE_PACK_STRINGS = 'languagePackStrings'
        LEAVE_CHAT = 'leaveChat'
        LEAVE_GROUP_CALL = 'leaveGroupCall'
        LOAD_GROUP_CALL_PARTICIPANTS = 'loadGroupCallParticipants'
        LOCAL_FILE = 'localFile'
        LOCALIZATION_TARGET_INFO = 'localizationTargetInfo'
        LOCATION = 'location'
        LOG_OUT = 'logOut'
        LOG_STREAM = 'logStream'
        LOG_STREAM_DEFAULT = 'logStreamDefault'
        LOG_STREAM_EMPTY = 'logStreamEmpty'
        LOG_STREAM_FILE = 'logStreamFile'
        LOG_TAGS = 'logTags'
        LOG_VERBOSITY_LEVEL = 'logVerbosityLevel'
        LOGIN_URL_INFO = 'loginUrlInfo'
        LOGIN_URL_INFO_OPEN = 'loginUrlInfoOpen'
        LOGIN_URL_INFO_REQUEST_CONFIRMATION = 'loginUrlInfoRequestConfirmation'
        MASK_POINT = 'maskPoint'
        MASK_POINT_CHIN = 'maskPointChin'
        MASK_POINT_EYES = 'maskPointEyes'
        MASK_POINT_FOREHEAD = 'maskPointForehead'
        MASK_POINT_MOUTH = 'maskPointMouth'
        MASK_POSITION = 'maskPosition'
        MESSAGE = 'message'
        MESSAGE_CONTENT = 'messageContent'
        MESSAGE_ANIMATION = 'messageAnimation'
        MESSAGE_AUDIO = 'messageAudio'
        MESSAGE_BASIC_GROUP_CHAT_CREATE = 'messageBasicGroupChatCreate'
        MESSAGE_CALL = 'messageCall'
        MESSAGE_CHAT_ADD_MEMBERS = 'messageChatAddMembers'
        MESSAGE_CHAT_CHANGE_PHOTO = 'messageChatChangePhoto'
        MESSAGE_CHAT_CHANGE_TITLE = 'messageChatChangeTitle'
        MESSAGE_CHAT_DELETE_MEMBER = 'messageChatDeleteMember'
        MESSAGE_CHAT_DELETE_PHOTO = 'messageChatDeletePhoto'
        MESSAGE_CHAT_JOIN_BY_LINK = 'messageChatJoinByLink'
        MESSAGE_CHAT_SET_TTL = 'messageChatSetTtl'
        MESSAGE_CHAT_UPGRADE_FROM = 'messageChatUpgradeFrom'
        MESSAGE_CHAT_UPGRADE_TO = 'messageChatUpgradeTo'
        MESSAGE_CONTACT = 'messageContact'
        MESSAGE_CONTACT_REGISTERED = 'messageContactRegistered'
        MESSAGE_CUSTOM_SERVICE_ACTION = 'messageCustomServiceAction'
        MESSAGE_DICE = 'messageDice'
        MESSAGE_DOCUMENT = 'messageDocument'
        MESSAGE_EXPIRED_PHOTO = 'messageExpiredPhoto'
        MESSAGE_EXPIRED_VIDEO = 'messageExpiredVideo'
        MESSAGE_GAME = 'messageGame'
        MESSAGE_GAME_SCORE = 'messageGameScore'
        MESSAGE_INVITE_VOICE_CHAT_PARTICIPANTS = 'messageInviteVoiceChatParticipants'
        MESSAGE_INVOICE = 'messageInvoice'
        MESSAGE_LOCATION = 'messageLocation'
        MESSAGE_PASSPORT_DATA_RECEIVED = 'messagePassportDataReceived'
        MESSAGE_PASSPORT_DATA_SENT = 'messagePassportDataSent'
        MESSAGE_PAYMENT_SUCCESSFUL = 'messagePaymentSuccessful'
        MESSAGE_PAYMENT_SUCCESSFUL_BOT = 'messagePaymentSuccessfulBot'
        MESSAGE_PHOTO = 'messagePhoto'
        MESSAGE_PIN_MESSAGE = 'messagePinMessage'
        MESSAGE_POLL = 'messagePoll'
        MESSAGE_PROXIMITY_ALERT_TRIGGERED = 'messageProximityAlertTriggered'
        MESSAGE_SCREENSHOT_TAKEN = 'messageScreenshotTaken'
        MESSAGE_STICKER = 'messageSticker'
        MESSAGE_SUPERGROUP_CHAT_CREATE = 'messageSupergroupChatCreate'
        MESSAGE_TEXT = 'messageText'
        MESSAGE_UNSUPPORTED = 'messageUnsupported'
        MESSAGE_VENUE = 'messageVenue'
        MESSAGE_VIDEO = 'messageVideo'
        MESSAGE_VIDEO_NOTE = 'messageVideoNote'
        MESSAGE_VOICE_CHAT_ENDED = 'messageVoiceChatEnded'
        MESSAGE_VOICE_CHAT_STARTED = 'messageVoiceChatStarted'
        MESSAGE_VOICE_NOTE = 'messageVoiceNote'
        MESSAGE_WEBSITE_CONNECTED = 'messageWebsiteConnected'
        MESSAGE_COPY_OPTIONS = 'messageCopyOptions'
        MESSAGE_FILE_TYPE = 'messageFileType'
        MESSAGE_FILE_TYPE_GROUP = 'messageFileTypeGroup'
        MESSAGE_FILE_TYPE_PRIVATE = 'messageFileTypePrivate'
        MESSAGE_FILE_TYPE_UNKNOWN = 'messageFileTypeUnknown'
        MESSAGE_FORWARD_INFO = 'messageForwardInfo'
        MESSAGE_FORWARD_ORIGIN = 'messageForwardOrigin'
        MESSAGE_FORWARD_ORIGIN_CHANNEL = 'messageForwardOriginChannel'
        MESSAGE_FORWARD_ORIGIN_CHAT = 'messageForwardOriginChat'
        MESSAGE_FORWARD_ORIGIN_HIDDEN_USER = 'messageForwardOriginHiddenUser'
        MESSAGE_FORWARD_ORIGIN_MESSAGE_IMPORT = 'messageForwardOriginMessageImport'
        MESSAGE_FORWARD_ORIGIN_USER = 'messageForwardOriginUser'
        MESSAGE_INTERACTION_INFO = 'messageInteractionInfo'
        MESSAGE_LINK = 'messageLink'
        MESSAGE_LINK_INFO = 'messageLinkInfo'
        MESSAGE_REPLY_INFO = 'messageReplyInfo'
        MESSAGE_SCHEDULING_STATE = 'messageSchedulingState'
        MESSAGE_SCHEDULING_STATE_SEND_AT_DATE = 'messageSchedulingStateSendAtDate'
        MESSAGE_SCHEDULING_STATE_SEND_WHEN_ONLINE = 'messageSchedulingStateSendWhenOnline'
        MESSAGE_SEND_OPTIONS = 'messageSendOptions'
        MESSAGE_SENDER = 'messageSender'
        MESSAGE_SENDER_CHAT = 'messageSenderChat'
        MESSAGE_SENDER_USER = 'messageSenderUser'
        MESSAGE_SENDERS = 'messageSenders'
        MESSAGE_SENDING_STATE = 'messageSendingState'
        MESSAGE_SENDING_STATE_FAILED = 'messageSendingStateFailed'
        MESSAGE_SENDING_STATE_PENDING = 'messageSendingStatePending'
        MESSAGE_STATISTICS = 'messageStatistics'
        MESSAGE_THREAD_INFO = 'messageThreadInfo'
        MESSAGES = 'messages'
        MINITHUMBNAIL = 'minithumbnail'
        NETWORK_STATISTICS = 'networkStatistics'
        NETWORK_STATISTICS_ENTRY = 'networkStatisticsEntry'
        NETWORK_STATISTICS_ENTRY_CALL = 'networkStatisticsEntryCall'
        NETWORK_STATISTICS_ENTRY_FILE = 'networkStatisticsEntryFile'
        NETWORK_TYPE = 'networkType'
        NETWORK_TYPE_MOBILE = 'networkTypeMobile'
        NETWORK_TYPE_MOBILE_ROAMING = 'networkTypeMobileRoaming'
        NETWORK_TYPE_NONE = 'networkTypeNone'
        NETWORK_TYPE_OTHER = 'networkTypeOther'
        NETWORK_TYPE_WI_FI = 'networkTypeWiFi'
        NOTIFICATION = 'notification'
        NOTIFICATION_GROUP = 'notificationGroup'
        NOTIFICATION_GROUP_TYPE = 'notificationGroupType'
        NOTIFICATION_GROUP_TYPE_CALLS = 'notificationGroupTypeCalls'
        NOTIFICATION_GROUP_TYPE_MENTIONS = 'notificationGroupTypeMentions'
        NOTIFICATION_GROUP_TYPE_MESSAGES = 'notificationGroupTypeMessages'
        NOTIFICATION_GROUP_TYPE_SECRET_CHAT = 'notificationGroupTypeSecretChat'
        NOTIFICATION_SETTINGS_SCOPE = 'notificationSettingsScope'
        NOTIFICATION_SETTINGS_SCOPE_CHANNEL_CHATS = 'notificationSettingsScopeChannelChats'
        NOTIFICATION_SETTINGS_SCOPE_GROUP_CHATS = 'notificationSettingsScopeGroupChats'
        NOTIFICATION_SETTINGS_SCOPE_PRIVATE_CHATS = 'notificationSettingsScopePrivateChats'
        NOTIFICATION_TYPE = 'notificationType'
        NOTIFICATION_TYPE_NEW_CALL = 'notificationTypeNewCall'
        NOTIFICATION_TYPE_NEW_MESSAGE = 'notificationTypeNewMessage'
        NOTIFICATION_TYPE_NEW_PUSH_MESSAGE = 'notificationTypeNewPushMessage'
        NOTIFICATION_TYPE_NEW_SECRET_CHAT = 'notificationTypeNewSecretChat'
        OK = 'ok'
        OPEN_CHAT = 'openChat'
        OPEN_MESSAGE_CONTENT = 'openMessageContent'
        OPTIMIZE_STORAGE = 'optimizeStorage'
        OPTION_VALUE = 'optionValue'
        OPTION_VALUE_BOOLEAN = 'optionValueBoolean'
        OPTION_VALUE_EMPTY = 'optionValueEmpty'
        OPTION_VALUE_INTEGER = 'optionValueInteger'
        OPTION_VALUE_STRING = 'optionValueString'
        ORDER_INFO = 'orderInfo'
        PAGE_BLOCK = 'pageBlock'
        PAGE_BLOCK_ANCHOR = 'pageBlockAnchor'
        PAGE_BLOCK_ANIMATION = 'pageBlockAnimation'
        PAGE_BLOCK_AUDIO = 'pageBlockAudio'
        PAGE_BLOCK_AUTHOR_DATE = 'pageBlockAuthorDate'
        PAGE_BLOCK_BLOCK_QUOTE = 'pageBlockBlockQuote'
        PAGE_BLOCK_CHAT_LINK = 'pageBlockChatLink'
        PAGE_BLOCK_COLLAGE = 'pageBlockCollage'
        PAGE_BLOCK_COVER = 'pageBlockCover'
        PAGE_BLOCK_DETAILS = 'pageBlockDetails'
        PAGE_BLOCK_DIVIDER = 'pageBlockDivider'
        PAGE_BLOCK_EMBEDDED = 'pageBlockEmbedded'
        PAGE_BLOCK_EMBEDDED_POST = 'pageBlockEmbeddedPost'
        PAGE_BLOCK_FOOTER = 'pageBlockFooter'
        PAGE_BLOCK_HEADER = 'pageBlockHeader'
        PAGE_BLOCK_KICKER = 'pageBlockKicker'
        PAGE_BLOCK_LIST = 'pageBlockList'
        PAGE_BLOCK_MAP = 'pageBlockMap'
        PAGE_BLOCK_PARAGRAPH = 'pageBlockParagraph'
        PAGE_BLOCK_PHOTO = 'pageBlockPhoto'
        PAGE_BLOCK_PREFORMATTED = 'pageBlockPreformatted'
        PAGE_BLOCK_PULL_QUOTE = 'pageBlockPullQuote'
        PAGE_BLOCK_RELATED_ARTICLES = 'pageBlockRelatedArticles'
        PAGE_BLOCK_SLIDESHOW = 'pageBlockSlideshow'
        PAGE_BLOCK_SUBHEADER = 'pageBlockSubheader'
        PAGE_BLOCK_SUBTITLE = 'pageBlockSubtitle'
        PAGE_BLOCK_TABLE = 'pageBlockTable'
        PAGE_BLOCK_TITLE = 'pageBlockTitle'
        PAGE_BLOCK_VIDEO = 'pageBlockVideo'
        PAGE_BLOCK_VOICE_NOTE = 'pageBlockVoiceNote'
        PAGE_BLOCK_CAPTION = 'pageBlockCaption'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT = 'pageBlockHorizontalAlignment'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_CENTER = 'pageBlockHorizontalAlignmentCenter'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_LEFT = 'pageBlockHorizontalAlignmentLeft'
        PAGE_BLOCK_HORIZONTAL_ALIGNMENT_RIGHT = 'pageBlockHorizontalAlignmentRight'
        PAGE_BLOCK_RELATED_ARTICLE = 'pageBlockRelatedArticle'
        PAGE_BLOCK_TABLE_CELL = 'pageBlockTableCell'
        PAGE_BLOCK_VERTICAL_ALIGNMENT = 'pageBlockVerticalAlignment'
        PAGE_BLOCK_VERTICAL_ALIGNMENT_BOTTOM = 'pageBlockVerticalAlignmentBottom'
        PAGE_BLOCK_VERTICAL_ALIGNMENT_MIDDLE = 'pageBlockVerticalAlignmentMiddle'
        PAGE_BLOCK_VERTICAL_ALIGNMENT_TOP = 'pageBlockVerticalAlignmentTop'
        PARSE_MARKDOWN = 'parseMarkdown'
        PARSE_TEXT_ENTITIES = 'parseTextEntities'
        PASSPORT_AUTHORIZATION_FORM = 'passportAuthorizationForm'
        PASSPORT_ELEMENT = 'passportElement'
        PASSPORT_ELEMENT_ADDRESS = 'passportElementAddress'
        PASSPORT_ELEMENT_BANK_STATEMENT = 'passportElementBankStatement'
        PASSPORT_ELEMENT_DRIVER_LICENSE = 'passportElementDriverLicense'
        PASSPORT_ELEMENT_EMAIL_ADDRESS = 'passportElementEmailAddress'
        PASSPORT_ELEMENT_IDENTITY_CARD = 'passportElementIdentityCard'
        PASSPORT_ELEMENT_INTERNAL_PASSPORT = 'passportElementInternalPassport'
        PASSPORT_ELEMENT_PASSPORT = 'passportElementPassport'
        PASSPORT_ELEMENT_PASSPORT_REGISTRATION = 'passportElementPassportRegistration'
        PASSPORT_ELEMENT_PERSONAL_DETAILS = 'passportElementPersonalDetails'
        PASSPORT_ELEMENT_PHONE_NUMBER = 'passportElementPhoneNumber'
        PASSPORT_ELEMENT_RENTAL_AGREEMENT = 'passportElementRentalAgreement'
        PASSPORT_ELEMENT_TEMPORARY_REGISTRATION = 'passportElementTemporaryRegistration'
        PASSPORT_ELEMENT_UTILITY_BILL = 'passportElementUtilityBill'
        PASSPORT_ELEMENT_ERROR = 'passportElementError'
        PASSPORT_ELEMENT_ERROR_SOURCE = 'passportElementErrorSource'
        PASSPORT_ELEMENT_ERROR_SOURCE_DATA_FIELD = 'passportElementErrorSourceDataField'
        PASSPORT_ELEMENT_ERROR_SOURCE_FILE = 'passportElementErrorSourceFile'
        PASSPORT_ELEMENT_ERROR_SOURCE_FILES = 'passportElementErrorSourceFiles'
        PASSPORT_ELEMENT_ERROR_SOURCE_FRONT_SIDE = 'passportElementErrorSourceFrontSide'
        PASSPORT_ELEMENT_ERROR_SOURCE_REVERSE_SIDE = 'passportElementErrorSourceReverseSide'
        PASSPORT_ELEMENT_ERROR_SOURCE_SELFIE = 'passportElementErrorSourceSelfie'
        PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILE = 'passportElementErrorSourceTranslationFile'
        PASSPORT_ELEMENT_ERROR_SOURCE_TRANSLATION_FILES = 'passportElementErrorSourceTranslationFiles'
        PASSPORT_ELEMENT_ERROR_SOURCE_UNSPECIFIED = 'passportElementErrorSourceUnspecified'
        PASSPORT_ELEMENT_TYPE = 'passportElementType'
        PASSPORT_ELEMENT_TYPE_ADDRESS = 'passportElementTypeAddress'
        PASSPORT_ELEMENT_TYPE_BANK_STATEMENT = 'passportElementTypeBankStatement'
        PASSPORT_ELEMENT_TYPE_DRIVER_LICENSE = 'passportElementTypeDriverLicense'
        PASSPORT_ELEMENT_TYPE_EMAIL_ADDRESS = 'passportElementTypeEmailAddress'
        PASSPORT_ELEMENT_TYPE_IDENTITY_CARD = 'passportElementTypeIdentityCard'
        PASSPORT_ELEMENT_TYPE_INTERNAL_PASSPORT = 'passportElementTypeInternalPassport'
        PASSPORT_ELEMENT_TYPE_PASSPORT = 'passportElementTypePassport'
        PASSPORT_ELEMENT_TYPE_PASSPORT_REGISTRATION = 'passportElementTypePassportRegistration'
        PASSPORT_ELEMENT_TYPE_PERSONAL_DETAILS = 'passportElementTypePersonalDetails'
        PASSPORT_ELEMENT_TYPE_PHONE_NUMBER = 'passportElementTypePhoneNumber'
        PASSPORT_ELEMENT_TYPE_RENTAL_AGREEMENT = 'passportElementTypeRentalAgreement'
        PASSPORT_ELEMENT_TYPE_TEMPORARY_REGISTRATION = 'passportElementTypeTemporaryRegistration'
        PASSPORT_ELEMENT_TYPE_UTILITY_BILL = 'passportElementTypeUtilityBill'
        PASSPORT_ELEMENTS = 'passportElements'
        PASSPORT_ELEMENTS_WITH_ERRORS = 'passportElementsWithErrors'
        PASSPORT_REQUIRED_ELEMENT = 'passportRequiredElement'
        PASSPORT_SUITABLE_ELEMENT = 'passportSuitableElement'
        PASSWORD_STATE = 'passwordState'
        PAYMENT_FORM = 'paymentForm'
        PAYMENT_RECEIPT = 'paymentReceipt'
        PAYMENT_RESULT = 'paymentResult'
        PAYMENTS_PROVIDER_STRIPE = 'paymentsProviderStripe'
        PERSONAL_DETAILS = 'personalDetails'
        PERSONAL_DOCUMENT = 'personalDocument'
        PHONE_NUMBER_AUTHENTICATION_SETTINGS = 'phoneNumberAuthenticationSettings'
        PHONE_NUMBER_INFO = 'phoneNumberInfo'
        PHOTO = 'photo'
        PHOTO_SIZE = 'photoSize'
        PIN_CHAT_MESSAGE = 'pinChatMessage'
        PING_PROXY = 'pingProxy'
        POINT = 'point'
        POLL = 'poll'
        POLL_OPTION = 'pollOption'
        POLL_TYPE = 'pollType'
        POLL_TYPE_QUIZ = 'pollTypeQuiz'
        POLL_TYPE_REGULAR = 'pollTypeRegular'
        PROCESS_PUSH_NOTIFICATION = 'processPushNotification'
        PROFILE_PHOTO = 'profilePhoto'
        PROXIES = 'proxies'
        PROXY = 'proxy'
        PROXY_TYPE = 'proxyType'
        PROXY_TYPE_HTTP = 'proxyTypeHttp'
        PROXY_TYPE_MTPROTO = 'proxyTypeMtproto'
        PROXY_TYPE_SOCKS5 = 'proxyTypeSocks5'
        PUBLIC_CHAT_TYPE = 'publicChatType'
        PUBLIC_CHAT_TYPE_HAS_USERNAME = 'publicChatTypeHasUsername'
        PUBLIC_CHAT_TYPE_IS_LOCATION_BASED = 'publicChatTypeIsLocationBased'
        PUSH_MESSAGE_CONTENT = 'pushMessageContent'
        PUSH_MESSAGE_CONTENT_ANIMATION = 'pushMessageContentAnimation'
        PUSH_MESSAGE_CONTENT_AUDIO = 'pushMessageContentAudio'
        PUSH_MESSAGE_CONTENT_BASIC_GROUP_CHAT_CREATE = 'pushMessageContentBasicGroupChatCreate'
        PUSH_MESSAGE_CONTENT_CHAT_ADD_MEMBERS = 'pushMessageContentChatAddMembers'
        PUSH_MESSAGE_CONTENT_CHAT_CHANGE_PHOTO = 'pushMessageContentChatChangePhoto'
        PUSH_MESSAGE_CONTENT_CHAT_CHANGE_TITLE = 'pushMessageContentChatChangeTitle'
        PUSH_MESSAGE_CONTENT_CHAT_DELETE_MEMBER = 'pushMessageContentChatDeleteMember'
        PUSH_MESSAGE_CONTENT_CHAT_JOIN_BY_LINK = 'pushMessageContentChatJoinByLink'
        PUSH_MESSAGE_CONTENT_CONTACT = 'pushMessageContentContact'
        PUSH_MESSAGE_CONTENT_CONTACT_REGISTERED = 'pushMessageContentContactRegistered'
        PUSH_MESSAGE_CONTENT_DOCUMENT = 'pushMessageContentDocument'
        PUSH_MESSAGE_CONTENT_GAME = 'pushMessageContentGame'
        PUSH_MESSAGE_CONTENT_GAME_SCORE = 'pushMessageContentGameScore'
        PUSH_MESSAGE_CONTENT_HIDDEN = 'pushMessageContentHidden'
        PUSH_MESSAGE_CONTENT_INVOICE = 'pushMessageContentInvoice'
        PUSH_MESSAGE_CONTENT_LOCATION = 'pushMessageContentLocation'
        PUSH_MESSAGE_CONTENT_MEDIA_ALBUM = 'pushMessageContentMediaAlbum'
        PUSH_MESSAGE_CONTENT_MESSAGE_FORWARDS = 'pushMessageContentMessageForwards'
        PUSH_MESSAGE_CONTENT_PHOTO = 'pushMessageContentPhoto'
        PUSH_MESSAGE_CONTENT_POLL = 'pushMessageContentPoll'
        PUSH_MESSAGE_CONTENT_SCREENSHOT_TAKEN = 'pushMessageContentScreenshotTaken'
        PUSH_MESSAGE_CONTENT_STICKER = 'pushMessageContentSticker'
        PUSH_MESSAGE_CONTENT_TEXT = 'pushMessageContentText'
        PUSH_MESSAGE_CONTENT_VIDEO = 'pushMessageContentVideo'
        PUSH_MESSAGE_CONTENT_VIDEO_NOTE = 'pushMessageContentVideoNote'
        PUSH_MESSAGE_CONTENT_VOICE_NOTE = 'pushMessageContentVoiceNote'
        PUSH_RECEIVER_ID = 'pushReceiverId'
        READ_ALL_CHAT_MENTIONS = 'readAllChatMentions'
        READ_FILE_PART = 'readFilePart'
        RECOMMENDED_CHAT_FILTER = 'recommendedChatFilter'
        RECOMMENDED_CHAT_FILTERS = 'recommendedChatFilters'
        RECOVER_AUTHENTICATION_PASSWORD = 'recoverAuthenticationPassword'
        RECOVER_PASSWORD = 'recoverPassword'
        RECOVERY_EMAIL_ADDRESS = 'recoveryEmailAddress'
        REGISTER_DEVICE = 'registerDevice'
        REGISTER_USER = 'registerUser'
        REMOTE_FILE = 'remoteFile'
        REMOVE_BACKGROUND = 'removeBackground'
        REMOVE_CHAT_ACTION_BAR = 'removeChatActionBar'
        REMOVE_CONTACTS = 'removeContacts'
        REMOVE_FAVORITE_STICKER = 'removeFavoriteSticker'
        REMOVE_NOTIFICATION = 'removeNotification'
        REMOVE_NOTIFICATION_GROUP = 'removeNotificationGroup'
        REMOVE_PROXY = 'removeProxy'
        REMOVE_RECENT_HASHTAG = 'removeRecentHashtag'
        REMOVE_RECENT_STICKER = 'removeRecentSticker'
        REMOVE_RECENTLY_FOUND_CHAT = 'removeRecentlyFoundChat'
        REMOVE_SAVED_ANIMATION = 'removeSavedAnimation'
        REMOVE_STICKER_FROM_SET = 'removeStickerFromSet'
        REMOVE_TOP_CHAT = 'removeTopChat'
        REORDER_CHAT_FILTERS = 'reorderChatFilters'
        REORDER_INSTALLED_STICKER_SETS = 'reorderInstalledStickerSets'
        REPLACE_PRIMARY_CHAT_INVITE_LINK = 'replacePrimaryChatInviteLink'
        REPLY_MARKUP = 'replyMarkup'
        REPLY_MARKUP_FORCE_REPLY = 'replyMarkupForceReply'
        REPLY_MARKUP_INLINE_KEYBOARD = 'replyMarkupInlineKeyboard'
        REPLY_MARKUP_REMOVE_KEYBOARD = 'replyMarkupRemoveKeyboard'
        REPLY_MARKUP_SHOW_KEYBOARD = 'replyMarkupShowKeyboard'
        REPORT_CHAT = 'reportChat'
        REPORT_CHAT_PHOTO = 'reportChatPhoto'
        REPORT_SUPERGROUP_SPAM = 'reportSupergroupSpam'
        REQUEST_AUTHENTICATION_PASSWORD_RECOVERY = 'requestAuthenticationPasswordRecovery'
        REQUEST_PASSWORD_RECOVERY = 'requestPasswordRecovery'
        REQUEST_QR_CODE_AUTHENTICATION = 'requestQrCodeAuthentication'
        RESEND_AUTHENTICATION_CODE = 'resendAuthenticationCode'
        RESEND_CHANGE_PHONE_NUMBER_CODE = 'resendChangePhoneNumberCode'
        RESEND_EMAIL_ADDRESS_VERIFICATION_CODE = 'resendEmailAddressVerificationCode'
        RESEND_MESSAGES = 'resendMessages'
        RESEND_PHONE_NUMBER_CONFIRMATION_CODE = 'resendPhoneNumberConfirmationCode'
        RESEND_PHONE_NUMBER_VERIFICATION_CODE = 'resendPhoneNumberVerificationCode'
        RESEND_RECOVERY_EMAIL_ADDRESS_CODE = 'resendRecoveryEmailAddressCode'
        RESET_ALL_NOTIFICATION_SETTINGS = 'resetAllNotificationSettings'
        RESET_BACKGROUNDS = 'resetBackgrounds'
        RESET_NETWORK_STATISTICS = 'resetNetworkStatistics'
        REVOKE_CHAT_INVITE_LINK = 'revokeChatInviteLink'
        REVOKE_GROUP_CALL_INVITE_LINK = 'revokeGroupCallInviteLink'
        RICH_TEXT = 'richText'
        RICH_TEXT_ANCHOR = 'richTextAnchor'
        RICH_TEXT_ANCHOR_LINK = 'richTextAnchorLink'
        RICH_TEXT_BOLD = 'richTextBold'
        RICH_TEXT_EMAIL_ADDRESS = 'richTextEmailAddress'
        RICH_TEXT_FIXED = 'richTextFixed'
        RICH_TEXT_ICON = 'richTextIcon'
        RICH_TEXT_ITALIC = 'richTextItalic'
        RICH_TEXT_MARKED = 'richTextMarked'
        RICH_TEXT_PHONE_NUMBER = 'richTextPhoneNumber'
        RICH_TEXT_PLAIN = 'richTextPlain'
        RICH_TEXT_REFERENCE = 'richTextReference'
        RICH_TEXT_STRIKETHROUGH = 'richTextStrikethrough'
        RICH_TEXT_SUBSCRIPT = 'richTextSubscript'
        RICH_TEXT_SUPERSCRIPT = 'richTextSuperscript'
        RICH_TEXT_UNDERLINE = 'richTextUnderline'
        RICH_TEXT_URL = 'richTextUrl'
        RICH_TEXTS = 'richTexts'
        SAVE_APPLICATION_LOG_EVENT = 'saveApplicationLogEvent'
        SAVED_CREDENTIALS = 'savedCredentials'
        SCOPE_NOTIFICATION_SETTINGS = 'scopeNotificationSettings'
        SEARCH_BACKGROUND = 'searchBackground'
        SEARCH_CALL_MESSAGES = 'searchCallMessages'
        SEARCH_CHAT_MEMBERS = 'searchChatMembers'
        SEARCH_CHAT_MESSAGES = 'searchChatMessages'
        SEARCH_CHAT_RECENT_LOCATION_MESSAGES = 'searchChatRecentLocationMessages'
        SEARCH_CHATS = 'searchChats'
        SEARCH_CHATS_NEARBY = 'searchChatsNearby'
        SEARCH_CHATS_ON_SERVER = 'searchChatsOnServer'
        SEARCH_CONTACTS = 'searchContacts'
        SEARCH_EMOJIS = 'searchEmojis'
        SEARCH_HASHTAGS = 'searchHashtags'
        SEARCH_INSTALLED_STICKER_SETS = 'searchInstalledStickerSets'
        SEARCH_MESSAGES = 'searchMessages'
        SEARCH_MESSAGES_FILTER = 'searchMessagesFilter'
        SEARCH_MESSAGES_FILTER_ANIMATION = 'searchMessagesFilterAnimation'
        SEARCH_MESSAGES_FILTER_AUDIO = 'searchMessagesFilterAudio'
        SEARCH_MESSAGES_FILTER_CALL = 'searchMessagesFilterCall'
        SEARCH_MESSAGES_FILTER_CHAT_PHOTO = 'searchMessagesFilterChatPhoto'
        SEARCH_MESSAGES_FILTER_DOCUMENT = 'searchMessagesFilterDocument'
        SEARCH_MESSAGES_FILTER_EMPTY = 'searchMessagesFilterEmpty'
        SEARCH_MESSAGES_FILTER_FAILED_TO_SEND = 'searchMessagesFilterFailedToSend'
        SEARCH_MESSAGES_FILTER_MENTION = 'searchMessagesFilterMention'
        SEARCH_MESSAGES_FILTER_MISSED_CALL = 'searchMessagesFilterMissedCall'
        SEARCH_MESSAGES_FILTER_PHOTO = 'searchMessagesFilterPhoto'
        SEARCH_MESSAGES_FILTER_PHOTO_AND_VIDEO = 'searchMessagesFilterPhotoAndVideo'
        SEARCH_MESSAGES_FILTER_PINNED = 'searchMessagesFilterPinned'
        SEARCH_MESSAGES_FILTER_UNREAD_MENTION = 'searchMessagesFilterUnreadMention'
        SEARCH_MESSAGES_FILTER_URL = 'searchMessagesFilterUrl'
        SEARCH_MESSAGES_FILTER_VIDEO = 'searchMessagesFilterVideo'
        SEARCH_MESSAGES_FILTER_VIDEO_NOTE = 'searchMessagesFilterVideoNote'
        SEARCH_MESSAGES_FILTER_VOICE_AND_VIDEO_NOTE = 'searchMessagesFilterVoiceAndVideoNote'
        SEARCH_MESSAGES_FILTER_VOICE_NOTE = 'searchMessagesFilterVoiceNote'
        SEARCH_PUBLIC_CHAT = 'searchPublicChat'
        SEARCH_PUBLIC_CHATS = 'searchPublicChats'
        SEARCH_SECRET_MESSAGES = 'searchSecretMessages'
        SEARCH_STICKER_SET = 'searchStickerSet'
        SEARCH_STICKER_SETS = 'searchStickerSets'
        SEARCH_STICKERS = 'searchStickers'
        SECONDS = 'seconds'
        SECRET_CHAT = 'secretChat'
        SECRET_CHAT_STATE = 'secretChatState'
        SECRET_CHAT_STATE_CLOSED = 'secretChatStateClosed'
        SECRET_CHAT_STATE_PENDING = 'secretChatStatePending'
        SECRET_CHAT_STATE_READY = 'secretChatStateReady'
        SEND_BOT_START_MESSAGE = 'sendBotStartMessage'
        SEND_CALL_DEBUG_INFORMATION = 'sendCallDebugInformation'
        SEND_CALL_RATING = 'sendCallRating'
        SEND_CALL_SIGNALING_DATA = 'sendCallSignalingData'
        SEND_CHAT_ACTION = 'sendChatAction'
        SEND_CHAT_SCREENSHOT_TAKEN_NOTIFICATION = 'sendChatScreenshotTakenNotification'
        SEND_CUSTOM_REQUEST = 'sendCustomRequest'
        SEND_EMAIL_ADDRESS_VERIFICATION_CODE = 'sendEmailAddressVerificationCode'
        SEND_INLINE_QUERY_RESULT_MESSAGE = 'sendInlineQueryResultMessage'
        SEND_MESSAGE = 'sendMessage'
        SEND_MESSAGE_ALBUM = 'sendMessageAlbum'
        SEND_PASSPORT_AUTHORIZATION_FORM = 'sendPassportAuthorizationForm'
        SEND_PAYMENT_FORM = 'sendPaymentForm'
        SEND_PHONE_NUMBER_CONFIRMATION_CODE = 'sendPhoneNumberConfirmationCode'
        SEND_PHONE_NUMBER_VERIFICATION_CODE = 'sendPhoneNumberVerificationCode'
        SESSION = 'session'
        SESSIONS = 'sessions'
        SET_ACCOUNT_TTL = 'setAccountTtl'
        SET_ALARM = 'setAlarm'
        SET_AUTHENTICATION_PHONE_NUMBER = 'setAuthenticationPhoneNumber'
        SET_AUTO_DOWNLOAD_SETTINGS = 'setAutoDownloadSettings'
        SET_BACKGROUND = 'setBackground'
        SET_BIO = 'setBio'
        SET_BOT_UPDATES_STATUS = 'setBotUpdatesStatus'
        SET_CHAT_CLIENT_DATA = 'setChatClientData'
        SET_CHAT_DESCRIPTION = 'setChatDescription'
        SET_CHAT_DISCUSSION_GROUP = 'setChatDiscussionGroup'
        SET_CHAT_DRAFT_MESSAGE = 'setChatDraftMessage'
        SET_CHAT_LOCATION = 'setChatLocation'
        SET_CHAT_MEMBER_STATUS = 'setChatMemberStatus'
        SET_CHAT_MESSAGE_TTL_SETTING = 'setChatMessageTtlSetting'
        SET_CHAT_NOTIFICATION_SETTINGS = 'setChatNotificationSettings'
        SET_CHAT_PERMISSIONS = 'setChatPermissions'
        SET_CHAT_PHOTO = 'setChatPhoto'
        SET_CHAT_SLOW_MODE_DELAY = 'setChatSlowModeDelay'
        SET_CHAT_TITLE = 'setChatTitle'
        SET_COMMANDS = 'setCommands'
        SET_CUSTOM_LANGUAGE_PACK = 'setCustomLanguagePack'
        SET_CUSTOM_LANGUAGE_PACK_STRING = 'setCustomLanguagePackString'
        SET_DATABASE_ENCRYPTION_KEY = 'setDatabaseEncryptionKey'
        SET_FILE_GENERATION_PROGRESS = 'setFileGenerationProgress'
        SET_GAME_SCORE = 'setGameScore'
        SET_GROUP_CALL_PARTICIPANT_IS_SPEAKING = 'setGroupCallParticipantIsSpeaking'
        SET_GROUP_CALL_PARTICIPANT_VOLUME_LEVEL = 'setGroupCallParticipantVolumeLevel'
        SET_GROUP_CALL_TITLE = 'setGroupCallTitle'
        SET_INLINE_GAME_SCORE = 'setInlineGameScore'
        SET_LOCATION = 'setLocation'
        SET_LOG_STREAM = 'setLogStream'
        SET_LOG_TAG_VERBOSITY_LEVEL = 'setLogTagVerbosityLevel'
        SET_LOG_VERBOSITY_LEVEL = 'setLogVerbosityLevel'
        SET_NAME = 'setName'
        SET_NETWORK_TYPE = 'setNetworkType'
        SET_OPTION = 'setOption'
        SET_PASSPORT_ELEMENT = 'setPassportElement'
        SET_PASSPORT_ELEMENT_ERRORS = 'setPassportElementErrors'
        SET_PASSWORD = 'setPassword'
        SET_PINNED_CHATS = 'setPinnedChats'
        SET_POLL_ANSWER = 'setPollAnswer'
        SET_PROFILE_PHOTO = 'setProfilePhoto'
        SET_RECOVERY_EMAIL_ADDRESS = 'setRecoveryEmailAddress'
        SET_SCOPE_NOTIFICATION_SETTINGS = 'setScopeNotificationSettings'
        SET_STICKER_POSITION_IN_SET = 'setStickerPositionInSet'
        SET_STICKER_SET_THUMBNAIL = 'setStickerSetThumbnail'
        SET_SUPERGROUP_STICKER_SET = 'setSupergroupStickerSet'
        SET_SUPERGROUP_USERNAME = 'setSupergroupUsername'
        SET_TDLIB_PARAMETERS = 'setTdlibParameters'
        SET_USER_PRIVACY_SETTING_RULES = 'setUserPrivacySettingRules'
        SET_USERNAME = 'setUsername'
        SHARE_PHONE_NUMBER = 'sharePhoneNumber'
        SHIPPING_OPTION = 'shippingOption'
        START_GROUP_CALL_RECORDING = 'startGroupCallRecording'
        STATISTICAL_GRAPH = 'statisticalGraph'
        STATISTICAL_GRAPH_ASYNC = 'statisticalGraphAsync'
        STATISTICAL_GRAPH_DATA = 'statisticalGraphData'
        STATISTICAL_GRAPH_ERROR = 'statisticalGraphError'
        STATISTICAL_VALUE = 'statisticalValue'
        STICKER = 'sticker'
        STICKER_SET = 'stickerSet'
        STICKER_SET_INFO = 'stickerSetInfo'
        STICKER_SETS = 'stickerSets'
        STICKERS = 'stickers'
        STOP_POLL = 'stopPoll'
        STORAGE_STATISTICS = 'storageStatistics'
        STORAGE_STATISTICS_BY_CHAT = 'storageStatisticsByChat'
        STORAGE_STATISTICS_BY_FILE_TYPE = 'storageStatisticsByFileType'
        STORAGE_STATISTICS_FAST = 'storageStatisticsFast'
        SUGGESTED_ACTION = 'suggestedAction'
        SUGGESTED_ACTION_CHECK_PHONE_NUMBER = 'suggestedActionCheckPhoneNumber'
        SUGGESTED_ACTION_CONVERT_TO_BROADCAST_GROUP = 'suggestedActionConvertToBroadcastGroup'
        SUGGESTED_ACTION_ENABLE_ARCHIVE_AND_MUTE_NEW_CHATS = 'suggestedActionEnableArchiveAndMuteNewChats'
        SUGGESTED_ACTION_SEE_TICKS_HINT = 'suggestedActionSeeTicksHint'
        SUPERGROUP = 'supergroup'
        SUPERGROUP_FULL_INFO = 'supergroupFullInfo'
        SUPERGROUP_MEMBERS_FILTER = 'supergroupMembersFilter'
        SUPERGROUP_MEMBERS_FILTER_ADMINISTRATORS = 'supergroupMembersFilterAdministrators'
        SUPERGROUP_MEMBERS_FILTER_BANNED = 'supergroupMembersFilterBanned'
        SUPERGROUP_MEMBERS_FILTER_BOTS = 'supergroupMembersFilterBots'
        SUPERGROUP_MEMBERS_FILTER_CONTACTS = 'supergroupMembersFilterContacts'
        SUPERGROUP_MEMBERS_FILTER_MENTION = 'supergroupMembersFilterMention'
        SUPERGROUP_MEMBERS_FILTER_RECENT = 'supergroupMembersFilterRecent'
        SUPERGROUP_MEMBERS_FILTER_RESTRICTED = 'supergroupMembersFilterRestricted'
        SUPERGROUP_MEMBERS_FILTER_SEARCH = 'supergroupMembersFilterSearch'
        SYNCHRONIZE_LANGUAGE_PACK = 'synchronizeLanguagePack'
        T_ME_URL = 'tMeUrl'
        T_ME_URL_TYPE = 'tMeUrlType'
        T_ME_URL_TYPE_CHAT_INVITE = 'tMeUrlTypeChatInvite'
        T_ME_URL_TYPE_STICKER_SET = 'tMeUrlTypeStickerSet'
        T_ME_URL_TYPE_SUPERGROUP = 'tMeUrlTypeSupergroup'
        T_ME_URL_TYPE_USER = 'tMeUrlTypeUser'
        T_ME_URLS = 'tMeUrls'
        TDLIB_PARAMETERS = 'tdlibParameters'
        TEMPORARY_PASSWORD_STATE = 'temporaryPasswordState'
        TERMINATE_ALL_OTHER_SESSIONS = 'terminateAllOtherSessions'
        TERMINATE_SESSION = 'terminateSession'
        TERMS_OF_SERVICE = 'termsOfService'
        TEST_BYTES = 'testBytes'
        TEST_CALL_BYTES = 'testCallBytes'
        TEST_CALL_EMPTY = 'testCallEmpty'
        TEST_CALL_STRING = 'testCallString'
        TEST_CALL_VECTOR_INT = 'testCallVectorInt'
        TEST_CALL_VECTOR_INT_OBJECT = 'testCallVectorIntObject'
        TEST_CALL_VECTOR_STRING = 'testCallVectorString'
        TEST_CALL_VECTOR_STRING_OBJECT = 'testCallVectorStringObject'
        TEST_GET_DIFFERENCE = 'testGetDifference'
        TEST_INT = 'testInt'
        TEST_NETWORK = 'testNetwork'
        TEST_PROXY = 'testProxy'
        TEST_RETURN_ERROR = 'testReturnError'
        TEST_SQUARE_INT = 'testSquareInt'
        TEST_STRING = 'testString'
        TEST_USE_UPDATE = 'testUseUpdate'
        TEST_VECTOR_INT = 'testVectorInt'
        TEST_VECTOR_INT_OBJECT = 'testVectorIntObject'
        TEST_VECTOR_STRING = 'testVectorString'
        TEST_VECTOR_STRING_OBJECT = 'testVectorStringObject'
        TEXT = 'text'
        TEXT_ENTITIES = 'textEntities'
        TEXT_ENTITY = 'textEntity'
        TEXT_ENTITY_TYPE = 'textEntityType'
        TEXT_ENTITY_TYPE_BANK_CARD_NUMBER = 'textEntityTypeBankCardNumber'
        TEXT_ENTITY_TYPE_BOLD = 'textEntityTypeBold'
        TEXT_ENTITY_TYPE_BOT_COMMAND = 'textEntityTypeBotCommand'
        TEXT_ENTITY_TYPE_CASHTAG = 'textEntityTypeCashtag'
        TEXT_ENTITY_TYPE_CODE = 'textEntityTypeCode'
        TEXT_ENTITY_TYPE_EMAIL_ADDRESS = 'textEntityTypeEmailAddress'
        TEXT_ENTITY_TYPE_HASHTAG = 'textEntityTypeHashtag'
        TEXT_ENTITY_TYPE_ITALIC = 'textEntityTypeItalic'
        TEXT_ENTITY_TYPE_MENTION = 'textEntityTypeMention'
        TEXT_ENTITY_TYPE_MENTION_NAME = 'textEntityTypeMentionName'
        TEXT_ENTITY_TYPE_PHONE_NUMBER = 'textEntityTypePhoneNumber'
        TEXT_ENTITY_TYPE_PRE = 'textEntityTypePre'
        TEXT_ENTITY_TYPE_PRE_CODE = 'textEntityTypePreCode'
        TEXT_ENTITY_TYPE_STRIKETHROUGH = 'textEntityTypeStrikethrough'
        TEXT_ENTITY_TYPE_TEXT_URL = 'textEntityTypeTextUrl'
        TEXT_ENTITY_TYPE_UNDERLINE = 'textEntityTypeUnderline'
        TEXT_ENTITY_TYPE_URL = 'textEntityTypeUrl'
        TEXT_PARSE_MODE = 'textParseMode'
        TEXT_PARSE_MODE_HTML = 'textParseModeHTML'
        TEXT_PARSE_MODE_MARKDOWN = 'textParseModeMarkdown'
        THUMBNAIL = 'thumbnail'
        THUMBNAIL_FORMAT = 'thumbnailFormat'
        THUMBNAIL_FORMAT_GIF = 'thumbnailFormatGif'
        THUMBNAIL_FORMAT_JPEG = 'thumbnailFormatJpeg'
        THUMBNAIL_FORMAT_MPEG4 = 'thumbnailFormatMpeg4'
        THUMBNAIL_FORMAT_PNG = 'thumbnailFormatPng'
        THUMBNAIL_FORMAT_TGS = 'thumbnailFormatTgs'
        THUMBNAIL_FORMAT_WEBP = 'thumbnailFormatWebp'
        TOGGLE_CHAT_DEFAULT_DISABLE_NOTIFICATION = 'toggleChatDefaultDisableNotification'
        TOGGLE_CHAT_IS_MARKED_AS_UNREAD = 'toggleChatIsMarkedAsUnread'
        TOGGLE_CHAT_IS_PINNED = 'toggleChatIsPinned'
        TOGGLE_GROUP_CALL_MUTE_NEW_PARTICIPANTS = 'toggleGroupCallMuteNewParticipants'
        TOGGLE_GROUP_CALL_PARTICIPANT_IS_HAND_RAISED = 'toggleGroupCallParticipantIsHandRaised'
        TOGGLE_GROUP_CALL_PARTICIPANT_IS_MUTED = 'toggleGroupCallParticipantIsMuted'
        TOGGLE_MESSAGE_SENDER_IS_BLOCKED = 'toggleMessageSenderIsBlocked'
        TOGGLE_SUPERGROUP_IS_ALL_HISTORY_AVAILABLE = 'toggleSupergroupIsAllHistoryAvailable'
        TOGGLE_SUPERGROUP_IS_BROADCAST_GROUP = 'toggleSupergroupIsBroadcastGroup'
        TOGGLE_SUPERGROUP_SIGN_MESSAGES = 'toggleSupergroupSignMessages'
        TOP_CHAT_CATEGORY = 'topChatCategory'
        TOP_CHAT_CATEGORY_BOTS = 'topChatCategoryBots'
        TOP_CHAT_CATEGORY_CALLS = 'topChatCategoryCalls'
        TOP_CHAT_CATEGORY_CHANNELS = 'topChatCategoryChannels'
        TOP_CHAT_CATEGORY_FORWARD_CHATS = 'topChatCategoryForwardChats'
        TOP_CHAT_CATEGORY_GROUPS = 'topChatCategoryGroups'
        TOP_CHAT_CATEGORY_INLINE_BOTS = 'topChatCategoryInlineBots'
        TOP_CHAT_CATEGORY_USERS = 'topChatCategoryUsers'
        TRANSFER_CHAT_OWNERSHIP = 'transferChatOwnership'
        UNPIN_ALL_CHAT_MESSAGES = 'unpinAllChatMessages'
        UNPIN_CHAT_MESSAGE = 'unpinChatMessage'
        UPDATE = 'update'
        UPDATE_ACTIVE_NOTIFICATIONS = 'updateActiveNotifications'
        UPDATE_ANIMATION_SEARCH_PARAMETERS = 'updateAnimationSearchParameters'
        UPDATE_AUTHORIZATION_STATE = 'updateAuthorizationState'
        UPDATE_BASIC_GROUP = 'updateBasicGroup'
        UPDATE_BASIC_GROUP_FULL_INFO = 'updateBasicGroupFullInfo'
        UPDATE_CALL = 'updateCall'
        UPDATE_CHAT_ACTION_BAR = 'updateChatActionBar'
        UPDATE_CHAT_DEFAULT_DISABLE_NOTIFICATION = 'updateChatDefaultDisableNotification'
        UPDATE_CHAT_DRAFT_MESSAGE = 'updateChatDraftMessage'
        UPDATE_CHAT_FILTERS = 'updateChatFilters'
        UPDATE_CHAT_HAS_SCHEDULED_MESSAGES = 'updateChatHasScheduledMessages'
        UPDATE_CHAT_IS_BLOCKED = 'updateChatIsBlocked'
        UPDATE_CHAT_IS_MARKED_AS_UNREAD = 'updateChatIsMarkedAsUnread'
        UPDATE_CHAT_LAST_MESSAGE = 'updateChatLastMessage'
        UPDATE_CHAT_MEMBER = 'updateChatMember'
        UPDATE_CHAT_MESSAGE_TTL_SETTING = 'updateChatMessageTtlSetting'
        UPDATE_CHAT_NOTIFICATION_SETTINGS = 'updateChatNotificationSettings'
        UPDATE_CHAT_ONLINE_MEMBER_COUNT = 'updateChatOnlineMemberCount'
        UPDATE_CHAT_PERMISSIONS = 'updateChatPermissions'
        UPDATE_CHAT_PHOTO = 'updateChatPhoto'
        UPDATE_CHAT_POSITION = 'updateChatPosition'
        UPDATE_CHAT_READ_INBOX = 'updateChatReadInbox'
        UPDATE_CHAT_READ_OUTBOX = 'updateChatReadOutbox'
        UPDATE_CHAT_REPLY_MARKUP = 'updateChatReplyMarkup'
        UPDATE_CHAT_TITLE = 'updateChatTitle'
        UPDATE_CHAT_UNREAD_MENTION_COUNT = 'updateChatUnreadMentionCount'
        UPDATE_CHAT_VOICE_CHAT = 'updateChatVoiceChat'
        UPDATE_CONNECTION_STATE = 'updateConnectionState'
        UPDATE_DELETE_MESSAGES = 'updateDeleteMessages'
        UPDATE_DICE_EMOJIS = 'updateDiceEmojis'
        UPDATE_FAVORITE_STICKERS = 'updateFavoriteStickers'
        UPDATE_FILE = 'updateFile'
        UPDATE_FILE_GENERATION_START = 'updateFileGenerationStart'
        UPDATE_FILE_GENERATION_STOP = 'updateFileGenerationStop'
        UPDATE_GROUP_CALL = 'updateGroupCall'
        UPDATE_GROUP_CALL_PARTICIPANT = 'updateGroupCallParticipant'
        UPDATE_HAVE_PENDING_NOTIFICATIONS = 'updateHavePendingNotifications'
        UPDATE_INSTALLED_STICKER_SETS = 'updateInstalledStickerSets'
        UPDATE_LANGUAGE_PACK_STRINGS = 'updateLanguagePackStrings'
        UPDATE_MESSAGE_CONTENT = 'updateMessageContent'
        UPDATE_MESSAGE_CONTENT_OPENED = 'updateMessageContentOpened'
        UPDATE_MESSAGE_EDITED = 'updateMessageEdited'
        UPDATE_MESSAGE_INTERACTION_INFO = 'updateMessageInteractionInfo'
        UPDATE_MESSAGE_IS_PINNED = 'updateMessageIsPinned'
        UPDATE_MESSAGE_LIVE_LOCATION_VIEWED = 'updateMessageLiveLocationViewed'
        UPDATE_MESSAGE_MENTION_READ = 'updateMessageMentionRead'
        UPDATE_MESSAGE_SEND_ACKNOWLEDGED = 'updateMessageSendAcknowledged'
        UPDATE_MESSAGE_SEND_FAILED = 'updateMessageSendFailed'
        UPDATE_MESSAGE_SEND_SUCCEEDED = 'updateMessageSendSucceeded'
        UPDATE_NEW_CALL_SIGNALING_DATA = 'updateNewCallSignalingData'
        UPDATE_NEW_CALLBACK_QUERY = 'updateNewCallbackQuery'
        UPDATE_NEW_CHAT = 'updateNewChat'
        UPDATE_NEW_CHOSEN_INLINE_RESULT = 'updateNewChosenInlineResult'
        UPDATE_NEW_CUSTOM_EVENT = 'updateNewCustomEvent'
        UPDATE_NEW_CUSTOM_QUERY = 'updateNewCustomQuery'
        UPDATE_NEW_INLINE_CALLBACK_QUERY = 'updateNewInlineCallbackQuery'
        UPDATE_NEW_INLINE_QUERY = 'updateNewInlineQuery'
        UPDATE_NEW_MESSAGE = 'updateNewMessage'
        UPDATE_NEW_PRE_CHECKOUT_QUERY = 'updateNewPreCheckoutQuery'
        UPDATE_NEW_SHIPPING_QUERY = 'updateNewShippingQuery'
        UPDATE_NOTIFICATION = 'updateNotification'
        UPDATE_NOTIFICATION_GROUP = 'updateNotificationGroup'
        UPDATE_OPTION = 'updateOption'
        UPDATE_POLL = 'updatePoll'
        UPDATE_POLL_ANSWER = 'updatePollAnswer'
        UPDATE_RECENT_STICKERS = 'updateRecentStickers'
        UPDATE_SAVED_ANIMATIONS = 'updateSavedAnimations'
        UPDATE_SCOPE_NOTIFICATION_SETTINGS = 'updateScopeNotificationSettings'
        UPDATE_SECRET_CHAT = 'updateSecretChat'
        UPDATE_SELECTED_BACKGROUND = 'updateSelectedBackground'
        UPDATE_SERVICE_NOTIFICATION = 'updateServiceNotification'
        UPDATE_STICKER_SET = 'updateStickerSet'
        UPDATE_SUGGESTED_ACTIONS = 'updateSuggestedActions'
        UPDATE_SUPERGROUP = 'updateSupergroup'
        UPDATE_SUPERGROUP_FULL_INFO = 'updateSupergroupFullInfo'
        UPDATE_TERMS_OF_SERVICE = 'updateTermsOfService'
        UPDATE_TRENDING_STICKER_SETS = 'updateTrendingStickerSets'
        UPDATE_UNREAD_CHAT_COUNT = 'updateUnreadChatCount'
        UPDATE_UNREAD_MESSAGE_COUNT = 'updateUnreadMessageCount'
        UPDATE_USER = 'updateUser'
        UPDATE_USER_CHAT_ACTION = 'updateUserChatAction'
        UPDATE_USER_FULL_INFO = 'updateUserFullInfo'
        UPDATE_USER_PRIVACY_SETTING_RULES = 'updateUserPrivacySettingRules'
        UPDATE_USER_STATUS = 'updateUserStatus'
        UPDATE_USERS_NEARBY = 'updateUsersNearby'
        UPDATES = 'updates'
        UPGRADE_BASIC_GROUP_CHAT_TO_SUPERGROUP_CHAT = 'upgradeBasicGroupChatToSupergroupChat'
        UPLOAD_FILE = 'uploadFile'
        UPLOAD_STICKER_FILE = 'uploadStickerFile'
        USER = 'user'
        USER_FULL_INFO = 'userFullInfo'
        USER_PRIVACY_SETTING = 'userPrivacySetting'
        USER_PRIVACY_SETTING_ALLOW_CALLS = 'userPrivacySettingAllowCalls'
        USER_PRIVACY_SETTING_ALLOW_CHAT_INVITES = 'userPrivacySettingAllowChatInvites'
        USER_PRIVACY_SETTING_ALLOW_FINDING_BY_PHONE_NUMBER = 'userPrivacySettingAllowFindingByPhoneNumber'
        USER_PRIVACY_SETTING_ALLOW_PEER_TO_PEER_CALLS = 'userPrivacySettingAllowPeerToPeerCalls'
        USER_PRIVACY_SETTING_SHOW_LINK_IN_FORWARDED_MESSAGES = 'userPrivacySettingShowLinkInForwardedMessages'
        USER_PRIVACY_SETTING_SHOW_PHONE_NUMBER = 'userPrivacySettingShowPhoneNumber'
        USER_PRIVACY_SETTING_SHOW_PROFILE_PHOTO = 'userPrivacySettingShowProfilePhoto'
        USER_PRIVACY_SETTING_SHOW_STATUS = 'userPrivacySettingShowStatus'
        USER_PRIVACY_SETTING_RULE = 'userPrivacySettingRule'
        USER_PRIVACY_SETTING_RULE_ALLOW_ALL = 'userPrivacySettingRuleAllowAll'
        USER_PRIVACY_SETTING_RULE_ALLOW_CHAT_MEMBERS = 'userPrivacySettingRuleAllowChatMembers'
        USER_PRIVACY_SETTING_RULE_ALLOW_CONTACTS = 'userPrivacySettingRuleAllowContacts'
        USER_PRIVACY_SETTING_RULE_ALLOW_USERS = 'userPrivacySettingRuleAllowUsers'
        USER_PRIVACY_SETTING_RULE_RESTRICT_ALL = 'userPrivacySettingRuleRestrictAll'
        USER_PRIVACY_SETTING_RULE_RESTRICT_CHAT_MEMBERS = 'userPrivacySettingRuleRestrictChatMembers'
        USER_PRIVACY_SETTING_RULE_RESTRICT_CONTACTS = 'userPrivacySettingRuleRestrictContacts'
        USER_PRIVACY_SETTING_RULE_RESTRICT_USERS = 'userPrivacySettingRuleRestrictUsers'
        USER_PRIVACY_SETTING_RULES = 'userPrivacySettingRules'
        USER_STATUS = 'userStatus'
        USER_STATUS_EMPTY = 'userStatusEmpty'
        USER_STATUS_LAST_MONTH = 'userStatusLastMonth'
        USER_STATUS_LAST_WEEK = 'userStatusLastWeek'
        USER_STATUS_OFFLINE = 'userStatusOffline'
        USER_STATUS_ONLINE = 'userStatusOnline'
        USER_STATUS_RECENTLY = 'userStatusRecently'
        USER_TYPE = 'userType'
        USER_TYPE_BOT = 'userTypeBot'
        USER_TYPE_DELETED = 'userTypeDeleted'
        USER_TYPE_REGULAR = 'userTypeRegular'
        USER_TYPE_UNKNOWN = 'userTypeUnknown'
        USERS = 'users'
        VALIDATE_ORDER_INFO = 'validateOrderInfo'
        VALIDATED_ORDER_INFO = 'validatedOrderInfo'
        VECTOR_PATH_COMMAND = 'vectorPathCommand'
        VECTOR_PATH_COMMAND_CUBIC_BEZIER_CURVE = 'vectorPathCommandCubicBezierCurve'
        VECTOR_PATH_COMMAND_LINE = 'vectorPathCommandLine'
        VENUE = 'venue'
        VIDEO = 'video'
        VIDEO_NOTE = 'videoNote'
        VIEW_MESSAGES = 'viewMessages'
        VIEW_TRENDING_STICKER_SETS = 'viewTrendingStickerSets'
        VOICE_CHAT = 'voiceChat'
        VOICE_NOTE = 'voiceNote'
        WEB_PAGE = 'webPage'
        WEB_PAGE_INSTANT_VIEW = 'webPageInstantView'
        WRITE_GENERATED_FILE_PART = 'writeGeneratedFilePart'

    def __init__(self, client: 'Client'):
        self.client = client
    
    async def accept_call(
            self,
            call_id: int,
            protocol: CallProtocol,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Accepts an incoming call
        
        Params:
            call_id (:class:`int`)
                Call identifier
            
            protocol (:class:`CallProtocol`)
                Description of the call protocols supported by the application
            
        """
        _constructor = AcceptCall.construct if skip_validation else AcceptCall
        
        return await self.client.request(
            _constructor(
                call_id=call_id,
                protocol=protocol,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def accept_terms_of_service(
            self,
            terms_of_service_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Accepts Telegram terms of services
        
        Params:
            terms_of_service_id (:class:`str`)
                Terms of service identifier
            
        """
        _constructor = AcceptTermsOfService.construct if skip_validation else AcceptTermsOfService
        
        return await self.client.request(
            _constructor(
                terms_of_service_id=terms_of_service_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_chat_member(
            self,
            chat_id: int,
            user_id: int,
            forward_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a new member to a chat. Members can't be added to private or secret chats
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            user_id (:class:`int`)
                Identifier of the user
            
            forward_limit (:class:`int`)
                The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels
            
        """
        _constructor = AddChatMember.construct if skip_validation else AddChatMember
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
                forward_limit=forward_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_chat_members(
            self,
            chat_id: int,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds multiple new members to a chat. Currently this method is only available for supergroups and channels. This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            user_ids (:obj:`list[int]`)
                Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels
            
        """
        _constructor = AddChatMembers.construct if skip_validation else AddChatMembers
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_chat_to_list(
            self,
            chat_id: int,
            chat_list: ChatList,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            chat_list (:class:`ChatList`)
                The chat list. Use getChatListsToAddChat to get suitable chat lists
            
        """
        _constructor = AddChatToList.construct if skip_validation else AddChatToList
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                chat_list=chat_list,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_contact(
            self,
            contact: Contact,
            share_phone_number: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a user to the contact list or edits an existing contact by their user identifier
        
        Params:
            contact (:class:`Contact`)
                The contact to add or edit; phone number can be empty and needs to be specified only if known, vCard is ignored
            
            share_phone_number (:class:`bool`)
                True, if the new contact needs to be allowed to see current user's phone number. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed. Use the field UserFullInfo.need_phone_number_privacy_exception to check whether the current user needs to be asked to share their phone number
            
        """
        _constructor = AddContact.construct if skip_validation else AddContact
        
        return await self.client.request(
            _constructor(
                contact=contact,
                share_phone_number=share_phone_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_custom_server_language_pack(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization
        
        Params:
            language_pack_id (:class:`str`)
                Identifier of a language pack to be added; may be different from a name that is used in an "https://t.me/setlanguage/" link
            
        """
        _constructor = AddCustomServerLanguagePack.construct if skip_validation else AddCustomServerLanguagePack
        
        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_favorite_sticker(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list
        
        Params:
            sticker (:class:`InputFile`)
                Sticker file to add
            
        """
        _constructor = AddFavoriteSticker.construct if skip_validation else AddFavoriteSticker
        
        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_local_message(
            self,
            chat_id: int,
            sender: MessageSender,
            reply_to_message_id: int,
            disable_notification: bool,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message
        
        Params:
            chat_id (:class:`int`)
                Target chat
            
            sender (:class:`MessageSender`)
                The sender sender of the message
            
            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0
            
            disable_notification (:class:`bool`)
                Pass true to disable notification for the message
            
            input_message_content (:class:`InputMessageContent`)
                The content of the message to be added
            
        """
        _constructor = AddLocalMessage.construct if skip_validation else AddLocalMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                sender=sender,
                reply_to_message_id=reply_to_message_id,
                disable_notification=disable_notification,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_log_message(
            self,
            verbosity_level: int,
            text: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a message to TDLib internal log. Can be called synchronously
        
        Params:
            verbosity_level (:class:`int`)
                The minimum verbosity level needed for the message to be logged; 0-1023
            
            text (:class:`str`)
                Text of a message to log
            
        """
        _constructor = AddLogMessage.construct if skip_validation else AddLogMessage
        
        return await self.client.request(
            _constructor(
                verbosity_level=verbosity_level,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_network_statistics(
            self,
            entry: NetworkStatisticsEntry,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds the specified data to data usage statistics. Can be called before authorization
        
        Params:
            entry (:class:`NetworkStatisticsEntry`)
                The network statistics entry with the data to be added to statistics
            
        """
        _constructor = AddNetworkStatistics.construct if skip_validation else AddNetworkStatistics
        
        return await self.client.request(
            _constructor(
                entry=entry,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_proxy(
            self,
            server: str,
            port: int,
            enable: bool,
            type_: ProxyType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Proxy:
        """
        Adds a proxy server for network requests. Can be called before authorization
        
        Params:
            server (:class:`str`)
                Proxy server IP address
            
            port (:class:`int`)
                Proxy server port
            
            enable (:class:`bool`)
                True, if the proxy should be enabled
            
            type_ (:class:`ProxyType`)
                Proxy type
            
        """
        _constructor = AddProxy.construct if skip_validation else AddProxy
        
        return await self.client.request(
            _constructor(
                server=server,
                port=port,
                enable=enable,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_recent_sticker(
            self,
            is_attached: bool,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list
        
        Params:
            is_attached (:class:`bool`)
                Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers
            
            sticker (:class:`InputFile`)
                Sticker file to add
            
        """
        _constructor = AddRecentSticker.construct if skip_validation else AddRecentSticker
        
        return await self.client.request(
            _constructor(
                is_attached=is_attached,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_recently_found_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to add
            
        """
        _constructor = AddRecentlyFoundChat.construct if skip_validation else AddRecentlyFoundChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_saved_animation(
            self,
            animation: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first. Only non-secret video animations with MIME type "video/mp4" can be added to the list
        
        Params:
            animation (:class:`InputFile`)
                The animation file to be added. Only animations known to the server (i.e. successfully sent via a message) can be added to the list
            
        """
        _constructor = AddSavedAnimation.construct if skip_validation else AddSavedAnimation
        
        return await self.client.request(
            _constructor(
                animation=animation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def add_sticker_to_set(
            self,
            user_id: int,
            name: str,
            sticker: InputSticker,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Adds a new sticker to a set; for bots only. Returns the sticker set
        
        Params:
            user_id (:class:`int`)
                Sticker set owner
            
            name (:class:`str`)
                Sticker set name
            
            sticker (:class:`InputSticker`)
                Sticker to add to the set
            
        """
        _constructor = AddStickerToSet.construct if skip_validation else AddStickerToSet
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                name=name,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def answer_callback_query(
            self,
            callback_query_id: int,
            text: str,
            show_alert: bool,
            url: str,
            cache_time: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of a callback query; for bots only
        
        Params:
            callback_query_id (:class:`int`)
                Identifier of the callback query
            
            text (:class:`str`)
                Text of the answer
            
            show_alert (:class:`bool`)
                If true, an alert should be shown to the user instead of a toast notification
            
            url (:class:`str`)
                URL to be opened
            
            cache_time (:class:`int`)
                Time during which the result of the query can be cached, in seconds
            
        """
        _constructor = AnswerCallbackQuery.construct if skip_validation else AnswerCallbackQuery
        
        return await self.client.request(
            _constructor(
                callback_query_id=callback_query_id,
                text=text,
                show_alert=show_alert,
                url=url,
                cache_time=cache_time,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def answer_custom_query(
            self,
            custom_query_id: int,
            data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Answers a custom query; for bots only
        
        Params:
            custom_query_id (:class:`int`)
                Identifier of a custom query
            
            data (:class:`str`)
                JSON-serialized answer to the query
            
        """
        _constructor = AnswerCustomQuery.construct if skip_validation else AnswerCustomQuery
        
        return await self.client.request(
            _constructor(
                custom_query_id=custom_query_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def answer_inline_query(
            self,
            inline_query_id: int,
            is_personal: bool,
            results: list[InputInlineQueryResult],
            cache_time: int,
            next_offset: str,
            switch_pm_text: str,
            switch_pm_parameter: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of an inline query; for bots only
        
        Params:
            inline_query_id (:class:`int`)
                Identifier of the inline query
            
            is_personal (:class:`bool`)
                True, if the result of the query can be cached for the specified user
            
            results (:obj:`list[InputInlineQueryResult]`)
                The results of the query
            
            cache_time (:class:`int`)
                Allowed time to cache the results of the query, in seconds
            
            next_offset (:class:`str`)
                Offset for the next inline query; pass an empty string if there are no more results
            
            switch_pm_text (:class:`str`)
                If non-empty, this text should be shown on the button that opens a private chat with the bot and sends a start message to the bot with the parameter switch_pm_parameter
            
            switch_pm_parameter (:class:`str`)
                The parameter for the bot start message
            
        """
        _constructor = AnswerInlineQuery.construct if skip_validation else AnswerInlineQuery
        
        return await self.client.request(
            _constructor(
                inline_query_id=inline_query_id,
                is_personal=is_personal,
                results=results,
                cache_time=cache_time,
                next_offset=next_offset,
                switch_pm_text=switch_pm_text,
                switch_pm_parameter=switch_pm_parameter,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def answer_pre_checkout_query(
            self,
            pre_checkout_query_id: int,
            error_message: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of a pre-checkout query; for bots only
        
        Params:
            pre_checkout_query_id (:class:`int`)
                Identifier of the pre-checkout query
            
            error_message (:class:`str`)
                An error message, empty on success
            
        """
        _constructor = AnswerPreCheckoutQuery.construct if skip_validation else AnswerPreCheckoutQuery
        
        return await self.client.request(
            _constructor(
                pre_checkout_query_id=pre_checkout_query_id,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def answer_shipping_query(
            self,
            shipping_query_id: int,
            shipping_options: list[ShippingOption],
            error_message: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the result of a shipping query; for bots only
        
        Params:
            shipping_query_id (:class:`int`)
                Identifier of the shipping query
            
            shipping_options (:obj:`list[ShippingOption]`)
                Available shipping options
            
            error_message (:class:`str`)
                An error message, empty on success
            
        """
        _constructor = AnswerShippingQuery.construct if skip_validation else AnswerShippingQuery
        
        return await self.client.request(
            _constructor(
                shipping_query_id=shipping_query_id,
                shipping_options=shipping_options,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def ban_chat_member(
            self,
            chat_id: int,
            user_id: int,
            banned_until_date: int,
            revoke_messages: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Bans a member in a chat. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            user_id (:class:`int`)
                Identifier of the user
            
            banned_until_date (:class:`int`)
                Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups
            
            revoke_messages (:class:`bool`)
                Pass true to delete all messages in the chat for the user. Always true for supergroups and channels
            
        """
        _constructor = BanChatMember.construct if skip_validation else BanChatMember
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
                banned_until_date=banned_until_date,
                revoke_messages=revoke_messages,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def block_message_sender_from_replies(
            self,
            message_id: int,
            delete_message: bool,
            delete_all_messages: bool,
            report_spam: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Blocks an original sender of a message in the Replies chat
        
        Params:
            message_id (:class:`int`)
                The identifier of an incoming message in the Replies chat
            
            delete_message (:class:`bool`)
                Pass true if the message must be deleted
            
            delete_all_messages (:class:`bool`)
                Pass true if all messages from the same sender must be deleted
            
            report_spam (:class:`bool`)
                Pass true if the sender must be reported to the Telegram moderators
            
        """
        _constructor = BlockMessageSenderFromReplies.construct if skip_validation else BlockMessageSenderFromReplies
        
        return await self.client.request(
            _constructor(
                message_id=message_id,
                delete_message=delete_message,
                delete_all_messages=delete_all_messages,
                report_spam=report_spam,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def can_transfer_ownership(self, *, request_id: str = None, request_timeout: int = None) -> CanTransferOwnershipResult:
        """
        Checks whether the current session can be used to transfer a chat ownership to another user
        
        """
        return await self.client.request(
            CanTransferOwnership(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def cancel_download_file(
            self,
            file_id: int,
            only_if_pending: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Stops the downloading of a file. If a file has already been downloaded, does nothing
        
        Params:
            file_id (:class:`int`)
                Identifier of a file to stop downloading
            
            only_if_pending (:class:`bool`)
                Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server
            
        """
        _constructor = CancelDownloadFile.construct if skip_validation else CancelDownloadFile
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
                only_if_pending=only_if_pending,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def cancel_upload_file(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Stops the uploading of a file. Supported only for files uploaded by using uploadFile. For other files the behavior is undefined
        
        Params:
            file_id (:class:`int`)
                Identifier of the file to stop uploading
            
        """
        _constructor = CancelUploadFile.construct if skip_validation else CancelUploadFile
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def change_imported_contacts(
            self,
            contacts: list[Contact],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ImportedContacts:
        """
        Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts. Query result depends on the result of the previous query, so only one query is possible at the same time
        
        Params:
            contacts (:obj:`list[Contact]`)
                The new list of contacts, contact's vCard are ignored and are not imported
            
        """
        _constructor = ChangeImportedContacts.construct if skip_validation else ChangeImportedContacts
        
        return await self.client.request(
            _constructor(
                contacts=contacts,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def change_phone_number(
            self,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AuthenticationCodeInfo:
        """
        Changes the phone number of the user and sends an authentication code to the user's new phone number. On success, returns information about the sent code
        
        Params:
            phone_number (:class:`str`)
                The new phone number of the user in international format
            
            settings (:class:`PhoneNumberAuthenticationSettings`)
                Settings for the authentication of the user's phone number
            
        """
        _constructor = ChangePhoneNumber.construct if skip_validation else ChangePhoneNumber
        
        return await self.client.request(
            _constructor(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def change_sticker_set(
            self,
            set_id: int,
            is_installed: bool,
            is_archived: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Installs/uninstalls or activates/archives a sticker set
        
        Params:
            set_id (:class:`int`)
                Identifier of the sticker set
            
            is_installed (:class:`bool`)
                The new value of is_installed
            
            is_archived (:class:`bool`)
                The new value of is_archived. A sticker set can't be installed and archived simultaneously
            
        """
        _constructor = ChangeStickerSet.construct if skip_validation else ChangeStickerSet
        
        return await self.client.request(
            _constructor(
                set_id=set_id,
                is_installed=is_installed,
                is_archived=is_archived,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_authentication_bot_token(
            self,
            token: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in
        
        Params:
            token (:class:`str`)
                The bot token
            
        """
        _constructor = CheckAuthenticationBotToken.construct if skip_validation else CheckAuthenticationBotToken
        
        return await self.client.request(
            _constructor(
                token=token,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_authentication_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode
        
        Params:
            code (:class:`str`)
                The verification code received via SMS, Telegram message, phone call, or flash call
            
        """
        _constructor = CheckAuthenticationCode.construct if skip_validation else CheckAuthenticationCode
        
        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_authentication_password(
            self,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication password for correctness. Works only when the current authorization state is authorizationStateWaitPassword
        
        Params:
            password (:class:`str`)
                The password to check
            
        """
        _constructor = CheckAuthenticationPassword.construct if skip_validation else CheckAuthenticationPassword
        
        return await self.client.request(
            _constructor(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_change_phone_number_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the authentication code sent to confirm a new phone number of the user
        
        Params:
            code (:class:`str`)
                Verification code received by SMS, phone call or flash call
            
        """
        _constructor = CheckChangePhoneNumberCode.construct if skip_validation else CheckChangePhoneNumberCode
        
        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_chat_invite_link(
            self,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinkInfo:
        """
        Checks the validity of an invite link for a chat and returns information about the corresponding chat
        
        Params:
            invite_link (:class:`str`)
                Invite link to be checked; must have URL "t.me", "telegram.me", or "telegram.dog" and query beginning with "/joinchat/" or "/+"
            
        """
        _constructor = CheckChatInviteLink.construct if skip_validation else CheckChatInviteLink
        
        return await self.client.request(
            _constructor(
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_chat_username(
            self,
            chat_id: int,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CheckChatUsernameResult:
        """
        Checks whether a username can be set for a chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier; should be identifier of a supergroup chat, or a channel chat, or a private chat with self, or zero if chat is being created
            
            username (:class:`str`)
                Username to be checked
            
        """
        _constructor = CheckChatUsername.construct if skip_validation else CheckChatUsername
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_created_public_chats_limit(
            self,
            type_: PublicChatType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached
        
        Params:
            type_ (:class:`PublicChatType`)
                Type of the public chats, for which to check the limit
            
        """
        _constructor = CheckCreatedPublicChatsLimit.construct if skip_validation else CheckCreatedPublicChatsLimit
        
        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_database_encryption_key(
            self,
            encryption_key: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the database encryption key for correctness. Works only when the current authorization state is authorizationStateWaitEncryptionKey
        
        Params:
            encryption_key (:class:`str`)
                Encryption key to check or set up
            
        """
        _constructor = CheckDatabaseEncryptionKey.construct if skip_validation else CheckDatabaseEncryptionKey
        
        return await self.client.request(
            _constructor(
                encryption_key=encryption_key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_email_address_verification_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the email address verification code for Telegram Passport
        
        Params:
            code (:class:`str`)
                Verification code
            
        """
        _constructor = CheckEmailAddressVerificationCode.construct if skip_validation else CheckEmailAddressVerificationCode
        
        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_phone_number_confirmation_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks phone number confirmation code
        
        Params:
            code (:class:`str`)
                The phone number confirmation code
            
        """
        _constructor = CheckPhoneNumberConfirmationCode.construct if skip_validation else CheckPhoneNumberConfirmationCode
        
        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_phone_number_verification_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Checks the phone number verification code for Telegram Passport
        
        Params:
            code (:class:`str`)
                Verification code
            
        """
        _constructor = CheckPhoneNumberVerificationCode.construct if skip_validation else CheckPhoneNumberVerificationCode
        
        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def check_recovery_email_address_code(
            self,
            code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Checks the 2-step verification recovery email address verification code
        
        Params:
            code (:class:`str`)
                Verification code
            
        """
        _constructor = CheckRecoveryEmailAddressCode.construct if skip_validation else CheckRecoveryEmailAddressCode
        
        return await self.client.request(
            _constructor(
                code=code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def clean_file_name(
            self,
            file_name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. Can be called synchronously
        
        Params:
            file_name (:class:`str`)
                File name or path to the file
            
        """
        _constructor = CleanFileName.construct if skip_validation else CleanFileName
        
        return await self.client.request(
            _constructor(
                file_name=file_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def clear_all_draft_messages(
            self,
            exclude_secret_chats: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Clears draft messages in all chats
        
        Params:
            exclude_secret_chats (:class:`bool`)
                If true, local draft messages in secret chats will not be cleared
            
        """
        _constructor = ClearAllDraftMessages.construct if skip_validation else ClearAllDraftMessages
        
        return await self.client.request(
            _constructor(
                exclude_secret_chats=exclude_secret_chats,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def clear_imported_contacts(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears all imported contacts, contact list remains unchanged
        
        """
        return await self.client.request(
            ClearImportedContacts(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def clear_recent_stickers(
            self,
            is_attached: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Clears the list of recently used stickers
        
        Params:
            is_attached (:class:`bool`)
                Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers
            
        """
        _constructor = ClearRecentStickers.construct if skip_validation else ClearRecentStickers
        
        return await self.client.request(
            _constructor(
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def clear_recently_found_chats(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Clears the list of recently found chats
        
        """
        return await self.client.request(
            ClearRecentlyFoundChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def close(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance. All databases will be flushed to disk and properly closed. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent. Can be called before initialization
        
        """
        return await self.client.request(
            Close(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def close_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = CloseChat.construct if skip_validation else CloseChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def close_secret_chat(
            self,
            secret_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Closes a secret chat, effectively transferring its state to secretChatStateClosed
        
        Params:
            secret_chat_id (:class:`int`)
                Secret chat identifier
            
        """
        _constructor = CloseSecretChat.construct if skip_validation else CloseSecretChat
        
        return await self.client.request(
            _constructor(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def confirm_qr_code_authentication(
            self,
            link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Session:
        """
        Confirms QR code authentication on another device. Returns created session on success
        
        Params:
            link (:class:`str`)
                A link from a QR code. The link must be scanned by the in-app camera
            
        """
        _constructor = ConfirmQrCodeAuthentication.construct if skip_validation else ConfirmQrCodeAuthentication
        
        return await self.client.request(
            _constructor(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_basic_group_chat(
            self,
            basic_group_id: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known basic group
        
        Params:
            basic_group_id (:class:`int`)
                Basic group identifier
            
            force (:class:`bool`)
                If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
            
        """
        _constructor = CreateBasicGroupChat.construct if skip_validation else CreateBasicGroupChat
        
        return await self.client.request(
            _constructor(
                basic_group_id=basic_group_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_call(
            self,
            user_id: int,
            protocol: CallProtocol,
            is_video: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CallId:
        """
        Creates a new call
        
        Params:
            user_id (:class:`int`)
                Identifier of the user to be called
            
            protocol (:class:`CallProtocol`)
                Description of the call protocols supported by the application
            
            is_video (:class:`bool`)
                True, if a video call needs to be created
            
        """
        _constructor = CreateCall.construct if skip_validation else CreateCall
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                protocol=protocol,
                is_video=is_video,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_chat_filter(
            self,
            filter_: ChatFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatFilterInfo:
        """
        Creates new chat filter. Returns information about the created chat filter
        
        Params:
            filter_ (:class:`ChatFilter`)
                Chat filter
            
        """
        _constructor = CreateChatFilter.construct if skip_validation else CreateChatFilter
        
        return await self.client.request(
            _constructor(
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_chat_invite_link(
            self,
            chat_id: int,
            expire_date: int,
            member_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Creates a new invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            expire_date (:class:`int`)
                Point in time (Unix timestamp) when the link will expire; pass 0 if never
            
            member_limit (:class:`int`)
                Maximum number of chat members that can join the chat by the link simultaneously; 0-99999; pass 0 if not limited
            
        """
        _constructor = CreateChatInviteLink.construct if skip_validation else CreateChatInviteLink
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                expire_date=expire_date,
                member_limit=member_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_new_basic_group_chat(
            self,
            user_ids: list[int],
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat
        
        Params:
            user_ids (:obj:`list[int]`)
                Identifiers of users to be added to the basic group
            
            title (:class:`str`)
                Title of the new basic group; 1-128 characters
            
        """
        _constructor = CreateNewBasicGroupChat.construct if skip_validation else CreateNewBasicGroupChat
        
        return await self.client.request(
            _constructor(
                user_ids=user_ids,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_new_secret_chat(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new secret chat. Returns the newly created chat
        
        Params:
            user_id (:class:`int`)
                Identifier of the target user
            
        """
        _constructor = CreateNewSecretChat.construct if skip_validation else CreateNewSecretChat
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_new_sticker_set(
            self,
            user_id: int,
            title: str,
            name: str,
            is_masks: bool,
            stickers: list[InputSticker],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Creates a new sticker set; for bots only. Returns the newly created sticker set
        
        Params:
            user_id (:class:`int`)
                Sticker set owner
            
            title (:class:`str`)
                Sticker set title; 1-64 characters
            
            name (:class:`str`)
                Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive); 1-64 characters
            
            is_masks (:class:`bool`)
                True, if stickers are masks. Animated stickers can't be masks
            
            stickers (:obj:`list[InputSticker]`)
                List of stickers to be added to the set; must be non-empty. All stickers must be of the same type
            
        """
        _constructor = CreateNewStickerSet.construct if skip_validation else CreateNewStickerSet
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                title=title,
                name=name,
                is_masks=is_masks,
                stickers=stickers,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_new_supergroup_chat(
            self,
            title: str,
            is_channel: bool,
            param_description: str,
            location: ChatLocation,
            for_import: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat
        
        Params:
            title (:class:`str`)
                Title of the new chat; 1-128 characters
            
            is_channel (:class:`bool`)
                True, if a channel chat needs to be created
            
            param_description (:class:`str`)
                Chat description; 0-255 characters
            
            location (:class:`ChatLocation`)
                Chat location if a location-based supergroup is being created
            
            for_import (:class:`bool`)
                True, if the supergroup is created for importing messages using importMessage
            
        """
        _constructor = CreateNewSupergroupChat.construct if skip_validation else CreateNewSupergroupChat
        
        return await self.client.request(
            _constructor(
                title=title,
                is_channel=is_channel,
                param_description=param_description,
                location=location,
                for_import=for_import,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_private_chat(
            self,
            user_id: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a given user
        
        Params:
            user_id (:class:`int`)
                User identifier
            
            force (:class:`bool`)
                If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
            
        """
        _constructor = CreatePrivateChat.construct if skip_validation else CreatePrivateChat
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_secret_chat(
            self,
            secret_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known secret chat
        
        Params:
            secret_chat_id (:class:`int`)
                Secret chat identifier
            
        """
        _constructor = CreateSecretChat.construct if skip_validation else CreateSecretChat
        
        return await self.client.request(
            _constructor(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_supergroup_chat(
            self,
            supergroup_id: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns an existing chat corresponding to a known supergroup or channel
        
        Params:
            supergroup_id (:class:`int`)
                Supergroup or channel identifier
            
            force (:class:`bool`)
                If true, the chat will be created without network request. In this case all information about the chat except its type, title and photo can be incorrect
            
        """
        _constructor = CreateSupergroupChat.construct if skip_validation else CreateSupergroupChat
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_temporary_password(
            self,
            password: str,
            valid_for: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TemporaryPasswordState:
        """
        Creates a new temporary password for processing payments
        
        Params:
            password (:class:`str`)
                Persistent user password
            
            valid_for (:class:`int`)
                Time during which the temporary password will be valid, in seconds; should be between 60 and 86400
            
        """
        _constructor = CreateTemporaryPassword.construct if skip_validation else CreateTemporaryPassword
        
        return await self.client.request(
            _constructor(
                password=password,
                valid_for=valid_for,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def create_voice_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GroupCallId:
        """
        Creates a voice chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_voice_chats rights
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = CreateVoiceChat.construct if skip_validation else CreateVoiceChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_account(
            self,
            reason: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword
        
        Params:
            reason (:class:`str`)
                The reason why the account was deleted; optional
            
        """
        _constructor = DeleteAccount.construct if skip_validation else DeleteAccount
        
        return await self.client.request(
            _constructor(
                reason=reason,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_all_call_messages(
            self,
            revoke: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all call messages
        
        Params:
            revoke (:class:`bool`)
                Pass true to delete the messages for all users
            
        """
        _constructor = DeleteAllCallMessages.construct if skip_validation else DeleteAllCallMessages
        
        return await self.client.request(
            _constructor(
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_all_revoked_chat_invite_links(
            self,
            chat_id: int,
            creator_user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            creator_user_id (:class:`int`)
                User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner
            
        """
        _constructor = DeleteAllRevokedChatInviteLinks.construct if skip_validation else DeleteAllRevokedChatInviteLinks
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a chat along with all messages in the corresponding chat for all chat members; requires owner privileges. For group chats this will release the username and remove all members. Chats with more than 1000 members can't be deleted using this method
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = DeleteChat.construct if skip_validation else DeleteChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_chat_filter(
            self,
            chat_filter_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes existing chat filter
        
        Params:
            chat_filter_id (:class:`int`)
                Chat filter identifier
            
        """
        _constructor = DeleteChatFilter.construct if skip_validation else DeleteChatFilter
        
        return await self.client.request(
            _constructor(
                chat_filter_id=chat_filter_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_chat_history(
            self,
            chat_id: int,
            remove_from_chat_list: bool,
            revoke: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all messages in the chat. Use Chat.can_be_deleted_only_for_self and Chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            remove_from_chat_list (:class:`bool`)
                Pass true if the chat should be removed from the chat list
            
            revoke (:class:`bool`)
                Pass true to try to delete chat history for all users
            
        """
        _constructor = DeleteChatHistory.construct if skip_validation else DeleteChatHistory
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                remove_from_chat_list=remove_from_chat_list,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_chat_messages_from_user(
            self,
            chat_id: int,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all messages sent by the specified user to a chat. Supported only for supergroups; requires can_delete_messages administrator privileges
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            user_id (:class:`int`)
                User identifier
            
        """
        _constructor = DeleteChatMessagesFromUser.construct if skip_validation else DeleteChatMessagesFromUser
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_chat_reply_markup(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a ForceReply reply markup has been used. UpdateChatReplyMarkup will be sent if the reply markup will be changed
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_id (:class:`int`)
                The message identifier of the used keyboard
            
        """
        _constructor = DeleteChatReplyMarkup.construct if skip_validation else DeleteChatReplyMarkup
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_file(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a file from the TDLib file cache
        
        Params:
            file_id (:class:`int`)
                Identifier of the file to delete
            
        """
        _constructor = DeleteFile.construct if skip_validation else DeleteFile
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_language_pack(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted. Can be called before authorization
        
        Params:
            language_pack_id (:class:`str`)
                Identifier of the language pack to delete
            
        """
        _constructor = DeleteLanguagePack.construct if skip_validation else DeleteLanguagePack
        
        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_messages(
            self,
            chat_id: int,
            message_ids: list[int],
            revoke: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes messages
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_ids (:obj:`list[int]`)
                Identifiers of the messages to be deleted
            
            revoke (:class:`bool`)
                Pass true to try to delete messages for all chat members. Always true for supergroups, channels and secret chats
            
        """
        _constructor = DeleteMessages.construct if skip_validation else DeleteMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=revoke,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_passport_element(
            self,
            type_: PassportElementType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a Telegram Passport element
        
        Params:
            type_ (:class:`PassportElementType`)
                Element type
            
        """
        _constructor = DeletePassportElement.construct if skip_validation else DeletePassportElement
        
        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_profile_photo(
            self,
            profile_photo_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes a profile photo
        
        Params:
            profile_photo_id (:class:`int`)
                Identifier of the profile photo to delete
            
        """
        _constructor = DeleteProfilePhoto.construct if skip_validation else DeleteProfilePhoto
        
        return await self.client.request(
            _constructor(
                profile_photo_id=profile_photo_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_revoked_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            invite_link (:class:`str`)
                Invite link to revoke
            
        """
        _constructor = DeleteRevokedChatInviteLink.construct if skip_validation else DeleteRevokedChatInviteLink
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_saved_credentials(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes saved credentials for all payment provider bots
        
        """
        return await self.client.request(
            DeleteSavedCredentials(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def delete_saved_order_info(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Deletes saved order info
        
        """
        return await self.client.request(
            DeleteSavedOrderInfo(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def destroy(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance, destroying all local data without a proper logout. The current user session will remain in the list of all active sessions. All local data will be destroyed. After the destruction completes updateAuthorizationState with authorizationStateClosed will be sent. Can be called before authorization
        
        """
        return await self.client.request(
            Destroy(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def disable_proxy(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Disables the currently enabled proxy. Can be called before authorization
        
        """
        return await self.client.request(
            DisableProxy(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def discard_call(
            self,
            call_id: int,
            is_disconnected: bool,
            duration: int,
            is_video: bool,
            connection_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Discards a call
        
        Params:
            call_id (:class:`int`)
                Call identifier
            
            is_disconnected (:class:`bool`)
                True, if the user was disconnected
            
            duration (:class:`int`)
                The call duration, in seconds
            
            is_video (:class:`bool`)
                True, if the call was a video call
            
            connection_id (:class:`int`)
                Identifier of the connection used during the call
            
        """
        _constructor = DiscardCall.construct if skip_validation else DiscardCall
        
        return await self.client.request(
            _constructor(
                call_id=call_id,
                is_disconnected=is_disconnected,
                duration=duration,
                is_video=is_video,
                connection_id=connection_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def discard_group_call(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Discards a group call. Requires groupCall.can_be_managed
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
        """
        _constructor = DiscardGroupCall.construct if skip_validation else DiscardGroupCall
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def disconnect_all_websites(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Disconnects all websites from the current user's Telegram account
        
        """
        return await self.client.request(
            DisconnectAllWebsites(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def disconnect_website(
            self,
            website_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Disconnects website from the current user's Telegram account
        
        Params:
            website_id (:class:`int`)
                Website identifier
            
        """
        _constructor = DisconnectWebsite.construct if skip_validation else DisconnectWebsite
        
        return await self.client.request(
            _constructor(
                website_id=website_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def download_file(
            self,
            file_id: int,
            priority: int,
            offset: int,
            limit: int,
            synchronous: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates
        
        Params:
            file_id (:class:`int`)
                Identifier of the file to download
            
            priority (:class:`int`)
                Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile was called will be downloaded first
            
            offset (:class:`int`)
                The starting position from which the file should be downloaded
            
            limit (:class:`int`)
                Number of bytes which should be downloaded starting from the "offset" position before the download will be automatically cancelled; use 0 to download without a limit
            
            synchronous (:class:`bool`)
                If false, this request returns file state just after the download has been started. If true, this request returns file state only after the download has succeeded, has failed, has been cancelled or a new downloadFile request with different offset/limit parameters was sent
            
        """
        _constructor = DownloadFile.construct if skip_validation else DownloadFile
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
                priority=priority,
                offset=offset,
                limit=limit,
                synchronous=synchronous,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_chat_filter(
            self,
            chat_filter_id: int,
            filter_: ChatFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatFilterInfo:
        """
        Edits existing chat filter. Returns information about the edited chat filter
        
        Params:
            chat_filter_id (:class:`int`)
                Chat filter identifier
            
            filter_ (:class:`ChatFilter`)
                The edited chat filter
            
        """
        _constructor = EditChatFilter.construct if skip_validation else EditChatFilter
        
        return await self.client.request(
            _constructor(
                chat_filter_id=chat_filter_id,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            expire_date: int,
            member_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            invite_link (:class:`str`)
                Invite link to be edited
            
            expire_date (:class:`int`)
                Point in time (Unix timestamp) when the link will expire; pass 0 if never
            
            member_limit (:class:`int`)
                Maximum number of chat members that can join the chat by the link simultaneously; 0-99999; pass 0 if not limited
            
        """
        _constructor = EditChatInviteLink.construct if skip_validation else EditChatInviteLink
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
                expire_date=expire_date,
                member_limit=member_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_custom_language_pack_info(
            self,
            info: LanguagePackInfo,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits information about a custom local language pack in the current localization target. Can be called before authorization
        
        Params:
            info (:class:`LanguagePackInfo`)
                New information about the custom local language pack
            
        """
        _constructor = EditCustomLanguagePackInfo.construct if skip_validation else EditCustomLanguagePackInfo
        
        return await self.client.request(
            _constructor(
                info=info,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_inline_message_caption(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            caption: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the caption of an inline message sent via a bot; for bots only
        
        Params:
            inline_message_id (:class:`str`)
                Inline message identifier
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup
            
            caption (:class:`FormattedText`)
                New message content caption; 0-GetOption("message_caption_length_max") characters
            
        """
        _constructor = EditInlineMessageCaption.construct if skip_validation else EditInlineMessageCaption
        
        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_inline_message_live_location(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            location: Location,
            heading: int,
            proximity_alert_radius: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the content of a live location in an inline message sent via a bot; for bots only
        
        Params:
            inline_message_id (:class:`str`)
                Inline message identifier
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup
            
            location (:class:`Location`)
                New location content of the message; may be null. Pass null to stop sharing the live location
            
            heading (:class:`int`)
                The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
            
            proximity_alert_radius (:class:`int`)
                The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
            
        """
        _constructor = EditInlineMessageLiveLocation.construct if skip_validation else EditInlineMessageLiveLocation
        
        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                location=location,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_inline_message_media(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only
        
        Params:
            inline_message_id (:class:`str`)
                Inline message identifier
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup; for bots only
            
            input_message_content (:class:`InputMessageContent`)
                New content of the message. Must be one of the following types: InputMessageAnimation, InputMessageAudio, InputMessageDocument, InputMessagePhoto or InputMessageVideo
            
        """
        _constructor = EditInlineMessageMedia.construct if skip_validation else EditInlineMessageMedia
        
        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_inline_message_reply_markup(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the reply markup of an inline message sent via a bot; for bots only
        
        Params:
            inline_message_id (:class:`str`)
                Inline message identifier
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup
            
        """
        _constructor = EditInlineMessageReplyMarkup.construct if skip_validation else EditInlineMessageReplyMarkup
        
        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_inline_message_text(
            self,
            inline_message_id: str,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the text of an inline text or game message sent via a bot; for bots only
        
        Params:
            inline_message_id (:class:`str`)
                Inline message identifier
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup
            
            input_message_content (:class:`InputMessageContent`)
                New text content of the message. Should be of type InputMessageText
            
        """
        _constructor = EditInlineMessageText.construct if skip_validation else EditInlineMessageText
        
        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_message_caption(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            caption: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the message content caption. Returns the edited message after the edit is completed on the server side
        
        Params:
            chat_id (:class:`int`)
                The chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup; for bots only
            
            caption (:class:`FormattedText`)
                New message content caption; 0-GetOption("message_caption_length_max") characters
            
        """
        _constructor = EditMessageCaption.construct if skip_validation else EditMessageCaption
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                caption=caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_message_live_location(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            location: Location,
            heading: int,
            proximity_alert_radius: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location. Returns the edited message after the edit is completed on the server side
        
        Params:
            chat_id (:class:`int`)
                The chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup; for bots only
            
            location (:class:`Location`)
                New location content of the message; may be null. Pass null to stop sharing the live location
            
            heading (:class:`int`)
                The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
            
            proximity_alert_radius (:class:`int`)
                The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled
            
        """
        _constructor = EditMessageLiveLocation.construct if skip_validation else EditMessageLiveLocation
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                location=location,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_message_media(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the content of a message with an animation, an audio, a document, a photo or a video. The media in the message can't be replaced if the message was set to self-destruct. Media can't be replaced by self-destructing media. Media in an album can be edited only to contain a photo or a video. Returns the edited message after the edit is completed on the server side
        
        Params:
            chat_id (:class:`int`)
                The chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup; for bots only
            
            input_message_content (:class:`InputMessageContent`)
                New content of the message. Must be one of the following types: InputMessageAnimation, InputMessageAudio, InputMessageDocument, InputMessagePhoto or InputMessageVideo
            
        """
        _constructor = EditMessageMedia.construct if skip_validation else EditMessageMedia
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_message_reply_markup(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side
        
        Params:
            chat_id (:class:`int`)
                The chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup
            
        """
        _constructor = EditMessageReplyMarkup.construct if skip_validation else EditMessageReplyMarkup
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_message_scheduling_state(
            self,
            chat_id: int,
            message_id: int,
            scheduling_state: MessageSchedulingState,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed
        
        Params:
            chat_id (:class:`int`)
                The chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message
            
            scheduling_state (:class:`MessageSchedulingState`)
                The new message scheduling state. Pass null to send the message immediately
            
        """
        _constructor = EditMessageSchedulingState.construct if skip_validation else EditMessageSchedulingState
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                scheduling_state=scheduling_state,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_message_text(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side
        
        Params:
            chat_id (:class:`int`)
                The chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup; for bots only
            
            input_message_content (:class:`InputMessageContent`)
                New text content of the message. Should be of type InputMessageText
            
        """
        _constructor = EditMessageText.construct if skip_validation else EditMessageText
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def edit_proxy(
            self,
            proxy_id: int,
            server: str,
            port: int,
            enable: bool,
            type_: ProxyType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Proxy:
        """
        Edits an existing proxy server for network requests. Can be called before authorization
        
        Params:
            proxy_id (:class:`int`)
                Proxy identifier
            
            server (:class:`str`)
                Proxy server IP address
            
            port (:class:`int`)
                Proxy server port
            
            enable (:class:`bool`)
                True, if the proxy should be enabled
            
            type_ (:class:`ProxyType`)
                Proxy type
            
        """
        _constructor = EditProxy.construct if skip_validation else EditProxy
        
        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
                server=server,
                port=port,
                enable=enable,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def enable_proxy(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Enables a proxy. Only one proxy can be enabled at a time. Can be called before authorization
        
        Params:
            proxy_id (:class:`int`)
                Proxy identifier
            
        """
        _constructor = EnableProxy.construct if skip_validation else EnableProxy
        
        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def end_group_call_recording(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Ends recording of a group call. Requires groupCall.can_be_managed group call flag
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
        """
        _constructor = EndGroupCallRecording.construct if skip_validation else EndGroupCallRecording
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def finish_file_generation(
            self,
            generation_id: int,
            error: Error,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Finishes the file generation
        
        Params:
            generation_id (:class:`int`)
                The identifier of the generation process
            
            error (:class:`Error`)
                If set, means that file generation has failed and should be terminated
            
        """
        _constructor = FinishFileGeneration.construct if skip_validation else FinishFileGeneration
        
        return await self.client.request(
            _constructor(
                generation_id=generation_id,
                error=error,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def forward_messages(
            self,
            chat_id: int,
            from_chat_id: int,
            message_ids: list[int],
            options: MessageSendOptions,
            send_copy: bool,
            remove_caption: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to which to forward messages
            
            from_chat_id (:class:`int`)
                Identifier of the chat from which to forward messages
            
            message_ids (:obj:`list[int]`)
                Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously
            
            options (:class:`MessageSendOptions`)
                Options to be used to send the messages
            
            send_copy (:class:`bool`)
                True, if content of the messages needs to be copied without links to the original messages. Always true if the messages are forwarded to a secret chat
            
            remove_caption (:class:`bool`)
                True, if media caption of message copies needs to be removed. Ignored if send_copy is false
            
        """
        _constructor = ForwardMessages.construct if skip_validation else ForwardMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                from_chat_id=from_chat_id,
                message_ids=message_ids,
                options=options,
                send_copy=send_copy,
                remove_caption=remove_caption,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_account_ttl(self, *, request_id: str = None, request_timeout: int = None) -> AccountTtl:
        """
        Returns the period of inactivity after which the account of the current user will automatically be deleted
        
        """
        return await self.client.request(
            GetAccountTtl(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_active_live_location_messages(self, *, request_id: str = None, request_timeout: int = None) -> Messages:
        """
        Returns all active live locations that should be updated by the application. The list is persistent across application restarts only if the message database is used
        
        """
        return await self.client.request(
            GetActiveLiveLocationMessages(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_active_sessions(self, *, request_id: str = None, request_timeout: int = None) -> Sessions:
        """
        Returns all active sessions of the current user
        
        """
        return await self.client.request(
            GetActiveSessions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_all_passport_elements(
            self,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElements:
        """
        Returns all available Telegram Passport elements
        
        Params:
            password (:class:`str`)
                Password of the current user
            
        """
        _constructor = GetAllPassportElements.construct if skip_validation else GetAllPassportElements
        
        return await self.client.request(
            _constructor(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_application_config(self, *, request_id: str = None, request_timeout: int = None) -> JsonValue:
        """
        Returns application config, provided by the server. Can be called before authorization
        
        """
        return await self.client.request(
            GetApplicationConfig(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_archived_sticker_sets(
            self,
            is_masks: bool,
            offset_sticker_set_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of archived sticker sets
        
        Params:
            is_masks (:class:`bool`)
                Pass true to return mask stickers sets; pass false to return ordinary sticker sets
            
            offset_sticker_set_id (:class:`int`)
                Identifier of the sticker set from which to return the result
            
            limit (:class:`int`)
                The maximum number of sticker sets to return
            
        """
        _constructor = GetArchivedStickerSets.construct if skip_validation else GetArchivedStickerSets
        
        return await self.client.request(
            _constructor(
                is_masks=is_masks,
                offset_sticker_set_id=offset_sticker_set_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_attached_sticker_sets(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of sticker sets attached to a file. Currently only photos and videos can have attached sticker sets
        
        Params:
            file_id (:class:`int`)
                File identifier
            
        """
        _constructor = GetAttachedStickerSets.construct if skip_validation else GetAttachedStickerSets
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_authorization_state(self, *, request_id: str = None, request_timeout: int = None) -> AuthorizationState:
        """
        Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
        
        """
        return await self.client.request(
            GetAuthorizationState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_auto_download_settings_presets(self, *, request_id: str = None, request_timeout: int = None) -> AutoDownloadSettingsPresets:
        """
        Returns auto-download settings presets for the current user
        
        """
        return await self.client.request(
            GetAutoDownloadSettingsPresets(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_available_voice_chat_aliases(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageSenders:
        """
        Returns list of user and chat, which can be used as aliases to join a voice chat in the chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = GetAvailableVoiceChatAliases.construct if skip_validation else GetAvailableVoiceChatAliases
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_background_url(
            self,
            name: str,
            type_: BackgroundType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Constructs a persistent HTTP URL for a background
        
        Params:
            name (:class:`str`)
                Background name
            
            type_ (:class:`BackgroundType`)
                Background type
            
        """
        _constructor = GetBackgroundUrl.construct if skip_validation else GetBackgroundUrl
        
        return await self.client.request(
            _constructor(
                name=name,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_backgrounds(
            self,
            for_dark_theme: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Backgrounds:
        """
        Returns backgrounds installed by the user
        
        Params:
            for_dark_theme (:class:`bool`)
                True, if the backgrounds must be ordered for dark theme
            
        """
        _constructor = GetBackgrounds.construct if skip_validation else GetBackgrounds
        
        return await self.client.request(
            _constructor(
                for_dark_theme=for_dark_theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_bank_card_info(
            self,
            bank_card_number: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BankCardInfo:
        """
        Returns information about a bank card
        
        Params:
            bank_card_number (:class:`str`)
                The bank card number
            
        """
        _constructor = GetBankCardInfo.construct if skip_validation else GetBankCardInfo
        
        return await self.client.request(
            _constructor(
                bank_card_number=bank_card_number,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_basic_group(
            self,
            basic_group_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BasicGroup:
        """
        Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot
        
        Params:
            basic_group_id (:class:`int`)
                Basic group identifier
            
        """
        _constructor = GetBasicGroup.construct if skip_validation else GetBasicGroup
        
        return await self.client.request(
            _constructor(
                basic_group_id=basic_group_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_basic_group_full_info(
            self,
            basic_group_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> BasicGroupFullInfo:
        """
        Returns full information about a basic group by its identifier
        
        Params:
            basic_group_id (:class:`int`)
                Basic group identifier
            
        """
        _constructor = GetBasicGroupFullInfo.construct if skip_validation else GetBasicGroupFullInfo
        
        return await self.client.request(
            _constructor(
                basic_group_id=basic_group_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_blocked_message_senders(
            self,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageSenders:
        """
        Returns users and chats that were blocked by the current user
        
        Params:
            offset (:class:`int`)
                Number of users and chats to skip in the result; must be non-negative
            
            limit (:class:`int`)
                The maximum number of users and chats to return; up to 100
            
        """
        _constructor = GetBlockedMessageSenders.construct if skip_validation else GetBlockedMessageSenders
        
        return await self.client.request(
            _constructor(
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_callback_query_answer(
            self,
            chat_id: int,
            message_id: int,
            payload: CallbackQueryPayload,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CallbackQueryAnswer:
        """
        Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat with the message
            
            message_id (:class:`int`)
                Identifier of the message from which the query originated
            
            payload (:class:`CallbackQueryPayload`)
                Query payload
            
        """
        _constructor = GetCallbackQueryAnswer.construct if skip_validation else GetCallbackQueryAnswer
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_callback_query_message(
            self,
            chat_id: int,
            message_id: int,
            callback_query_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message with the callback button that originated a callback query; for bots only
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat the message belongs to
            
            message_id (:class:`int`)
                Message identifier
            
            callback_query_id (:class:`int`)
                Identifier of the callback query
            
        """
        _constructor = GetCallbackQueryMessage.construct if skip_validation else GetCallbackQueryMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                callback_query_id=callback_query_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Returns information about a chat by its identifier, this is an offline request if the current user is not a bot
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = GetChat.construct if skip_validation else GetChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_administrators(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatAdministrators:
        """
        Returns a list of administrators of the chat with their custom titles
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = GetChatAdministrators.construct if skip_validation else GetChatAdministrators
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_event_log(
            self,
            chat_id: int,
            query: str,
            from_event_id: int,
            limit: int,
            filters: ChatEventLogFilters,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatEvents:
        """
        Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i. e., in order of decreasing event_id)
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            query (:class:`str`)
                Search query by which to filter events
            
            from_event_id (:class:`int`)
                Identifier of an event from which to return results. Use 0 to get results from the latest events
            
            limit (:class:`int`)
                The maximum number of events to return; up to 100
            
            filters (:class:`ChatEventLogFilters`)
                The types of events to return. By default, all types will be returned
            
            user_ids (:obj:`list[int]`)
                User identifiers by which to filter events. By default, events relating to all users will be returned
            
        """
        _constructor = GetChatEventLog.construct if skip_validation else GetChatEventLog
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                from_event_id=from_event_id,
                limit=limit,
                filters=filters,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_filter(
            self,
            chat_filter_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatFilter:
        """
        Returns information about a chat filter by its identifier
        
        Params:
            chat_filter_id (:class:`int`)
                Chat filter identifier
            
        """
        _constructor = GetChatFilter.construct if skip_validation else GetChatFilter
        
        return await self.client.request(
            _constructor(
                chat_filter_id=chat_filter_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_filter_default_icon_name(
            self,
            filter_: ChatFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns default icon name for a filter. Can be called synchronously
        
        Params:
            filter_ (:class:`ChatFilter`)
                Chat filter
            
        """
        _constructor = GetChatFilterDefaultIconName.construct if skip_validation else GetChatFilterDefaultIconName
        
        return await self.client.request(
            _constructor(
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_history(
            self,
            chat_id: int,
            from_message_id: int,
            offset: int,
            limit: int,
            only_local: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance the number of returned messages is chosen by the library. This is an offline request if only_local is true
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            from_message_id (:class:`int`)
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
            
            offset (:class:`int`)
                Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
            
            limit (:class:`int`)
                The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
            
            only_local (:class:`bool`)
                If true, returns only messages that are available locally without sending network requests
            
        """
        _constructor = GetChatHistory.construct if skip_validation else GetChatHistory
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                only_local=only_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            invite_link (:class:`str`)
                Invite link to get
            
        """
        _constructor = GetChatInviteLink.construct if skip_validation else GetChatInviteLink
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_invite_link_counts(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinkCounts:
        """
        Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = GetChatInviteLinkCounts.construct if skip_validation else GetChatInviteLinkCounts
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_invite_link_members(
            self,
            chat_id: int,
            invite_link: str,
            offset_member: ChatInviteLinkMember,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinkMembers:
        """
        Returns chat members joined a chat by an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            invite_link (:class:`str`)
                Invite link for which to return chat members
            
            offset_member (:class:`ChatInviteLinkMember`)
                A chat member from which to return next chat members; use null to get results from the beginning
            
            limit (:class:`int`)
                Maximum number of chat members to return
            
        """
        _constructor = GetChatInviteLinkMembers.construct if skip_validation else GetChatInviteLinkMembers
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
                offset_member=offset_member,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_invite_links(
            self,
            chat_id: int,
            creator_user_id: int,
            is_revoked: bool,
            offset_date: int,
            offset_invite_link: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinks:
        """
        Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            creator_user_id (:class:`int`)
                User identifier of a chat administrator. Must be an identifier of the current user for non-owner
            
            is_revoked (:class:`bool`)
                Pass true if revoked links needs to be returned instead of active or expired
            
            offset_date (:class:`int`)
                Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
            
            offset_invite_link (:class:`str`)
                Invite link starting after which to return invite links; use empty string to get results from the beginning
            
            limit (:class:`int`)
                Maximum number of invite links to return
            
        """
        _constructor = GetChatInviteLinks.construct if skip_validation else GetChatInviteLinks
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                creator_user_id=creator_user_id,
                is_revoked=is_revoked,
                offset_date=offset_date,
                offset_invite_link=offset_invite_link,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_lists_to_add_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatLists:
        """
        Returns chat lists to which the chat can be added. This is an offline request
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = GetChatListsToAddChat.construct if skip_validation else GetChatListsToAddChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_member(
            self,
            chat_id: int,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatMember:
        """
        Returns information about a single member of a chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            user_id (:class:`int`)
                User identifier
            
        """
        _constructor = GetChatMember.construct if skip_validation else GetChatMember
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_message_by_date(
            self,
            chat_id: int,
            date: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns the last message sent in a chat no later than the specified date
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            date (:class:`int`)
                Point in time (Unix timestamp) relative to which to search for messages
            
        """
        _constructor = GetChatMessageByDate.construct if skip_validation else GetChatMessageByDate
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                date=date,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_message_count(
            self,
            chat_id: int,
            filter_: SearchMessagesFilter,
            return_local: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Count:
        """
        Returns approximate number of messages of the specified type in the chat
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat in which to count messages
            
            filter_ (:class:`SearchMessagesFilter`)
                Filter for message content; searchMessagesFilterEmpty is unsupported in this function
            
            return_local (:class:`bool`)
                If true, returns count that is available locally without sending network requests, returning -1 if the number of messages is unknown
            
        """
        _constructor = GetChatMessageCount.construct if skip_validation else GetChatMessageCount
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                filter=filter_,
                return_local=return_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_notification_settings_exceptions(
            self,
            scope: NotificationSettingsScope,
            compare_sound: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns list of chats with non-default notification settings
        
        Params:
            scope (:class:`NotificationSettingsScope`)
                If specified, only chats from the specified scope will be returned
            
            compare_sound (:class:`bool`)
                If true, also chats with non-default sound will be returned
            
        """
        _constructor = GetChatNotificationSettingsExceptions.construct if skip_validation else GetChatNotificationSettingsExceptions
        
        return await self.client.request(
            _constructor(
                scope=scope,
                compare_sound=compare_sound,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_pinned_message(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a newest pinned message in the chat
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat the message belongs to
            
        """
        _constructor = GetChatPinnedMessage.construct if skip_validation else GetChatPinnedMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_scheduled_messages(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns all scheduled messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = GetChatScheduledMessages.construct if skip_validation else GetChatScheduledMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_statistics(
            self,
            chat_id: int,
            is_dark: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatStatistics:
        """
        Returns detailed statistics about a chat. Currently this method can be used only for supergroups and channels. Can be used only if SupergroupFullInfo.can_get_statistics == true
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            is_dark (:class:`bool`)
                Pass true if a dark theme is used by the application
            
        """
        _constructor = GetChatStatistics.construct if skip_validation else GetChatStatistics
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                is_dark=is_dark,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chat_statistics_url(
            self,
            chat_id: int,
            parameters: str,
            is_dark: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTP URL with the chat statistics. Currently this method of getting the statistics are disabled and can be deleted in the future
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            parameters (:class:`str`)
                Parameters from "tg://statsrefresh?params=******" link
            
            is_dark (:class:`bool`)
                Pass true if a URL with the dark theme must be returned
            
        """
        _constructor = GetChatStatisticsUrl.construct if skip_validation else GetChatStatisticsUrl
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                parameters=parameters,
                is_dark=is_dark,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_chats(
            self,
            chat_list: ChatList,
            offset_order: int,
            offset_chat_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns an ordered list of chats in a chat list. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. (For example, to get a list of chats from the beginning, the offset_order should be equal to a biggest signed 64-bit number 9223372036854775807 == 2^63 - 1). For optimal performance the number of returned chats is chosen by the library
        
        Params:
            chat_list (:class:`ChatList`)
                The chat list in which to return chats
            
            offset_order (:class:`int`)
                Chat order to return chats from
            
            offset_chat_id (:class:`int`)
                Chat identifier to return chats from
            
            limit (:class:`int`)
                The maximum number of chats to be returned. It is possible that fewer chats than the limit are returned even if the end of the list is not reached
            
        """
        _constructor = GetChats.construct if skip_validation else GetChats
        
        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                offset_order=offset_order,
                offset_chat_id=offset_chat_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_connected_websites(self, *, request_id: str = None, request_timeout: int = None) -> ConnectedWebsites:
        """
        Returns all website where the current user used Telegram to log in
        
        """
        return await self.client.request(
            GetConnectedWebsites(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_contacts(self, *, request_id: str = None, request_timeout: int = None) -> Users:
        """
        Returns all user contacts
        
        """
        return await self.client.request(
            GetContacts(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_countries(self, *, request_id: str = None, request_timeout: int = None) -> Countries:
        """
        Returns information about existing countries. Can be called before authorization
        
        """
        return await self.client.request(
            GetCountries(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_country_code(self, *, request_id: str = None, request_timeout: int = None) -> Text:
        """
        Uses the current IP address to find the current country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization
        
        """
        return await self.client.request(
            GetCountryCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_created_public_chats(
            self,
            type_: PublicChatType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns a list of public chats of the specified type, owned by the user
        
        Params:
            type_ (:class:`PublicChatType`)
                Type of the public chats to return
            
        """
        _constructor = GetCreatedPublicChats.construct if skip_validation else GetCreatedPublicChats
        
        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_current_state(self, *, request_id: str = None, request_timeout: int = None) -> Updates:
        """
        Returns all updates needed to restore current TDLib state, i.e. all actual UpdateAuthorizationState/UpdateUser/UpdateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization
        
        """
        return await self.client.request(
            GetCurrentState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_database_statistics(self, *, request_id: str = None, request_timeout: int = None) -> DatabaseStatistics:
        """
        Returns database statistics
        
        """
        return await self.client.request(
            GetDatabaseStatistics(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_deep_link_info(
            self,
            link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> DeepLinkInfo:
        """
        Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links. Can be called before authorization
        
        Params:
            link (:class:`str`)
                The link
            
        """
        _constructor = GetDeepLinkInfo.construct if skip_validation else GetDeepLinkInfo
        
        return await self.client.request(
            _constructor(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_emoji_suggestions_url(
            self,
            language_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation
        
        Params:
            language_code (:class:`str`)
                Language code for which the emoji replacements will be suggested
            
        """
        _constructor = GetEmojiSuggestionsUrl.construct if skip_validation else GetEmojiSuggestionsUrl
        
        return await self.client.request(
            _constructor(
                language_code=language_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_external_link(
            self,
            link: str,
            allow_write_access: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed
        
        Params:
            link (:class:`str`)
                The HTTP link
            
            allow_write_access (:class:`bool`)
                True, if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages
            
        """
        _constructor = GetExternalLink.construct if skip_validation else GetExternalLink
        
        return await self.client.request(
            _constructor(
                link=link,
                allow_write_access=allow_write_access,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_external_link_info(
            self,
            link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LoginUrlInfo:
        """
        Returns information about an action to be done when the current user clicks an HTTP link. This method can be used to automatically authorize the current user on a website. Don't use this method for links from secret chats if link preview is disabled in secret chats
        
        Params:
            link (:class:`str`)
                The HTTP link
            
        """
        _constructor = GetExternalLinkInfo.construct if skip_validation else GetExternalLinkInfo
        
        return await self.client.request(
            _constructor(
                link=link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_favorite_stickers(self, *, request_id: str = None, request_timeout: int = None) -> Stickers:
        """
        Returns favorite stickers
        
        """
        return await self.client.request(
            GetFavoriteStickers(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_file(
            self,
            file_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Returns information about a file; this is an offline request
        
        Params:
            file_id (:class:`int`)
                Identifier of the file to get
            
        """
        _constructor = GetFile.construct if skip_validation else GetFile
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_file_downloaded_prefix_size(
            self,
            file_id: int,
            offset: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Count:
        """
        Returns file downloaded prefix size from a given offset
        
        Params:
            file_id (:class:`int`)
                Identifier of the file
            
            offset (:class:`int`)
                Offset from which downloaded prefix size should be calculated
            
        """
        _constructor = GetFileDownloadedPrefixSize.construct if skip_validation else GetFileDownloadedPrefixSize
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
                offset=offset,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_file_extension(
            self,
            mime_type: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously
        
        Params:
            mime_type (:class:`str`)
                The MIME type of the file
            
        """
        _constructor = GetFileExtension.construct if skip_validation else GetFileExtension
        
        return await self.client.request(
            _constructor(
                mime_type=mime_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_file_mime_type(
            self,
            file_name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously
        
        Params:
            file_name (:class:`str`)
                The name of the file or path to the file
            
        """
        _constructor = GetFileMimeType.construct if skip_validation else GetFileMimeType
        
        return await self.client.request(
            _constructor(
                file_name=file_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_game_high_scores(
            self,
            chat_id: int,
            message_id: int,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GameHighScores:
        """
        Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only
        
        Params:
            chat_id (:class:`int`)
                The chat that contains the message with the game
            
            message_id (:class:`int`)
                Identifier of the message
            
            user_id (:class:`int`)
                User identifier
            
        """
        _constructor = GetGameHighScores.construct if skip_validation else GetGameHighScores
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_group_call(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GroupCall:
        """
        Returns information about a group call
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
        """
        _constructor = GetGroupCall.construct if skip_validation else GetGroupCall
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_group_call_invite_link(
            self,
            group_call_id: int,
            can_self_unmute: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns invite link to a voice chat in a public chat
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            can_self_unmute (:class:`bool`)
                Pass true if the invite_link should contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themself. Requires groupCall.can_be_managed group call flag
            
        """
        _constructor = GetGroupCallInviteLink.construct if skip_validation else GetGroupCallInviteLink
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                can_self_unmute=can_self_unmute,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_group_call_stream_segment(
            self,
            group_call_id: int,
            time_offset: int,
            scale: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FilePart:
        """
        Returns a file with a segment of a group call stream in a modified OGG format
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            time_offset (:class:`int`)
                Point in time when the stream segment begins; Unix timestamp in milliseconds
            
            scale (:class:`int`)
                Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
            
        """
        _constructor = GetGroupCallStreamSegment.construct if skip_validation else GetGroupCallStreamSegment
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                time_offset=time_offset,
                scale=scale,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_groups_in_common(
            self,
            user_id: int,
            offset_chat_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns a list of common group chats with a given user. Chats are sorted by their type and creation date
        
        Params:
            user_id (:class:`int`)
                User identifier
            
            offset_chat_id (:class:`int`)
                Chat identifier starting from which to return chats; use 0 for the first request
            
            limit (:class:`int`)
                The maximum number of chats to be returned; up to 100
            
        """
        _constructor = GetGroupsInCommon.construct if skip_validation else GetGroupsInCommon
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                offset_chat_id=offset_chat_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_imported_contact_count(self, *, request_id: str = None, request_timeout: int = None) -> Count:
        """
        Returns the total number of imported contacts
        
        """
        return await self.client.request(
            GetImportedContactCount(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_inactive_supergroup_chats(self, *, request_id: str = None, request_timeout: int = None) -> Chats:
        """
        Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error
        
        """
        return await self.client.request(
            GetInactiveSupergroupChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_inline_game_high_scores(
            self,
            inline_message_id: str,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GameHighScores:
        """
        Returns game high scores and some part of the high score table in the range of the specified user; for bots only
        
        Params:
            inline_message_id (:class:`str`)
                Inline message identifier
            
            user_id (:class:`int`)
                User identifier
            
        """
        _constructor = GetInlineGameHighScores.construct if skip_validation else GetInlineGameHighScores
        
        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_inline_query_results(
            self,
            bot_user_id: int,
            chat_id: int,
            user_location: Location,
            query: str,
            offset: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> InlineQueryResults:
        """
        Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
        
        Params:
            bot_user_id (:class:`int`)
                The identifier of the target bot
            
            chat_id (:class:`int`)
                Identifier of the chat where the query was sent
            
            user_location (:class:`Location`)
                Location of the user, only if needed
            
            query (:class:`str`)
                Text of the query
            
            offset (:class:`str`)
                Offset of the first entry to return
            
        """
        _constructor = GetInlineQueryResults.construct if skip_validation else GetInlineQueryResults
        
        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                user_location=user_location,
                query=query,
                offset=offset,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_installed_sticker_sets(
            self,
            is_masks: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of installed sticker sets
        
        Params:
            is_masks (:class:`bool`)
                Pass true to return mask sticker sets; pass false to return ordinary sticker sets
            
        """
        _constructor = GetInstalledStickerSets.construct if skip_validation else GetInstalledStickerSets
        
        return await self.client.request(
            _constructor(
                is_masks=is_masks,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_invite_text(self, *, request_id: str = None, request_timeout: int = None) -> Text:
        """
        Returns the default text for invitation messages to be used as a placeholder when the current user invites friends to Telegram
        
        """
        return await self.client.request(
            GetInviteText(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_json_string(
            self,
            json_value: JsonValue,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously
        
        Params:
            json_value (:class:`JsonValue`)
                The JsonValue object
            
        """
        _constructor = GetJsonString.construct if skip_validation else GetJsonString
        
        return await self.client.request(
            _constructor(
                json_value=json_value,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_json_value(
            self,
            json_: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> JsonValue:
        """
        Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously
        
        Params:
            json_ (:class:`str`)
                The JSON-serialized string
            
        """
        _constructor = GetJsonValue.construct if skip_validation else GetJsonValue
        
        return await self.client.request(
            _constructor(
                json=json_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_language_pack_info(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LanguagePackInfo:
        """
        Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization
        
        Params:
            language_pack_id (:class:`str`)
                Language pack identifier
            
        """
        _constructor = GetLanguagePackInfo.construct if skip_validation else GetLanguagePackInfo
        
        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_language_pack_string(
            self,
            language_pack_database_path: str,
            localization_target: str,
            language_pack_id: str,
            key: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LanguagePackStringValue:
        """
        Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously
        
        Params:
            language_pack_database_path (:class:`str`)
                Path to the language pack database in which strings are stored
            
            localization_target (:class:`str`)
                Localization target to which the language pack belongs
            
            language_pack_id (:class:`str`)
                Language pack identifier
            
            key (:class:`str`)
                Language pack key of the string to be returned
            
        """
        _constructor = GetLanguagePackString.construct if skip_validation else GetLanguagePackString
        
        return await self.client.request(
            _constructor(
                language_pack_database_path=language_pack_database_path,
                localization_target=localization_target,
                language_pack_id=language_pack_id,
                key=key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_language_pack_strings(
            self,
            language_pack_id: str,
            keys: list[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LanguagePackStrings:
        """
        Returns strings from a language pack in the current localization target by their keys. Can be called before authorization
        
        Params:
            language_pack_id (:class:`str`)
                Language pack identifier of the strings to be returned
            
            keys (:obj:`list[str]`)
                Language pack keys of the strings to be returned; leave empty to request all available strings
            
        """
        _constructor = GetLanguagePackStrings.construct if skip_validation else GetLanguagePackStrings
        
        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
                keys=keys,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_localization_target_info(
            self,
            only_local: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LocalizationTargetInfo:
        """
        Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization
        
        Params:
            only_local (:class:`bool`)
                If true, returns only locally available information without sending network requests
            
        """
        _constructor = GetLocalizationTargetInfo.construct if skip_validation else GetLocalizationTargetInfo
        
        return await self.client.request(
            _constructor(
                only_local=only_local,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_log_stream(self, *, request_id: str = None, request_timeout: int = None) -> LogStream:
        """
        Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
        
        """
        return await self.client.request(
            GetLogStream(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_log_tag_verbosity_level(
            self,
            tag: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LogVerbosityLevel:
        """
        Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously
        
        Params:
            tag (:class:`str`)
                Logging tag to change verbosity level
            
        """
        _constructor = GetLogTagVerbosityLevel.construct if skip_validation else GetLogTagVerbosityLevel
        
        return await self.client.request(
            _constructor(
                tag=tag,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_log_tags(self, *, request_id: str = None, request_timeout: int = None) -> LogTags:
        """
        Returns list of available TDLib internal log tags, for example, ["actor", "binlog", "connections", "notifications", "proxy"]. Can be called synchronously
        
        """
        return await self.client.request(
            GetLogTags(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_log_verbosity_level(self, *, request_id: str = None, request_timeout: int = None) -> LogVerbosityLevel:
        """
        Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
        
        """
        return await self.client.request(
            GetLogVerbosityLevel(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_login_url(
            self,
            chat_id: int,
            message_id: int,
            button_id: int,
            allow_write_access: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the message with the button
            
            message_id (:class:`int`)
                Message identifier of the message with the button
            
            button_id (:class:`int`)
                Button identifier
            
            allow_write_access (:class:`bool`)
                True, if the user allowed the bot to send them messages
            
        """
        _constructor = GetLoginUrl.construct if skip_validation else GetLoginUrl
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
                allow_write_access=allow_write_access,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_login_url_info(
            self,
            chat_id: int,
            message_id: int,
            button_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> LoginUrlInfo:
        """
        Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the message with the button
            
            message_id (:class:`int`)
                Message identifier of the message with the button
            
            button_id (:class:`int`)
                Button identifier
            
        """
        _constructor = GetLoginUrlInfo.construct if skip_validation else GetLoginUrlInfo
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                button_id=button_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_map_thumbnail_file(
            self,
            location: Location,
            zoom: int,
            width: int,
            height: int,
            scale: int,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded
        
        Params:
            location (:class:`Location`)
                Location of the map center
            
            zoom (:class:`int`)
                Map zoom level; 13-20
            
            width (:class:`int`)
                Map width in pixels before applying scale; 16-1024
            
            height (:class:`int`)
                Map height in pixels before applying scale; 16-1024
            
            scale (:class:`int`)
                Map scale; 1-3
            
            chat_id (:class:`int`)
                Identifier of a chat, in which the thumbnail will be shown. Use 0 if unknown
            
        """
        _constructor = GetMapThumbnailFile.construct if skip_validation else GetMapThumbnailFile
        
        return await self.client.request(
            _constructor(
                location=location,
                zoom=zoom,
                width=width,
                height=height,
                scale=scale,
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_markdown_text(
            self,
            text: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FormattedText:
        """
        Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously
        
        Params:
            text (:class:`FormattedText`)
                The text
            
        """
        _constructor = GetMarkdownText.construct if skip_validation else GetMarkdownText
        
        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_me(self, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Returns the current user
        
        """
        return await self.client.request(
            GetMe(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message to get
            
        """
        _constructor = GetMessage.construct if skip_validation else GetMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_embedding_code(
            self,
            chat_id: int,
            message_id: int,
            for_album: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to which the message belongs
            
            message_id (:class:`int`)
                Identifier of the message
            
            for_album (:class:`bool`)
                Pass true to return an HTML code for embedding of the whole media album
            
        """
        _constructor = GetMessageEmbeddingCode.construct if skip_validation else GetMessageEmbeddingCode
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                for_album=for_album,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_file_type(
            self,
            message_file_head: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageFileType:
        """
        Returns information about a file with messages exported from another app
        
        Params:
            message_file_head (:class:`str`)
                Beginning of the message file; up to 100 first lines
            
        """
        _constructor = GetMessageFileType.construct if skip_validation else GetMessageFileType
        
        return await self.client.request(
            _constructor(
                message_file_head=message_file_head,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_import_confirmation_text(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns a confirmation text to be shown to the user before starting message import
        
        Params:
            chat_id (:class:`int`)
                Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
            
        """
        _constructor = GetMessageImportConfirmationText.construct if skip_validation else GetMessageImportConfirmationText
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_link(
            self,
            chat_id: int,
            message_id: int,
            for_album: bool,
            for_comment: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageLink:
        """
        Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels. This is an offline request
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to which the message belongs
            
            message_id (:class:`int`)
                Identifier of the message
            
            for_album (:class:`bool`)
                Pass true to create a link for the whole media album
            
            for_comment (:class:`bool`)
                Pass true to create a link to the message as a channel post comment, or from a message thread
            
        """
        _constructor = GetMessageLink.construct if skip_validation else GetMessageLink
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                for_album=for_album,
                for_comment=for_comment,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_link_info(
            self,
            url: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageLinkInfo:
        """
        Returns information about a public or private message link
        
        Params:
            url (:class:`str`)
                The message link in the format "https://t.me/c/...", or "tg://privatepost?...", or "https://t.me/username/...", or "tg://resolve?..."
            
        """
        _constructor = GetMessageLinkInfo.construct if skip_validation else GetMessageLinkInfo
        
        return await self.client.request(
            _constructor(
                url=url,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_locally(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message, if it is available locally without sending network request. This is an offline request
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message to get
            
        """
        _constructor = GetMessageLocally.construct if skip_validation else GetMessageLocally
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_public_forwards(
            self,
            chat_id: int,
            message_id: int,
            offset: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FoundMessages:
        """
        Returns forwarded copies of a channel message to different public channels. For optimal performance the number of returned messages is chosen by the library
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the message
            
            message_id (:class:`int`)
                Message identifier
            
            offset (:class:`str`)
                Offset of the first entry to return as received from the previous request; use empty string to get first chunk of results
            
            limit (:class:`int`)
                The maximum number of messages to be returned; must be positive and can't be greater than 100. Fewer messages may be returned than specified by the limit, even if the end of the list has not been reached
            
        """
        _constructor = GetMessagePublicForwards.construct if skip_validation else GetMessagePublicForwards
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_statistics(
            self,
            chat_id: int,
            message_id: int,
            is_dark: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageStatistics:
        """
        Returns detailed statistics about a message. Can be used only if Message.can_get_statistics == true
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_id (:class:`int`)
                Message identifier
            
            is_dark (:class:`bool`)
                Pass true if a dark theme is used by the application
            
        """
        _constructor = GetMessageStatistics.construct if skip_validation else GetMessageStatistics
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                is_dark=is_dark,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_thread(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> MessageThreadInfo:
        """
        Returns information about a message thread. Can be used only if message.can_get_message_thread == true
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_id (:class:`int`)
                Identifier of the message
            
        """
        _constructor = GetMessageThread.construct if skip_validation else GetMessageThread
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_message_thread_history(
            self,
            chat_id: int,
            message_id: int,
            from_message_id: int,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns messages in a message thread of a message. Can be used only if message.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance the number of returned messages is chosen by the library
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_id (:class:`int`)
                Message identifier, which thread history needs to be returned
            
            from_message_id (:class:`int`)
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
            
            offset (:class:`int`)
                Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
            
            limit (:class:`int`)
                The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. Fewer messages may be returned than specified by the limit, even if the end of the message thread history has not been reached
            
        """
        _constructor = GetMessageThreadHistory.construct if skip_validation else GetMessageThreadHistory
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_messages(
            self,
            chat_id: int,
            message_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns information about messages. If a message is not found, returns null on the corresponding position of the result
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat the messages belong to
            
            message_ids (:obj:`list[int]`)
                Identifiers of the messages to get
            
        """
        _constructor = GetMessages.construct if skip_validation else GetMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_network_statistics(
            self,
            only_current: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> NetworkStatistics:
        """
        Returns network data usage statistics. Can be called before authorization
        
        Params:
            only_current (:class:`bool`)
                If true, returns only data for the current library launch
            
        """
        _constructor = GetNetworkStatistics.construct if skip_validation else GetNetworkStatistics
        
        return await self.client.request(
            _constructor(
                only_current=only_current,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_option(
            self,
            name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> OptionValue:
        """
        Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization
        
        Params:
            name (:class:`str`)
                The name of the option
            
        """
        _constructor = GetOption.construct if skip_validation else GetOption
        
        return await self.client.request(
            _constructor(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_passport_authorization_form(
            self,
            bot_user_id: int,
            scope: str,
            public_key: str,
            nonce: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportAuthorizationForm:
        """
        Returns a Telegram Passport authorization form for sharing data with a service
        
        Params:
            bot_user_id (:class:`int`)
                User identifier of the service's bot
            
            scope (:class:`str`)
                Telegram Passport element types requested by the service
            
            public_key (:class:`str`)
                Service's public_key
            
            nonce (:class:`str`)
                Authorization form nonce provided by the service
            
        """
        _constructor = GetPassportAuthorizationForm.construct if skip_validation else GetPassportAuthorizationForm
        
        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                scope=scope,
                public_key=public_key,
                nonce=nonce,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_passport_authorization_form_available_elements(
            self,
            autorization_form_id: int,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElementsWithErrors:
        """
        Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form
        
        Params:
            autorization_form_id (:class:`int`)
                Authorization form identifier
            
            password (:class:`str`)
                Password of the current user
            
        """
        _constructor = GetPassportAuthorizationFormAvailableElements.construct if skip_validation else GetPassportAuthorizationFormAvailableElements
        
        return await self.client.request(
            _constructor(
                autorization_form_id=autorization_form_id,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_passport_element(
            self,
            type_: PassportElementType,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElement:
        """
        Returns one of the available Telegram Passport elements
        
        Params:
            type_ (:class:`PassportElementType`)
                Telegram Passport element type
            
            password (:class:`str`)
                Password of the current user
            
        """
        _constructor = GetPassportElement.construct if skip_validation else GetPassportElement
        
        return await self.client.request(
            _constructor(
                type=type_,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_password_state(self, *, request_id: str = None, request_timeout: int = None) -> PasswordState:
        """
        Returns the current state of 2-step verification
        
        """
        return await self.client.request(
            GetPasswordState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_payment_form(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PaymentForm:
        """
        Returns an invoice payment form. This method should be called when the user presses inlineKeyboardButtonBuy
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the Invoice message
            
            message_id (:class:`int`)
                Message identifier
            
        """
        _constructor = GetPaymentForm.construct if skip_validation else GetPaymentForm
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_payment_receipt(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PaymentReceipt:
        """
        Returns information about a successful payment
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the PaymentSuccessful message
            
            message_id (:class:`int`)
                Message identifier
            
        """
        _constructor = GetPaymentReceipt.construct if skip_validation else GetPaymentReceipt
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_phone_number_info(
            self,
            phone_number_prefix: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PhoneNumberInfo:
        """
        Returns information about a phone number by its prefix. Can be called before authorization
        
        Params:
            phone_number_prefix (:class:`str`)
                The phone number prefix
            
        """
        _constructor = GetPhoneNumberInfo.construct if skip_validation else GetPhoneNumberInfo
        
        return await self.client.request(
            _constructor(
                phone_number_prefix=phone_number_prefix,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_poll_voters(
            self,
            chat_id: int,
            message_id: int,
            option_id: int,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Users:
        """
        Returns users voted for the specified option in a non-anonymous polls. For the optimal performance the number of returned users is chosen by the library
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to which the poll belongs
            
            message_id (:class:`int`)
                Identifier of the message containing the poll
            
            option_id (:class:`int`)
                0-based identifier of the answer option
            
            offset (:class:`int`)
                Number of users to skip in the result; must be non-negative
            
            limit (:class:`int`)
                The maximum number of users to be returned; must be positive and can't be greater than 50. Fewer users may be returned than specified by the limit, even if the end of the voter list has not been reached
            
        """
        _constructor = GetPollVoters.construct if skip_validation else GetPollVoters
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                option_id=option_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_preferred_country_language(
            self,
            country_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Text:
        """
        Returns an IETF language tag of the language preferred in the country, which should be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown
        
        Params:
            country_code (:class:`str`)
                A two-letter ISO 3166-1 alpha-2 country code
            
        """
        _constructor = GetPreferredCountryLanguage.construct if skip_validation else GetPreferredCountryLanguage
        
        return await self.client.request(
            _constructor(
                country_code=country_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_proxies(self, *, request_id: str = None, request_timeout: int = None) -> Proxies:
        """
        Returns list of proxies that are currently set up. Can be called before authorization
        
        """
        return await self.client.request(
            GetProxies(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_proxy_link(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> HttpUrl:
        """
        Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization
        
        Params:
            proxy_id (:class:`int`)
                Proxy identifier
            
        """
        _constructor = GetProxyLink.construct if skip_validation else GetProxyLink
        
        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_push_receiver_id(
            self,
            payload: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PushReceiverId:
        """
        Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously
        
        Params:
            payload (:class:`str`)
                JSON-encoded push notification payload
            
        """
        _constructor = GetPushReceiverId.construct if skip_validation else GetPushReceiverId
        
        return await self.client.request(
            _constructor(
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_recent_inline_bots(self, *, request_id: str = None, request_timeout: int = None) -> Users:
        """
        Returns up to 20 recently used inline bots in the order of their last usage
        
        """
        return await self.client.request(
            GetRecentInlineBots(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_recent_stickers(
            self,
            is_attached: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Returns a list of recently used stickers
        
        Params:
            is_attached (:class:`bool`)
                Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers
            
        """
        _constructor = GetRecentStickers.construct if skip_validation else GetRecentStickers
        
        return await self.client.request(
            _constructor(
                is_attached=is_attached,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_recently_visited_t_me_urls(
            self,
            referrer: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TMeUrls:
        """
        Returns t.me URLs recently visited by a newly registered user
        
        Params:
            referrer (:class:`str`)
                Google Play referrer to identify the user
            
        """
        _constructor = GetRecentlyVisitedTMeUrls.construct if skip_validation else GetRecentlyVisitedTMeUrls
        
        return await self.client.request(
            _constructor(
                referrer=referrer,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_recommended_chat_filters(self, *, request_id: str = None, request_timeout: int = None) -> RecommendedChatFilters:
        """
        Returns recommended chat filters for the current user
        
        """
        return await self.client.request(
            GetRecommendedChatFilters(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_recovery_email_address(
            self,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> RecoveryEmailAddress:
        """
        Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user
        
        Params:
            password (:class:`str`)
                The password for the current user
            
        """
        _constructor = GetRecoveryEmailAddress.construct if skip_validation else GetRecoveryEmailAddress
        
        return await self.client.request(
            _constructor(
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_remote_file(
            self,
            remote_file_id: str,
            file_type: FileType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Returns information about a file by its remote ID; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application
        
        Params:
            remote_file_id (:class:`str`)
                Remote identifier of the file to get
            
            file_type (:class:`FileType`)
                File type, if known
            
        """
        _constructor = GetRemoteFile.construct if skip_validation else GetRemoteFile
        
        return await self.client.request(
            _constructor(
                remote_file_id=remote_file_id,
                file_type=file_type,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_replied_message(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Returns information about a message that is replied by a given message. Also returns the pinned message, the game message, and the invoice message for messages of the types messagePinMessage, messageGameScore, and messagePaymentSuccessful respectively
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat the message belongs to
            
            message_id (:class:`int`)
                Identifier of the message reply to which to get
            
        """
        _constructor = GetRepliedMessage.construct if skip_validation else GetRepliedMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_saved_animations(self, *, request_id: str = None, request_timeout: int = None) -> Animations:
        """
        Returns saved animations
        
        """
        return await self.client.request(
            GetSavedAnimations(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_saved_order_info(self, *, request_id: str = None, request_timeout: int = None) -> OrderInfo:
        """
        Returns saved order info, if any
        
        """
        return await self.client.request(
            GetSavedOrderInfo(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_scope_notification_settings(
            self,
            scope: NotificationSettingsScope,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ScopeNotificationSettings:
        """
        Returns the notification settings for chats of a given type
        
        Params:
            scope (:class:`NotificationSettingsScope`)
                Types of chats for which to return the notification settings information
            
        """
        _constructor = GetScopeNotificationSettings.construct if skip_validation else GetScopeNotificationSettings
        
        return await self.client.request(
            _constructor(
                scope=scope,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_secret_chat(
            self,
            secret_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> SecretChat:
        """
        Returns information about a secret chat by its identifier. This is an offline request
        
        Params:
            secret_chat_id (:class:`int`)
                Secret chat identifier
            
        """
        _constructor = GetSecretChat.construct if skip_validation else GetSecretChat
        
        return await self.client.request(
            _constructor(
                secret_chat_id=secret_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_statistical_graph(
            self,
            chat_id: int,
            token: str,
            x: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StatisticalGraph:
        """
        Loads an asynchronous or a zoomed in statistical graph
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            token (:class:`str`)
                The token for graph loading
            
            x (:class:`int`)
                X-value for zoomed in graph or 0 otherwise
            
        """
        _constructor = GetStatisticalGraph.construct if skip_validation else GetStatisticalGraph
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                token=token,
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_sticker_emojis(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Emojis:
        """
        Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
        
        Params:
            sticker (:class:`InputFile`)
                Sticker file identifier
            
        """
        _constructor = GetStickerEmojis.construct if skip_validation else GetStickerEmojis
        
        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_sticker_set(
            self,
            set_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Returns information about a sticker set by its identifier
        
        Params:
            set_id (:class:`int`)
                Identifier of the sticker set
            
        """
        _constructor = GetStickerSet.construct if skip_validation else GetStickerSet
        
        return await self.client.request(
            _constructor(
                set_id=set_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_stickers(
            self,
            emoji: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Returns stickers from the installed sticker sets that correspond to a given emoji. If the emoji is not empty, favorite and recently used stickers may also be returned
        
        Params:
            emoji (:class:`str`)
                String representation of emoji. If empty, returns all known installed stickers
            
            limit (:class:`int`)
                The maximum number of stickers to be returned
            
        """
        _constructor = GetStickers.construct if skip_validation else GetStickers
        
        return await self.client.request(
            _constructor(
                emoji=emoji,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_storage_statistics(
            self,
            chat_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StorageStatistics:
        """
        Returns storage usage statistics. Can be called before authorization
        
        Params:
            chat_limit (:class:`int`)
                The maximum number of chats with the largest storage usage for which separate statistics should be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0
            
        """
        _constructor = GetStorageStatistics.construct if skip_validation else GetStorageStatistics
        
        return await self.client.request(
            _constructor(
                chat_limit=chat_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_storage_statistics_fast(self, *, request_id: str = None, request_timeout: int = None) -> StorageStatisticsFast:
        """
        Quickly returns approximate storage usage statistics. Can be called before authorization
        
        """
        return await self.client.request(
            GetStorageStatisticsFast(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_suitable_discussion_chats(self, *, request_id: str = None, request_timeout: int = None) -> Chats:
        """
        Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first
        
        """
        return await self.client.request(
            GetSuitableDiscussionChats(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_supergroup(
            self,
            supergroup_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Supergroup:
        """
        Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot
        
        Params:
            supergroup_id (:class:`int`)
                Supergroup or channel identifier
            
        """
        _constructor = GetSupergroup.construct if skip_validation else GetSupergroup
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_supergroup_full_info(
            self,
            supergroup_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> SupergroupFullInfo:
        """
        Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute
        
        Params:
            supergroup_id (:class:`int`)
                Supergroup or channel identifier
            
        """
        _constructor = GetSupergroupFullInfo.construct if skip_validation else GetSupergroupFullInfo
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_supergroup_members(
            self,
            supergroup_id: int,
            filter_: SupergroupMembersFilter,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatMembers:
        """
        Returns information about members or banned users in a supergroup or channel. Can be used only if SupergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters
        
        Params:
            supergroup_id (:class:`int`)
                Identifier of the supergroup or channel
            
            filter_ (:class:`SupergroupMembersFilter`)
                The type of users to return. By default, supergroupMembersFilterRecent
            
            offset (:class:`int`)
                Number of users to skip
            
            limit (:class:`int`)
                The maximum number of users be returned; up to 200
            
        """
        _constructor = GetSupergroupMembers.construct if skip_validation else GetSupergroupMembers
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                filter=filter_,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_support_user(self, *, request_id: str = None, request_timeout: int = None) -> User:
        """
        Returns a user that can be contacted to get support
        
        """
        return await self.client.request(
            GetSupportUser(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_temporary_password_state(self, *, request_id: str = None, request_timeout: int = None) -> TemporaryPasswordState:
        """
        Returns information about the current temporary password
        
        """
        return await self.client.request(
            GetTemporaryPasswordState(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_text_entities(
            self,
            text: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TextEntities:
        """
        Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) contained in the text. Can be called synchronously
        
        Params:
            text (:class:`str`)
                The text in which to look for entites
            
        """
        _constructor = GetTextEntities.construct if skip_validation else GetTextEntities
        
        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_top_chats(
            self,
            category: TopChatCategory,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Returns a list of frequently used chats. Supported only if the chat info database is enabled
        
        Params:
            category (:class:`TopChatCategory`)
                Category of chats to be returned
            
            limit (:class:`int`)
                The maximum number of chats to be returned; up to 30
            
        """
        _constructor = GetTopChats.construct if skip_validation else GetTopChats
        
        return await self.client.request(
            _constructor(
                category=category,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_trending_sticker_sets(
            self,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Returns a list of trending sticker sets. For the optimal performance the number of returned sticker sets is chosen by the library
        
        Params:
            offset (:class:`int`)
                The offset from which to return the sticker sets; must be non-negative
            
            limit (:class:`int`)
                The maximum number of sticker sets to be returned; must be non-negative. Fewer sticker sets may be returned than specified by the limit, even if the end of the list has not been reached
            
        """
        _constructor = GetTrendingStickerSets.construct if skip_validation else GetTrendingStickerSets
        
        return await self.client.request(
            _constructor(
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_user(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> User:
        """
        Returns information about a user by their identifier. This is an offline request if the current user is not a bot
        
        Params:
            user_id (:class:`int`)
                User identifier
            
        """
        _constructor = GetUser.construct if skip_validation else GetUser
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_user_full_info(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> UserFullInfo:
        """
        Returns full information about a user by their identifier
        
        Params:
            user_id (:class:`int`)
                User identifier
            
        """
        _constructor = GetUserFullInfo.construct if skip_validation else GetUserFullInfo
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_user_privacy_setting_rules(
            self,
            setting: UserPrivacySetting,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> UserPrivacySettingRules:
        """
        Returns the current privacy settings
        
        Params:
            setting (:class:`UserPrivacySetting`)
                The privacy setting
            
        """
        _constructor = GetUserPrivacySettingRules.construct if skip_validation else GetUserPrivacySettingRules
        
        return await self.client.request(
            _constructor(
                setting=setting,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_user_profile_photos(
            self,
            user_id: int,
            offset: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatPhotos:
        """
        Returns the profile photos of a user. The result of this query may be outdated: some photos might have been deleted already
        
        Params:
            user_id (:class:`int`)
                User identifier
            
            offset (:class:`int`)
                The number of photos to skip; must be non-negative
            
            limit (:class:`int`)
                The maximum number of photos to be returned; up to 100
            
        """
        _constructor = GetUserProfilePhotos.construct if skip_validation else GetUserProfilePhotos
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                offset=offset,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_web_page_instant_view(
            self,
            url: str,
            force_full: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> WebPageInstantView:
        """
        Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page
        
        Params:
            url (:class:`str`)
                The web page URL
            
            force_full (:class:`bool`)
                If true, the full instant view for the web page will be returned
            
        """
        _constructor = GetWebPageInstantView.construct if skip_validation else GetWebPageInstantView
        
        return await self.client.request(
            _constructor(
                url=url,
                force_full=force_full,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def get_web_page_preview(
            self,
            text: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> WebPage:
        """
        Returns a web page preview by the text of the message. Do not call this function too often. Returns a 404 error if the web page has no preview
        
        Params:
            text (:class:`FormattedText`)
                Message text with formatting
            
        """
        _constructor = GetWebPagePreview.construct if skip_validation else GetWebPagePreview
        
        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def hide_suggested_action(
            self,
            action: SuggestedAction,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Hides a suggested action
        
        Params:
            action (:class:`SuggestedAction`)
                Suggested action to hide
            
        """
        _constructor = HideSuggestedAction.construct if skip_validation else HideSuggestedAction
        
        return await self.client.request(
            _constructor(
                action=action,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def import_contacts(
            self,
            contacts: list[Contact],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ImportedContacts:
        """
        Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored
        
        Params:
            contacts (:obj:`list[Contact]`)
                The list of contacts to import or edit; contacts' vCard are ignored and are not imported
            
        """
        _constructor = ImportContacts.construct if skip_validation else ImportContacts
        
        return await self.client.request(
            _constructor(
                contacts=contacts,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def import_messages(
            self,
            chat_id: int,
            message_file: InputFile,
            attached_files: list[InputFile],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Imports messages exported from another app
        
        Params:
            chat_id (:class:`int`)
                Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right
            
            message_file (:class:`InputFile`)
                File with messages to import. Only inputFileLocal and inputFileGenerated are supported. The file must not be previously uploaded
            
            attached_files (:obj:`list[InputFile]`)
                Files used in the imported messages. Only inputFileLocal and inputFileGenerated are supported. The files must not be previously uploaded
            
        """
        _constructor = ImportMessages.construct if skip_validation else ImportMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_file=message_file,
                attached_files=attached_files,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def invite_group_call_participants(
            self,
            group_call_id: int,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Invites users to a group call. Sends a service message of type messageInviteToGroupCall for voice chats
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            user_ids (:obj:`list[int]`)
                User identifiers. At most 10 users can be invited simultaneously
            
        """
        _constructor = InviteGroupCallParticipants.construct if skip_validation else InviteGroupCallParticipants
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def join_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = JoinChat.construct if skip_validation else JoinChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def join_chat_by_invite_link(
            self,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Uses an invite link to add the current user to the chat if possible
        
        Params:
            invite_link (:class:`str`)
                Invite link to import; must have URL "t.me", "telegram.me", or "telegram.dog" and query beginning with "/joinchat/" or "/+"
            
        """
        _constructor = JoinChatByInviteLink.construct if skip_validation else JoinChatByInviteLink
        
        return await self.client.request(
            _constructor(
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def join_group_call(
            self,
            group_call_id: int,
            participant_alias: MessageSender,
            payload: GroupCallPayload,
            source: int,
            is_muted: bool,
            invite_hash: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> GroupCallJoinResponse:
        """
        Joins a group call
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            participant_alias (:class:`MessageSender`)
                Identifier of the group call participant, which will be used to join the call; voice chats only
            
            payload (:class:`GroupCallPayload`)
                Group join payload; received from tgcalls
            
            source (:class:`int`)
                Caller synchronization source identifier; received from tgcalls
            
            is_muted (:class:`bool`)
                True, if the user's microphone is muted
            
            invite_hash (:class:`str`)
                If non-empty, invite hash to be used to join the group call without being muted by administrators
            
        """
        _constructor = JoinGroupCall.construct if skip_validation else JoinGroupCall
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant_alias=participant_alias,
                payload=payload,
                source=source,
                is_muted=is_muted,
                invite_hash=invite_hash,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def leave_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes the current user from chat members. Private and secret chats can't be left using this method
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = LeaveChat.construct if skip_validation else LeaveChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def leave_group_call(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Leaves a group call
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
        """
        _constructor = LeaveGroupCall.construct if skip_validation else LeaveGroupCall
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def load_group_call_participants(
            self,
            group_call_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Loads more group call participants. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants has already been loaded
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined
            
            limit (:class:`int`)
                Maximum number of participants to load
            
        """
        _constructor = LoadGroupCallParticipants.construct if skip_validation else LoadGroupCallParticipants
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def log_out(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Closes the TDLib instance after a proper logout. Requires an available network connection. All local data will be destroyed. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent
        
        """
        return await self.client.request(
            LogOut(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def open_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats)
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = OpenChat.construct if skip_validation else OpenChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def open_message_content(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the message
            
            message_id (:class:`int`)
                Identifier of the message with the opened content
            
        """
        _constructor = OpenMessageContent.construct if skip_validation else OpenMessageContent
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def optimize_storage(
            self,
            size: int,
            ttl: int,
            count: int,
            immunity_delay: int,
            file_types: list[FileType],
            chat_ids: list[int],
            exclude_chat_ids: list[int],
            return_deleted_file_statistics: bool,
            chat_limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StorageStatistics:
        """
        Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted
        
        Params:
            size (:class:`int`)
                Limit on the total size of files after deletion. Pass -1 to use the default limit
            
            ttl (:class:`int`)
                Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit
            
            count (:class:`int`)
                Limit on the total count of files after deletion. Pass -1 to use the default limit
            
            immunity_delay (:class:`int`)
                The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value
            
            file_types (:obj:`list[FileType]`)
                If not empty, only files with the given type(s) are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted
            
            chat_ids (:obj:`list[int]`)
                If not empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)
            
            exclude_chat_ids (:obj:`list[int]`)
                If not empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)
            
            return_deleted_file_statistics (:class:`bool`)
                Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics
            
            chat_limit (:class:`int`)
                Same as in getStorageStatistics. Affects only returned statistics
            
        """
        _constructor = OptimizeStorage.construct if skip_validation else OptimizeStorage
        
        return await self.client.request(
            _constructor(
                size=size,
                ttl=ttl,
                count=count,
                immunity_delay=immunity_delay,
                file_types=file_types,
                chat_ids=chat_ids,
                exclude_chat_ids=exclude_chat_ids,
                return_deleted_file_statistics=return_deleted_file_statistics,
                chat_limit=chat_limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def parse_markdown(
            self,
            text: FormattedText,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FormattedText:
        """
        Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously
        
        Params:
            text (:class:`FormattedText`)
                The text to parse. For example, "__italic__ ~~strikethrough~~ **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**"
            
        """
        _constructor = ParseMarkdown.construct if skip_validation else ParseMarkdown
        
        return await self.client.request(
            _constructor(
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def parse_text_entities(
            self,
            text: str,
            parse_mode: TextParseMode,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FormattedText:
        """
        Parses Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text. Can be called synchronously
        
        Params:
            text (:class:`str`)
                The text to parse
            
            parse_mode (:class:`TextParseMode`)
                Text parse mode
            
        """
        _constructor = ParseTextEntities.construct if skip_validation else ParseTextEntities
        
        return await self.client.request(
            _constructor(
                text=text,
                parse_mode=parse_mode,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def pin_chat_message(
            self,
            chat_id: int,
            message_id: int,
            disable_notification: bool,
            only_for_self: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Pins a message in a chat; requires can_pin_messages rights or can_edit_messages rights in the channel
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat
            
            message_id (:class:`int`)
                Identifier of the new pinned message
            
            disable_notification (:class:`bool`)
                True, if there should be no notification about the pinned message. Notifications are always disabled in channels and private chats
            
            only_for_self (:class:`bool`)
                True, if the message needs to be pinned for one side only; private chats only
            
        """
        _constructor = PinChatMessage.construct if skip_validation else PinChatMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                disable_notification=disable_notification,
                only_for_self=only_for_self,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def ping_proxy(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Seconds:
        """
        Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization
        
        Params:
            proxy_id (:class:`int`)
                Proxy identifier. Use 0 to ping a Telegram server without a proxy
            
        """
        _constructor = PingProxy.construct if skip_validation else PingProxy
        
        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def process_push_notification(
            self,
            payload: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization
        
        Params:
            payload (:class:`str`)
                JSON-encoded push notification payload with all fields sent by the server, and "google.sent_time" and "google.notification.sound" fields added
            
        """
        _constructor = ProcessPushNotification.construct if skip_validation else ProcessPushNotification
        
        return await self.client.request(
            _constructor(
                payload=payload,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def read_all_chat_mentions(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Marks all mentions in a chat as read
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = ReadAllChatMentions.construct if skip_validation else ReadAllChatMentions
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def read_file_part(
            self,
            file_id: int,
            offset: int,
            count: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FilePart:
        """
        Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file
        
        Params:
            file_id (:class:`int`)
                Identifier of the file. The file must be located in the TDLib file cache
            
            offset (:class:`int`)
                The offset from which to read the file
            
            count (:class:`int`)
                Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position
            
        """
        _constructor = ReadFilePart.construct if skip_validation else ReadFilePart
        
        return await self.client.request(
            _constructor(
                file_id=file_id,
                offset=offset,
                count=count,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def recover_authentication_password(
            self,
            recovery_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Recovers the password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
        
        Params:
            recovery_code (:class:`str`)
                Recovery code to check
            
        """
        _constructor = RecoverAuthenticationPassword.construct if skip_validation else RecoverAuthenticationPassword
        
        return await self.client.request(
            _constructor(
                recovery_code=recovery_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def recover_password(
            self,
            recovery_code: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Recovers the password using a recovery code sent to an email address that was previously set up
        
        Params:
            recovery_code (:class:`str`)
                Recovery code to check
            
        """
        _constructor = RecoverPassword.construct if skip_validation else RecoverPassword
        
        return await self.client.request(
            _constructor(
                recovery_code=recovery_code,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def register_device(
            self,
            device_token: DeviceToken,
            other_user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PushReceiverId:
        """
        Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription
        
        Params:
            device_token (:class:`DeviceToken`)
                Device token
            
            other_user_ids (:obj:`list[int]`)
                List of user identifiers of other users currently using the application
            
        """
        _constructor = RegisterDevice.construct if skip_validation else RegisterDevice
        
        return await self.client.request(
            _constructor(
                device_token=device_token,
                other_user_ids=other_user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def register_user(
            self,
            first_name: str,
            last_name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration
        
        Params:
            first_name (:class:`str`)
                The first name of the user; 1-64 characters
            
            last_name (:class:`str`)
                The last name of the user; 0-64 characters
            
        """
        _constructor = RegisterUser.construct if skip_validation else RegisterUser
        
        return await self.client.request(
            _constructor(
                first_name=first_name,
                last_name=last_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_background(
            self,
            background_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes background from the list of installed backgrounds
        
        Params:
            background_id (:class:`int`)
                The background identifier
            
        """
        _constructor = RemoveBackground.construct if skip_validation else RemoveBackground
        
        return await self.client.request(
            _constructor(
                background_id=background_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_chat_action_bar(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a chat action bar without any other action
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = RemoveChatActionBar.construct if skip_validation else RemoveChatActionBar
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_contacts(
            self,
            user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes users from the contact list
        
        Params:
            user_ids (:obj:`list[int]`)
                Identifiers of users to be deleted
            
        """
        _constructor = RemoveContacts.construct if skip_validation else RemoveContacts
        
        return await self.client.request(
            _constructor(
                user_ids=user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_favorite_sticker(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a sticker from the list of favorite stickers
        
        Params:
            sticker (:class:`InputFile`)
                Sticker file to delete from the list
            
        """
        _constructor = RemoveFavoriteSticker.construct if skip_validation else RemoveFavoriteSticker
        
        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_notification(
            self,
            notification_group_id: int,
            notification_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user
        
        Params:
            notification_group_id (:class:`int`)
                Identifier of notification group to which the notification belongs
            
            notification_id (:class:`int`)
                Identifier of removed notification
            
        """
        _constructor = RemoveNotification.construct if skip_validation else RemoveNotification
        
        return await self.client.request(
            _constructor(
                notification_group_id=notification_group_id,
                notification_id=notification_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_notification_group(
            self,
            notification_group_id: int,
            max_notification_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user
        
        Params:
            notification_group_id (:class:`int`)
                Notification group identifier
            
            max_notification_id (:class:`int`)
                The maximum identifier of removed notifications
            
        """
        _constructor = RemoveNotificationGroup.construct if skip_validation else RemoveNotificationGroup
        
        return await self.client.request(
            _constructor(
                notification_group_id=notification_group_id,
                max_notification_id=max_notification_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_proxy(
            self,
            proxy_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a proxy server. Can be called before authorization
        
        Params:
            proxy_id (:class:`int`)
                Proxy identifier
            
        """
        _constructor = RemoveProxy.construct if skip_validation else RemoveProxy
        
        return await self.client.request(
            _constructor(
                proxy_id=proxy_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_recent_hashtag(
            self,
            hashtag: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a hashtag from the list of recently used hashtags
        
        Params:
            hashtag (:class:`str`)
                Hashtag to delete
            
        """
        _constructor = RemoveRecentHashtag.construct if skip_validation else RemoveRecentHashtag
        
        return await self.client.request(
            _constructor(
                hashtag=hashtag,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_recent_sticker(
            self,
            is_attached: bool,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a sticker from the list of recently used stickers
        
        Params:
            is_attached (:class:`bool`)
                Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
            
            sticker (:class:`InputFile`)
                Sticker file to delete
            
        """
        _constructor = RemoveRecentSticker.construct if skip_validation else RemoveRecentSticker
        
        return await self.client.request(
            _constructor(
                is_attached=is_attached,
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_recently_found_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a chat from the list of recently found chats
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to be removed
            
        """
        _constructor = RemoveRecentlyFoundChat.construct if skip_validation else RemoveRecentlyFoundChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_saved_animation(
            self,
            animation: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes an animation from the list of saved animations
        
        Params:
            animation (:class:`InputFile`)
                Animation file to be removed
            
        """
        _constructor = RemoveSavedAnimation.construct if skip_validation else RemoveSavedAnimation
        
        return await self.client.request(
            _constructor(
                animation=animation,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_sticker_from_set(
            self,
            sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot
        
        Params:
            sticker (:class:`InputFile`)
                Sticker
            
        """
        _constructor = RemoveStickerFromSet.construct if skip_validation else RemoveStickerFromSet
        
        return await self.client.request(
            _constructor(
                sticker=sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def remove_top_chat(
            self,
            category: TopChatCategory,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled
        
        Params:
            category (:class:`TopChatCategory`)
                Category of frequently used chats
            
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = RemoveTopChat.construct if skip_validation else RemoveTopChat
        
        return await self.client.request(
            _constructor(
                category=category,
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def reorder_chat_filters(
            self,
            chat_filter_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the order of chat filters
        
        Params:
            chat_filter_ids (:obj:`list[int]`)
                Identifiers of chat filters in the new correct order
            
        """
        _constructor = ReorderChatFilters.construct if skip_validation else ReorderChatFilters
        
        return await self.client.request(
            _constructor(
                chat_filter_ids=chat_filter_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def reorder_installed_sticker_sets(
            self,
            is_masks: bool,
            sticker_set_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the order of installed sticker sets
        
        Params:
            is_masks (:class:`bool`)
                Pass true to change the order of mask sticker sets; pass false to change the order of ordinary sticker sets
            
            sticker_set_ids (:obj:`list[int]`)
                Identifiers of installed sticker sets in the new correct order
            
        """
        _constructor = ReorderInstalledStickerSets.construct if skip_validation else ReorderInstalledStickerSets
        
        return await self.client.request(
            _constructor(
                is_masks=is_masks,
                sticker_set_ids=sticker_set_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def replace_primary_chat_invite_link(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLink:
        """
        Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = ReplacePrimaryChatInviteLink.construct if skip_validation else ReplacePrimaryChatInviteLink
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def report_chat(
            self,
            chat_id: int,
            message_ids: list[int],
            reason: ChatReportReason,
            text: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if this is a private chat with a bot, a private chat with a user sharing their location, a supergroup, or a channel, since other chats can't be checked by moderators
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_ids (:obj:`list[int]`)
                Identifiers of reported messages, if any
            
            reason (:class:`ChatReportReason`)
                The reason for reporting the chat
            
            text (:class:`str`)
                Additional report details; 0-1024 characters
            
        """
        _constructor = ReportChat.construct if skip_validation else ReportChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
                reason=reason,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def report_chat_photo(
            self,
            chat_id: int,
            file_id: int,
            reason: ChatReportReason,
            text: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Reports a chat photo to the Telegram moderators. A chat photo can be reported only if this is a private chat with a bot, a private chat with a user sharing their location, a supergroup, or a channel, since other chats can't be checked by moderators
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            file_id (:class:`int`)
                Identifier of the photo to report. Only full photos from chatPhoto can be reported
            
            reason (:class:`ChatReportReason`)
                The reason for reporting the chat photo
            
            text (:class:`str`)
                Additional report details; 0-1024 characters
            
        """
        _constructor = ReportChatPhoto.construct if skip_validation else ReportChatPhoto
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                file_id=file_id,
                reason=reason,
                text=text,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def report_supergroup_spam(
            self,
            supergroup_id: int,
            user_id: int,
            message_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Reports some messages from a user in a supergroup as spam; requires administrator rights in the supergroup
        
        Params:
            supergroup_id (:class:`int`)
                Supergroup identifier
            
            user_id (:class:`int`)
                User identifier
            
            message_ids (:obj:`list[int]`)
                Identifiers of messages sent in the supergroup by the user. This list must be non-empty
            
        """
        _constructor = ReportSupergroupSpam.construct if skip_validation else ReportSupergroupSpam
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                user_id=user_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def request_authentication_password_recovery(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Requests to send a password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
        
        """
        return await self.client.request(
            RequestAuthenticationPasswordRecovery(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def request_password_recovery(self, *, request_id: str = None, request_timeout: int = None) -> EmailAddressAuthenticationCodeInfo:
        """
        Requests to send a password recovery code to an email address that was previously set up
        
        """
        return await self.client.request(
            RequestPasswordRecovery(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def request_qr_code_authentication(
            self,
            other_user_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword
        
        Params:
            other_user_ids (:obj:`list[int]`)
                List of user identifiers of other users currently using the application
            
        """
        _constructor = RequestQrCodeAuthentication.construct if skip_validation else RequestQrCodeAuthentication
        
        return await self.client.request(
            _constructor(
                other_user_ids=other_user_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def resend_authentication_code(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Re-sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode and the next_code_type of the result is not null
        
        """
        return await self.client.request(
            ResendAuthenticationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def resend_change_phone_number_code(self, *, request_id: str = None, request_timeout: int = None) -> AuthenticationCodeInfo:
        """
        Re-sends the authentication code sent to confirm a new phone number for the user. Works only if the previously received authenticationCodeInfo next_code_type was not null
        
        """
        return await self.client.request(
            ResendChangePhoneNumberCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def resend_email_address_verification_code(self, *, request_id: str = None, request_timeout: int = None) -> EmailAddressAuthenticationCodeInfo:
        """
        Re-sends the code to verify an email address to be added to a user's Telegram Passport
        
        """
        return await self.client.request(
            ResendEmailAddressVerificationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def resend_messages(
            self,
            chat_id: int,
            message_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to send messages
            
            message_ids (:obj:`list[int]`)
                Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order
            
        """
        _constructor = ResendMessages.construct if skip_validation else ResendMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_ids=message_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def resend_phone_number_confirmation_code(self, *, request_id: str = None, request_timeout: int = None) -> AuthenticationCodeInfo:
        """
        Resends phone number confirmation code
        
        """
        return await self.client.request(
            ResendPhoneNumberConfirmationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def resend_phone_number_verification_code(self, *, request_id: str = None, request_timeout: int = None) -> AuthenticationCodeInfo:
        """
        Re-sends the code to verify a phone number to be added to a user's Telegram Passport
        
        """
        return await self.client.request(
            ResendPhoneNumberVerificationCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def resend_recovery_email_address_code(self, *, request_id: str = None, request_timeout: int = None) -> PasswordState:
        """
        Resends the 2-step verification recovery email address verification code
        
        """
        return await self.client.request(
            ResendRecoveryEmailAddressCode(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def reset_all_notification_settings(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets all notification settings to their default values. By default, all chats are unmuted, the sound is set to "default" and message previews are shown
        
        """
        return await self.client.request(
            ResetAllNotificationSettings(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def reset_backgrounds(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets list of installed backgrounds to its default value
        
        """
        return await self.client.request(
            ResetBackgrounds(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def reset_network_statistics(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Resets all network data usage statistics to zero. Can be called before authorization
        
        """
        return await self.client.request(
            ResetNetworkStatistics(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def revoke_chat_invite_link(
            self,
            chat_id: int,
            invite_link: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatInviteLinks:
        """
        Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links. If a primary link is revoked, then additionally to the revoked link returns new primary link
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            invite_link (:class:`str`)
                Invite link to be revoked
            
        """
        _constructor = RevokeChatInviteLink.construct if skip_validation else RevokeChatInviteLink
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                invite_link=invite_link,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def revoke_group_call_invite_link(
            self,
            group_call_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
        """
        _constructor = RevokeGroupCallInviteLink.construct if skip_validation else RevokeGroupCallInviteLink
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def save_application_log_event(
            self,
            type_: str,
            chat_id: int,
            data: JsonValue,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Saves application log event on the server. Can be called before authorization
        
        Params:
            type_ (:class:`str`)
                Event type
            
            chat_id (:class:`int`)
                Optional chat identifier, associated with the event
            
            data (:class:`JsonValue`)
                The log event data
            
        """
        _constructor = SaveApplicationLogEvent.construct if skip_validation else SaveApplicationLogEvent
        
        return await self.client.request(
            _constructor(
                type=type_,
                chat_id=chat_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_background(
            self,
            name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Background:
        """
        Searches for a background by its name
        
        Params:
            name (:class:`str`)
                The name of the background
            
        """
        _constructor = SearchBackground.construct if skip_validation else SearchBackground
        
        return await self.client.request(
            _constructor(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_call_messages(
            self,
            from_message_id: int,
            limit: int,
            only_missed: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Searches for call messages. Returns the results in reverse chronological order (i. e., in order of decreasing message_id). For optimal performance the number of returned messages is chosen by the library
        
        Params:
            from_message_id (:class:`int`)
                Identifier of the message from which to search; use 0 to get results from the last message
            
            limit (:class:`int`)
                The maximum number of messages to be returned; up to 100. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
            
            only_missed (:class:`bool`)
                If true, returns only messages with missed calls
            
        """
        _constructor = SearchCallMessages.construct if skip_validation else SearchCallMessages
        
        return await self.client.request(
            _constructor(
                from_message_id=from_message_id,
                limit=limit,
                only_missed=only_missed,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_chat_members(
            self,
            chat_id: int,
            query: str,
            limit: int,
            filter_: ChatMembersFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatMembers:
        """
        Searches for a specified query in the first name, last name and username of the members of a specified chat. Requires administrator rights in channels
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            query (:class:`str`)
                Query to search for
            
            limit (:class:`int`)
                The maximum number of users to be returned
            
            filter_ (:class:`ChatMembersFilter`)
                The type of users to return. By default, chatMembersFilterMembers
            
        """
        _constructor = SearchChatMembers.construct if skip_validation else SearchChatMembers
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                limit=limit,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_chat_messages(
            self,
            chat_id: int,
            query: str,
            sender: MessageSender,
            from_message_id: int,
            offset: int,
            limit: int,
            filter_: SearchMessagesFilter,
            message_thread_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query (searchSecretMessages should be used instead), or without an enabled message database. For optimal performance the number of returned messages is chosen by the library
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat in which to search messages
            
            query (:class:`str`)
                Query to search for
            
            sender (:class:`MessageSender`)
                If not null, only messages sent by the specified sender will be returned. Not supported in secret chats
            
            from_message_id (:class:`int`)
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
            
            offset (:class:`int`)
                Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages
            
            limit (:class:`int`)
                The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
            
            filter_ (:class:`SearchMessagesFilter`)
                Filter for message content in the search results
            
            message_thread_id (:class:`int`)
                If not 0, only messages in the specified thread will be returned; supergroups only
            
        """
        _constructor = SearchChatMessages.construct if skip_validation else SearchChatMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                sender=sender,
                from_message_id=from_message_id,
                offset=offset,
                limit=limit,
                filter=filter_,
                message_thread_id=message_thread_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_chat_recent_location_messages(
            self,
            chat_id: int,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            limit (:class:`int`)
                The maximum number of messages to be returned
            
        """
        _constructor = SearchChatRecentLocationMessages.construct if skip_validation else SearchChatRecentLocationMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_chats(
            self,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats, this is an offline request. Returns chats in the order seen in the main chat list
        
        Params:
            query (:class:`str`)
                Query to search for. If the query is empty, returns up to 20 recently found chats
            
            limit (:class:`int`)
                The maximum number of chats to be returned
            
        """
        _constructor = SearchChats.construct if skip_validation else SearchChats
        
        return await self.client.request(
            _constructor(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_chats_nearby(
            self,
            location: Location,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ChatsNearby:
        """
        Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby. The request should be sent again every 25 seconds with adjusted location to not miss new chats
        
        Params:
            location (:class:`Location`)
                Current user location
            
        """
        _constructor = SearchChatsNearby.construct if skip_validation else SearchChatsNearby
        
        return await self.client.request(
            _constructor(
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_chats_on_server(
            self,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the main chat list
        
        Params:
            query (:class:`str`)
                Query to search for
            
            limit (:class:`int`)
                The maximum number of chats to be returned
            
        """
        _constructor = SearchChatsOnServer.construct if skip_validation else SearchChatsOnServer
        
        return await self.client.request(
            _constructor(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_contacts(
            self,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Users:
        """
        Searches for the specified query in the first names, last names and usernames of the known user contacts
        
        Params:
            query (:class:`str`)
                Query to search for; may be empty to return all contacts
            
            limit (:class:`int`)
                The maximum number of users to be returned
            
        """
        _constructor = SearchContacts.construct if skip_validation else SearchContacts
        
        return await self.client.request(
            _constructor(
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_emojis(
            self,
            text: str,
            exact_match: bool,
            input_language_codes: list[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Emojis:
        """
        Searches for emojis by keywords. Supported only if the file database is enabled
        
        Params:
            text (:class:`str`)
                Text to search for
            
            exact_match (:class:`bool`)
                True, if only emojis, which exactly match text needs to be returned
            
            input_language_codes (:obj:`list[str]`)
                List of possible IETF language tags of the user's input language; may be empty if unknown
            
        """
        _constructor = SearchEmojis.construct if skip_validation else SearchEmojis
        
        return await self.client.request(
            _constructor(
                text=text,
                exact_match=exact_match,
                input_language_codes=input_language_codes,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_hashtags(
            self,
            prefix: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Hashtags:
        """
        Searches for recently used hashtags by their prefix
        
        Params:
            prefix (:class:`str`)
                Hashtag prefix to search for
            
            limit (:class:`int`)
                The maximum number of hashtags to be returned
            
        """
        _constructor = SearchHashtags.construct if skip_validation else SearchHashtags
        
        return await self.client.request(
            _constructor(
                prefix=prefix,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_installed_sticker_sets(
            self,
            is_masks: bool,
            query: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Searches for installed sticker sets by looking for specified query in their title and name
        
        Params:
            is_masks (:class:`bool`)
                Pass true to return mask sticker sets; pass false to return ordinary sticker sets
            
            query (:class:`str`)
                Query to search for
            
            limit (:class:`int`)
                The maximum number of sticker sets to return
            
        """
        _constructor = SearchInstalledStickerSets.construct if skip_validation else SearchInstalledStickerSets
        
        return await self.client.request(
            _constructor(
                is_masks=is_masks,
                query=query,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_messages(
            self,
            chat_list: ChatList,
            query: str,
            offset_date: int,
            offset_chat_id: int,
            offset_message_id: int,
            limit: int,
            filter_: SearchMessagesFilter,
            min_date: int,
            max_date: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance the number of returned messages is chosen by the library
        
        Params:
            chat_list (:class:`ChatList`)
                Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported
            
            query (:class:`str`)
                Query to search for
            
            offset_date (:class:`int`)
                The date of the message starting from which the results should be fetched. Use 0 or any date in the future to get results from the last message
            
            offset_chat_id (:class:`int`)
                The chat identifier of the last found message, or 0 for the first request
            
            offset_message_id (:class:`int`)
                The message identifier of the last found message, or 0 for the first request
            
            limit (:class:`int`)
                The maximum number of messages to be returned; up to 100. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
            
            filter_ (:class:`SearchMessagesFilter`)
                Filter for message content in the search results; searchMessagesFilterCall, searchMessagesFilterMissedCall, searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterFailedToSend and searchMessagesFilterPinned are unsupported in this function
            
            min_date (:class:`int`)
                If not 0, the minimum date of the messages to return
            
            max_date (:class:`int`)
                If not 0, the maximum date of the messages to return
            
        """
        _constructor = SearchMessages.construct if skip_validation else SearchMessages
        
        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                query=query,
                offset_date=offset_date,
                offset_chat_id=offset_chat_id,
                offset_message_id=offset_message_id,
                limit=limit,
                filter=filter_,
                min_date=min_date,
                max_date=max_date,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_public_chat(
            self,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Searches a public chat by its username. Currently only private chats, supergroups and channels can be public. Returns the chat if found; otherwise an error is returned
        
        Params:
            username (:class:`str`)
                Username to be resolved
            
        """
        _constructor = SearchPublicChat.construct if skip_validation else SearchPublicChat
        
        return await self.client.request(
            _constructor(
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_public_chats(
            self,
            query: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chats:
        """
        Searches public chats by looking for specified query in their username and title. Currently only private chats, supergroups and channels can be public. Returns a meaningful number of results. Returns nothing if the length of the searched username prefix is less than 5. Excludes private chats with contacts and chats from the chat list from the results
        
        Params:
            query (:class:`str`)
                Query to search for
            
        """
        _constructor = SearchPublicChats.construct if skip_validation else SearchPublicChats
        
        return await self.client.request(
            _constructor(
                query=query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_secret_messages(
            self,
            chat_id: int,
            query: str,
            offset: str,
            limit: int,
            filter_: SearchMessagesFilter,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> FoundMessages:
        """
        Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance the number of returned messages is chosen by the library
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat in which to search. Specify 0 to search in all secret chats
            
            query (:class:`str`)
                Query to search for. If empty, searchChatMessages should be used instead
            
            offset (:class:`str`)
                Offset of the first entry to return as received from the previous request; use empty string to get first chunk of results
            
            limit (:class:`int`)
                The maximum number of messages to be returned; up to 100. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
            
            filter_ (:class:`SearchMessagesFilter`)
                A filter for message content in the search results
            
        """
        _constructor = SearchSecretMessages.construct if skip_validation else SearchSecretMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                query=query,
                offset=offset,
                limit=limit,
                filter=filter_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_sticker_set(
            self,
            name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Searches for a sticker set by its name
        
        Params:
            name (:class:`str`)
                Name of the sticker set
            
        """
        _constructor = SearchStickerSet.construct if skip_validation else SearchStickerSet
        
        return await self.client.request(
            _constructor(
                name=name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_sticker_sets(
            self,
            query: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSets:
        """
        Searches for ordinary sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results
        
        Params:
            query (:class:`str`)
                Query to search for
            
        """
        _constructor = SearchStickerSets.construct if skip_validation else SearchStickerSets
        
        return await self.client.request(
            _constructor(
                query=query,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def search_stickers(
            self,
            emoji: str,
            limit: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Stickers:
        """
        Searches for stickers from public sticker sets that correspond to a given emoji
        
        Params:
            emoji (:class:`str`)
                String representation of emoji; must be non-empty
            
            limit (:class:`int`)
                The maximum number of stickers to be returned
            
        """
        _constructor = SearchStickers.construct if skip_validation else SearchStickers
        
        return await self.client.request(
            _constructor(
                emoji=emoji,
                limit=limit,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_bot_start_message(
            self,
            bot_user_id: int,
            chat_id: int,
            parameter: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Invites a bot to a chat (if it is not yet a member) and sends it the /start command. Bots can't be invited to a private chat other than the chat with the bot. Bots can't be invited to channels (although they can be added as admins) and secret chats. Returns the sent message
        
        Params:
            bot_user_id (:class:`int`)
                Identifier of the bot
            
            chat_id (:class:`int`)
                Identifier of the target chat
            
            parameter (:class:`str`)
                A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)
            
        """
        _constructor = SendBotStartMessage.construct if skip_validation else SendBotStartMessage
        
        return await self.client.request(
            _constructor(
                bot_user_id=bot_user_id,
                chat_id=chat_id,
                parameter=parameter,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_call_debug_information(
            self,
            call_id: int,
            debug_information: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends debug information for a call
        
        Params:
            call_id (:class:`int`)
                Call identifier
            
            debug_information (:class:`str`)
                Debug information in application-specific format
            
        """
        _constructor = SendCallDebugInformation.construct if skip_validation else SendCallDebugInformation
        
        return await self.client.request(
            _constructor(
                call_id=call_id,
                debug_information=debug_information,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_call_rating(
            self,
            call_id: int,
            rating: int,
            comment: str,
            problems: list[CallProblem],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a call rating
        
        Params:
            call_id (:class:`int`)
                Call identifier
            
            rating (:class:`int`)
                Call rating; 1-5
            
            comment (:class:`str`)
                An optional user comment if the rating is less than 5
            
            problems (:obj:`list[CallProblem]`)
                List of the exact types of problems with the call, specified by the user
            
        """
        _constructor = SendCallRating.construct if skip_validation else SendCallRating
        
        return await self.client.request(
            _constructor(
                call_id=call_id,
                rating=rating,
                comment=comment,
                problems=problems,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_call_signaling_data(
            self,
            call_id: int,
            data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends call signaling data
        
        Params:
            call_id (:class:`int`)
                Call identifier
            
            data (:class:`str`)
                The data
            
        """
        _constructor = SendCallSignalingData.construct if skip_validation else SendCallSignalingData
        
        return await self.client.request(
            _constructor(
                call_id=call_id,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_chat_action(
            self,
            chat_id: int,
            message_thread_id: int,
            action: ChatAction,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a notification about user activity in a chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_thread_id (:class:`int`)
                If not 0, a message thread identifier in which the action was performed
            
            action (:class:`ChatAction`)
                The action description
            
        """
        _constructor = SendChatAction.construct if skip_validation else SendChatAction
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                action=action,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_chat_screenshot_taken_notification(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a notification about a screenshot taken in a chat. Supported only in private and secret chats
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
        """
        _constructor = SendChatScreenshotTakenNotification.construct if skip_validation else SendChatScreenshotTakenNotification
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_custom_request(
            self,
            method: str,
            parameters: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> CustomRequestResult:
        """
        Sends a custom request; for bots only
        
        Params:
            method (:class:`str`)
                The method name
            
            parameters (:class:`str`)
                JSON-serialized method parameters
            
        """
        _constructor = SendCustomRequest.construct if skip_validation else SendCustomRequest
        
        return await self.client.request(
            _constructor(
                method=method,
                parameters=parameters,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_email_address_verification_code(
            self,
            email_address: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> EmailAddressAuthenticationCodeInfo:
        """
        Sends a code to verify an email address to be added to a user's Telegram Passport
        
        Params:
            email_address (:class:`str`)
                Email address
            
        """
        _constructor = SendEmailAddressVerificationCode.construct if skip_validation else SendEmailAddressVerificationCode
        
        return await self.client.request(
            _constructor(
                email_address=email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_inline_query_result_message(
            self,
            chat_id: int,
            message_thread_id: int,
            reply_to_message_id: int,
            options: MessageSendOptions,
            query_id: int,
            result_id: str,
            hide_via_bot: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message
        
        Params:
            chat_id (:class:`int`)
                Target chat
            
            message_thread_id (:class:`int`)
                If not 0, a message thread identifier in which the message will be sent
            
            reply_to_message_id (:class:`int`)
                Identifier of a message to reply to or 0
            
            options (:class:`MessageSendOptions`)
                Options to be used to send the message
            
            query_id (:class:`int`)
                Identifier of the inline query
            
            result_id (:class:`str`)
                Identifier of the inline result
            
            hide_via_bot (:class:`bool`)
                If true, there will be no mention of a bot, via which the message is sent. Can be used only for bots GetOption("animation_search_bot_username"), GetOption("photo_search_bot_username") and GetOption("venue_search_bot_username")
            
        """
        _constructor = SendInlineQueryResultMessage.construct if skip_validation else SendInlineQueryResultMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                options=options,
                query_id=query_id,
                result_id=result_id,
                hide_via_bot=hide_via_bot,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_message(
            self,
            chat_id: int,
            message_thread_id: int,
            reply_to_message_id: int,
            options: MessageSendOptions,
            reply_markup: ReplyMarkup,
            input_message_content: InputMessageContent,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Sends a message. Returns the sent message
        
        Params:
            chat_id (:class:`int`)
                Target chat
            
            message_thread_id (:class:`int`)
                If not 0, a message thread identifier in which the message will be sent
            
            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0
            
            options (:class:`MessageSendOptions`)
                Options to be used to send the message
            
            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only
            
            input_message_content (:class:`InputMessageContent`)
                The content of the message to be sent
            
        """
        _constructor = SendMessage.construct if skip_validation else SendMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                options=options,
                reply_markup=reply_markup,
                input_message_content=input_message_content,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_message_album(
            self,
            chat_id: int,
            message_thread_id: int,
            reply_to_message_id: int,
            options: MessageSendOptions,
            input_message_contents: list[InputMessageContent],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Messages:
        """
        Sends 2-10 messages grouped together into an album. Currently only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages
        
        Params:
            chat_id (:class:`int`)
                Target chat
            
            message_thread_id (:class:`int`)
                If not 0, a message thread identifier in which the messages will be sent
            
            reply_to_message_id (:class:`int`)
                Identifier of a message to reply to or 0
            
            options (:class:`MessageSendOptions`)
                Options to be used to send the messages
            
            input_message_contents (:obj:`list[InputMessageContent]`)
                Contents of messages to be sent. At most 10 messages can be added to an album
            
        """
        _constructor = SendMessageAlbum.construct if skip_validation else SendMessageAlbum
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                reply_to_message_id=reply_to_message_id,
                options=options,
                input_message_contents=input_message_contents,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_passport_authorization_form(
            self,
            autorization_form_id: int,
            types: list[PassportElementType],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused
        
        Params:
            autorization_form_id (:class:`int`)
                Authorization form identifier
            
            types (:obj:`list[PassportElementType]`)
                Types of Telegram Passport elements chosen by user to complete the authorization form
            
        """
        _constructor = SendPassportAuthorizationForm.construct if skip_validation else SendPassportAuthorizationForm
        
        return await self.client.request(
            _constructor(
                autorization_form_id=autorization_form_id,
                types=types,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_payment_form(
            self,
            chat_id: int,
            message_id: int,
            order_info_id: str,
            shipping_option_id: str,
            credentials: InputCredentials,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PaymentResult:
        """
        Sends a filled-out payment form to the bot for final verification
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the Invoice message
            
            message_id (:class:`int`)
                Message identifier
            
            order_info_id (:class:`str`)
                Identifier returned by ValidateOrderInfo, or an empty string
            
            shipping_option_id (:class:`str`)
                Identifier of a chosen shipping option, if applicable
            
            credentials (:class:`InputCredentials`)
                The credentials chosen by user for payment
            
        """
        _constructor = SendPaymentForm.construct if skip_validation else SendPaymentForm
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                order_info_id=order_info_id,
                shipping_option_id=shipping_option_id,
                credentials=credentials,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_phone_number_confirmation_code(
            self,
            hash_: str,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AuthenticationCodeInfo:
        """
        Sends phone number confirmation code. Should be called when user presses "https://t.me/confirmphone?phone=*******&hash=**********" or "tg://confirmphone?phone=*******&hash=**********" link
        
        Params:
            hash_ (:class:`str`)
                Value of the "hash" parameter from the link
            
            phone_number (:class:`str`)
                Value of the "phone" parameter from the link
            
            settings (:class:`PhoneNumberAuthenticationSettings`)
                Settings for the authentication of the user's phone number
            
        """
        _constructor = SendPhoneNumberConfirmationCode.construct if skip_validation else SendPhoneNumberConfirmationCode
        
        return await self.client.request(
            _constructor(
                hash=hash_,
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def send_phone_number_verification_code(
            self,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> AuthenticationCodeInfo:
        """
        Sends a code to verify a phone number to be added to a user's Telegram Passport
        
        Params:
            phone_number (:class:`str`)
                The phone number of the user, in international format
            
            settings (:class:`PhoneNumberAuthenticationSettings`)
                Settings for the authentication of the user's phone number
            
        """
        _constructor = SendPhoneNumberVerificationCode.construct if skip_validation else SendPhoneNumberVerificationCode
        
        return await self.client.request(
            _constructor(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_account_ttl(
            self,
            ttl: AccountTtl,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the period of inactivity after which the account of the current user will automatically be deleted
        
        Params:
            ttl (:class:`AccountTtl`)
                New account TTL
            
        """
        _constructor = SetAccountTtl.construct if skip_validation else SetAccountTtl
        
        return await self.client.request(
            _constructor(
                ttl=ttl,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_alarm(
            self,
            seconds: float,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Succeeds after a specified amount of time has passed. Can be called before initialization
        
        Params:
            seconds (:class:`float`)
                Number of seconds before the function returns
            
        """
        _constructor = SetAlarm.construct if skip_validation else SetAlarm
        
        return await self.client.request(
            _constructor(
                seconds=seconds,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_authentication_phone_number(
            self,
            phone_number: str,
            settings: PhoneNumberAuthenticationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword
        
        Params:
            phone_number (:class:`str`)
                The phone number of the user, in international format
            
            settings (:class:`PhoneNumberAuthenticationSettings`)
                Settings for the authentication of the user's phone number
            
        """
        _constructor = SetAuthenticationPhoneNumber.construct if skip_validation else SetAuthenticationPhoneNumber
        
        return await self.client.request(
            _constructor(
                phone_number=phone_number,
                settings=settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_auto_download_settings(
            self,
            settings: AutoDownloadSettings,
            type_: NetworkType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets auto-download settings
        
        Params:
            settings (:class:`AutoDownloadSettings`)
                New user auto-download settings
            
            type_ (:class:`NetworkType`)
                Type of the network for which the new settings are applied
            
        """
        _constructor = SetAutoDownloadSettings.construct if skip_validation else SetAutoDownloadSettings
        
        return await self.client.request(
            _constructor(
                settings=settings,
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_background(
            self,
            background: InputBackground,
            type_: BackgroundType,
            for_dark_theme: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Background:
        """
        Changes the background selected by the user; adds background to the list of installed backgrounds
        
        Params:
            background (:class:`InputBackground`)
                The input background to use, null for filled backgrounds
            
            type_ (:class:`BackgroundType`)
                Background type; null for default background. The method will return error 404 if type is null
            
            for_dark_theme (:class:`bool`)
                True, if the background is chosen for dark theme
            
        """
        _constructor = SetBackground.construct if skip_validation else SetBackground
        
        return await self.client.request(
            _constructor(
                background=background,
                type=type_,
                for_dark_theme=for_dark_theme,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_bio(
            self,
            bio: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the bio of the current user
        
        Params:
            bio (:class:`str`)
                The new value of the user bio; 0-70 characters without line feeds
            
        """
        _constructor = SetBio.construct if skip_validation else SetBio
        
        return await self.client.request(
            _constructor(
                bio=bio,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_bot_updates_status(
            self,
            pending_update_count: int,
            error_message: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only
        
        Params:
            pending_update_count (:class:`int`)
                The number of pending updates
            
            error_message (:class:`str`)
                The last error message
            
        """
        _constructor = SetBotUpdatesStatus.construct if skip_validation else SetBotUpdatesStatus
        
        return await self.client.request(
            _constructor(
                pending_update_count=pending_update_count,
                error_message=error_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_client_data(
            self,
            chat_id: int,
            client_data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes application-specific data associated with a chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            client_data (:class:`str`)
                New value of client_data
            
        """
        _constructor = SetChatClientData.construct if skip_validation else SetChatClientData
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                client_data=client_data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_description(
            self,
            chat_id: int,
            param_description: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat
            
            param_description (:class:`str`)
                New chat description; 0-255 characters
            
        """
        _constructor = SetChatDescription.construct if skip_validation else SetChatDescription
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                param_description=param_description,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_discussion_group(
            self,
            chat_id: int,
            discussion_chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the discussion group of a channel chat; requires can_change_info administrator right in the channel if it is specified
        
        Params:
            chat_id (:class:`int`)
                Identifier of the channel chat. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages rights in the supergroup)
            
            discussion_chat_id (:class:`int`)
                Identifier of a new channel's discussion group. Use 0 to remove the discussion group. Use the method getSuitableDiscussionChats to find all suitable groups. Basic group chats must be first upgraded to supergroup chats. If new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable must be used first to change that
            
        """
        _constructor = SetChatDiscussionGroup.construct if skip_validation else SetChatDiscussionGroup
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                discussion_chat_id=discussion_chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_draft_message(
            self,
            chat_id: int,
            message_thread_id: int,
            draft_message: DraftMessage,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the draft message in a chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_thread_id (:class:`int`)
                If not 0, a message thread identifier in which the draft was changed
            
            draft_message (:class:`DraftMessage`)
                New draft message; may be null
            
        """
        _constructor = SetChatDraftMessage.construct if skip_validation else SetChatDraftMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                draft_message=draft_message,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_location(
            self,
            chat_id: int,
            location: ChatLocation,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            location (:class:`ChatLocation`)
                New location for the chat; must be valid and not null
            
        """
        _constructor = SetChatLocation.construct if skip_validation else SetChatLocation
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_member_status(
            self,
            chat_id: int,
            user_id: int,
            status: ChatMemberStatus,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for adding new members to the chat and transferring chat ownership; instead, use addChatMember or transferChatOwnership
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            user_id (:class:`int`)
                User identifier
            
            status (:class:`ChatMemberStatus`)
                The new status of the member in the chat
            
        """
        _constructor = SetChatMemberStatus.construct if skip_validation else SetChatMemberStatus
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
                status=status,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_message_ttl_setting(
            self,
            chat_id: int,
            ttl: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the message TTL setting (sets a new self-destruct timer) in a chat. Requires can_delete_messages administrator right in basic groups, supergroups and channels Message TTL setting of a chat with the current user (Saved Messages) and the chat 777000 (Telegram) can't be changed
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            ttl (:class:`int`)
                New TTL value, in seconds; must be one of 0, 86400, 604800 unless chat is secret
            
        """
        _constructor = SetChatMessageTtlSetting.construct if skip_validation else SetChatMessageTtlSetting
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                ttl=ttl,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_notification_settings(
            self,
            chat_id: int,
            notification_settings: ChatNotificationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            notification_settings (:class:`ChatNotificationSettings`)
                New notification settings for the chat. If the chat is muted for more than 1 week, it is considered to be muted forever
            
        """
        _constructor = SetChatNotificationSettings.construct if skip_validation else SetChatNotificationSettings
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                notification_settings=notification_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_permissions(
            self,
            chat_id: int,
            permissions: ChatPermissions,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            permissions (:class:`ChatPermissions`)
                New non-administrator members permissions in the chat
            
        """
        _constructor = SetChatPermissions.construct if skip_validation else SetChatPermissions
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                permissions=permissions,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_photo(
            self,
            chat_id: int,
            photo: InputChatPhoto,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            photo (:class:`InputChatPhoto`)
                New chat photo. Pass null to delete the chat photo
            
        """
        _constructor = SetChatPhoto.construct if skip_validation else SetChatPhoto
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_slow_mode_delay(
            self,
            chat_id: int,
            slow_mode_delay: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members rights
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            slow_mode_delay (:class:`int`)
                New slow mode delay for the chat; must be one of 0, 10, 30, 60, 300, 900, 3600
            
        """
        _constructor = SetChatSlowModeDelay.construct if skip_validation else SetChatSlowModeDelay
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                slow_mode_delay=slow_mode_delay,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_chat_title(
            self,
            chat_id: int,
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            title (:class:`str`)
                New title of the chat; 1-128 characters
            
        """
        _constructor = SetChatTitle.construct if skip_validation else SetChatTitle
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_commands(
            self,
            commands: list[BotCommand],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the list of commands supported by the bot; for bots only
        
        Params:
            commands (:obj:`list[BotCommand]`)
                List of the bot's commands
            
        """
        _constructor = SetCommands.construct if skip_validation else SetCommands
        
        return await self.client.request(
            _constructor(
                commands=commands,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_custom_language_pack(
            self,
            info: LanguagePackInfo,
            strings: list[LanguagePackString],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds or changes a custom local language pack to the current localization target
        
        Params:
            info (:class:`LanguagePackInfo`)
                Information about the language pack. Language pack ID must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization
            
            strings (:obj:`list[LanguagePackString]`)
                Strings of the new language pack
            
        """
        _constructor = SetCustomLanguagePack.construct if skip_validation else SetCustomLanguagePack
        
        return await self.client.request(
            _constructor(
                info=info,
                strings=strings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_custom_language_pack_string(
            self,
            language_pack_id: str,
            new_string: LanguagePackString,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Adds, edits or deletes a string in a custom local language pack. Can be called before authorization
        
        Params:
            language_pack_id (:class:`str`)
                Identifier of a previously added custom local language pack in the current localization target
            
            new_string (:class:`LanguagePackString`)
                New language pack string
            
        """
        _constructor = SetCustomLanguagePackString.construct if skip_validation else SetCustomLanguagePackString
        
        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
                new_string=new_string,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_database_encryption_key(
            self,
            new_encryption_key: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain
        
        Params:
            new_encryption_key (:class:`str`)
                New encryption key
            
        """
        _constructor = SetDatabaseEncryptionKey.construct if skip_validation else SetDatabaseEncryptionKey
        
        return await self.client.request(
            _constructor(
                new_encryption_key=new_encryption_key,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_file_generation_progress(
            self,
            generation_id: int,
            expected_size: int,
            local_prefix_size: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib on a file generation progress
        
        Params:
            generation_id (:class:`int`)
                The identifier of the generation process
            
            expected_size (:class:`int`)
                Expected size of the generated file, in bytes; 0 if unknown
            
            local_prefix_size (:class:`int`)
                The number of bytes already generated
            
        """
        _constructor = SetFileGenerationProgress.construct if skip_validation else SetFileGenerationProgress
        
        return await self.client.request(
            _constructor(
                generation_id=generation_id,
                expected_size=expected_size,
                local_prefix_size=local_prefix_size,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_game_score(
            self,
            chat_id: int,
            message_id: int,
            edit_message: bool,
            user_id: int,
            score: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Message:
        """
        Updates the game score of the specified user in the game; for bots only
        
        Params:
            chat_id (:class:`int`)
                The chat to which the message with the game belongs
            
            message_id (:class:`int`)
                Identifier of the message
            
            edit_message (:class:`bool`)
                True, if the message should be edited
            
            user_id (:class:`int`)
                User identifier
            
            score (:class:`int`)
                The new score
            
            force (:class:`bool`)
                Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
            
        """
        _constructor = SetGameScore.construct if skip_validation else SetGameScore
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                edit_message=edit_message,
                user_id=user_id,
                score=score,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_group_call_participant_is_speaking(
            self,
            group_call_id: int,
            source: int,
            is_speaking: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that a group call participant speaking state has changed
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            source (:class:`int`)
                Group call participant's synchronization source identifier, or 0 for the current user
            
            is_speaking (:class:`bool`)
                True, if the user is speaking
            
        """
        _constructor = SetGroupCallParticipantIsSpeaking.construct if skip_validation else SetGroupCallParticipantIsSpeaking
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                source=source,
                is_speaking=is_speaking,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_group_call_participant_volume_level(
            self,
            group_call_id: int,
            participant: MessageSender,
            volume_level: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes a group call participant's volume level. If the current user can manage the group call, then the participant's volume level will be changed for all users with default volume level
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            participant (:class:`MessageSender`)
                Participant identifier
            
            volume_level (:class:`int`)
                New participant's volume level; 1-20000 in hundreds of percents
            
        """
        _constructor = SetGroupCallParticipantVolumeLevel.construct if skip_validation else SetGroupCallParticipantVolumeLevel
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant=participant,
                volume_level=volume_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_group_call_title(
            self,
            group_call_id: int,
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets group call title. Requires groupCall.can_be_managed group call flag
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            title (:class:`str`)
                New group call title; 1-64 characters
            
        """
        _constructor = SetGroupCallTitle.construct if skip_validation else SetGroupCallTitle
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_inline_game_score(
            self,
            inline_message_id: str,
            edit_message: bool,
            user_id: int,
            score: int,
            force: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Updates the game score of the specified user in a game; for bots only
        
        Params:
            inline_message_id (:class:`str`)
                Inline message identifier
            
            edit_message (:class:`bool`)
                True, if the message should be edited
            
            user_id (:class:`int`)
                User identifier
            
            score (:class:`int`)
                The new score
            
            force (:class:`bool`)
                Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
            
        """
        _constructor = SetInlineGameScore.construct if skip_validation else SetInlineGameScore
        
        return await self.client.request(
            _constructor(
                inline_message_id=inline_message_id,
                edit_message=edit_message,
                user_id=user_id,
                score=score,
                force=force,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_location(
            self,
            location: Location,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the location of the current user. Needs to be called if GetOption("is_location_visible") is true and location changes for more than 1 kilometer
        
        Params:
            location (:class:`Location`)
                The new location of the user
            
        """
        _constructor = SetLocation.construct if skip_validation else SetLocation
        
        return await self.client.request(
            _constructor(
                location=location,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_log_stream(
            self,
            log_stream: LogStream,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets new log stream for internal logging of TDLib. Can be called synchronously
        
        Params:
            log_stream (:class:`LogStream`)
                New log stream
            
        """
        _constructor = SetLogStream.construct if skip_validation else SetLogStream
        
        return await self.client.request(
            _constructor(
                log_stream=log_stream,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_log_tag_verbosity_level(
            self,
            tag: str,
            new_verbosity_level: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously
        
        Params:
            tag (:class:`str`)
                Logging tag to change verbosity level
            
            new_verbosity_level (:class:`int`)
                New verbosity level; 1-1024
            
        """
        _constructor = SetLogTagVerbosityLevel.construct if skip_validation else SetLogTagVerbosityLevel
        
        return await self.client.request(
            _constructor(
                tag=tag,
                new_verbosity_level=new_verbosity_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_log_verbosity_level(
            self,
            new_verbosity_level: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the verbosity level of the internal logging of TDLib. Can be called synchronously
        
        Params:
            new_verbosity_level (:class:`int`)
                New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging
            
        """
        _constructor = SetLogVerbosityLevel.construct if skip_validation else SetLogVerbosityLevel
        
        return await self.client.request(
            _constructor(
                new_verbosity_level=new_verbosity_level,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_name(
            self,
            first_name: str,
            last_name: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the first and last name of the current user
        
        Params:
            first_name (:class:`str`)
                The new value of the first name for the user; 1-64 characters
            
            last_name (:class:`str`)
                The new value of the optional last name for the user; 0-64 characters
            
        """
        _constructor = SetName.construct if skip_validation else SetName
        
        return await self.client.request(
            _constructor(
                first_name=first_name,
                last_name=last_name,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_network_type(
            self,
            type_: NetworkType,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it should be called whenever the network is changed, even if the network type remains the same. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics
        
        Params:
            type_ (:class:`NetworkType`)
                The new network type. By default, networkTypeOther
            
        """
        _constructor = SetNetworkType.construct if skip_validation else SetNetworkType
        
        return await self.client.request(
            _constructor(
                type=type_,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_option(
            self,
            name: str,
            value: OptionValue,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization
        
        Params:
            name (:class:`str`)
                The name of the option
            
            value (:class:`OptionValue`)
                The new value of the option
            
        """
        _constructor = SetOption.construct if skip_validation else SetOption
        
        return await self.client.request(
            _constructor(
                name=name,
                value=value,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_passport_element(
            self,
            element: InputPassportElement,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PassportElement:
        """
        Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first
        
        Params:
            element (:class:`InputPassportElement`)
                Input Telegram Passport element
            
            password (:class:`str`)
                Password of the current user
            
        """
        _constructor = SetPassportElement.construct if skip_validation else SetPassportElement
        
        return await self.client.request(
            _constructor(
                element=element,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_passport_element_errors(
            self,
            user_id: int,
            errors: list[InputPassportElementError],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed
        
        Params:
            user_id (:class:`int`)
                User identifier
            
            errors (:obj:`list[InputPassportElementError]`)
                The errors
            
        """
        _constructor = SetPassportElementErrors.construct if skip_validation else SetPassportElementErrors
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                errors=errors,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_password(
            self,
            old_password: str,
            new_password: str,
            new_hint: str,
            set_recovery_email_address: bool,
            new_recovery_email_address: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Changes the password for the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed
        
        Params:
            old_password (:class:`str`)
                Previous password of the user
            
            new_password (:class:`str`)
                New password of the user; may be empty to remove the password
            
            new_hint (:class:`str`)
                New password hint; may be empty
            
            set_recovery_email_address (:class:`bool`)
                Pass true if the recovery email address should be changed
            
            new_recovery_email_address (:class:`str`)
                New recovery email address; may be empty
            
        """
        _constructor = SetPassword.construct if skip_validation else SetPassword
        
        return await self.client.request(
            _constructor(
                old_password=old_password,
                new_password=new_password,
                new_hint=new_hint,
                set_recovery_email_address=set_recovery_email_address,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_pinned_chats(
            self,
            chat_list: ChatList,
            chat_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the order of pinned chats
        
        Params:
            chat_list (:class:`ChatList`)
                Chat list in which to change the order of pinned chats
            
            chat_ids (:obj:`list[int]`)
                The new list of pinned chats
            
        """
        _constructor = SetPinnedChats.construct if skip_validation else SetPinnedChats
        
        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                chat_ids=chat_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_poll_answer(
            self,
            chat_id: int,
            message_id: int,
            option_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the user answer to a poll. A poll in quiz mode can be answered only once
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to which the poll belongs
            
            message_id (:class:`int`)
                Identifier of the message containing the poll
            
            option_ids (:obj:`list[int]`)
                0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
            
        """
        _constructor = SetPollAnswer.construct if skip_validation else SetPollAnswer
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                option_ids=option_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_profile_photo(
            self,
            photo: InputChatPhoto,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes a profile photo for the current user
        
        Params:
            photo (:class:`InputChatPhoto`)
                Profile photo to set
            
        """
        _constructor = SetProfilePhoto.construct if skip_validation else SetProfilePhoto
        
        return await self.client.request(
            _constructor(
                photo=photo,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_recovery_email_address(
            self,
            password: str,
            new_recovery_email_address: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> PasswordState:
        """
        Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed. If new_recovery_email_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation
        
        Params:
            password (:class:`str`)
                Password of the current user
            
            new_recovery_email_address (:class:`str`)
                New recovery email address
            
        """
        _constructor = SetRecoveryEmailAddress.construct if skip_validation else SetRecoveryEmailAddress
        
        return await self.client.request(
            _constructor(
                password=password,
                new_recovery_email_address=new_recovery_email_address,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_scope_notification_settings(
            self,
            scope: NotificationSettingsScope,
            notification_settings: ScopeNotificationSettings,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes notification settings for chats of a given type
        
        Params:
            scope (:class:`NotificationSettingsScope`)
                Types of chats for which to change the notification settings
            
            notification_settings (:class:`ScopeNotificationSettings`)
                The new notification settings for the given scope
            
        """
        _constructor = SetScopeNotificationSettings.construct if skip_validation else SetScopeNotificationSettings
        
        return await self.client.request(
            _constructor(
                scope=scope,
                notification_settings=notification_settings,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_sticker_position_in_set(
            self,
            sticker: InputFile,
            position: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot
        
        Params:
            sticker (:class:`InputFile`)
                Sticker
            
            position (:class:`int`)
                New position of the sticker in the set, zero-based
            
        """
        _constructor = SetStickerPositionInSet.construct if skip_validation else SetStickerPositionInSet
        
        return await self.client.request(
            _constructor(
                sticker=sticker,
                position=position,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_sticker_set_thumbnail(
            self,
            user_id: int,
            name: str,
            thumbnail: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> StickerSet:
        """
        Sets a sticker set thumbnail; for bots only. Returns the sticker set
        
        Params:
            user_id (:class:`int`)
                Sticker set owner
            
            name (:class:`str`)
                Sticker set name
            
            thumbnail (:class:`InputFile`)
                Thumbnail to set in PNG or TGS format. Animated thumbnail must be set for animated sticker sets and only for them. Pass a zero InputFileId to delete the thumbnail
            
        """
        _constructor = SetStickerSetThumbnail.construct if skip_validation else SetStickerSetThumbnail
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                name=name,
                thumbnail=thumbnail,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_supergroup_sticker_set(
            self,
            supergroup_id: int,
            sticker_set_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the sticker set of a supergroup; requires can_change_info administrator right
        
        Params:
            supergroup_id (:class:`int`)
                Identifier of the supergroup
            
            sticker_set_id (:class:`int`)
                New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set
            
        """
        _constructor = SetSupergroupStickerSet.construct if skip_validation else SetSupergroupStickerSet
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                sticker_set_id=sticker_set_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_supergroup_username(
            self,
            supergroup_id: int,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the username of a supergroup or channel, requires owner privileges in the supergroup or channel
        
        Params:
            supergroup_id (:class:`int`)
                Identifier of the supergroup or channel
            
            username (:class:`str`)
                New value of the username. Use an empty string to remove the username
            
        """
        _constructor = SetSupergroupUsername.construct if skip_validation else SetSupergroupUsername
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_tdlib_parameters(
            self,
            parameters: TdlibParameters,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters
        
        Params:
            parameters (:class:`TdlibParameters`)
                Parameters
            
        """
        _constructor = SetTdlibParameters.construct if skip_validation else SetTdlibParameters
        
        return await self.client.request(
            _constructor(
                parameters=parameters,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_user_privacy_setting_rules(
            self,
            setting: UserPrivacySetting,
            rules: UserPrivacySettingRules,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes user privacy settings
        
        Params:
            setting (:class:`UserPrivacySetting`)
                The privacy setting
            
            rules (:class:`UserPrivacySettingRules`)
                The new privacy rules
            
        """
        _constructor = SetUserPrivacySettingRules.construct if skip_validation else SetUserPrivacySettingRules
        
        return await self.client.request(
            _constructor(
                setting=setting,
                rules=rules,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def set_username(
            self,
            username: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the username of the current user
        
        Params:
            username (:class:`str`)
                The new value of the username. Use an empty string to remove the username
            
        """
        _constructor = SetUsername.construct if skip_validation else SetUsername
        
        return await self.client.request(
            _constructor(
                username=username,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def share_phone_number(
            self,
            user_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber
        
        Params:
            user_id (:class:`int`)
                Identifier of the user with whom to share the phone number. The user must be a mutual contact
            
        """
        _constructor = SharePhoneNumber.construct if skip_validation else SharePhoneNumber
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def start_group_call_recording(
            self,
            group_call_id: int,
            title: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Starts recording of a group call. Requires groupCall.can_be_managed group call flag
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            title (:class:`str`)
                Group call recording title; 0-64 characters
            
        """
        _constructor = StartGroupCallRecording.construct if skip_validation else StartGroupCallRecording
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                title=title,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def stop_poll(
            self,
            chat_id: int,
            message_id: int,
            reply_markup: ReplyMarkup,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Stops a poll. A poll in a message can be stopped when the message has can_be_edited flag set
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to which the poll belongs
            
            message_id (:class:`int`)
                Identifier of the message containing the poll
            
            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup; for bots only
            
        """
        _constructor = StopPoll.construct if skip_validation else StopPoll
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=reply_markup,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def synchronize_language_pack(
            self,
            language_pack_id: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Fetches the latest versions of all strings from a language pack in the current localization target from the server. This method shouldn't be called explicitly for the current used/base language packs. Can be called before authorization
        
        Params:
            language_pack_id (:class:`str`)
                Language pack identifier
            
        """
        _constructor = SynchronizeLanguagePack.construct if skip_validation else SynchronizeLanguagePack
        
        return await self.client.request(
            _constructor(
                language_pack_id=language_pack_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def terminate_all_other_sessions(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Terminates all other sessions of the current user
        
        """
        return await self.client.request(
            TerminateAllOtherSessions(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def terminate_session(
            self,
            session_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Terminates a session of the current user
        
        Params:
            session_id (:class:`int`)
                Session identifier
            
        """
        _constructor = TerminateSession.construct if skip_validation else TerminateSession
        
        return await self.client.request(
            _constructor(
                session_id=session_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_call_bytes(
            self,
            x: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestBytes:
        """
        Returns the received bytes; for testing only. This is an offline method. Can be called before authorization
        
        Params:
            x (:class:`str`)
                Bytes to return
            
        """
        _constructor = TestCallBytes.construct if skip_validation else TestCallBytes
        
        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_call_empty(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Does nothing; for testing only. This is an offline method. Can be called before authorization
        
        """
        return await self.client.request(
            TestCallEmpty(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_call_string(
            self,
            x: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestString:
        """
        Returns the received string; for testing only. This is an offline method. Can be called before authorization
        
        Params:
            x (:class:`str`)
                String to return
            
        """
        _constructor = TestCallString.construct if skip_validation else TestCallString
        
        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_call_vector_int(
            self,
            x: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorInt:
        """
        Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization
        
        Params:
            x (:obj:`list[int]`)
                Vector of numbers to return
            
        """
        _constructor = TestCallVectorInt.construct if skip_validation else TestCallVectorInt
        
        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_call_vector_int_object(
            self,
            x: list[TestInt],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorIntObject:
        """
        Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization
        
        Params:
            x (:obj:`list[TestInt]`)
                Vector of objects to return
            
        """
        _constructor = TestCallVectorIntObject.construct if skip_validation else TestCallVectorIntObject
        
        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_call_vector_string(
            self,
            x: list[str],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorString:
        """
        Returns the received vector of strings; for testing only. This is an offline method. Can be called before authorization
        
        Params:
            x (:obj:`list[str]`)
                Vector of strings to return
            
        """
        _constructor = TestCallVectorString.construct if skip_validation else TestCallVectorString
        
        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_call_vector_string_object(
            self,
            x: list[TestString],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestVectorStringObject:
        """
        Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization
        
        Params:
            x (:obj:`list[TestString]`)
                Vector of objects to return
            
        """
        _constructor = TestCallVectorStringObject.construct if skip_validation else TestCallVectorStringObject
        
        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_get_difference(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Forces an updates.getDifference call to the Telegram servers; for testing only
        
        """
        return await self.client.request(
            TestGetDifference(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_network(self, *, request_id: str = None, request_timeout: int = None) -> Ok:
        """
        Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
        
        """
        return await self.client.request(
            TestNetwork(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_proxy(
            self,
            server: str,
            port: int,
            type_: ProxyType,
            dc_id: int,
            timeout: float,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization
        
        Params:
            server (:class:`str`)
                Proxy server IP address
            
            port (:class:`int`)
                Proxy server port
            
            type_ (:class:`ProxyType`)
                Proxy type
            
            dc_id (:class:`int`)
                Identifier of a datacenter, with which to test connection
            
            timeout (:class:`float`)
                The maximum overall timeout for the request
            
        """
        _constructor = TestProxy.construct if skip_validation else TestProxy
        
        return await self.client.request(
            _constructor(
                server=server,
                port=port,
                type=type_,
                dc_id=dc_id,
                timeout=timeout,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_return_error(
            self,
            error: Error,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Error:
        """
        Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously
        
        Params:
            error (:class:`Error`)
                The error to be returned
            
        """
        _constructor = TestReturnError.construct if skip_validation else TestReturnError
        
        return await self.client.request(
            _constructor(
                error=error,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_square_int(
            self,
            x: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> TestInt:
        """
        Returns the squared received number; for testing only. This is an offline method. Can be called before authorization
        
        Params:
            x (:class:`int`)
                Number to square
            
        """
        _constructor = TestSquareInt.construct if skip_validation else TestSquareInt
        
        return await self.client.request(
            _constructor(
                x=x,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def test_use_update(self, *, request_id: str = None, request_timeout: int = None) -> Update:
        """
        Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization
        
        """
        return await self.client.request(
            TestUseUpdate(),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_chat_default_disable_notification(
            self,
            chat_id: int,
            default_disable_notification: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the value of the default disable_notification parameter, used when a message is sent to a chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            default_disable_notification (:class:`bool`)
                New value of default_disable_notification
            
        """
        _constructor = ToggleChatDefaultDisableNotification.construct if skip_validation else ToggleChatDefaultDisableNotification
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                default_disable_notification=default_disable_notification,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_chat_is_marked_as_unread(
            self,
            chat_id: int,
            is_marked_as_unread: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the marked as unread state of a chat
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            is_marked_as_unread (:class:`bool`)
                New value of is_marked_as_unread
            
        """
        _constructor = ToggleChatIsMarkedAsUnread.construct if skip_validation else ToggleChatIsMarkedAsUnread
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                is_marked_as_unread=is_marked_as_unread,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_chat_is_pinned(
            self,
            chat_list: ChatList,
            chat_id: int,
            is_pinned: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the pinned state of a chat. There can be up to GetOption("pinned_chat_count_max")/GetOption("pinned_archived_chat_count_max") pinned non-secret chats and the same number of secret chats in the main/arhive chat list
        
        Params:
            chat_list (:class:`ChatList`)
                Chat list in which to change the pinned state of the chat
            
            chat_id (:class:`int`)
                Chat identifier
            
            is_pinned (:class:`bool`)
                True, if the chat is pinned
            
        """
        _constructor = ToggleChatIsPinned.construct if skip_validation else ToggleChatIsPinned
        
        return await self.client.request(
            _constructor(
                chat_list=chat_list,
                chat_id=chat_id,
                is_pinned=is_pinned,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_group_call_mute_new_participants(
            self,
            group_call_id: int,
            mute_new_participants: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_change_mute_new_participants group call flag
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            mute_new_participants (:class:`bool`)
                New value of the mute_new_participants setting
            
        """
        _constructor = ToggleGroupCallMuteNewParticipants.construct if skip_validation else ToggleGroupCallMuteNewParticipants
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                mute_new_participants=mute_new_participants,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_group_call_participant_is_hand_raised(
            self,
            group_call_id: int,
            participant: MessageSender,
            is_hand_raised: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether a group call participant hand is rased
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            participant (:class:`MessageSender`)
                Participant identifier
            
            is_hand_raised (:class:`bool`)
                Pass true if the user's hand should be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand
            
        """
        _constructor = ToggleGroupCallParticipantIsHandRaised.construct if skip_validation else ToggleGroupCallParticipantIsHandRaised
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant=participant,
                is_hand_raised=is_hand_raised,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_group_call_participant_is_muted(
            self,
            group_call_id: int,
            participant: MessageSender,
            is_muted: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether a group call participant is muted, unmuted, or allowed to unmute themself
        
        Params:
            group_call_id (:class:`int`)
                Group call identifier
            
            participant (:class:`MessageSender`)
                Participant identifier
            
            is_muted (:class:`bool`)
                Pass true if the user must be muted and false otherwise
            
        """
        _constructor = ToggleGroupCallParticipantIsMuted.construct if skip_validation else ToggleGroupCallParticipantIsMuted
        
        return await self.client.request(
            _constructor(
                group_call_id=group_call_id,
                participant=participant,
                is_muted=is_muted,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_message_sender_is_blocked(
            self,
            sender: MessageSender,
            is_blocked: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the block state of a message sender. Currently, only users and supergroup chats can be blocked
        
        Params:
            sender (:class:`MessageSender`)
                Message Sender
            
            is_blocked (:class:`bool`)
                New value of is_blocked
            
        """
        _constructor = ToggleMessageSenderIsBlocked.construct if skip_validation else ToggleMessageSenderIsBlocked
        
        return await self.client.request(
            _constructor(
                sender=sender,
                is_blocked=is_blocked,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_supergroup_is_all_history_available(
            self,
            supergroup_id: int,
            is_all_history_available: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles whether the message history of a supergroup is available to new members; requires can_change_info administrator right
        
        Params:
            supergroup_id (:class:`int`)
                The identifier of the supergroup
            
            is_all_history_available (:class:`bool`)
                The new value of is_all_history_available
            
        """
        _constructor = ToggleSupergroupIsAllHistoryAvailable.construct if skip_validation else ToggleSupergroupIsAllHistoryAvailable
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                is_all_history_available=is_all_history_available,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_supergroup_is_broadcast_group(
            self,
            supergroup_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup
        
        Params:
            supergroup_id (:class:`int`)
                Identifier of the supergroup
            
        """
        _constructor = ToggleSupergroupIsBroadcastGroup.construct if skip_validation else ToggleSupergroupIsBroadcastGroup
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def toggle_supergroup_sign_messages(
            self,
            supergroup_id: int,
            sign_messages: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Toggles sender signatures messages sent in a channel; requires can_change_info administrator right
        
        Params:
            supergroup_id (:class:`int`)
                Identifier of the channel
            
            sign_messages (:class:`bool`)
                New value of sign_messages
            
        """
        _constructor = ToggleSupergroupSignMessages.construct if skip_validation else ToggleSupergroupSignMessages
        
        return await self.client.request(
            _constructor(
                supergroup_id=supergroup_id,
                sign_messages=sign_messages,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def transfer_chat_ownership(
            self,
            chat_id: int,
            user_id: int,
            password: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Changes the owner of a chat. The current user must be a current owner of the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            user_id (:class:`int`)
                Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user
            
            password (:class:`str`)
                The password of the current user
            
        """
        _constructor = TransferChatOwnership.construct if skip_validation else TransferChatOwnership
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                user_id=user_id,
                password=password,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def unpin_all_chat_messages(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes all pinned messages from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat
            
        """
        _constructor = UnpinAllChatMessages.construct if skip_validation else UnpinAllChatMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def unpin_chat_message(
            self,
            chat_id: int,
            message_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Removes a pinned message from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat
            
            message_id (:class:`int`)
                Identifier of the removed pinned message
            
        """
        _constructor = UnpinChatMessage.construct if skip_validation else UnpinChatMessage
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def upgrade_basic_group_chat_to_supergroup_chat(
            self,
            chat_id: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Chat:
        """
        Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group
        
        Params:
            chat_id (:class:`int`)
                Identifier of the chat to upgrade
            
        """
        _constructor = UpgradeBasicGroupChatToSupergroupChat.construct if skip_validation else UpgradeBasicGroupChatToSupergroupChat
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def upload_file(
            self,
            file: InputFile,
            file_type: FileType,
            priority: int,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Asynchronously uploads a file to the cloud without sending it in a message. updateFile will be used to notify about upload progress and successful completion of the upload. The file will not have a persistent remote identifier until it will be sent in a message
        
        Params:
            file (:class:`InputFile`)
                File to upload
            
            file_type (:class:`FileType`)
                File type
            
            priority (:class:`int`)
                Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which uploadFile was called will be uploaded first
            
        """
        _constructor = UploadFile.construct if skip_validation else UploadFile
        
        return await self.client.request(
            _constructor(
                file=file,
                file_type=file_type,
                priority=priority,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def upload_sticker_file(
            self,
            user_id: int,
            png_sticker: InputFile,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> File:
        """
        Uploads a PNG image with a sticker; for bots only; returns the uploaded file
        
        Params:
            user_id (:class:`int`)
                Sticker file owner
            
            png_sticker (:class:`InputFile`)
                PNG image with the sticker; must be up to 512 KB in size and fit in 512x512 square
            
        """
        _constructor = UploadStickerFile.construct if skip_validation else UploadStickerFile
        
        return await self.client.request(
            _constructor(
                user_id=user_id,
                png_sticker=png_sticker,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def validate_order_info(
            self,
            chat_id: int,
            message_id: int,
            order_info: OrderInfo,
            allow_save: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> ValidatedOrderInfo:
        """
        Validates the order information provided by a user and returns the available shipping options for a flexible invoice
        
        Params:
            chat_id (:class:`int`)
                Chat identifier of the Invoice message
            
            message_id (:class:`int`)
                Message identifier
            
            order_info (:class:`OrderInfo`)
                The order information, provided by the user
            
            allow_save (:class:`bool`)
                True, if the order information can be saved
            
        """
        _constructor = ValidateOrderInfo.construct if skip_validation else ValidateOrderInfo
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_id=message_id,
                order_info=order_info,
                allow_save=allow_save,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def view_messages(
            self,
            chat_id: int,
            message_thread_id: int,
            message_ids: list[int],
            force_read: bool,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs TDLib that messages are being viewed by the user. Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels)
        
        Params:
            chat_id (:class:`int`)
                Chat identifier
            
            message_thread_id (:class:`int`)
                If not 0, a message thread identifier in which the messages are being viewed
            
            message_ids (:obj:`list[int]`)
                The identifiers of the messages being viewed
            
            force_read (:class:`bool`)
                True, if messages in closed chats should be marked as read by the request
            
        """
        _constructor = ViewMessages.construct if skip_validation else ViewMessages
        
        return await self.client.request(
            _constructor(
                chat_id=chat_id,
                message_thread_id=message_thread_id,
                message_ids=message_ids,
                force_read=force_read,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def view_trending_sticker_sets(
            self,
            sticker_set_ids: list[int],
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Informs the server that some trending sticker sets have been viewed by the user
        
        Params:
            sticker_set_ids (:obj:`list[int]`)
                Identifiers of viewed trending sticker sets
            
        """
        _constructor = ViewTrendingStickerSets.construct if skip_validation else ViewTrendingStickerSets
        
        return await self.client.request(
            _constructor(
                sticker_set_ids=sticker_set_ids,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    
    async def write_generated_file_part(
            self,
            generation_id: int,
            offset: int,
            data: str,
            *,
            request_id: str = None,
            request_timeout: int = None,
            skip_validation: bool = False
    ) -> Ok:
        """
        Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file
        
        Params:
            generation_id (:class:`int`)
                The identifier of the generation process
            
            offset (:class:`int`)
                The offset from which to write the data to the file
            
            data (:class:`str`)
                The data to write
            
        """
        _constructor = WriteGeneratedFilePart.construct if skip_validation else WriteGeneratedFilePart
        
        return await self.client.request(
            _constructor(
                generation_id=generation_id,
                offset=offset,
                data=data,
            ),
            request_id=request_id,
            request_timeout=request_timeout,
        )
    