from django.contrib.auth.forms import UserCreationForm,UserChangeForm,get_user_model
from .models import SomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = SomUser
        fields=['username','password1','password2','introduce']

class SomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [ 'introduce']