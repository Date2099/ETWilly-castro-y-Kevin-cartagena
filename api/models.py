from django.db import models
from django.contrib.auth.models import User

class Suscripcion(models.Model):
    user_email = models.EmailField(max_length=100)
    status = models.BooleanField(default=False)

