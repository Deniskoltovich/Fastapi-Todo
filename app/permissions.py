from typing import List

from fastapi import Depends, HTTPException

from app.models.user import User
from app.services.auth import AuthService


class RoleChecker:
    def __init__(self, allowed_role: list):
        self.allowed_role = allowed_role

    def __call__(
        self,
        user: User = Depends(AuthService.get_current_user_from_token),
    ):
        if user.role not in self.allowed_role:
            raise HTTPException(
                status_code=403, detail="Operation not permitted"
            )
