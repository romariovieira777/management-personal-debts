from fastapi import APIRouter, Depends
from starlette.requests import Request
from src.repository.repository import JWTBearer
from src.schema.schema import ResponseSchema, RegisterSchema, UpdateUserSchema
from src.service.user_service import UserService

router = APIRouter()

@router.post('/register')
async def register(request: Request, register: RegisterSchema):
    try:

        user = UserService.register(register)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success register user",
                              result=user).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.put('/update/{user_id}', dependencies=[Depends(JWTBearer())])
async def update(request: Request, user_id: int, register: UpdateUserSchema):
    try:

        user = UserService.update(register, user_id)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success update user",
                              result=user).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)
