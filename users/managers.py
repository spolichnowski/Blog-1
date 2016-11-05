from django.contrib.auth.base_user import BaseUserManager
from . import constants


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            msg = constsnts.USER_MUST_HAVE_A_VALID_EMAIL_ADRESS
            raise ValueError(msg)

        if not kwargs.get('first_name'):
            msg = constants.USER_MUST_HAVE_A_VALID_USER_NAME
            raise ValueError()

        if not kwargs.get('last_name'):
            msg = constants.USER_MUST_HAVE_A_VALID_LAST_NAME
            raise ValueError()

        if password is None:
            msg = constants.USER_MUST_HAVE_A_VALID_PASSWORD
            raise ValueError()

        user = self.model(
            email=self.normalize_email(email), **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
