# Session Authentication Project

## Table of Contents
1. [Background Context](#background-context)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [Tasks](#tasks)

## Background Context
In this project, you will implement Session Authentication. You are not allowed to install any other module. In the industry, you should use a module or framework that handles session authentication for you (e.g., Flask-HTTPAuth in Python-Flask). However, for learning purposes, we will walk through each step of this mechanism to understand it by doing.

## Resources
Read or watch:
1. [Session Authentication in Flask - YouTube](https://www.youtube.com/watch?v=501dpx2IjGY)
2. [HTTP Cookie - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
3. [Flask](https://palletsprojects.com/p/flask/)
4. [Flask Quickstart - Cookies](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Requirements
### Python Scripts
| Requirement | Description |
| ----------- | ----------- |
| **Python version** | All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7) |
| **New line** | All your files should end with a new line |
| **First line** | The first line of all your files should be exactly `#!/usr/bin/env python3` |
| **README.md** | A `README.md` file, at the root of the folder of the project, is mandatory |
| **Code style** | Your code should use the `pycodestyle` style (version 2.5) |
| **Executable** | All your files must be executable |
| **Length** | The length of your files will be tested using `wc` |
| **Documentation** | All your modules, classes, and functions should have a documentation |
| **Documentation format** | Documentation is not just a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified) |

## Tasks
### Task 0: Et moi et moi et moi!
- Copy all your work from the 0x06. Basic authentication project into this new folder.
- Add a new endpoint: `GET /users/me` to retrieve the authenticated User object.

### Task 1: Empty session
- Create a class `SessionAuth` that inherits from `Auth`. This class will initially be empty.

### Task 2: Create a session
- Update the `SessionAuth` class to include:
  - A class attribute `user_id_by_session_id` initialized as an empty dictionary
  - An instance method `create_session(self, user_id: str = None) -> str` to create a Session ID for a user_id

### Task 3: User ID for Session ID
- Update the `SessionAuth` class to include:
  - An instance method `user_id_for_session_id(self, session_id: str = None) -> str` to return a User ID based on a Session ID

### Task 4: Session cookie
- Update `api/v1/auth/auth.py` to add the method `def session_cookie(self, request=None):` that returns a cookie value from a request

### Task 5: Before request
- Update the `@app.before_request` method in `api/v1/app.py` to:
  - Add the URL path `/api/v1/auth_session/login/` to the list of excluded paths of the method `require_auth`
  - Abort with a 401 status if both `auth.authorization_header(request)` and `auth.session_cookie(request)` return `None`

### Task 6: Use Session ID for identifying a User
- Update the `SessionAuth` class to include:
  - An instance method `current_user(self, request=None)` that returns a User instance based on a cookie value

### Task 7: New view for Session Authentication
- Create a new Flask view in `api/v1/views/session_auth.py` to handle the route `POST /auth_session/login`

### Task 8: Logout
- Update the `SessionAuth` class to include:
  - A method `destroy_session(self, request=None)` that deletes the user session (logout)
- Add a new route `DELETE /api/v1/auth_session/logout` in `api/v1/views/session_auth.py`

### Task 9: Expiration?
- Create a class `SessionExpAuth` that inherits from `SessionAuth` in the file `api/v1/auth/session_exp_auth.py`:
  - Overload `def __init__(self):` method:
    - Assign an instance attribute `session_duration` to the environment variable `SESSION_DURATION` cast to an integer
    - If this environment variable doesn’t exist or can’t be parsed to an integer, assign to 0
  - Overload `def create_session(self, user_id=None):`
    - Create a Session ID by calling `super()` - `super()` will call the `create_session()` method of `SessionAuth`
    - Return `None` if `super()` can’t create a Session ID
    - Use this Session ID as key of the dictionary `user_id_by_session_id` - the value for this key must be a dictionary (called “session dictionary”):
      - The key `user_id` must be set to the variable `user_id`
      - The key `created_at` must be set to the current datetime - you must use `datetime.now()`
    - Return the Session ID created
  - Overload `def user_id_for_session_id(self, session_id=None):`
    - Return `None` if `session_id` is `None`
    - Return `None` if `user_id_by_session_id` doesn’t contain any key equals to `session_id`
    - Return the `user_id` key from the session dictionary if `self.session_duration` is equal or under 0
    - Return `None` if session dictionary doesn’t contain a key `created_at`
    - Return `None` if the `created_at + session_duration` seconds are before the current datetime (`datetime - timedelta`)
    - Otherwise, return `user_id` from the session dictionary
- Update `api/v1/app.py` to instantiate `auth` with `SessionExpAuth` if the environment variable `AUTH_TYPE` is equal to `session_exp_auth`.

### Task 10: Sessions in database
- Create a new model `UserSession` in `models/user_session.py` that inherits from `Base`:
  - Implement the `def __init__(self, *args: list, **kwargs: dict):` like in `User` but for these 2 attributes:
    - `user_id`: string
    - `session_id`: string
- Create a new authentication class `SessionDBAuth` in `api/v1/auth/session_db_auth.py` that inherits from `SessionExpAuth`:
  - Overload `def create_session(self, user_id=None):` that creates and stores a new instance of `UserSession` and returns the Session ID
  - Overload `def user_id_for_session_id(self, session_id=None):` that returns the User ID by requesting `UserSession` in the database based on `session_id`
  - Overload `def destroy_session(self, request=None):` that destroys the `UserSession` based on the Session ID from the request cookie
- Update `api/v1/app.py` to instantiate `auth` with `SessionDBAuth` if the environment variable `AUTH_TYPE` is equal to `session_db_auth`.

## Repository
- GitHub repository: `alx-backend-user-data`
- Directory: `0x02-Session_authentication`

