from django.db import models

class Review(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True, null=True)  # positive, negative, neutral
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

