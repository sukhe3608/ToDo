from django.db import models 
from django.contrib.auth.models import User #import the usermodel for django authentication

class TODO(models.Model):
    srno = models.AutoField(primary_key=True , auto_created=True)
    title = models.CharField(max_length=25)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    
