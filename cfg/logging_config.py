import os
from logging import basicConfig, getLogger
from logging import DEBUG, INFO
from logging import error, warning, debug, info, critical, Formatter
from logging import FileHandler, StreamHandler

from cfg import (
    ProjectDefinitions,
)

ROOT_DIR = ProjectDefinitions.getROOTDir()
program_session_id = ProjectDefinitions.getProgramSessionID()


class LoggingConfig:

    __logger = None

    __general_file_handler_mode = "a"
    __general_log_path = os.path.join(ROOT_DIR, "./logs/general_log_path.log")
    __handlers = [
        FileHandler(__general_log_path, __general_file_handler_mode),
        StreamHandler(),
    ]

    @staticmethod
    def get_active_logger(__name__):

        if LoggingConfig.__logger == None:
            LoggingConfig.default_setup_logging()
            LoggingConfig.__logger = getLogger(__name__)
        return LoggingConfig.__logger

    @staticmethod
    def default_setup_logging():

        handlers = LoggingConfig.__handlers

        for handler in handlers:
            handler.setFormatter(LoggingConfig.logging_formater())

        basicConfig(
            level=DEBUG,
            encoding="utf-8",
            handlers=handlers,
        )

    @staticmethod
    def addSpecificFileHandler(logger, specific_log_path, specific_file_handler_mode):

        specific_log_path = os.path.join(ROOT_DIR, specific_log_path)
        specific_file_handler = FileHandler(
            specific_log_path, specific_file_handler_mode
        )
        specific_file_handler.setFormatter(LoggingConfig.logging_formater())

        LoggingConfig.__handlers.append(specific_file_handler)
        LoggingConfig.get_active_logger(__name__).addHandler(specific_file_handler)

        logger.info(
            f"File handler adicionado aos logs : {specific_log_path}\n Modo: {specific_file_handler_mode}"
        )

    @staticmethod
    def logging_formater():
        formatter = Formatter(
            f"Sessao do programa {program_session_id} - %(asctime)s - [%(levelname)s]: - Executando arquivo: %(filename)s - LOG: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        return formatter


if __name__ == "__main__":
    logger = LoggingConfig.get_active_logger(__name__)
    logger.info("Este é um log de informação geral")
    LoggingConfig.addSpecificFileHandler(logger, "./logs/tst.log", "a")
    logger.info("Este é um log de informação no arquivo específico. 777")
