from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base


default_invent = "0/" * 9 + "0"


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(52))
    password = Column(Integer)

    users = relationship("RoomUser", back_populates="room")


class RoomUser(Base):
    __tablename__ = "roomsusers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    invent = Column(String, default=default_invent)
    room_id = Column(Integer, ForeignKey("rooms.id"), index=True)
