# Use the Travertino font definitions as-is
from travertino import constants
from travertino.constants import ITALIC  # noqa: F401
from travertino.constants import (  # noqa: F401
    BOLD,
    CURSIVE,
    FANTASY,
    MESSAGE,
    MONOSPACE,
    NORMAL,
    OBLIQUE,
    SANS_SERIF,
    SERIF,
    SMALL_CAPS,
    SYSTEM,
)
from travertino.fonts import font  # noqa: F401
from travertino.fonts import Font as BaseFont

from toga.platform import get_platform_factory

SYSTEM_DEFAULT_FONTS = {SYSTEM, MESSAGE, SERIF, SANS_SERIF, CURSIVE, FANTASY, MONOSPACE}
SYSTEM_DEFAULT_FONT_SIZE = -1
_REGISTERED_FONT_CACHE = {}


class Font(BaseFont):
    def __init__(self, family, size, style=NORMAL, variant=NORMAL, weight=NORMAL):
        super().__init__(family, size, style, variant, weight)
        self.factory = get_platform_factory()
        self._impl = self.factory.Font(self)

    def __str__(self):
        size = (
            "system size" if self.size == SYSTEM_DEFAULT_FONT_SIZE else f"{self.size}pt"
        )
        weight = f" {self.weight}" if self.weight != NORMAL else ""
        variant = f" {self.variant}" if self.variant != NORMAL else ""
        style = f" {self.style}" if self.style != NORMAL else ""
        return f"{self.family} {size}{weight}{variant}{style}"

    @staticmethod
    def register(family, path, weight=NORMAL, style=NORMAL, variant=NORMAL):
        """Registers a file-based font with it's family name, style, variant
        and weight. When invalid values for style, variant or weight are passed,
        ``NORMAL`` will be used.

        When a font file includes multiple font weight/style/etc, each variant
        must be registerered separately::

            # Register a simple regular font
            Font.register("Font Awesome 5 Free Solid", "resources/Font Awesome 5 Free-Solid-900.otf")

            # Register a regular and bold font, contained in separate font files
            Font.register("Roboto", "resources/Roboto-Regular.ttf")
            Font.register("Roboto", "resources/Roboto-Bold.ttf", weight=Font.BOLD)

            # Register a single font file that contains both
            # a regular and bold weight
            Font.register("Bahnschrift", "resources/Bahnschrift.ttf")
            Font.register("Bahnschrift", "resources/Bahnschrift.ttf", weight=Font.BOLD)

        :param family: The font family name. This is the name that can be
            referenced in style definitions.
        :param path: The path to the font file.
        :param weight: The font weight; ``NORMAL`` (default) or ``BOLD``
        :param style: The font style; ``NORMAL`` (default), ``ITALIC`` or
            ``OBLIQUE``
        :param variant: The font variant; ``NORMAL`` (default) or ``SMALL_CAPS``
        """
        font_key = Font.registered_font_key(
            family, weight=weight, style=style, variant=variant
        )
        _REGISTERED_FONT_CACHE[font_key] = path

    @staticmethod
    def registered_font_key(family, weight, style, variant):
        """Creates a key for storing a registered font in the font cache.

        If weight, style or variant contain an invalid value, Font.NORMAL is
        used instead.

        :param family: The font family name
        :param weight: The font weight: Font.NORMAL (default) or a value from Font.FONT_WEIGHTS
        :param style: The font style: Font.NORMAL (default) or a value from Font.FONT_STYLES
        :param variant: The font variant: Font.NORMAL (default) or a value from Font.FONT_VARIANTS
        :returns: The font key
        """
        if weight not in constants.FONT_WEIGHTS:
            weight = NORMAL
        if style not in constants.FONT_STYLES:
            style = NORMAL
        if variant not in constants.FONT_VARIANTS:
            variant = NORMAL

        return (family, weight, style, variant)
