"""
 this code defines a function customLogger that creates a logger object with a specified
 logging level and configuration, including writing log messages to a file.
 It uses the inspect module to dynamically obtain the name of the calling function/method as
 the name of the logger.
"""

import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]

    logger = logging.getLogger(loggerName)
    # By default, log all messages

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(r"C:\Binay\PyChamp\upmove_framework\logs\automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
