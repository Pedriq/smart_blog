from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Extended base user model.

    Added two fields:
    image(for avatar),
    is_verified_email (mark user verified via email)
    """
    
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
