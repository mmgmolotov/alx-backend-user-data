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
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path.endswith('/') is False:
            path = path + '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') is False:
                excluded_path = excluded_path + '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header from the request.
        """
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> None:
        """

        """
        return
