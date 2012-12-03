from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField()
    join_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.email

