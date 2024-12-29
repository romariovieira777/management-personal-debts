from fastapi import APIRouter

from backend.src.controller import auth_controller

router = APIRouter()

router.include_router(auth_controller.router, prefix='/api/management-personal-debts/auth', tags=['Authentication'])