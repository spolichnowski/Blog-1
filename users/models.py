from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=35)
    email = models.CharField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', )

    class Meta:
        app_label = 'users'
        ordering = ('-last_name', )
        verbose_name = 'użytkownik'
        verbose_name_plural = 'użytkownicy'

    def __str__(self):
        return '{} {}' .format(self.first_name, self.last_name)

    def return_message(self, data):
        return send_mail(
            data['subject'],
            data['message'],
            settings.EMAIL_HOST_USER,
            (self.email, ),
            fail_silently=True,
        )
