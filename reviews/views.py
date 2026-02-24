from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request):
    if request.method == "POST":
        entered_name = request.POST["your-name"]

        if entered_name == "" or len(entered_name) < 3:
            return render(request, "reviews/review.html", {"has_error": True})
        print(entered_name)
        return HttpResponseRedirect("/thank-you/")
    
    return render(request, "reviews/review.html", {"has_error": False})

def thank_you(request):
    return render(request, "reviews/thank_you.html")
