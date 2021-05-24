from datetime import date

from count import Count
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()
