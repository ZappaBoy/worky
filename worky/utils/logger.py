import logging

from worky.models.log_level import LogLevel


class Logger:
    def __init__(self, log_level: LogLevel | int = LogLevel.INFO):
        self.log_level = log_level
        self.logger = logging.getLogger()
        self.set_log_level(log_level)
        self.format = '%(levelname)-5s :: %(message)s'
        logging.basicConfig(format=self.format)

    def set_log_level(self, log_level: LogLevel | int = LogLevel.INFO):
        if isinstance(log_level, int):
            log_level = LogLevel(log_level)
        if log_level == LogLevel.DISABLED:
            self.disable()
        else:
            self.logger.setLevel(level=log_level.value)

    @staticmethod
    def disable():
        logging.disable(logging.CRITICAL)

    @staticmethod
    def format_log(log):
        return log

    def info(self, log):
        logging.info(self.format_log(log))

    def warning(self, log):
        logging.warning(self.format_log(log))

    def error(self, log):
        logging.error(self.format_log(log))

    def debug(self, log):
        logging.debug(self.format_log(log))

    def critical(self, log):
        logging.critical(self.format_log(log))

    def exception(self, log):
        logging.exception(self.format_log(log))
