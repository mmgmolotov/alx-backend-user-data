#!/usr/bin/env python3
""" SessionDBAuth module for the API """
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from models import storage
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class for session storage in database """

    def create_session(self, user_id=None):
        """ Create and store new instance of UserSession """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id,
                                   session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Return the User ID by querying UserSession """
        if session_id is None:
            return None
        try:
            sessions = storage.search(UserSession,
                                      {"session_id": session_id})
        except Exception:
            return None
        if not sessions or len(sessions) == 0:
            return None
        session = sessions[0]
        if self.session_duration <= 0:
            return session.user_id
        if session.created_at + timedelta(seconds=self.session_duration
                                          ) < datetime.now():
            return None
        return session.user_id

    def destroy_session(self, request=None):
        """ Destroy the UserSession based on the
        Session ID from the request cookie
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        try:
            sessions = storage.search(UserSession,
                                      {"session_id": session_id})
        except Exception:
            return False
        if not sessions or len(sessions) == 0:
            return False
        session = sessions[0]
        session.remove()
        return True
