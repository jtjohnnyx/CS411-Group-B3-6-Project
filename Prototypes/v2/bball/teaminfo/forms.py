
from django import forms

class TeamForm(forms.Form):
   Team_name = forms.CharField(required=True)
   #email = forms.EmailField()
   #message = forms.CharField(max_length=1000)

class PlayerForm(forms.Form):
   Player_name = forms.CharField(required=True)