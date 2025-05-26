from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    time = models.TimeField(null=True, blank=True)  # NEW FIELD

    def __str__(self):
        return self.title
