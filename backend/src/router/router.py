from fastapi import APIRouter
from backend.src.controller import auth_controller, user_controller, debts_controller, category_controller, \
    payments_historic_controller

router = APIRouter()

router.include_router(auth_controller.router, prefix='/api/auth', tags=['Authentication'])
router.include_router(user_controller.router, prefix='/api/users', tags=['Users'])
router.include_router(debts_controller.router, prefix='/api/debts', tags=['Debts'])
router.include_router(category_controller.router, prefix='/api/category', tags=['Category'])
router.include_router(payments_historic_controller.router, prefix='/api/payments/historic', tags=['Payments Historic'])