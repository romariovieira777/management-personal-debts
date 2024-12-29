from backend.src.config.config import get_db_serasa
from backend.src.model.users import UserModel
from backend.src.repository.repository import UserRepository
from backend.src.schema.schema import RegisterSchema

"""
    Users
"""


class UserService:

    @classmethod
    def register(cls, request: RegisterSchema):

        session = next(get_db_serasa())

        try:

            existing_user = UserRepository.retrieve_by_first_email(session, UserModel, request.email)

            if existing_user is None:

                user = UserModel(
                    first_model=request.first_name,
                    last_name=request.last_name,
                    email=request.last_name,
                    password_hash=request.get_password_hash()
                )

                UserRepository.insert(session, user)

                return user

        except Exception as e:
            raise f"Failed to add user: {str(e)}"

        finally:
            session.close()



