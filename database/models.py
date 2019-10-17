from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Integer, func, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Company(Base):
    __tablename__ = 'company'

    company_id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=func.now())


class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(UUID(as_uuid=True), primary_key=True)
    config_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    username = Column(String(30), unique=True, nullable=False)
    password_hash = Column(String(500), nullable=False)
    email = Column(String(500), unique=True, nullable=False)
    email_confirmation_token = Column(UUID(as_uuid=True), unique=True, nullable=False)
    email_confirmed_at = Column(DateTime, nullable=True)
    password_reset_token = Column(UUID(as_uuid=True), unique=True, nullable=True)
    frequency_capping_enabled = Column(Boolean, default=True)
    max_frequency = Column(Integer, nullable=True)
    company_id = Column(ForeignKey('company.company_id'), nullable=False, index=True)

    company = relationship(Company)



class Chatbot(Base):
    __tablename__ = 'chatbots'

    chatbot_id = Column(UUID(as_uuid=True), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=func.now())
    active = Column(Boolean, default=True)
    deleted_at = Column(DateTime, nullable=True, default=func.now())
    # user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    name = Column(String(30), nullable=False)
    description = Column(String, nullable=False)
    language = Column(String(30), nullable=False)
    model_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    archive_options = Column(String(30), nullable=True)
    company_id = Column(ForeignKey('company.company_id'), nullable=False, index=True)

    company = relationship(Company)
    # users = relationship(User)


class DataSet(Base):
    __tablename__ = 'datasets'

    dataset_id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(30), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    # user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    language = Column(String(30), nullable=False)
    deleted_at = Column(DateTime, nullable=True, default=func.now())
    company_id = Column(ForeignKey('company.company_id'), nullable=False, index=True)

    company = relationship(Company)
    # users = relationship(User)

