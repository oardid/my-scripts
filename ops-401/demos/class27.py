#!/usr/bin/python3

#Import libraries
import logging, time, os
from logging.handlers import RotatingFileHandler


# Create logger object and naming it my logger
logger = logging.getlogger("my_logger")

# Basic config of our logger - set file, level timestamp, etc.
logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')

# Create handler object
handler = RotatingFileHandler("my_logs.log",maxBytes=20, backupCount=3)

# Tell the handler to handle the logs of my logger
logger.addHandler(handler)

# For loop
for i in range(3):
    logmsg = "Hello World"
    logmsg += str(i)
    logger.warning(logmsg)
    print("Logging Hellow World! number", i)
    os.sytem("ls -al")
    time.sleep(.1)