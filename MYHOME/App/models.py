from django.db import models

# Create your models here.
class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=20)
    travel = models.CharField(max_length=20)
    ctime=models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=20)
    class Meta:

        db_table = 'travel'