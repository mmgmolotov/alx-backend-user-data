#!/usr/bin/env python3
"""
Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """

        """
        return False

    def authorization_header(self, request=None) -> str:
        """

        """
        return

    def current_user(self, request=None) -> TypeVar('User'):
        """

        """
        return


if __name__ == "__main__":
    a = Auth()
    print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
    print(a.authorization_header())
    print(a.current_user())
