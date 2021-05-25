from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database:
    __instance = None

    @staticmethod
    def getInstance(user, passwd, host, db, port=5432):

        if Database.__instance == None:
            Database(user, passwd, host, db, port)
        return Database.__instance

    def __init__(self, user, passwd, host, db, port=5432):

        if Database.__instance != None:
            raise Exception("This class is a Database!")
        else:
            self.engine = create_engine(f'postgresql://{user}:{passwd}@{host}:{port}/{db}')
            self.session = sessionmaker(bind=self.engine)
            self.base = declarative_base()
            Database.__instance = self
