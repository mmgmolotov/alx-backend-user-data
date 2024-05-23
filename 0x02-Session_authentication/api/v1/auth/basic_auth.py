#!/usr/bin/env python3
"""
Basic Auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar, Tuple, Optional


class BasicAuth(Auth):
    """
    Basic Authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """

        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """

        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """

        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> Optional[TypeVar('User')]:
        """

        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> Optional[TypeVar('User')]:
        """

        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        if decoded_auth_header is None:
            return None

        email, password = self.extract_user_credentials(decoded_auth_header)
        if email is None or password is None:
            return None

        user = self.user_object_from_credentials(email, password)
        return user
