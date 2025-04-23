from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class HardcodedAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None
        
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

