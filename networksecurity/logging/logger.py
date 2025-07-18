
import logging
import os
from datetime import datetime

# Generate log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Create logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE_NAME)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[(%(asctime)s)] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

