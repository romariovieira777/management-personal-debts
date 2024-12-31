from fastapi import APIRouter, Depends
from starlette.requests import Request
from backend.src.repository.repository import JWTBearer
from backend.src.schema.schema import ResponseSchema

router = APIRouter()

@router.get('/list/{user_id}', dependencies=[Depends(JWTBearer())])
async def list_user(request: Request, user_id: int):
    try:

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success list debts",
                              result=None).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.get('/list/{debt_id}', dependencies=[Depends(JWTBearer())])
async def list_debt(request: Request, debt_id: int):
    try:

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success list debts",
                              result=None).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)