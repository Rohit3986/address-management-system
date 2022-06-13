from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database


class Address(database.Base):
    __tablename__ = "address"
    address_id = Column(Integer, primary_key=True, index=True)
    house_number = Column(String, unique=True)
    area = Column(String)
    district = Column(String, default=True)
    state = Column(String, default=True)
    country = Column(String, default=True)
