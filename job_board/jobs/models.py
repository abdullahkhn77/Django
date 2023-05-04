from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title