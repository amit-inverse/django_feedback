from django import forms


class ReviewForm(forms.Form):
    your_name = forms.CharField(label="Your Name", min_length=3, max_length=100, error_messages={
        "required": "Your name must not be empty",
        "min_length": "Your name must be at least 3 characters long",
        "max_length": "Your name must be less than 100 characters long"})
    
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, min_length=10, max_length=500, error_messages={
        "required": "Your feedback must not be empty"})
    
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5, error_messages={
        "required": "Please provide a rating between 1 and 5"})