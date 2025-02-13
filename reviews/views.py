from django.shortcuts import render
from django.http import HttpResponse
from .utils import analyze_sentiment
from .models import Review

def home(request):
    if request.method == "POST":
        text = request.POST.get("review_text")
        sentiment = analyze_sentiment(text)
        review = Review.objects.create(text=text, sentiment=sentiment)
        review.save()
    reviews = Review.objects.all()
    return render(request, "reviews/home.html", {"reviews": reviews})
