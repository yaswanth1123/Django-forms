from socket import fromshare
from django import forms

class schoolform(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=100)
