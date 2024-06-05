#!/usr/bin/python3

# Import libraries
import logging

# Create a custom logger
logger = logging.getLogger('my_logger')

# Create handlers

# Stream Handler - errors sent to screen
s_handler = logging.StreamHandler()
s_handler.setLevel(logging.WARNING)
s_format = logging.Formatter('%(name)s - %(levelname)s - %(messsage)s')
s_handler.setFormatter(s_format)

# File Handler - errors sent to file
f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.WARNING)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(s_handler)
logger.addHandler(f_handler)

logging.warning("This is a warning")
logging.error("This is an error")