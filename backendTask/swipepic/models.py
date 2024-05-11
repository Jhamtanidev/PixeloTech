from django.db import models
from django.contrib.auth.models import User

class ImageHistory(models.Model):
    image_path = models.URLField()
    action = models.CharField(max_length=10, choices=[('accept', 'Accept'), ('reject', 'Reject')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.image_path} ({self.user.first_name})"