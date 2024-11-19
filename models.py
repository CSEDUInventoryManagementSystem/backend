
from xmlrpc.client import Boolean
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, Text, Enum
from sqlalchemy.orm import relationship

from datetime import datetime, timedelta
from sqlalchemy import DateTime

from enum import Enum as PyEnum




class RoleEnum(PyEnum):
    ADMIN = "ADMIN"
    TEACHER = "TEACHER"
    STOREOFFICER = "STOREOFFICER"
    OFFICER = "OFFICER"
    ROOMATTENDANT = "ROOMATTENDANT"

class StatusEnum(PyEnum):
    PENDING = "PENDING"
    VERIFIED = "VERIFIED"
    REJECTED = "REJECTED"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashedPassword = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.OFFICER)
    phone = Column(String)
    userName = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.PENDING)
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, default=lambda: datetime.now())
