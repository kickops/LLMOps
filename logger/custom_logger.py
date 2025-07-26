import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(logs_dir, exist_ok=True)
        LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        LOG_FILE = os.path.join(self.logs_dir, LOG_FILE)

        #configure logging
        logging.basicConfig(
            filename=LOG_FILE,
            format="[%(asctime)s] %(levelname)s %(name)s (line:%(lineno)d) -  %(message)s",
            level=logging.INFO,
        )
        

    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))
    
if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("Custom logger initialized.")
