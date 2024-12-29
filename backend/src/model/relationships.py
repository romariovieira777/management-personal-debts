from sqlalchemy.orm import relationship
from .debts import DebtsModel
from .users import UserModel


def setup_relationships():
    UserModel.debts = relationship("DebtsModel", back_populates="user", cascade="all, delete-orphan")
    UserModel.categories = relationship("CategoryModel", back_populates="user", cascade="all, delete-orphan")
    UserModel.payments = relationship("PaymentHistoryModel", back_populates="user")

    DebtsModel.user = relationship("UserModel", back_populates="debts")
    DebtsModel.category = relationship("CategoryModel", back_populates="debts")
    DebtsModel.payments = relationship("PaymentHistoryModel", back_populates="debt", cascade="all, delete-orphan")
    DebtsModel.attachments = relationship("AttachmentModel", back_populates="debt", cascade="all, delete-orphan")