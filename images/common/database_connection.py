from common.logger import setup_logger
from sqlalchemy import create_engine
import os

def database_connection():

    logger = setup_logger("./logs/logs.log", "DEBUG", "database_logger")

    user = os.environ.get("MYSQL_USER")
    password = os.environ.get("MYSQL_PASSWORD")
    db_name = os.environ.get("MYSQL_DATABASE")

    con_str = f"mysql://{user}:{password}@database/{db_name}"

    try:
        # Connect to the database
        engine = create_engine(con_str)
    except Exception as e:
        logger.error(f"Failed to create engine: {e}")
    
    return engine