from django.db import models
from django.contrib.auth.models import BaseUserManager, Group
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from access.models import Access

class CustomUserManager(BaseUserManager):

    def create_user(self,username, full_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            full_name = full_name,
        )

        user.set_password(password)
        #set password in built for password
        user.save(using=self._db)
        return user

    def create_superuser(self,username, full_name, email, password):

        user = self.create_user(
            email = self.normalize_email(email),
            #normalize email makes capital email small
            username = username,
            password = password,
            full_name = full_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(("Email Address"), max_length=254, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class OldHashes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,editable=False)
    pwd = models.CharField('Password hash',max_length=255,editable=False)
    date = models.DateTimeField('Date',auto_now_add=True,editable=False)
   
    def __str__(self) -> str:
        return self.user


    