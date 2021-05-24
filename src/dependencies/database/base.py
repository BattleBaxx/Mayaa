from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database:

    def __init__(self, user, passwd, host, db, port=5432):
        self.engine = create_engine(f'postgresql://{user}:{passwd}@{host}:{port}/{db}')
        self.session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()