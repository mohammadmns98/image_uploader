from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None,**extra_fields):
        if not email:
            raise ValueError('Email Must be provided')

        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        # user = self.create_user(email=email, password=password)
        # user.is_admin = True
        # user.save(using=self._db)

        # return user

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
