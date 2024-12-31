from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12
)

class Shared:

    @classmethod
    def get_password_hash(cls, password: str):
        return pwd_context.hash(password)
