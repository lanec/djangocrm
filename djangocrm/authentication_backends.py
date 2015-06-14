from django.contrib.auth import get_user_model
from django.db.models import Q


User.objects.get(Q(username="JOE") | Q(email="Jjjasinski@joe.com"))

class UserEmailAuthentication(object):

    def authenticate(self, username_or_email=None, password=None, **kwargs):
        UserModel = get_user_model()

    	try:
            user = UserModel._default_manager.get(Q(username=username_or_email) | Q(email=username_or_email))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
        	UserModel().set_password(password)


