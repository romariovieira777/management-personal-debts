from backend.src.config.config import get_db_serasa
from backend.src.model import DebtsModel
from backend.src.repository.repository import DebtsRepository
from backend.src.schema.schema import DebtsSchema

"""
    Debts
"""


class DebtsService:

    @classmethod
    def list(cls, user_id):

        session = next(get_db_serasa())

        try:

            debts = DebtsRepository.retrieve_by_first_id(session, DebtsModel, user_id)

            return debts

        except Exception as e:
            raise f"Failed to list debts: {str(e)}"

        finally:
            session.close()

    @classmethod
    def register(cls, request: DebtsSchema):

        session = next(get_db_serasa())

        try:
            debt = DebtsModel(
                user_id=request.user_id,
                category_id=request.category_id,
                title=request.title,
                amount=request.amount,
                due_date=request.due_date,
                status=request.status,
                notes=request.notes,
                is_deleted=request.is_deleted
            )

            DebtsRepository.insert(session, debt)

            return debt

        except Exception as e:
            raise f"Failed to add debt: {str(e)}"

        finally:
            session.close()


    @classmethod
    def update(cls, request: DebtsSchema, debt_id: int):

        session = next(get_db_serasa())

        try:

            debt = DebtsRepository.retrieve_by_first_id(session, DebtsModel, debt_id)

            if debt is not None:

                debt.category_id=request.category_id,
                debt.title=request.title,
                debt.amount=request.amount,
                debt.due_date=request.due_date,
                debt.status=request.status,
                debt.notes=request.notes,
                debt.is_deleted=request.is_deleted

                DebtsRepository.update(session, debt)

                return debt

            raise "Not found debt"

        except Exception as e:
            raise f"Failed to update debt: {str(e)}"

        finally:
            session.close()


    @classmethod
    def disable_debit(cls, request: DebtsSchema, debt_id: int):

        session = next(get_db_serasa())

        try:

            debt = DebtsRepository.retrieve_by_first_id(session, DebtsModel, debt_id)

            if debt is not None:

                debt.is_deleted=request.is_deleted

                DebtsRepository.update(session, debt)

                return debt

            raise "Not found debt"

        except Exception as e:
            raise f"Failed to disable debt: {str(e)}"

        finally:
            session.close()