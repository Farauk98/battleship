from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import UserManager
from .models import ChatMessage

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

class ShotForm(forms.Form):
    x = forms.IntegerField(min_value=0, max_value=9, label="X Coordinate")
    y = forms.IntegerField(min_value=0, max_value=9, label="Y Coordinate")


class CreateInvitationForm(forms.Form):
    
    numbers = forms.CharField(widget=forms.Textarea, label="Wpisz liczby")
    user = forms.ModelChoiceField(queryset=None, label="Wybierz użytkownika")

    def __init__(self, current_user, *args, **kwargs):
        super(CreateInvitationForm, self).__init__(*args, **kwargs)
        # Set the queryset to exclude the current user
        self.fields['user'].queryset = User.objects.exclude(id=current_user.id)
        self.fields['user'].required = True

    def clean_numbers(self):
        numbers_string = self.cleaned_data['numbers']
        
        # Sprawdzanie, czy wszystkie znaki to liczby lub spacje
        if not all(char.isdigit() or char.isspace() for char in numbers_string):
            raise ValidationError("Wpisz tylko liczby całkowite oddzielone pojedynczymi spacjami.")

        # Przekształć ciąg tekstowy na listę liczb, sprawdzając przy tym pojedyncze spacje
        try:
            numbers = [int(num) for num in numbers_string.split()]
        except ValueError:
            raise ValidationError("Upewnij się, że liczby są oddzielone pojedynczymi spacjami.")

        # Sprawdź, czy liczba elementów jest w zakresie od 1 do 7
        if not (1 <= len(numbers) <= 7):
            raise ValidationError("Wpisz od 1 do 7 liczb.")

        # Sprawdź, czy każda liczba jest w zakresie od 1 do 6
        if not all(1 <= num <= 6 for num in numbers):
            raise ValidationError("Każda liczba musi być w zakresie od 1 do 6.")

        return numbers
    
class ChatForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['content']