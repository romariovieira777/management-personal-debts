from fastapi import APIRouter, Depends
from starlette.requests import Request
from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema, PaymentHistorySchema
from src.service.payment_historic_service import PaymentHistoryService

router = APIRouter()

@router.get('/list/{user_id}', dependencies=[Depends(JWTBearer())])
async def list_user(request: Request, user_id: int):
    try:

        payments_history = PaymentHistoryService.list_user_id(user_id)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success list debts",
                              result=payments_history).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.get('/list/{debt_id}', dependencies=[Depends(JWTBearer())])
async def list_debt(request: Request, debt_id: int):
    try:

        payments_history = PaymentHistoryService.list_debt_id(debt_id)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success list debts",
                              result=payments_history).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.post('/register', dependencies=[Depends(JWTBearer())])
async def register(request: Request, payment_historic: PaymentHistorySchema):
    try:

        payment_historic = PaymentHistoryService.register(payment_historic)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success list debts",
                              result=payment_historic).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)