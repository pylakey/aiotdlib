# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

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


class MessageAnimation(MessageContent):
    """
    An animation message (GIF-style).
    
    Params:
        animation (:class:`Animation`)
            The animation description
        
        caption (:class:`FormattedText`)
            Animation caption
        
        is_secret (:class:`bool`)
            True, if the animation thumbnail must be blurred and the animation must be shown only while tapped
        
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
    
    Params:
        audio (:class:`Audio`)
            The audio description
        
        caption (:class:`FormattedText`)
            Audio caption
        
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
    
    Params:
        title (:class:`str`)
            Title of the basic group
        
        member_user_ids (:obj:`list[int]`)
            User identifiers of members in the basic group
        
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
    
    Params:
        is_video (:class:`bool`)
            True, if the call was a video call
        
        discard_reason (:class:`CallDiscardReason`)
            Reason why the call was discarded
        
        duration (:class:`int`)
            Call duration, in seconds
        
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
    
    Params:
        member_user_ids (:obj:`list[int]`)
            User identifiers of the new members
        
    """

    ID: str = Field("messageChatAddMembers", alias="@type")
    member_user_ids: list[int]

    @staticmethod
    def read(q: dict) -> MessageChatAddMembers:
        return MessageChatAddMembers.construct(**q)


class MessageChatChangePhoto(MessageContent):
    """
    An updated chat photo
    
    Params:
        photo (:class:`ChatPhoto`)
            New chat photo
        
    """

    ID: str = Field("messageChatChangePhoto", alias="@type")
    photo: ChatPhoto

    @staticmethod
    def read(q: dict) -> MessageChatChangePhoto:
        return MessageChatChangePhoto.construct(**q)


class MessageChatChangeTitle(MessageContent):
    """
    An updated chat title
    
    Params:
        title (:class:`str`)
            New chat title
        
    """

    ID: str = Field("messageChatChangeTitle", alias="@type")
    title: str

    @staticmethod
    def read(q: dict) -> MessageChatChangeTitle:
        return MessageChatChangeTitle.construct(**q)


class MessageChatDeleteMember(MessageContent):
    """
    A chat member was deleted
    
    Params:
        user_id (:class:`int`)
            User identifier of the deleted chat member
        
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
    A new member joined the chat by invite link
    
    """

    ID: str = Field("messageChatJoinByLink", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageChatJoinByLink:
        return MessageChatJoinByLink.construct(**q)


class MessageChatSetTtl(MessageContent):
    """
    The TTL (Time To Live) setting for messages in the chat has been changed
    
    Params:
        ttl (:class:`int`)
            New message TTL setting
        
    """

    ID: str = Field("messageChatSetTtl", alias="@type")
    ttl: int

    @staticmethod
    def read(q: dict) -> MessageChatSetTtl:
        return MessageChatSetTtl.construct(**q)


class MessageChatUpgradeFrom(MessageContent):
    """
    A supergroup has been created from a basic group
    
    Params:
        title (:class:`str`)
            Title of the newly created supergroup
        
        basic_group_id (:class:`int`)
            The identifier of the original basic group
        
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
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the supergroup to which the basic group was upgraded
        
    """

    ID: str = Field("messageChatUpgradeTo", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> MessageChatUpgradeTo:
        return MessageChatUpgradeTo.construct(**q)


class MessageContact(MessageContent):
    """
    A message with a user contact
    
    Params:
        contact (:class:`Contact`)
            The contact description
        
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
    
    Params:
        text (:class:`str`)
            Message text to be shown in the chat
        
    """

    ID: str = Field("messageCustomServiceAction", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> MessageCustomServiceAction:
        return MessageCustomServiceAction.construct(**q)


class MessageDice(MessageContent):
    """
    A dice message. The dice value is randomly generated by the server
    
    Params:
        initial_state (:class:`DiceStickers`)
            The animated stickers with the initial dice animation; may be null if unknown. updateMessageContent will be sent when the sticker became known
        
        final_state (:class:`DiceStickers`)
            The animated stickers with the final dice animation; may be null if unknown. updateMessageContent will be sent when the sticker became known
        
        emoji (:class:`str`)
            Emoji on which the dice throw animation is based
        
        value (:class:`int`)
            The dice value. If the value is 0, the dice don't have final state yet
        
        success_animation_frame_number (:class:`int`)
            Number of frame after which a success animation like a shower of confetti needs to be shown on updateMessageSendSucceeded
        
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
    
    Params:
        document (:class:`Document`)
            The document description
        
        caption (:class:`FormattedText`)
            Document caption
        
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
    
    Params:
        game (:class:`Game`)
            The game description
        
    """

    ID: str = Field("messageGame", alias="@type")
    game: Game

    @staticmethod
    def read(q: dict) -> MessageGame:
        return MessageGame.construct(**q)


class MessageGameScore(MessageContent):
    """
    A new high score was achieved in a game
    
    Params:
        game_message_id (:class:`int`)
            Identifier of the message with the game, can be an identifier of a deleted message
        
        game_id (:class:`int`)
            Identifier of the game; may be different from the games presented in the message with the game
        
        score (:class:`int`)
            New score
        
    """

    ID: str = Field("messageGameScore", alias="@type")
    game_message_id: int
    game_id: int
    score: int

    @staticmethod
    def read(q: dict) -> MessageGameScore:
        return MessageGameScore.construct(**q)


class MessageInviteVoiceChatParticipants(MessageContent):
    """
    A message with information about an invite to a voice chat
    
    Params:
        group_call_id (:class:`int`)
            Identifier of the voice chat. The voice chat can be received through the method getGroupCall
        
        user_ids (:obj:`list[int]`)
            Invited user identifiers
        
    """

    ID: str = Field("messageInviteVoiceChatParticipants", alias="@type")
    group_call_id: int
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> MessageInviteVoiceChatParticipants:
        return MessageInviteVoiceChatParticipants.construct(**q)


class MessageInvoice(MessageContent):
    """
    A message with an invoice from a bot
    
    Params:
        title (:class:`str`)
            Product title
        
        param_description (:class:`str`)
            Product description
        
        photo (:class:`Photo`)
            Product photo; may be null
        
        currency (:class:`str`)
            Currency for the product price
        
        total_amount (:class:`int`)
            Product total price in the minimal quantity of the currency
        
        start_parameter (:class:`str`)
            Unique invoice bot start_parameter. To share an invoice use the URL https://t.me/{bot_username}?start={start_parameter}
        
        is_test (:class:`bool`)
            True, if the invoice is a test invoice
        
        need_shipping_address (:class:`bool`)
            True, if the shipping address should be specified
        
        receipt_message_id (:class:`int`)
            The identifier of the message with the receipt, after the product has been purchased
        
    """

    ID: str = Field("messageInvoice", alias="@type")
    title: str
    param_description: str
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
    
    Params:
        location (:class:`Location`)
            The location description
        
        live_period (:class:`int`)
            Time relative to the message send date, for which the location can be updated, in seconds
        
        expires_in (:class:`int`)
            Left time for which the location can be updated, in seconds. updateMessageContent is not sent when this field changes
        
        heading (:class:`int`)
            For live locations, a direction in which the location moves, in degrees; 1-360. If 0 the direction is unknown
        
        proximity_alert_radius (:class:`int`)
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). 0 if the notification is disabled. Available only for the message sender
        
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
    
    Params:
        elements (:obj:`list[EncryptedPassportElement]`)
            List of received Telegram Passport elements
        
        credentials (:class:`EncryptedCredentials`)
            Encrypted data credentials
        
    """

    ID: str = Field("messagePassportDataReceived", alias="@type")
    elements: list[EncryptedPassportElement]
    credentials: EncryptedCredentials

    @staticmethod
    def read(q: dict) -> MessagePassportDataReceived:
        return MessagePassportDataReceived.construct(**q)


class MessagePassportDataSent(MessageContent):
    """
    Telegram Passport data has been sent
    
    Params:
        types (:obj:`list[PassportElementType]`)
            List of Telegram Passport element types sent
        
    """

    ID: str = Field("messagePassportDataSent", alias="@type")
    types: list[PassportElementType]

    @staticmethod
    def read(q: dict) -> MessagePassportDataSent:
        return MessagePassportDataSent.construct(**q)


class MessagePaymentSuccessful(MessageContent):
    """
    A payment has been completed
    
    Params:
        invoice_message_id (:class:`int`)
            Identifier of the message with the corresponding invoice; can be an identifier of a deleted message
        
        currency (:class:`str`)
            Currency for the price of the product
        
        total_amount (:class:`int`)
            Total price for the product, in the minimal quantity of the currency
        
    """

    ID: str = Field("messagePaymentSuccessful", alias="@type")
    invoice_message_id: int
    currency: str
    total_amount: int

    @staticmethod
    def read(q: dict) -> MessagePaymentSuccessful:
        return MessagePaymentSuccessful.construct(**q)


class MessagePaymentSuccessfulBot(MessageContent):
    """
    A payment has been completed; for bots only
    
    Params:
        invoice_message_id (:class:`int`)
            Identifier of the message with the corresponding invoice; can be an identifier of a deleted message
        
        currency (:class:`str`)
            Currency for price of the product
        
        total_amount (:class:`int`)
            Total price for the product, in the minimal quantity of the currency
        
        invoice_payload (:class:`str`)
            Invoice payload
        
        shipping_option_id (:class:`str`)
            Identifier of the shipping option chosen by the user; may be empty if not applicable
        
        order_info (:class:`OrderInfo`)
            Information about the order; may be null
        
        telegram_payment_charge_id (:class:`str`)
            Telegram payment identifier
        
        provider_payment_charge_id (:class:`str`)
            Provider payment identifier
        
    """

    ID: str = Field("messagePaymentSuccessfulBot", alias="@type")
    invoice_message_id: int
    currency: str
    total_amount: int
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
    
    Params:
        photo (:class:`Photo`)
            The photo description
        
        caption (:class:`FormattedText`)
            Photo caption
        
        is_secret (:class:`bool`)
            True, if the photo must be blurred and must be shown only while tapped
        
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
    
    Params:
        message_id (:class:`int`)
            Identifier of the pinned message, can be an identifier of a deleted message or 0
        
    """

    ID: str = Field("messagePinMessage", alias="@type")
    message_id: int

    @staticmethod
    def read(q: dict) -> MessagePinMessage:
        return MessagePinMessage.construct(**q)


class MessagePoll(MessageContent):
    """
    A message with a poll
    
    Params:
        poll (:class:`Poll`)
            The poll description
        
    """

    ID: str = Field("messagePoll", alias="@type")
    poll: Poll

    @staticmethod
    def read(q: dict) -> MessagePoll:
        return MessagePoll.construct(**q)


class MessageProximityAlertTriggered(MessageContent):
    """
    A user in the chat came within proximity alert range
    
    Params:
        traveler (:class:`MessageSender`)
            The user or chat, which triggered the proximity alert
        
        watcher (:class:`MessageSender`)
            The user or chat, which subscribed for the proximity alert
        
        distance (:class:`int`)
            The distance between the users
        
    """

    ID: str = Field("messageProximityAlertTriggered", alias="@type")
    traveler: MessageSender
    watcher: MessageSender
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
    
    Params:
        sticker (:class:`Sticker`)
            The sticker description
        
    """

    ID: str = Field("messageSticker", alias="@type")
    sticker: Sticker

    @staticmethod
    def read(q: dict) -> MessageSticker:
        return MessageSticker.construct(**q)


class MessageSupergroupChatCreate(MessageContent):
    """
    A newly created supergroup or channel
    
    Params:
        title (:class:`str`)
            Title of the supergroup or channel
        
    """

    ID: str = Field("messageSupergroupChatCreate", alias="@type")
    title: str

    @staticmethod
    def read(q: dict) -> MessageSupergroupChatCreate:
        return MessageSupergroupChatCreate.construct(**q)


class MessageText(MessageContent):
    """
    A text message
    
    Params:
        text (:class:`FormattedText`)
            Text of the message
        
        web_page (:class:`WebPage`)
            A preview of the web page that's mentioned in the text; may be null
        
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
    
    Params:
        venue (:class:`Venue`)
            The venue description
        
    """

    ID: str = Field("messageVenue", alias="@type")
    venue: Venue

    @staticmethod
    def read(q: dict) -> MessageVenue:
        return MessageVenue.construct(**q)


class MessageVideo(MessageContent):
    """
    A video message
    
    Params:
        video (:class:`Video`)
            The video description
        
        caption (:class:`FormattedText`)
            Video caption
        
        is_secret (:class:`bool`)
            True, if the video thumbnail must be blurred and the video must be shown only while tapped
        
    """

    ID: str = Field("messageVideo", alias="@type")
    video: Video
    caption: FormattedText
    is_secret: bool

    @staticmethod
    def read(q: dict) -> MessageVideo:
        return MessageVideo.construct(**q)


class MessageVideoNote(MessageContent):
    """
    A video note message
    
    Params:
        video_note (:class:`VideoNote`)
            The video note description
        
        is_viewed (:class:`bool`)
            True, if at least one of the recipients has viewed the video note
        
        is_secret (:class:`bool`)
            True, if the video note thumbnail must be blurred and the video note must be shown only while tapped
        
    """

    ID: str = Field("messageVideoNote", alias="@type")
    video_note: VideoNote
    is_viewed: bool
    is_secret: bool

    @staticmethod
    def read(q: dict) -> MessageVideoNote:
        return MessageVideoNote.construct(**q)


class MessageVoiceChatEnded(MessageContent):
    """
    A message with information about an ended voice chat
    
    Params:
        duration (:class:`int`)
            Call duration
        
    """

    ID: str = Field("messageVoiceChatEnded", alias="@type")
    duration: int

    @staticmethod
    def read(q: dict) -> MessageVoiceChatEnded:
        return MessageVoiceChatEnded.construct(**q)


class MessageVoiceChatStarted(MessageContent):
    """
    A newly created voice chat
    
    Params:
        group_call_id (:class:`int`)
            Identifier of the voice chat. The voice chat can be received through the method getGroupCall
        
    """

    ID: str = Field("messageVoiceChatStarted", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> MessageVoiceChatStarted:
        return MessageVoiceChatStarted.construct(**q)


class MessageVoiceNote(MessageContent):
    """
    A voice note message
    
    Params:
        voice_note (:class:`VoiceNote`)
            The voice note description
        
        caption (:class:`FormattedText`)
            Voice note caption
        
        is_listened (:class:`bool`)
            True, if at least one of the recipients has listened to the voice note
        
    """

    ID: str = Field("messageVoiceNote", alias="@type")
    voice_note: VoiceNote
    caption: FormattedText
    is_listened: bool

    @staticmethod
    def read(q: dict) -> MessageVoiceNote:
        return MessageVoiceNote.construct(**q)


class MessageWebsiteConnected(MessageContent):
    """
    The current user has connected a website by logging in using Telegram Login Widget on it
    
    Params:
        domain_name (:class:`str`)
            Domain name of the connected website
        
    """

    ID: str = Field("messageWebsiteConnected", alias="@type")
    domain_name: str

    @staticmethod
    def read(q: dict) -> MessageWebsiteConnected:
        return MessageWebsiteConnected.construct(**q)
