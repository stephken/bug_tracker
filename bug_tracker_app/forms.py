from django import forms
from bug_tracker_app.models import MyUser, Ticket


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description"]

class InProgressForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["assigned_to"]