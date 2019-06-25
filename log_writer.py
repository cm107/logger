from .config import LoggerConfig
import os
from .logger_handler import logger

class LogWriter:
    def __init__(self):
        self.log_dir = LoggerConfig.logs_dir
        print('Using {} for log directory.'.format(self.log_dir))
        self.good_log_url = self.log_dir + '/good.log'
        self.info_log_url = self.log_dir + '/info.log'
        self.warning_log_url = self.log_dir + '/warning.log'
        self.error_log_url = self.log_dir + '/error.log'
        self.cumulative_log_url = self.log_dir + '/cumulative.log'
        logger.good("Log Writer initialized")

    def dir_exists(self, url: str):
        return os.path.isdir(url)

    def file_exists(self, url: str):
        return os.path.isfile(url)

    def delete_log_file(self, url: str):
        os.unlink(url)

    def delete_all_log_files(self):
        filenames = os.listdir(self.log_dir)
        for filename in filenames:
            if filename.endswith(".log"):
                filepath = os.path.join(self.log_dir, filename)
                self.delete_log_file(filepath)
                logger.info("Deleted {} from log directory.".format(filename))

    def init_log_dir(self):
        if not self.dir_exists(self.log_dir):
            os.mkdir(self.log_dir)
            logger.info("log directory created.")
        else:
            self.delete_all_log_files()
            logger.info("All log files have been deleted from log directory.")
        logger.info("Log directory initialized.")

    def write_log(self, logname: str, logdict: dict):
        try:
            filepath = "{}/{}.log".format(self.log_dir, logname)
            f = open(filepath, "w+")
            for key in logdict:
                log_type = logdict[key]["LogType"]
                log_time = logdict[key]["time"]
                log_text = logdict[key]["text"]
                line = "==={} {}===\n{}\n".format(log_type, log_time, log_text)
                f.write(line)
            f.close()
            logger.good("{}.log written successfully".format(logname))           
        except:
            logger.error("Failed to write to {}.log".format(logname))

    def write_all_logs(self):
        if LoggerConfig.write_log:
            self.init_log_dir()
            if LoggerConfig.write_good_log:
                self.write_log('good', logger.good_log)
            if LoggerConfig.write_info_log:
                self.write_log('info', logger.info_log)
            if LoggerConfig.write_warning_log:
                self.write_log('warning', logger.warning_log)
            if LoggerConfig.write_error_log:
                self.write_log('error', logger.error_log)
            if LoggerConfig.write_cumulative_log:
                self.write_log('cumulative', logger.cumulative_log)

log_writer = LogWriter()