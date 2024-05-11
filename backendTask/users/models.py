from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    phone_no=models.CharField(max_length=13)
    otp=models.CharField(max_length=6)
    uid=models.UUIDField(default=uuid.uuid4)