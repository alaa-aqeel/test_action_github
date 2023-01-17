import uuid
from django.db import models

# Create your models here.

class ListTopDO(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.text