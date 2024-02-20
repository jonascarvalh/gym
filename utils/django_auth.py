from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def authenticate_by_email(email, password):
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None
