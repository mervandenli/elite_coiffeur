from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control w3-input","placeholder":"Name"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control w3-input","placeholder":"Subject"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control w3-input","placeholder":"Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control w3-input","placeholder":"Message"}))

    class Meta:
        model = Feedback
        fields = ('__all__')