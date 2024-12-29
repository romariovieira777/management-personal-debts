import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.config.config import Base


class CategoryModel(Base):
    __tablename__ = 'tb_categories'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('tb_users.id'), nullable=False, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    color = Column(String(7), nullable=False)  # Format HEX: #RRGGBB
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.datetime.now())
    is_default = Column(Boolean, nullable=False, default=False)

    user = relationship("UserModel", back_populates="categories")

    debts = relationship("DebtsModel", back_populates="category")


    def __repr__(self):
        return f"<Category {self.name}>"

    @property
    def active_debts(self):
        return [debt for debt in self.debts if not debt.is_deleted]

    def add_debt(self, debt):
        if debt.user_id != self.user_id:
            raise ValueError("A dívida deve pertencer ao mesmo usuário da categoria")
        self.debts.append(debt)