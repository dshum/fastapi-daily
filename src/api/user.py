from fastapi import APIRouter

from lib.user import fastapi_users, auth_backend
from schemas.user import UserCreateDTO, UserReadDTO, UserUpdateDTO

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt"
)

router.include_router(
    fastapi_users.get_register_router(UserReadDTO, UserCreateDTO),
)

router.include_router(
    fastapi_users.get_reset_password_router(),
)

router.include_router(
    fastapi_users.get_verify_router(UserReadDTO),
)

router.include_router(
    fastapi_users.get_users_router(UserReadDTO, UserUpdateDTO),
)
