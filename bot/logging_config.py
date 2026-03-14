import logging, os

LOG_DIR = "logs"
LOG_FILE = "logs/trading.log"

#Ensure logs folder exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename= LOG_FILE,
    level = logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger():
    return logging.getLogger()