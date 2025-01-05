import os
import pytz
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SECRET_KEY = "8#y6wf4@t5$s#5r&l#6*kksb(-%omp4gvk(7g73(=pk-h&zjqb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1h

load_dotenv(find_dotenv())

ENVIRON = os.environ.get('ENVIRON')

TIMEZONE = pytz.timezone(os.environ.get('TIMEZONE'))

DATABASE = os.environ.get('DATABASE')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_URL = "postgresql://{}:{}@{}/{}".format(DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE)
ENGINE_SERASA = create_engine(DATABASE_URL, pool_size=3, max_overflow=20)
SESSION_SERASA = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE_SERASA)


USERNAME_API = os.environ.get('USERNAME_API')
EMAIL_API = os.environ.get('EMAIL_API')
PASSWORD_API = os.environ.get('PASSWORD_API')

Base = declarative_base()


def get_db_serasa():
    db = SESSION_SERASA()
    try:
        yield db
    except Exception as e:
        print(f"Error during a transaction: {e}")
        db.rollback()
    finally:
        db.close()


ORIGIN_CORS = [
    "*"
]
