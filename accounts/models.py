from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('email', unique=True, blank=True)
    # Booleano. Determina se este usuário pode acessar o site admin.
    is_staff = models.BooleanField('staff status', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
