from django.utils import timezone
from django.db import models

class BaseModel(models.Model):
    """Base model for all models in the system.

    Fields:
    1. CreatedAt: DateTimeField
    2. UpdatedAt: DateTimeField
    3. MetaStatus: CharField

    """

    CreatedAt = models.DateTimeField(auto_now_add=True, db_column="created_at")
    UpdatedAt = models.DateTimeField(auto_now=True, db_column="updated_at")
    MetaStatus = models.CharField(max_length=8 ,default="active", db_column="meta_status")

    class Meta:
        abstract = True
