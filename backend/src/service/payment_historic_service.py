from backend.src.config.config import get_db_serasa
from backend.src.model import PaymentHistoryModel, DebtsModel
from backend.src.repository.repository import PaymentsHistoryRepository, DebtsRepository
from backend.src.schema.schema import PaymentHistorySchema

"""
    Payment Historic
"""


class PaymentHistoryService:

    @classmethod
    def list_user_id(cls, user_id):

        session = next(get_db_serasa())

        try:

            payments_history = PaymentsHistoryRepository.retrieve_by_user_id(session, PaymentHistoryModel, user_id)

            return payments_history

        except Exception as e:
            raise f"Failed to list payments history: {str(e)}"

        finally:
            session.close()

    @classmethod
    def list_debt_id(cls, debt_id):

        session = next(get_db_serasa())

        try:

            payments_history = PaymentsHistoryRepository.retrieve_by_debt_id(session, PaymentHistoryModel, debt_id)

            return payments_history

        except Exception as e:
            raise f"Failed to list payments history: {str(e)}"

        finally:
            session.close()

    @classmethod
    def register(cls, request: PaymentHistorySchema):

        session = next(get_db_serasa())

        try:

            debt = DebtsRepository.retrieve_by_first_id(session, DebtsModel, request.debt_id)

            if debt:

                payments_historic_sum = PaymentsHistoryRepository.retrieve_sum_payments_by_debt_id(session, PaymentHistoryModel, debt.id)

                if (payments_historic_sum + request.amount_paid) <= debt.amount:

                    payment_history = PaymentHistoryModel(
                        debt_id=request.debt_id,
                        user_id=request.user_id,
                        amount_paid=request.amount_paid,
                        payment_date=request.payment_date,
                        notes=request.notes
                    )

                    PaymentsHistoryRepository.insert(session, payment_history)

                    return {
                        "payment_history": payment_history,
                        "paid": True if (payments_historic_sum + request.amount_paid) == debt.amount else False
                    }
                else:
                    return {
                        "payment_history": None,
                        "paid": True
                    }
            else:
                raise f"Debt not found"

        except Exception as e:
            raise f"Failed to add debt: {str(e)}"

        finally:
            session.close()