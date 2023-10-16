import logging
import os,pathlib

log_file_path = "F:/projects/Address_book/address_book.log"  
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file_path)
logger.addHandler(file_handler)



