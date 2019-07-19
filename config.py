import os

class LoggerConfig:
    # Directories
    logs_dir = f'{os.path.dirname(os.path.realpath(__file__))}/logs'
    messages_logs_dir = f"{logs_dir}/messages"
    debug_logs_dir = f"{logs_dir}/debug"
    simple_logs_dir = f"{logs_dir}/simple"
    dir_list = [
        logs_dir, messages_logs_dir, debug_logs_dir, simple_logs_dir
    ]
        
    # Global
    show_log = True
    write_log = True
    write_cumulative_log = True
    cumulative_log_path = f"{logs_dir}/cumulative.log"

    # Simple
    show_simple = True
    show_red_log = True
    show_green_log = True
    show_yellow_log = True
    show_blue_log = True
    show_purple_log = True
    show_cyan_log = True
    show_white_log = True

    write_simple = True
    write_red_log = True
    write_green_log = True
    write_yellow_log = True
    write_blue_log = True
    write_purple_log = True
    write_cyan_log = True
    write_white_log = True

    red_log_path = f"{simple_logs_dir}/red.txt"
    green_log_path = f"{simple_logs_dir}/green.txt"
    yellow_log_path = f"{simple_logs_dir}/yellow.txt"
    blue_log_path = f"{simple_logs_dir}/blue.txt"
    purple_log_path = f"{simple_logs_dir}/purple.txt"
    cyan_log_path = f"{simple_logs_dir}/cyan.txt"
    white_log_path = f"{simple_logs_dir}/white.txt"

    # Debug
    show_debug = True
    show_debug_normal_log = True
    show_debug_bold_log = True
    show_debug_crisp_log = True
    show_debug_italic_log = True
    show_debug_blink_log = True

    write_debug = True
    write_debug_normal_log = True
    write_debug_bold_log = True
    write_debug_crisp_log = True
    write_debug_italic_log = True
    write_debug_blink_log = True

    debug_normal_log_path = f"{debug_logs_dir}/debug_normal.txt"
    debug_bold_log_path = f"{debug_logs_dir}/debug_bold.txt"
    debug_crisp_log_path = f"{debug_logs_dir}/debug_crisp.txt"
    debug_italic_log_path = f"{debug_logs_dir}/debug_italic.txt"
    debug_blink_log_path = f"{debug_logs_dir}/debug_blink.txt"

    # Messages
    show_messages = True
    show_good_log = True
    show_info_log = True
    show_warning_log = True
    show_error_log = True

    write_messages = True
    write_good_log = True
    write_info_log = True
    write_warning_log = True
    write_error_log = True

    good_log_path = f"{messages_logs_dir}/good.log"
    info_log_path = f"{messages_logs_dir}/info.log"
    warning_log_path = f"{messages_logs_dir}/warning.log"
    error_log_path = f"{messages_logs_dir}/error.log"
