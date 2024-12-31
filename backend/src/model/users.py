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

    @property
    def full_name(self):
        """Retorna o nome completo do usuário"""
        return f"{self.first_name} {self.last_name}"

    @property
    def total_debt_amount(self):
        """Calcula o valor total das dívidas ativas do usuário"""
        return sum(debt.amount for debt in self.debts if not debt.is_deleted)

    @property
    def total_paid_amount(self):
        """Calcula o valor total já pago pelo usuário"""
        return sum(payment.amount_paid for payment in self.payments)

    def get_debts_by_status(self, status):
        """Retorna as dívidas do usuário filtradas por status"""
        return [debt for debt in self.debts if debt.status == status and not debt.is_deleted]

    def get_payments_in_period(self, start_date, end_date):
        """Retorna os pagamentos realizados em um período específico"""
        return [
            payment for payment in self.payments
            if start_date <= payment.payment_date <= end_date
        ]