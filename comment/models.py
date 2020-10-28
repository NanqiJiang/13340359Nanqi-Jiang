from django.db import models


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    comment = models.CharField(max_length=300)
    ctime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
