from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JsonData(models.Model):
    user_id=models.IntegerField()
    input_id=models.IntegerField()
    title=models.CharField(max_length=400)
    body=models.TextField(max_length=2000)
    modeluser=models.ForeignKey(User, on_delete=models.CASCADE,)

