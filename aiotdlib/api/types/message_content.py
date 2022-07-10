# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .animated_emoji import AnimatedEmoji
from .animation import Animation
from .audio import Audio
from .call_discard_reason import CallDiscardReason
from .chat_photo import ChatPhoto
from .contact import Contact
from .dice_stickers import DiceStickers
from .document import Document
from .encrypted_credentials import EncryptedCredentials
from .encrypted_passport_element import EncryptedPassportElement
from .formatted_text import FormattedText
from .game import Game
from .location import Location
from .message_sender import MessageSender
from .order_info import OrderInfo
from .passport_element_type import PassportElementType
from .photo import Photo
from .poll import Poll
from .sticker import Sticker
from .venue import Venue
from .video import Video
from .video_note import VideoNote
from .voice_note import VoiceNote
from .web_page import WebPage
from ..base_object import BaseObject


class MessageContent(BaseObject):
    """
    Contains the content of a message
    
    """

    ID: str = Field("messageContent", alias="@type")


class MessageAnimatedEmoji(MessageContent):
    """
    A message with an animated emoji
    
    :param animated_emoji: The animated emoji
    :type animated_emoji: :class:`AnimatedEmoji`
    
    :param emoji: The corresponding emoji
    :type emoji: :class:`str`
    
    """

    ID: str = Field("messageAnimatedEmoji", alias="@type")
    animated_emoji: AnimatedEmoji
    emoji: str

    @staticmethod
    def read(q: dict) -> MessageAnimatedEmoji:
        return MessageAnimatedEmoji.construct(**q)


class MessageAnimation(MessageContent):
    """
    An animation message (GIF-style).
    
    :param animation: The animation description
    :type animation: :class:`Animation`
    
    :param caption: Animation caption
    :type caption: :class:`FormattedText`
    
    :param is_secret: True, if the animation thumbnail must be blurred and the animation must be shown only while tapped
    :type is_secret: :class:`bool`
    
    """

    ID: str = Field("messageAnimation", alias="@type")
    animation: Animation
    caption: FormattedText
    is_secret: bool

    @staticmethod
    def read(q: dict) -> MessageAnimation:
        return MessageAnimation.construct(**q)


class MessageAudio(MessageContent):
    """
    An audio message
    
    :param audio: The audio description
    :type audio: :class:`Audio`
    
    :param caption: Audio caption
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("messageAudio", alias="@type")
    audio: Audio
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageAudio:
        return MessageAudio.construct(**q)


class MessageBasicGroupChatCreate(MessageContent):
    """
    A newly created basic group
    
    :param title: Title of the basic group
    :type title: :class:`str`
    
    :param member_user_ids: User identifiers of members in the basic group
    :type member_user_ids: :class:`list[int]`
    
    """

    ID: str = Field("messageBasicGroupChatCreate", alias="@type")
    title: str
    member_user_ids: list[int]

    @staticmethod
    def read(q: dict) -> MessageBasicGroupChatCreate:
        return MessageBasicGroupChatCreate.construct(**q)


class MessageCall(MessageContent):
    """
    A message with information about an ended call
    
    :param is_video: True, if the call was a video call
    :type is_video: :class:`bool`
    
    :param discard_reason: Reason why the call was discarded
    :type discard_reason: :class:`CallDiscardReason`
    
    :param duration: Call duration, in seconds
    :type duration: :class:`int`
    
    """

    ID: str = Field("messageCall", alias="@type")
    is_video: bool
    discard_reason: CallDiscardReason
    duration: int

    @staticmethod
    def read(q: dict) -> MessageCall:
        return MessageCall.construct(**q)


class MessageChatAddMembers(MessageContent):
    """
    New chat members were added
    
    :param member_user_ids: User identifiers of the new members
    :type member_user_ids: :class:`list[int]`
    
    """

    ID: str = Field("messageChatAddMembers", alias="@type")
    member_user_ids: list[int]

    @staticmethod
    def read(q: dict) -> MessageChatAddMembers:
        return MessageChatAddMembers.construct(**q)


class MessageChatChangePhoto(MessageContent):
    """
    An updated chat photo
    
    :param photo: New chat photo
    :type photo: :class:`ChatPhoto`
    
    """

    ID: str = Field("messageChatChangePhoto", alias="@type")
    photo: ChatPhoto

    @staticmethod
    def read(q: dict) -> MessageChatChangePhoto:
        return MessageChatChangePhoto.construct(**q)


class MessageChatChangeTitle(MessageContent):
    """
    An updated chat title
    
    :param title: New chat title
    :type title: :class:`str`
    
    """

    ID: str = Field("messageChatChangeTitle", alias="@type")
    title: str

    @staticmethod
    def read(q: dict) -> MessageChatChangeTitle:
        return MessageChatChangeTitle.construct(**q)


class MessageChatDeleteMember(MessageContent):
    """
    A chat member was deleted
    
    :param user_id: User identifier of the deleted chat member
    :type user_id: :class:`int`
    
    """

    ID: str = Field("messageChatDeleteMember", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> MessageChatDeleteMember:
        return MessageChatDeleteMember.construct(**q)


class MessageChatDeletePhoto(MessageContent):
    """
    A deleted chat photo
    
    """

    ID: str = Field("messageChatDeletePhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageChatDeletePhoto:
        return MessageChatDeletePhoto.construct(**q)


class MessageChatJoinByLink(MessageContent):
    """
    A new member joined the chat via an invite link
    
    """

    ID: str = Field("messageChatJoinByLink", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageChatJoinByLink:
        return MessageChatJoinByLink.construct(**q)


class MessageChatJoinByRequest(MessageContent):
    """
    A new member was accepted to the chat by an administrator
    
    """

    ID: str = Field("messageChatJoinByRequest", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageChatJoinByRequest:
        return MessageChatJoinByRequest.construct(**q)


class MessageChatSetTheme(MessageContent):
    """
    A theme in the chat has been changed
    
    :param theme_name: If non-empty, name of a new theme, set for the chat. Otherwise chat theme was reset to the default one
    :type theme_name: :class:`str`
    
    """

    ID: str = Field("messageChatSetTheme", alias="@type")
    theme_name: str

    @staticmethod
    def read(q: dict) -> MessageChatSetTheme:
        return MessageChatSetTheme.construct(**q)


class MessageChatSetTtl(MessageContent):
    """
    The TTL (Time To Live) setting for messages in the chat has been changed
    
    :param ttl: New message TTL
    :type ttl: :class:`int`
    
    """

    ID: str = Field("messageChatSetTtl", alias="@type")
    ttl: int

    @staticmethod
    def read(q: dict) -> MessageChatSetTtl:
        return MessageChatSetTtl.construct(**q)


class MessageChatUpgradeFrom(MessageContent):
    """
    A supergroup has been created from a basic group
    
    :param title: Title of the newly created supergroup
    :type title: :class:`str`
    
    :param basic_group_id: The identifier of the original basic group
    :type basic_group_id: :class:`int`
    
    """

    ID: str = Field("messageChatUpgradeFrom", alias="@type")
    title: str
    basic_group_id: int

    @staticmethod
    def read(q: dict) -> MessageChatUpgradeFrom:
        return MessageChatUpgradeFrom.construct(**q)


class MessageChatUpgradeTo(MessageContent):
    """
    A basic group was upgraded to a supergroup and was deactivated as the result
    
    :param supergroup_id: Identifier of the supergroup to which the basic group was upgraded
    :type supergroup_id: :class:`int`
    
    """

    ID: str = Field("messageChatUpgradeTo", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> MessageChatUpgradeTo:
        return MessageChatUpgradeTo.construct(**q)


class MessageContact(MessageContent):
    """
    A message with a user contact
    
    :param contact: The contact description
    :type contact: :class:`Contact`
    
    """

    ID: str = Field("messageContact", alias="@type")
    contact: Contact

    @staticmethod
    def read(q: dict) -> MessageContact:
        return MessageContact.construct(**q)


class MessageContactRegistered(MessageContent):
    """
    A contact has registered with Telegram
    
    """

    ID: str = Field("messageContactRegistered", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageContactRegistered:
        return MessageContactRegistered.construct(**q)


class MessageCustomServiceAction(MessageContent):
    """
    A non-standard action has happened in the chat
    
    :param text: Message text to be shown in the chat
    :type text: :class:`str`
    
    """

    ID: str = Field("messageCustomServiceAction", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> MessageCustomServiceAction:
        return MessageCustomServiceAction.construct(**q)


class MessageDice(MessageContent):
    """
    A dice message. The dice value is randomly generated by the server
    
    :param initial_state: The animated stickers with the initial dice animation; may be null if unknown. updateMessageContent will be sent when the sticker became known, defaults to None
    :type initial_state: :class:`DiceStickers`, optional
    
    :param final_state: The animated stickers with the final dice animation; may be null if unknown. updateMessageContent will be sent when the sticker became known, defaults to None
    :type final_state: :class:`DiceStickers`, optional
    
    :param emoji: Emoji on which the dice throw animation is based
    :type emoji: :class:`str`
    
    :param value: The dice value. If the value is 0, the dice don't have final state yet
    :type value: :class:`int`
    
    :param success_animation_frame_number: Number of frame after which a success animation like a shower of confetti needs to be shown on updateMessageSendSucceeded
    :type success_animation_frame_number: :class:`int`
    
    """

    ID: str = Field("messageDice", alias="@type")
    initial_state: typing.Optional[DiceStickers] = None
    final_state: typing.Optional[DiceStickers] = None
    emoji: str
    value: int
    success_animation_frame_number: int

    @staticmethod
    def read(q: dict) -> MessageDice:
        return MessageDice.construct(**q)


class MessageDocument(MessageContent):
    """
    A document message (general file)
    
    :param document: The document description
    :type document: :class:`Document`
    
    :param caption: Document caption
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("messageDocument", alias="@type")
    document: Document
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> MessageDocument:
        return MessageDocument.construct(**q)


class MessageExpiredPhoto(MessageContent):
    """
    An expired photo message (self-destructed after TTL has elapsed)
    
    """

    ID: str = Field("messageExpiredPhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageExpiredPhoto:
        return MessageExpiredPhoto.construct(**q)


class MessageExpiredVideo(MessageContent):
    """
    An expired video message (self-destructed after TTL has elapsed)
    
    """

    ID: str = Field("messageExpiredVideo", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageExpiredVideo:
        return MessageExpiredVideo.construct(**q)


class MessageGame(MessageContent):
    """
    A message with a game
    
    :param game: The game description
    :type game: :class:`Game`
    
    """

    ID: str = Field("messageGame", alias="@type")
    game: Game

    @staticmethod
    def read(q: dict) -> MessageGame:
        return MessageGame.construct(**q)


class MessageGameScore(MessageContent):
    """
    A new high score was achieved in a game
    
    :param game_message_id: Identifier of the message with the game, can be an identifier of a deleted message
    :type game_message_id: :class:`int`
    
    :param game_id: Identifier of the game; may be different from the games presented in the message with the game
    :type game_id: :class:`int`
    
    :param score: New score
    :type score: :class:`int`
    
    """

    ID: str = Field("messageGameScore", alias="@type")
    game_message_id: int
    game_id: int
    score: int

    @staticmethod
    def read(q: dict) -> MessageGameScore:
        return MessageGameScore.construct(**q)


class MessageInviteVideoChatParticipants(MessageContent):
    """
    A message with information about an invite to a video chat
    
    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`int`
    
    :param user_ids: Invited user identifiers
    :type user_ids: :class:`list[int]`
    
    """

    ID: str = Field("messageInviteVideoChatParticipants", alias="@type")
    group_call_id: int
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> MessageInviteVideoChatParticipants:
        return MessageInviteVideoChatParticipants.construct(**q)


class MessageInvoice(MessageContent):
    """
    A message with an invoice from a bot
    
    :param title: Product title
    :type title: :class:`str`
    
    :param param_description: Product description
    :type param_description: :class:`FormattedText`
    
    :param photo: Product photo; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    
    :param currency: Currency for the product price
    :type currency: :class:`str`
    
    :param total_amount: Product total price in the smallest units of the currency
    :type total_amount: :class:`int`
    
    :param start_parameter: Unique invoice bot start_parameter. To share an invoice use the URL https://t.me/{bot_username}?start={start_parameter}
    :type start_parameter: :class:`str`
    
    :param is_test: True, if the invoice is a test invoice
    :type is_test: :class:`bool`
    
    :param need_shipping_address: True, if the shipping address must be specified
    :type need_shipping_address: :class:`bool`
    
    :param receipt_message_id: The identifier of the message with the receipt, after the product has been purchased
    :type receipt_message_id: :class:`int`
    
    """

    ID: str = Field("messageInvoice", alias="@type")
    title: str
    param_description: FormattedText
    photo: typing.Optional[Photo] = None
    currency: str
    total_amount: int
    start_parameter: str
    is_test: bool
    need_shipping_address: bool
    receipt_message_id: int

    @staticmethod
    def read(q: dict) -> MessageInvoice:
        return MessageInvoice.construct(**q)


class MessageLocation(MessageContent):
    """
    A message with a location
    
    :param location: The location description
    :type location: :class:`Location`
    
    :param live_period: Time relative to the message send date, for which the location can be updated, in seconds
    :type live_period: :class:`int`
    
    :param expires_in: Left time for which the location can be updated, in seconds. updateMessageContent is not sent when this field changes
    :type expires_in: :class:`int`
    
    :param heading: For live locations, a direction in which the location moves, in degrees; 1-360. If 0 the direction is unknown
    :type heading: :class:`int`
    
    :param proximity_alert_radius: For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). 0 if the notification is disabled. Available only for the message sender
    :type proximity_alert_radius: :class:`int`
    
    """

    ID: str = Field("messageLocation", alias="@type")
    location: Location
    live_period: int
    expires_in: int
    heading: int
    proximity_alert_radius: int

    @staticmethod
    def read(q: dict) -> MessageLocation:
        return MessageLocation.construct(**q)


class MessagePassportDataReceived(MessageContent):
    """
    Telegram Passport data has been received; for bots only
    
    :param elements: List of received Telegram Passport elements
    :type elements: :class:`list[EncryptedPassportElement]`
    
    :param credentials: Encrypted data credentials
    :type credentials: :class:`EncryptedCredentials`
    
    """

    ID: str = Field("messagePassportDataReceived", alias="@type")
    elements: list[EncryptedPassportElement]
    credentials: EncryptedCredentials

    @staticmethod
    def read(q: dict) -> MessagePassportDataReceived:
        return MessagePassportDataReceived.construct(**q)


class MessagePassportDataSent(MessageContent):
    """
    Telegram Passport data has been sent to a bot
    
    :param types: List of Telegram Passport element types sent
    :type types: :class:`list[PassportElementType]`
    
    """

    ID: str = Field("messagePassportDataSent", alias="@type")
    types: list[PassportElementType]

    @staticmethod
    def read(q: dict) -> MessagePassportDataSent:
        return MessagePassportDataSent.construct(**q)


class MessagePaymentSuccessful(MessageContent):
    """
    A payment has been completed
    
    :param invoice_chat_id: Identifier of the chat, containing the corresponding invoice message; 0 if unknown
    :type invoice_chat_id: :class:`int`
    
    :param invoice_message_id: Identifier of the message with the corresponding invoice; can be 0 or an identifier of a deleted message
    :type invoice_message_id: :class:`int`
    
    :param currency: Currency for the price of the product
    :type currency: :class:`str`
    
    :param total_amount: Total price for the product, in the smallest units of the currency
    :type total_amount: :class:`int`
    
    :param is_recurring: True, if this is a recurring payment
    :type is_recurring: :class:`bool`
    
    :param is_first_recurring: True, if this is the first recurring payment
    :type is_first_recurring: :class:`bool`
    
    :param invoice_name: Name of the invoice; may be empty if unknown
    :type invoice_name: :class:`str`
    
    """

    ID: str = Field("messagePaymentSuccessful", alias="@type")
    invoice_chat_id: int
    invoice_message_id: int
    currency: str
    total_amount: int
    is_recurring: bool
    is_first_recurring: bool
    invoice_name: str

    @staticmethod
    def read(q: dict) -> MessagePaymentSuccessful:
        return MessagePaymentSuccessful.construct(**q)


class MessagePaymentSuccessfulBot(MessageContent):
    """
    A payment has been completed; for bots only
    
    :param currency: Currency for price of the product
    :type currency: :class:`str`
    
    :param total_amount: Total price for the product, in the smallest units of the currency
    :type total_amount: :class:`int`
    
    :param is_recurring: True, if this is a recurring payment
    :type is_recurring: :class:`bool`
    
    :param is_first_recurring: True, if this is the first recurring payment
    :type is_first_recurring: :class:`bool`
    
    :param invoice_payload: Invoice payload
    :type invoice_payload: :class:`str`
    
    :param shipping_option_id: Identifier of the shipping option chosen by the user; may be empty if not applicable
    :type shipping_option_id: :class:`str`
    
    :param order_info: Information about the order; may be null, defaults to None
    :type order_info: :class:`OrderInfo`, optional
    
    :param telegram_payment_charge_id: Telegram payment identifier
    :type telegram_payment_charge_id: :class:`str`
    
    :param provider_payment_charge_id: Provider payment identifier
    :type provider_payment_charge_id: :class:`str`
    
    """

    ID: str = Field("messagePaymentSuccessfulBot", alias="@type")
    currency: str
    total_amount: int
    is_recurring: bool
    is_first_recurring: bool
    invoice_payload: str
    shipping_option_id: str
    order_info: typing.Optional[OrderInfo] = None
    telegram_payment_charge_id: str
    provider_payment_charge_id: str

    @staticmethod
    def read(q: dict) -> MessagePaymentSuccessfulBot:
        return MessagePaymentSuccessfulBot.construct(**q)


class MessagePhoto(MessageContent):
    """
    A photo message
    
    :param photo: The photo description
    :type photo: :class:`Photo`
    
    :param caption: Photo caption
    :type caption: :class:`FormattedText`
    
    :param is_secret: True, if the photo must be blurred and must be shown only while tapped
    :type is_secret: :class:`bool`
    
    """

    ID: str = Field("messagePhoto", alias="@type")
    photo: Photo
    caption: FormattedText
    is_secret: bool

    @staticmethod
    def read(q: dict) -> MessagePhoto:
        return MessagePhoto.construct(**q)


class MessagePinMessage(MessageContent):
    """
    A message has been pinned
    
    :param message_id: Identifier of the pinned message, can be an identifier of a deleted message or 0
    :type message_id: :class:`int`
    
    """

    ID: str = Field("messagePinMessage", alias="@type")
    message_id: int

    @staticmethod
    def read(q: dict) -> MessagePinMessage:
        return MessagePinMessage.construct(**q)


class MessagePoll(MessageContent):
    """
    A message with a poll
    
    :param poll: The poll description
    :type poll: :class:`Poll`
    
    """

    ID: str = Field("messagePoll", alias="@type")
    poll: Poll

    @staticmethod
    def read(q: dict) -> MessagePoll:
        return MessagePoll.construct(**q)


class MessageProximityAlertTriggered(MessageContent):
    """
    A user in the chat came within proximity alert range
    
    :param traveler_id: The identifier of a user or chat that triggered the proximity alert
    :type traveler_id: :class:`MessageSender`
    
    :param watcher_id: The identifier of a user or chat that subscribed for the proximity alert
    :type watcher_id: :class:`MessageSender`
    
    :param distance: The distance between the users
    :type distance: :class:`int`
    
    """

    ID: str = Field("messageProximityAlertTriggered", alias="@type")
    traveler_id: MessageSender
    watcher_id: MessageSender
    distance: int

    @staticmethod
    def read(q: dict) -> MessageProximityAlertTriggered:
        return MessageProximityAlertTriggered.construct(**q)


class MessageScreenshotTaken(MessageContent):
    """
    A screenshot of a message in the chat has been taken
    
    """

    ID: str = Field("messageScreenshotTaken", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageScreenshotTaken:
        return MessageScreenshotTaken.construct(**q)


class MessageSticker(MessageContent):
    """
    A sticker message
    
    :param sticker: The sticker description
    :type sticker: :class:`Sticker`
    
    :param is_premium: True, if premium animation of the sticker must be played
    :type is_premium: :class:`bool`
    
    """

    ID: str = Field("messageSticker", alias="@type")
    sticker: Sticker
    is_premium: bool

    @staticmethod
    def read(q: dict) -> MessageSticker:
        return MessageSticker.construct(**q)


class MessageSupergroupChatCreate(MessageContent):
    """
    A newly created supergroup or channel
    
    :param title: Title of the supergroup or channel
    :type title: :class:`str`
    
    """

    ID: str = Field("messageSupergroupChatCreate", alias="@type")
    title: str

    @staticmethod
    def read(q: dict) -> MessageSupergroupChatCreate:
        return MessageSupergroupChatCreate.construct(**q)


class MessageText(MessageContent):
    """
    A text message
    
    :param text: Text of the message
    :type text: :class:`FormattedText`
    
    :param web_page: A preview of the web page that's mentioned in the text; may be null, defaults to None
    :type web_page: :class:`WebPage`, optional
    
    """

    ID: str = Field("messageText", alias="@type")
    text: FormattedText
    web_page: typing.Optional[WebPage] = None

    @staticmethod
    def read(q: dict) -> MessageText:
        return MessageText.construct(**q)


class MessageUnsupported(MessageContent):
    """
    Message content that is not supported in the current TDLib version
    
    """

    ID: str = Field("messageUnsupported", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageUnsupported:
        return MessageUnsupported.construct(**q)


class MessageVenue(MessageContent):
    """
    A message with information about a venue
    
    :param venue: The venue description
    :type venue: :class:`Venue`
    
    """

    ID: str = Field("messageVenue", alias="@type")
    venue: Venue

    @staticmethod
    def read(q: dict) -> MessageVenue:
        return MessageVenue.construct(**q)


class MessageVideo(MessageContent):
    """
    A video message
    
    :param video: The video description
    :type video: :class:`Video`
    
    :param caption: Video caption
    :type caption: :class:`FormattedText`
    
    :param is_secret: True, if the video thumbnail must be blurred and the video must be shown only while tapped
    :type is_secret: :class:`bool`
    
    """

    ID: str = Field("messageVideo", alias="@type")
    video: Video
    caption: FormattedText
    is_secret: bool

    @staticmethod
    def read(q: dict) -> MessageVideo:
        return MessageVideo.construct(**q)


class MessageVideoChatEnded(MessageContent):
    """
    A message with information about an ended video chat
    
    :param duration: Call duration, in seconds
    :type duration: :class:`int`
    
    """

    ID: str = Field("messageVideoChatEnded", alias="@type")
    duration: int

    @staticmethod
    def read(q: dict) -> MessageVideoChatEnded:
        return MessageVideoChatEnded.construct(**q)


class MessageVideoChatScheduled(MessageContent):
    """
    A new video chat was scheduled
    
    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`int`
    
    :param start_date: Point in time (Unix timestamp) when the group call is supposed to be started by an administrator
    :type start_date: :class:`int`
    
    """

    ID: str = Field("messageVideoChatScheduled", alias="@type")
    group_call_id: int
    start_date: int

    @staticmethod
    def read(q: dict) -> MessageVideoChatScheduled:
        return MessageVideoChatScheduled.construct(**q)


class MessageVideoChatStarted(MessageContent):
    """
    A newly created video chat
    
    :param group_call_id: Identifier of the video chat. The video chat can be received through the method getGroupCall
    :type group_call_id: :class:`int`
    
    """

    ID: str = Field("messageVideoChatStarted", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> MessageVideoChatStarted:
        return MessageVideoChatStarted.construct(**q)


class MessageVideoNote(MessageContent):
    """
    A video note message
    
    :param video_note: The video note description
    :type video_note: :class:`VideoNote`
    
    :param is_viewed: True, if at least one of the recipients has viewed the video note
    :type is_viewed: :class:`bool`
    
    :param is_secret: True, if the video note thumbnail must be blurred and the video note must be shown only while tapped
    :type is_secret: :class:`bool`
    
    """

    ID: str = Field("messageVideoNote", alias="@type")
    video_note: VideoNote
    is_viewed: bool
    is_secret: bool

    @staticmethod
    def read(q: dict) -> MessageVideoNote:
        return MessageVideoNote.construct(**q)


class MessageVoiceNote(MessageContent):
    """
    A voice note message
    
    :param voice_note: The voice note description
    :type voice_note: :class:`VoiceNote`
    
    :param caption: Voice note caption
    :type caption: :class:`FormattedText`
    
    :param is_listened: True, if at least one of the recipients has listened to the voice note
    :type is_listened: :class:`bool`
    
    """

    ID: str = Field("messageVoiceNote", alias="@type")
    voice_note: VoiceNote
    caption: FormattedText
    is_listened: bool

    @staticmethod
    def read(q: dict) -> MessageVoiceNote:
        return MessageVoiceNote.construct(**q)


class MessageWebAppDataReceived(MessageContent):
    """
    Data from a Web App has been received; for bots only
    
    :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
    :type button_text: :class:`str`
    
    :param data: Received data
    :type data: :class:`str`
    
    """

    ID: str = Field("messageWebAppDataReceived", alias="@type")
    button_text: str
    data: str

    @staticmethod
    def read(q: dict) -> MessageWebAppDataReceived:
        return MessageWebAppDataReceived.construct(**q)


class MessageWebAppDataSent(MessageContent):
    """
    Data from a Web App has been sent to a bot
    
    :param button_text: Text of the keyboardButtonTypeWebApp button, which opened the Web App
    :type button_text: :class:`str`
    
    """

    ID: str = Field("messageWebAppDataSent", alias="@type")
    button_text: str

    @staticmethod
    def read(q: dict) -> MessageWebAppDataSent:
        return MessageWebAppDataSent.construct(**q)


class MessageWebsiteConnected(MessageContent):
    """
    The current user has connected a website by logging in using Telegram Login Widget on it
    
    :param domain_name: Domain name of the connected website
    :type domain_name: :class:`str`
    
    """

    ID: str = Field("messageWebsiteConnected", alias="@type")
    domain_name: str

    @staticmethod
    def read(q: dict) -> MessageWebsiteConnected:
        return MessageWebsiteConnected.construct(**q)
