import uuid
from datetime import datetime,timedelta
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class Project(models.Model):
    
    def now_plus_30():
        return datetime.now()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=8)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(default=now_plus_30)
    username = models.ForeignKey(
      settings.AUTH_USER_MODEL, 
      on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, name, password=None, **extra_fields):
        """
        Creates and saves a User with the given name, username
        and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username = username,
            name=name, **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_staffuser(self, username, name,password, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            name=name,
            password=password, **extra_fields,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    
    
    def create_superuser(self, username, name, password, **extra_fields):
        """
        Creates and saves a superuser with the given name, username
        and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')
        
        return self.create_user(username,name, password, **extra_fields)
        



USERNAME_REGEX = '^[a-zA-Z0-9.@+-]*$'


class CustomUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
                max_length=255, 
                validators=[
                    RegexValidator(
                        regex = USERNAME_REGEX,
                        message = 'Username must be Alpahnumeric or contain any of the following: ". @ + -" ',
                        code='invalid_username'
                    )],
                unique=True,
            )
    
    name   = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their username 
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):              
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True