from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, email, nickname, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('User must have an email')

        now = timezone.localtime()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nickname=nickname,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create_user
    def create_user(self, email, password, **extra_fields):

        nickname = extra_fields.get('nickname', '사용자')

        return self._create_user(email, nickname, password, False, False, **extra_fields)

    # create_superuser
    def create_superuser(self, email, password, **extra_fields):

        nickname = extra_fields.get('nickname', '관리자')

        return self._create_user(email, nickname, password, True, True, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=255)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    profile_img = models.ImageField(
        upload_to='user/profile', null=True, blank=True)
    about_me = models.TextField(default='내 소개 : ', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_nickname(self):
        return self.user.nickname
