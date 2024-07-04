from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models

class CustomUser(AbstractBaseUser):
    """
    This model describes the base user of the system.

    Fields:
    1. UserID: PrimaryKey
    2. Email: EmailField
    3. UserName: CharField
    4. PhoneNumber: CharField
    5. Password: CharField
    6. IsAdmin: Bool
    7. CreatedAt: DateField
    8. UpdatedAt: DateField
    9. MetaStatus: CharField

    """
    
    UserID = models.AutoField(primary_key=True, db_column="user_id")
    Email = models.EmailField(unique=True,db_column="email")
    UserName = models.CharField(max_length=50, db_column="user_name")
    PhoneNumber = models.CharField(max_length=15, db_column="phone_number")
    password = models.CharField(max_length=128, db_column="password")
    IsAdmin = models.BooleanField(default=False, db_column="is_admin")
    CreatedAt = models.DateTimeField(auto_now_add=True, db_column="created_at")
    UpdatedAt = models.DateTimeField(auto_now=True, db_column="updated_at")
    MetaStatus = models.CharField(max_length=100, db_column='meta_status')
    
    objects = BaseUserManager()
    USERNAME_FIELD = "Email"
    REQUIRED_FIELDS = ["password"]

    class Meta:
        db_table = "custom_user"