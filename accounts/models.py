from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email ,password = None):
        if not username:
            raise ValueError('Users Must Have Valid Username')
        if not email:
            raise ValueError('Users Must Have Valid Email Address')
        
        user = self.model(
            username    = username,
            email       = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username    = username,
            password    = password,
            email       = self.normalize_email(email),
        )
        
        user.is_active      = True
        user.is_staff       = True
        user.is_superuser   = True

        user.save(self._db)
        return user




class AccountUser(AbstractBaseUser):
    username        = models.CharField(max_length=30,unique=True)
    email           = models.EmailField(verbose_name='email',max_length=60 , unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login',auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email',]
    
    objects = MyAccountManager()

    def __str__(self):
        return f'{self.username}'
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    class Meta:
        verbose_name = 'Account User'
        verbose_name_plural = 'Blog Users'

