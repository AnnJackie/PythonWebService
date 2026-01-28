from starlette import status
from starlette.exceptions import HTTPException


def token_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="The provided token is invalid"
    )

def username_taken_exception():
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="The provided username is taken"
    )


def user_credential_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )

