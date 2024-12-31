from fastapi import APIRouter, Depends
from starlette.requests import Request
from backend.src.repository.repository import JWTBearer
from backend.src.schema.schema import ResponseSchema, CategorySchema
from backend.src.service.category_service import CategoryService

router = APIRouter()

@router.get('/list/{user_id}', dependencies=[Depends(JWTBearer())])
async def list(request: Request, user_id: int):
    try:

        categories = CategoryService.list(user_id)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success list categories",
                              result=categories).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)



@router.post('/register', dependencies=[Depends(JWTBearer())])
async def register(request: Request, category: CategorySchema):
    try:

        category = CategoryService.register(category)

        return ResponseSchema(code="200",
                              status="Ok",
                              message="Success register debt",
                              result=category).model_dump(exclude_none=True)

    except Exception as e:
        return ResponseSchema(code="500",
                              status="Internal Server Error",
                              message=e.__str__()).model_dump(exclude_none=True)