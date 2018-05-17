from django.db import models

class GuestBook(models.Model):
    username = models.CharField(max_length=32, null=None)
    content = models.CharField(max_length=255, null=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 根据日期倒叙排序
        ordering = ['-date']

