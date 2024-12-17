from sqlalchemy import Column, Integer, String
from backend.app.database import Base

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    status = Column(String, default="processing")
    link = Column(String, nullable=True)
