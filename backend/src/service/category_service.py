from backend.src.config.config import get_db_serasa
from backend.src.model import CategoryModel
from backend.src.repository.repository import CategoryRepository
from backend.src.schema.schema import CategorySchema

"""
    Category
"""


class CategoryService:

    @classmethod
    def list(cls, user_id):

        session = next(get_db_serasa())

        try:

            debts = CategoryRepository.retrieve_by_user_id(session, CategoryModel, user_id)

            return debts

        except Exception as e:
            raise f"Failed to list debts: {str(e)}"

        finally:
            session.close()


    @classmethod
    def register(cls, request: CategorySchema):

        session = next(get_db_serasa())

        try:
            category = CategoryModel(
                user_id=request.user_id,
                name=request.name,
                description=request.description,
                color=request.color_rgb,
            )

            CategoryRepository.insert(session, category)

            return category

        except Exception as e:
            raise f"Failed to add category: {str(e)}"

        finally:
            session.close()