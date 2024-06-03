#!/usr/bin/pyhton3

# Import ilbraries
import logging
import os

# Basic config of our logger - set file, level timestamp, etc.
logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')

# Create a log object
test_log = logging.getLogger("my_logger")

# Set the level to capture
# test_log.setLevel(logging.DEBUG)

# Generate a set of test log messages
test_log.debug('Harmless debug message')
test_log.info('Just a little info')
test_log.warning('This is a warning')
test_log.error('This is an error')
test_log.critical('Your server is on fire')