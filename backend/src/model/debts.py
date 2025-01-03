import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Text, Boolean, Enum, func
from sqlalchemy.orm import relationship
from backend.src.config.config import Base


class DebtStatus(enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    OVERDUE = "OVERDUE"


class DebtsModel(Base):
    __tablename__ = 'tb_debts'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'), nullable=False, index=True)
    category_id = Column(Integer, ForeignKey('tb_categories.id'), nullable=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float(precision=2), nullable=False)
    due_date = Column(DateTime, nullable=False)
    status = Column(Enum(DebtStatus), nullable=False, default=DebtStatus.PENDING)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)

    user = relationship("UserModel", back_populates="debts")
    category = relationship("CategoryModel", back_populates="debts")
    payments = relationship("PaymentHistoryModel", back_populates="debt", cascade="all, delete-orphan")


    @property
    def total_paid(self):
        """Calcula o total pago para esta dívida"""
        return sum(payment.amount_paid for payment in self.payments)

    @property
    def remaining_amount(self):
        """Calcula o valor restante a ser pago"""
        return self.amount - self.total_paid