from django.contrib.auth.base_user import BaseUserManager

class AumUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, rfid, password, **extra_fields):
        # Creates and saves a User with the given attributes
        if not username:
            raise ValueError('A username must be set')
        if not email:
            raise ValueError('An email is required')
        if not rfid:
            raise ValueError('An RFID number is required')

        username = self.model.normalize_username(username)
        email    = self.normalize_email(email)
        user     = self.model(username=username, email=email, rfid=rfid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, rfid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, rfid, password, **extra_fields)

    def create_superuser(self, username, email, rfid, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, rfid, password, **extra_fields)
