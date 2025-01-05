from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.config.config import (
    ORIGIN_CORS,
    ENGINE_SERASA,
    Base,
    USERNAME_API,
    PASSWORD_API,
    EMAIL_API,
    get_db_serasa
)
from src.model.users import UserModel
from src.repository.repository import UserRepository
from src.router.router import router
from src.shared.shared import Shared


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_db()
    await add_user(USERNAME_API, EMAIL_API, PASSWORD_API)
    yield


app = FastAPI(
    title="Management Personal Debts API",
    description='API para gerenciamento de dívidas pessoais',
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGIN_CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def initialize_db() -> None:
    # setup_relationships()
    Base.metadata.create_all(bind=ENGINE_SERASA)


async def add_user(username: str, email: str, password: str) -> None:
    session = next(get_db_serasa())

    try:

        existing_user = UserRepository.retrieve_by_first_email(session, UserModel, email)

        if existing_user is None:

            password_hash = Shared.get_password_hash(password)

            new_user = UserModel(
                first_name=username,
                last_name=username,
                email=email,
                password_hash=password_hash
            )

            UserRepository.insert(session, new_user)

    except Exception as e:
        print(f"[+] Failed to add user: {str(e)}")
    finally:
        session.close()


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    return {
        "message": "Welcome to Management Personal Debts API | Serasa",
        "version": "1.0.0"
    }


app.include_router(router=router)