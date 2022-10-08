from django.db import models
from users.models import user
from post.models import post
import uuid


class comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    contents = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
