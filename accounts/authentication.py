from accounts.models import User, Token


class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        # tries to get back user through token
        try: 
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        # if user can't be found, creates new user from info in token
        except User.DoesNotExist:
            return User.objects.create(email=token.email)
        # if no token is found, does nothing
        except Token.DoesNotExist:
            return None


    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None