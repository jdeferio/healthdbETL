import os
import logging


from dotenv import load_dotenv, find_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


# set logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# load .env variables
load_dotenv(find_dotenv())

def connect_healthdb():    
    session_args = {
        'drivername': os.environ['DB_DRIVER'], 
        'username': os.environ['DB_USER'],
        'password': os.environ['DB_USER_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_PORT'],
        'database': os.environ['DB_NAME']
    }
    
    try:
        engine = create_engine(
            str(URL(**session_args))
        )
        _Session = sessionmaker(bind=engine)
        session = _Session()
        return engine, session
    except:
        logger.info(f"failed to connect to database: {session_args.get('database')}")

def close_db_session(session):
    """Closes connection to database"""
    session.close()