# src/common/password_hashing.py

from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["bcrypt"])


def hash_password(password: str) -> str:
    return crypt_context.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    return crypt_context.verify(password, password_hash)
