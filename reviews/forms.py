from django import forms


class ReviewForm(forms.Form):
    your_name = forms.CharField(label="Your Name", min_length=3)