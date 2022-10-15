from django.db import models

# Create your models here.


class breakes(models.Model):
    user_n = models.CharField(max_length=25)
    user_p = models.CharField(max_length=30)

    def __str__(self):
        return self.user_n
    
