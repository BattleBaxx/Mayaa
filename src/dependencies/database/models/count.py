from sqlalchemy import Column, String, BigInteger, Integer
from dependencies.database.base import Database
from bot.environment import DB_HOST, DB_PASSWORD, DB_NAME, DB_USER


class Count(Database.getInstance(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME).base):
    __tablename__ = 'Count'

    id = Column(String, primary_key=True)
    count = Column(Integer, default=0)

    def __init__(self, id, count):
        self.id = id
        self.count = count
