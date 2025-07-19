from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Max 200 chars
    author = models.CharField(max_length=100)  # Max 100 chars
    publication_year = models.IntegerField()  # Year as integer

    def _str_(self):
        return f"{self.title} by {self.author} ({self.publication_year})"