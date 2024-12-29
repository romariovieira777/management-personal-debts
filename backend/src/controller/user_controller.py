from fastapi import APIRouter

from backend.src.config.config import get_db_serasa
from backend.src.schema.schema import ResponseSchema, RegisterSchema
from backend.src.service.user_service import UserService

router = APIRouter()

@router.post('/register')
async def register(request: RegisterSchema):
    try:

        user = UserService.register(request)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success register user",
                              result=user).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)
