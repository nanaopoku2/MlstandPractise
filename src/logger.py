import logging
import os
from datetime import datetime


LOG_FIlE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FIlE)
os.makedirs(logs_path,exist_ok=True)


LOG_FIlE_PATH=os.path.join(logs_path,LOG_FIlE)


logging.basicConfig(
    filename=LOG_FIlE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# # Tesing the logger
if __name__=="__main__":
    logging.info("Logging has started")