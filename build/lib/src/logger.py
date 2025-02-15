import logging # keep track of all the module
import os #it provide the functionality to reading and writing to the file
from datetime import datetime 

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%s')}.log"

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) # final log path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level = logging.INFO
)