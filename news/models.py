from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class NewsPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('news:artikel', kwargs={'post_id': self.id})
