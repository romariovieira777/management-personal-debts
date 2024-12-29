import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.config.config import Base


class PaymentHistoryModel(Base):
    __tablename__ = 'tb_payment_history'

    id = Column(Integer, primary_key=True, index=True)
    debt_id = Column(Integer, ForeignKey('tb_debts.id'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'), nullable=False, index=True)
    amount_paid = Column(Float(precision=2), nullable=False)
    payment_date = Column(DateTime, nullable=False)
    payment_method = Column(String(50), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now())

    debt = relationship("DebtsModel", back_populates="payments")
    user = relationship("UserModel", back_populates="payments")

    def __repr__(self):
        return f"<Payment {self.amount_paid} for debt {self.debt_id}>"

    @property
    def is_valid_amount(self):
        """Verifica se o valor do pagamento é válido em relação à dívida"""
        return self.amount_paid <= self.debt.remaining_amount