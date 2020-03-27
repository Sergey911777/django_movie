from django import forms
from .models import Reviews, Rating, RatingStar, Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user']

class RegisterForm(forms.Form):
    username = forms.CharField(label=u"Имя пользователя")
    first_name = forms.CharField(label=u"Имя")
    last_name = forms.CharField(label=u"Фамилия")
    email = forms.EmailField(label=u"Email", required=False)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=u"Подтвердите пароль", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            self.add_error("password_confirm", u"Пароли не совпадают")
            return False
        return valid

class ReviewForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model = Reviews
        fields = ("name", "email","text")

class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect, empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)

