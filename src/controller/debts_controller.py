from fastapi import APIRouter, Depends
from starlette.requests import Request
from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema, DebtsSchema
from src.service.debts_service import DebtsService

router = APIRouter()

@router.get('/list/{user_id}', dependencies=[Depends(JWTBearer())])
async def list(request: Request, user_id: int):
    try:

        debts = DebtsService.list(user_id)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success list debts",
                              result=debts).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.post('/register', dependencies=[Depends(JWTBearer())])
async def register(request: Request, debts : DebtsSchema):
    try:

        debt = DebtsService.register(debts)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success register debt",
                              result=debt).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.put('/update/{debt_id}', dependencies=[Depends(JWTBearer())])
async def update(request: Request, debt_id: int, debts : DebtsSchema):
    try:

        debt = DebtsService.update(debts, debt_id)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success update debt",
                              result=debt).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.put('/disable/{debt_id}', dependencies=[Depends(JWTBearer())])
async def disable_debt(request: Request, debt_id: int, is_deleted: bool):
    try:

        debt = DebtsService.disable_debit(debt_id, is_deleted)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success disable debt",
                              result=debt).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)