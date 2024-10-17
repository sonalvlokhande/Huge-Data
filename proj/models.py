from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    mobile = Column(String(20), unique=True, nullable=False)
    otp = Column(String(10), nullable=True)
    last_login = Column(TIMESTAMP)