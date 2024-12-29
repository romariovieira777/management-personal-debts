from fastapi import APIRouter

from backend.src.controller import auth_controller, user_controller

router = APIRouter()

router.include_router(auth_controller.router, prefix='/api/auth', tags=['Authentication'])
router.include_router(user_controller.router, prefix='/api/users', tags=['Users'])