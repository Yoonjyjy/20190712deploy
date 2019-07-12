from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserFrom(UserCreationForm) :
    email = forms.EmailField(required=True)
    nickname = forms.CharField(required=True)

    class Meta :
        model = User
        fields = ("username", "email", "nickname", "password1", "password2")

    def save(self, commit=True) :
        user = super(CreateUserFrom, self).save(commit=False)
        user.nickname = self.cleaned_data["nickname"]
        user.email = self.cleaned_data["email"]
        if commit :
            user.save()
        return user