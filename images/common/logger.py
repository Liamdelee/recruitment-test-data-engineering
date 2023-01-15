#!/usr/bin/env python3
import logging

def setup_logger(log_file, log_level, logger_name=__name__):

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)

    # create a stream handler
    stream_handler = logging.StreamHandler(log_file)
    stream_handler.setLevel(log_level)

    # create a logging format for the file handler + stream handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger