from sqlalchemy import Column, String, Integer, Date

from base import Base

class Count(Base):

    __tablename__ = 'Count'

    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=0)

    def __init__(self, id, count):
        self.id = id
        self.count = count

