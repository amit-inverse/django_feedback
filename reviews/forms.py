from django import forms


class ReviewForm(forms.Form):
    your_name = forms.CharField(label="Your Name", min_length=3, max_length=100, error_messages={
        "required": "Your name must not be empty",
        "min_length": "Your name must be at least 3 characters long",
        "max_length": "Your name must be less than 100 characters long"})