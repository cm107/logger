from .config import LoggerConfig
import os, traceback
from .logger_handler import logger

class LogWriter:
    def __init__(self):
        self.log_dir = LoggerConfig.logs_dir
        logger.info(f'Using {self.log_dir} for log directory.')
        logger.good("Log Writer initialized")

    def dir_exists(self, url: str):
        return os.path.isdir(url)

    def file_exists(self, url: str):
        return os.path.isfile(url)

    def delete_log_file(self, url: str):
        os.unlink(url)

    def delete_all_log_files(self, dir_path: str):
        for root, dirs, files in os.walk(dir_path):
            for currentFile in files:
                exts = ('.log')
                if currentFile.lower().endswith(exts):
                    os.remove(os.path.join(root, currentFile))

    def init_log_dir(self):
        if not self.dir_exists(self.log_dir):
            for dir_path in LoggerConfig.dir_list:
                os.mkdir(dir_path)
            logger.info("log directory created.")
        else:
            self.delete_all_log_files(LoggerConfig.logs_dir)
            logger.info("All log files have been deleted from log directory.")
        logger.info("Log directory initialized.")

    def write_log(self, logname: str, logdir: str, logdict: dict):
        try:
            filepath = f"{logdir}/{logname}.log"
            f = open(filepath, "w+")
            for key in logdict:
                log_type = logdict[key]["LogType"]
                log_time = logdict[key]["time"]
                log_text = logdict[key]["text"]
                line = f"==={log_type} {log_time}===\n{log_text}\n"
                f.write(line)
            f.close()
            logger.good(f"{logname}.log written successfully")           
        except:
            traceback.print_exc()
            logger.error(f"Failed to write to {logname}.log")

    def write_all_logs(self):
        if LoggerConfig.write_log:
            self.init_log_dir()
            if LoggerConfig.write_debug:
                if LoggerConfig.write_debug_normal_log:
                    self.write_log(
                        'debug_normal', LoggerConfig.debug_logs_dir,
                        logger.debug_normal_log)
                if LoggerConfig.write_debug_bold_log:
                    self.write_log(
                        'debug_bold', LoggerConfig.debug_logs_dir,
                        logger.debug_bold_log)
                if LoggerConfig.write_debug_crisp_log:
                    self.write_log(
                        'debug_crisp', LoggerConfig.debug_logs_dir,
                        logger.debug_crisp_log)
                if LoggerConfig.write_debug_italic_log:
                    self.write_log(
                        'debug_italic', LoggerConfig.debug_logs_dir,
                        logger.debug_italic_log)
                if LoggerConfig.write_debug_blink_log:
                    self.write_log(
                        'debug_blink', LoggerConfig.debug_logs_dir,
                        logger.debug_blink_log)
            if LoggerConfig.write_messages:
                if LoggerConfig.write_good_log:
                    self.write_log(
                        'good', LoggerConfig.messages_logs_dir,
                        logger.good_log)
                if LoggerConfig.write_info_log:
                    self.write_log(
                        'info', LoggerConfig.messages_logs_dir,
                        logger.info_log)
                if LoggerConfig.write_warning_log:
                    self.write_log(
                        'warning', LoggerConfig.messages_logs_dir,
                        logger.warning_log)
                if LoggerConfig.write_error_log:
                    self.write_log(
                        'error', LoggerConfig.messages_logs_dir,
                        logger.error_log)
            if LoggerConfig.write_simple:
                if LoggerConfig.write_red_log:
                    self.write_log(
                        'red', LoggerConfig.simple_logs_dir,
                        logger.red_log)
                if LoggerConfig.write_green_log:
                    self.write_log(
                        'green', LoggerConfig.simple_logs_dir,
                        logger.green_log)
                if LoggerConfig.write_yellow_log:
                    self.write_log(
                        'yellow', LoggerConfig.simple_logs_dir,
                        logger.yellow_log)
                if LoggerConfig.write_blue_log:
                    self.write_log(
                        'blue', LoggerConfig.simple_logs_dir,
                        logger.blue_log)
                if LoggerConfig.write_purple_log:
                    self.write_log(
                        'purple', LoggerConfig.simple_logs_dir,
                        logger.purple_log)
                if LoggerConfig.write_cyan_log:
                    self.write_log(
                        'cyan', LoggerConfig.simple_logs_dir,
                        logger.cyan_log)
                if LoggerConfig.write_white_log:
                    self.write_log(
                        'white', LoggerConfig.simple_logs_dir,
                        logger.white_log)
            if LoggerConfig.write_cumulative_log:
                self.write_log(
                    'cumulative', LoggerConfig.logs_dir,
                    logger.cumulative_log)

log_writer = LogWriter()