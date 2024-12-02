import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',  
    handlers=[
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__) 
