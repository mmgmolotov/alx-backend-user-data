#!/usr/bin/env python3
"""
Auth
"""
from flask import request
from typing import List
from typing import TypeVar


class Auth:
    """
    Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.

        Returns True if the path is not in the list of excluded_paths.
        Returns True if path is None.
        Returns True if excluded_paths is None or empty.
        Returns False if path is in excluded_paths.
        """
        if path and not path.endswith('/'):
            path = path + '/'
        if not path or path not in excluded_paths:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> None:
        """

        """
        return

    def current_user(self, request=None) -> None:
        """

        """
        return
