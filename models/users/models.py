from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    id_vk = Column(Integer, index=True, unique=True)
    token_vk = Column(String, unique=True)

    rooms = relationship("RoomUser", back_populates="user")
