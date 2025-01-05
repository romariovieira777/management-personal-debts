from fastapi import APIRouter
from src.schema.schema import LoginSchema, ResponseSchema, TokenResponse
from src.service.authentication_service import AuthService

router = APIRouter()


@router.post('/login')
async def login(request: LoginSchema):
    try:
        token = AuthService.get_token(request=request)

        if token is not None:
            return ResponseSchema(code="200",
                                  status="Ok",
                                  message="Success Login",
                                  result=TokenResponse(access_token=token, token_type="Bearer")).model_dump(exclude_none=True)

        else:
            return ResponseSchema(code="500",
                                  status="Internal Server Error",
                                  message="Incorrect email or password").model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)
