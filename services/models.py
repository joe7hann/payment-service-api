from django.db import models
 

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    logo = models.URLField(max_length=5000)
    #logo = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'service'

#class user heritade



