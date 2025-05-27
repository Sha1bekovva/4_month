from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # <-- добавили это
from django.contrib.auth.views import LoginView

class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    next_page = '/films_list/'  # <--- это тоже сработает

GENDER = (
    ('male', 'male'),
    ('female', 'female'),
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='укажите email')
    phone_number = forms.CharField(required=True, label='укажите номер телефона')
    age = forms.IntegerField(required=True, label='Укажите возраст')
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
        )
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()
        return user