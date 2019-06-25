import datetime
from .config import LoggerConfig

class TextStyle:
    normal = '0'
    bold = '1'
    crisp = '2'
    italic = '3'
    blink = '5'

class TextColor:
    black = '30'
    red = '31'
    green = '32'
    yellow = '33'
    blue = '34'
    purple = '35'
    cyan = '36'
    white = '37'

class TextBackgroundColor:
    black = '40'
    red = '41'
    green = '42'
    yellow = '43'
    blue = '44'
    purple = '45'
    cyan = '46'
    white = '47'

class TextHeaderFactory:
    def __init__(self, style: TextStyle, text_color: TextColor, text_background_color: TextBackgroundColor):
        self.style = style
        self.color = text_color
        self.text_background_color = text_background_color
        self.header = "\033[{};{};{}m".format(style, text_color, text_background_color)

class TextHeaderFactoryHandler:
    def get_std_header(self):
        return "\033[0m"

    def get_debug_header(self, style: TextStyle):
        return TextHeaderFactory(style, TextColor.green, TextBackgroundColor.white).header

    def get_message_header(self, text_color: TextColor):
        return TextHeaderFactory(TextStyle.bold, text_color, TextBackgroundColor.black).header

class TextHeader:
    # Standard
    std = TextHeaderFactoryHandler().get_std_header()
    
    # Debug
    debug_normal = TextHeaderFactoryHandler().get_debug_header(TextStyle.normal)
    debug_bold = TextHeaderFactoryHandler().get_debug_header(TextStyle.bold)
    debug_crisp = TextHeaderFactoryHandler().get_debug_header(TextStyle.crisp)
    debug_italic = TextHeaderFactoryHandler().get_debug_header(TextStyle.italic)
    debug_blink = TextHeaderFactoryHandler().get_debug_header(TextStyle.blink)

    # Good
    good = TextHeaderFactoryHandler().get_message_header(TextColor.green)

    # Info
    info = TextHeaderFactoryHandler().get_message_header(TextColor.cyan)

    # Warning
    warning = TextHeaderFactoryHandler().get_message_header(TextColor.yellow)

    # Error
    error = TextHeaderFactoryHandler().get_message_header(TextColor.red)

class Logger:
    def __init__(self):
        self.good_log = {}
        self.info_log = {}
        self.warning_log = {}
        self.error_log = {}
        self.cumulative_log = {}

        self.good("Logger initialized.")

    def good(self, text):
        text_str = str(text)
        if LoggerConfig.show_log and LoggerConfig.show_good_log:
            print("{}{}{}".format(TextHeader.good, text_str, TextHeader.std))
        data = {
            'LogType': 'Good',
            'time': str(datetime.datetime.now()),
            'text': text_str
        }
        if LoggerConfig.write_good_log:
            self.good_log[len(self.good_log)] = data
        if LoggerConfig.write_cumulative_log:
            self.cumulative_log[len(self.cumulative_log)] = data

    def info(self, text):
        text_str = str(text)
        if LoggerConfig.show_log and LoggerConfig.show_info_log:
            print("{}{}{}".format(TextHeader.info, text_str, TextHeader.std))
        data = {
            'LogType': 'Info',
            'time': str(datetime.datetime.now()),
            'text': text_str
        }
        if LoggerConfig.write_info_log:
            self.info_log[len(self.info_log)] = data
        if LoggerConfig.write_cumulative_log:
            self.cumulative_log[len(self.cumulative_log)] = data

    def warning(self, text):
        text_str = str(text)
        if LoggerConfig.show_log and LoggerConfig.show_warning_log:
            print("{}{}{}".format(TextHeader.warning, text_str, TextHeader.std))
        data = {
            'LogType': 'Warning',
            'time': str(datetime.datetime.now()),
            'text': text_str
        }
        if LoggerConfig.write_warning_log:
            self.warning_log[len(self.warning_log)] = data
        if LoggerConfig.write_cumulative_log:
            self.cumulative_log[len(self.cumulative_log)] = data

    def error(self, text):
        text_str = str(text)
        if LoggerConfig.show_log and LoggerConfig.show_error_log:
            print("{}{}{}".format(TextHeader.error, text_str, TextHeader.std))
        data = {
            'LogType': 'Error',
            'time': str(datetime.datetime.now()),
            'text': text_str
        }
        if LoggerConfig.write_error_log:
            self.error_log[len(self.error_log)] = data
        if LoggerConfig.write_cumulative_log:
            self.cumulative_log[len(self.cumulative_log)] = data

    def debug_normal(self, text):
        text_str = str(text)
        print("{}{}{}".format(TextHeader.debug_normal, text_str, TextHeader.std))

    def debug_bold(self, text):
        text_str = str(text)
        print("{}{}{}".format(TextHeader.debug_bold, text_str, TextHeader.std))

    def debug_crisp(self, text):
        text_str = str(text)
        print("{}{}{}".format(TextHeader.debug_crisp, text_str, TextHeader.std))

    def debug_italic(self, text):
        text_str = str(text)
        print("{}{}{}".format(TextHeader.debug_italic, text_str, TextHeader.std))

    def debug_blink(self, text):
        text_str = str(text)
        print("{}{}{}".format(TextHeader.debug_blink, text_str, TextHeader.std))

    def test_logger(self):
        print('Hi')
        self.good('Good')
        print('Hi')
        self.info('Info')
        print('Hi')
        self.warning('Warning')
        print('Hi')
        self.error('Error')
        print('Hi')
        self.debug_normal('Debug Normal')
        print('Hi')
        self.debug_bold('Debug Bold')
        print('Hi')
        self.debug_crisp('Debug Crisp')
        print('Hi')
        self.debug_italic('Debug Italic')
        print('Hi')
        self.debug_blink('Debug Blink')
        print('Hi')


logger = Logger()