from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db.utils.common import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
