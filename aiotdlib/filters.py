import re
from abc import (
    ABC,
    abstractmethod,
)
from collections import (
    Callable,
    Coroutine,
)
from typing import (
    Any,
    NoReturn,
    Optional,
    Union,
)

from aiotdlib.api import (
    BaseObject,
    MessageAnimation,
    MessageAudio,
    MessageContact,
    MessageDice,
    MessageDocument,
    MessageGame,
    MessageInvoice,
    MessageLocation,
    MessagePhoto,
    MessagePoll,
    MessageSticker,
    MessageText,
    MessageUnsupported,
    MessageVenue,
    MessageVideo,
    MessageVideoNote,
    MessageVoiceNote,
    UpdateNewMessage,
)

FilterCallable = Callable[[BaseObject], Coroutine[Any, Any, bool]]


class BaseFilter(ABC):
    _name = None

    @abstractmethod
    async def __call__(self, update: BaseObject) -> Optional[Union[bool, dict]]:
        return True

    def __and__(self, other: 'BaseFilter') -> 'BaseFilter':
        return MergedFilter(self, and_filter=other)

    def __or__(self, other: 'BaseFilter') -> 'BaseFilter':
        return MergedFilter(self, or_filter=other)

    def __xor__(self, other: 'BaseFilter') -> 'BaseFilter':
        return XORFilter(self, other)

    def __invert__(self) -> 'BaseFilter':
        return InvertedFilter(self)

    def __repr__(self) -> str:
        # We do this here instead of in a __init__ so filter don't have to call __init__ or super()
        if self.name is None:
            self.name = self.__class__.__name__

        return self.name

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, name: Optional[str]) -> None:
        self._name = name


class BaseObjectFilter(BaseFilter, ABC):
    data_filter = False  # If True - dict, returned from filter() will be merged into update.EXTRA

    async def __call__(self, update: BaseObject) -> Optional[Union[bool, dict]]:
        super_result = await super().__call__(update)

        if not bool(super_result):
            return False

        return await self.filter(update)

    @abstractmethod
    async def filter(self, update: BaseObject) -> Optional[Union[bool, dict]]:
        pass


class InvertedFilter(BaseObjectFilter):
    def __init__(self, f: BaseFilter):
        self.f = f

    async def filter(self, update: BaseObject) -> bool:
        result = await self.f(update)
        return not bool(result)

    @property
    def name(self) -> str:
        return f"<inverted {self.f}>"

    @name.setter
    def name(self, name: str) -> NoReturn:
        raise RuntimeError('Cannot set name for InvertedFilter')


class MergedFilter(BaseObjectFilter):
    """Represents a filter consisting of two other filters.

    Args:
        base_filter: Filter 1 of the merged filter.
        and_filter: Optional filter to "and" with base_filter. Mutually exclusive with or_filter.
        or_filter: Optional filter to "or" with base_filter. Mutually exclusive with and_filter.

    """

    def __init__(
            self,
            base_filter: BaseFilter,
            and_filter: BaseFilter = None,
            or_filter: BaseFilter = None
    ):
        self.base_filter = base_filter

        if self.base_filter.data_filter:
            self.data_filter = True

        self.and_filter = and_filter

        if self.and_filter and not isinstance(self.and_filter, bool) and self.and_filter.data_filter:
            self.data_filter = True

        self.or_filter = or_filter

        if self.or_filter and not isinstance(self.and_filter, bool) and self.or_filter.data_filter:
            self.data_filter = True

    async def filter(self, update: BaseObject) -> Union[bool, dict]:  # pylint: disable=R0911
        base_output = await self.base_filter(update)

        # We need to check if the filters are data filters and if so return the merged data.
        # If it's not a data filter or an or_filter but no matches return bool
        if self.and_filter:
            # And filter needs to short circuit if base is falsey
            if base_output:
                comp_output = await self.and_filter(update)

                if comp_output:
                    if self.data_filter:
                        merged = (base_output or {}) | (comp_output or {})

                        if merged:
                            return merged

                    return True
        elif self.or_filter:
            # Or filter needs to short circuit if base is truthey
            if base_output:
                if self.data_filter:
                    return base_output

                return True

            comp_output = await self.or_filter(update)

            if comp_output:
                if self.data_filter:
                    return comp_output

                return True

        return False

    @property
    def name(self) -> str:
        return (
            f"<{self.base_filter} {'and' if self.and_filter else 'or'} "
            f"{self.and_filter or self.or_filter}>"
        )

    @name.setter
    def name(self, name: str) -> NoReturn:
        raise RuntimeError('Cannot set name for MergedFilter')


class XORFilter(BaseObjectFilter):
    """
    Convenience filter acting as wrapper for :class:`MergedFilter` representing the an XOR gate
    for two filters.

    Args:
        base_filter: Filter 1 of the merged filter.
        xor_filter: Filter 2 of the merged filter.

    """

    def __init__(self, base_filter: BaseFilter, xor_filter: BaseFilter):
        self.base_filter = base_filter
        self.xor_filter = xor_filter
        self.merged_filter = (base_filter & ~xor_filter) | (~base_filter & xor_filter)

    async def filter(self, update: BaseObject) -> Optional[Union[bool, dict]]:
        return await self.merged_filter(update)

    @property
    def name(self) -> str:
        return f'<{self.base_filter} xor {self.xor_filter}>'

    @name.setter
    def name(self, name: str) -> NoReturn:
        raise RuntimeError('Cannot set name for XORFilter')


# Predefined filters
class AllFilter(BaseObjectFilter):
    name = 'Filters.all'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return True


class MessageFilter(BaseObjectFilter):
    name = 'Filters.message'

    async def filter(self, update: UpdateNewMessage) -> Optional[Union[bool, dict]]:
        return isinstance(update, UpdateNewMessage)


class TextFilter(MessageFilter):
    name = 'Filters.text'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageText)


class AnimationFilter(MessageFilter):
    name = 'Filters.animation'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageAnimation)


class AudioFilter(MessageFilter):
    name = 'Filters.audio'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageAudio)


class ContactFilter(MessageFilter):
    name = 'Filters.contact'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageContact)


class DiceFilter(MessageFilter):
    name = 'Filters.dice'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageDice)


class DocumentFilter(MessageFilter):
    name = 'Filters.document'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageDocument)


class GameFilter(MessageFilter):
    name = 'Filters.game'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageGame)


class InvoiceFilter(MessageFilter):
    name = 'Filters.invoice'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageInvoice)


class LocationFilter(MessageFilter):
    name = 'Filters.location'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageLocation)


class PhotoFilter(MessageFilter):
    name = 'Filters.photo'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessagePhoto)


class PollFilter(MessageFilter):
    name = 'Filters.poll'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessagePoll)


class StickerFilter(MessageFilter):
    name = 'Filters.sticker'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageSticker)


class UnsupportedFilter(MessageFilter):
    name = 'Filters.unsupported'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageUnsupported)


class VenueFilter(MessageFilter):
    name = 'Filters.venue'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageVenue)


class VideoFilter(MessageFilter):
    name = 'Filters.video'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageVideo)


class VideoNoteFilter(MessageFilter):
    name = 'Filters.video_note'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageVideoNote)


class VoiceNoteFilter(MessageFilter):
    name = 'Filters.voice_note'

    async def filter(self, update: UpdateNewMessage) -> bool:
        return isinstance(update.message.content, MessageVoiceNote)


class BotCommandFilter(TextFilter):
    data_filter = True
    command: str = None

    def __init__(self, command: str = '*'):
        self.command = command

    async def filter(self, update: UpdateNewMessage) -> Union[bool, dict]:
        message_text = update.message.content.text.text

        if not message_text.startswith('/'):
            return False

        [bot_command, *bot_command_args] = message_text.lstrip('/').split()

        update.EXTRA['bot_command'] = bot_command
        update.EXTRA['bot_command_args'] = bot_command_args

        if not bool(self.command) or self.command in ["*", bot_command]:
            return {
                'bot_command': bot_command,
                'bot_command_args': bot_command_args
            }

        return False


class RegexFilter(TextFilter):
    data_filter = True
    regex: re.Pattern

    def __init__(self, pattern: str, flags: int = 0):
        self.regex = re.compile(pattern, flags=flags)

    async def filter(self, update: UpdateNewMessage) -> Union[bool, dict]:
        message_text = update.message.content.text.text
        match = self.regex.match(message_text)

        if bool(match):
            return {"regex_match": match}

        return False


class Filters:
    all = AllFilter()
    message = MessageFilter()
    text = TextFilter()
    audio = AudioFilter()
    contact = ContactFilter()
    dice = DiceFilter()
    document = DocumentFilter()
    game = GameFilter()
    invoice = InvoiceFilter()
    location = LocationFilter()
    photo = PhotoFilter()
    poll = PollFilter()
    sticker = StickerFilter()
    unsupported = UnsupportedFilter()
    venue = VenueFilter()
    video = VideoFilter()
    video_note = VideoNoteFilter()
    voice_note = VoiceNoteFilter()

    # "Callable" filters
    bot_command = BotCommandFilter
    regex = RegexFilter
