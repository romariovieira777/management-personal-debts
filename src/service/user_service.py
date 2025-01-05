from src.config.config import get_db_serasa
from src.model.users import UserModel
from src.repository.repository import UserRepository
from src.schema.schema import RegisterSchema, UpdateUserSchema

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



    @classmethod
    def update(cls, request: UpdateUserSchema, user_id: int):

        session = next(get_db_serasa())

        try:

            user = UserRepository.retrieve_by_first_id(session, UserModel, user_id)

            if user is not None:

                user.first_name=request.first_name,
                user.last_name=request.last_name,

                UserRepository.update(session, user)

                user_dict = user.__dict__
                user_dict.pop('password_hash', None)

                return user_dict

        except Exception as e:
            raise f"Failed to update user: {str(e)}"

        finally:
            session.close()


