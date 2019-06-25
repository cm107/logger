import os

class LoggerConfig:
    logs_dir = f'{os.path.dirname(os.path.realpath(__file__))}/logs'

    show_log = True
    show_good_log = True
    show_info_log = True
    show_warning_log = True
    show_error_log = True

    write_log = True
    write_good_log = True
    write_info_log = True
    write_warning_log = True
    write_error_log = True
    write_cumulative_log = True
