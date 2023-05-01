import platform

from os.path import join, dirname, abspath

from PyQt5.QtGui import QPalette, QColor

PLATFORM = platform.system()

def _apply_base_theme(app, theme_name):
    app.setStyle('Fusion')
    app_style = join(dirname(abspath(__file__)), '../../resources', theme_name, 'app.qss')
    default_style = join(dirname(abspath(__file__)), '../../resources', theme_name, 'default.qss')

    with open(app_style) as _style:
        sstring = _style.read()

    with open(default_style) as _style:
        sstring = sstring + '\n' + _style.read()
    app.setStyleSheet(sstring)


def _dark_palette(app):
    """ Apply Dark Theme to the Qt application instance.

        Args:
            app (QApplication): QApplication instance.
    """

    darkPalette = QPalette()
    # base
    darkPalette.setColor(QPalette.WindowText, QColor(180, 180, 180))
    darkPalette.setColor(QPalette.Button, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.Light, QColor(180, 180, 180))
    darkPalette.setColor(QPalette.Midlight, QColor(90, 90, 90))
    darkPalette.setColor(QPalette.Dark, QColor(35, 35, 35))
    darkPalette.setColor(QPalette.Text, QColor(180, 180, 180))
    darkPalette.setColor(QPalette.BrightText, QColor(180, 180, 180))
    darkPalette.setColor(QPalette.ButtonText, QColor(180, 180, 180))
    darkPalette.setColor(QPalette.Base, QColor(42, 42, 42))
    darkPalette.setColor(QPalette.Window, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.HighlightedText, QColor(180, 180, 180))
    darkPalette.setColor(QPalette.Link, QColor(62, 160, 238))
    darkPalette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
    darkPalette.setColor(QPalette.ToolTipBase, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ToolTipText, QColor(180, 180, 180))

    # disabled
    darkPalette.setColor(QPalette.Disabled, QPalette.WindowText,
                         QColor(127, 127, 127))
    darkPalette.setColor(QPalette.Disabled, QPalette.Text,
                         QColor(127, 127, 127))
    darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                         QColor(127, 127, 127))
    darkPalette.setColor(QPalette.Disabled, QPalette.Highlight,
                         QColor(80, 80, 80))
    darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                         QColor(127, 127, 127))

    app.setPalette(darkPalette)
    
    # _apply_base_theme(app)


def _contrast_palette(app):
    """ Apply Light Theme to the Qt application instance.

        Args:
            app (QApplication): QApplication instance.
    """

    contrastPalette = QPalette()

    # base
    contrastPalette.setColor(QPalette.WindowText, QColor(0, 0, 0))
    contrastPalette.setColor(QPalette.Button, QColor(240, 240, 240))
    contrastPalette.setColor(QPalette.Light, QColor(180, 180, 180))
    contrastPalette.setColor(QPalette.Midlight, QColor(200, 200, 200))
    contrastPalette.setColor(QPalette.Dark, QColor(225, 225, 225))
    contrastPalette.setColor(QPalette.Text, QColor(0, 0, 0))
    contrastPalette.setColor(QPalette.BrightText, QColor(0, 0, 0))
    contrastPalette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
    contrastPalette.setColor(QPalette.Base, QColor(237, 237, 237))
    contrastPalette.setColor(QPalette.Window, QColor(240, 240, 240))
    contrastPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    contrastPalette.setColor(QPalette.Highlight, QColor(76, 163, 224))
    contrastPalette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    contrastPalette.setColor(QPalette.Link, QColor(56, 143, 204))
    contrastPalette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
    contrastPalette.setColor(QPalette.ToolTipBase, QColor(240, 240, 240))
    contrastPalette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))

    # disabled
    contrastPalette.setColor(QPalette.Disabled, QPalette.WindowText,
                         QColor(115, 115, 115))
    contrastPalette.setColor(QPalette.Disabled, QPalette.Text,
                         QColor(115, 115, 115))
    contrastPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                         QColor(115, 115, 115))
    contrastPalette.setColor(QPalette.Disabled, QPalette.Highlight,
                         QColor(190, 190, 190))
    contrastPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                         QColor(115, 115, 115))

    app.setPalette(contrastPalette)

    # _apply_base_theme(app)
    
BASE_TONE = 96

def _light_palette(app):
    """ Apply Light Theme to the Qt application instance.

        Args:
            app (QApplication): QApplication instance.
    """

    lightPalette = QPalette()

    # base
    lightPalette.setColor(QPalette.WindowText, QColor(BASE_TONE,BASE_TONE,BASE_TONE))
    lightPalette.setColor(QPalette.Button, QColor(240, 240, 240))
    lightPalette.setColor(QPalette.Light, QColor(180, 180, 180))
    lightPalette.setColor(QPalette.Midlight, QColor(200, 200, 200))
    lightPalette.setColor(QPalette.Dark, QColor(225, 225, 225))
    lightPalette.setColor(QPalette.Text, QColor(BASE_TONE-28,BASE_TONE-28,BASE_TONE-28))
    lightPalette.setColor(QPalette.BrightText, QColor(BASE_TONE-32,BASE_TONE-32,BASE_TONE-32))
    lightPalette.setColor(QPalette.ButtonText, QColor(BASE_TONE-32,BASE_TONE-32,BASE_TONE-32))
    lightPalette.setColor(QPalette.Base, QColor(237, 237, 237))
    lightPalette.setColor(QPalette.Window, QColor(240, 240, 240))
    lightPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    lightPalette.setColor(QPalette.Highlight, QColor(86, 173, 234))
    lightPalette.setColor(QPalette.HighlightedText, QColor(64,64,64))
    lightPalette.setColor(QPalette.Link, QColor(56, 143, 224))
    lightPalette.setColor(QPalette.AlternateBase, QColor(225, 225, 225))
    lightPalette.setColor(QPalette.ToolTipBase, QColor(240, 240, 240))
    lightPalette.setColor(QPalette.ToolTipText, QColor(BASE_TONE-28,BASE_TONE-28,BASE_TONE-28))

    # disabled
    lightPalette.setColor(QPalette.Disabled, QPalette.WindowText,
                         QColor(115, 115, 115))
    lightPalette.setColor(QPalette.Disabled, QPalette.Text,
                         QColor(115, 115, 115))
    lightPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                         QColor(115, 115, 115))
    lightPalette.setColor(QPalette.Disabled, QPalette.Highlight,
                         QColor(190, 190, 190))
    lightPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                         QColor(115, 115, 115))

    app.setPalette(lightPalette)

    # _apply_base_theme(app)


THEME_DARK = 'qtmodern-dark'
THEME_CONTRAST = 'qtmodern-contrast'
THEME_LIGHT = 'qtmodern-light'


def get_themes()->list:
    return sorted([THEME_CONTRAST, THEME_DARK, THEME_LIGHT])


def set_theme(app, theme_name:str):
    if theme_name == THEME_DARK:
        _dark_palette(app)
    elif theme_name == THEME_CONTRAST:
        _contrast_palette(app)
    elif theme_name == THEME_LIGHT:
        _light_palette(app)
    _apply_base_theme(app, theme_name)
