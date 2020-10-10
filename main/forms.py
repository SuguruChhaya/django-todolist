from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    #!Can finish form without requirement
    check = forms.BooleanField(required=False)