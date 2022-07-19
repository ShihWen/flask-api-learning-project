from models.user import UserModel
import hmac


def authenticate(username, password):
    '''
    Check username and password when a user sending them from /auth endpoint.
    Return the user for generating JWT when everything is matched.
    '''
    user = UserModel.find_by_username(username)  # return None if no matches
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    '''
    Whenever the user request an endpoint which reqiure authentication,
    the method is used by using the identity, which is a user id, from payload comming from the request.
    '''
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)