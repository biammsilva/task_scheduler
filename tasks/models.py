from django.db import models


class Task(models.Model):
    status_code = models.IntegerField()
    response = models.JSONField()
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
