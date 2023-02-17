from django import forms
from account.models import User
from service.models import Sheba
class UserForm (forms.ModelForm):
    class Meta:
        # specify model to be used
        model = User
        fields = '__all__'


class ServiceForm(forms.ModelForm):
   class Meta:
        # specify model to be used
        model = Sheba
        fields = '__all__'

class LoginAdminForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs ={
                "class":"form-control"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs ={
                "class":"form-control"
            }
        )
    )