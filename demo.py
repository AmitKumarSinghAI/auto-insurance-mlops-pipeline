import sys
from src.exception import MyException,error_message_detail
from src.logger import logging

# logging.info("statr")
try:
    number = int("hello")

except Exception as e:
    raise error_message_detail(e,sys)