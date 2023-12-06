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


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    id_vk = Column(Integer, index=True, unique=True)
    token_vk = Column(String, unique=True)
    firstname = Column(String)
    lastname = Column(String)

    rooms = relationship("RoomUser", back_populates="user")


class RoomUser(Base):
    __tablename__ = "roomsusers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    invent = Column(String, default=default_invent)

    room_id = Column(
        Integer,
        ForeignKey("rooms.id", ondelete="CASCADE"),
        index=True,
    )

    user = relationship("User", back_populates="rooms")
    room = relationship("Room", back_populates="users")


class Friends(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True, index=True)

    user1_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    user2_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    user1 = relationship("User", foreign_keys=[user1_id])
    user2 = relationship("User", foreign_keys=[user2_id])


class Waiters(Base):
    __tablename__ = "waiters"

    id = Column(Integer, primary_key=True, index=True)

    user1_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    user2_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    user1 = relationship("User", foreign_keys=[user1_id])
    user2 = relationship("User", foreign_keys=[user2_id])
