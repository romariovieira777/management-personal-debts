import datetime
from datetime import timedelta
from backend.src.config.config import ACCESS_TOKEN_EXPIRE_MINUTES, get_db_serasa
from backend.src.model.users import UserModel
from backend.src.repository.repository import JWTRepo, UserRepository
from backend.src.schema.schema import LoginSchema

"""
    Authentication
"""


class AuthService:

    @classmethod
    def get_token(cls, request: LoginSchema):

        session = next(get_db_serasa())

        user = UserRepository.retrieve_by_first_email(session, UserModel, request.email)

        if user is not None:

            if UserRepository.verify_password(request.password, user.password_hash):

                token = JWTRepo.generate_token({
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

                # Atualiza o último login
                user.last_login = datetime.datetime.now()
                UserRepository.update(session, user)

                return token
            else:
                raise Exception("Incorrect email or password")