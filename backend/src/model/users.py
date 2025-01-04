from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from sqlalchemy.orm import relationship
from backend.src.config.config import Base


class UserModel(Base):
    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(60), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, nullable=False, default=True)
    last_login = Column(DateTime, nullable=True)

    debts = relationship("DebtsModel", back_populates="user", cascade="all, delete-orphan")
    categories = relationship("CategoryModel", back_populates="user", cascade="all, delete-orphan")
    payments = relationship("PaymentHistoryModel", back_populates="user")