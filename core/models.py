from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class demo(models.Model):
    post=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.post




        '''
        https://hiring.selfdecode.com/interviews/f680f37e-d51e-4317-9cbd-b74f61f31f7a
        '''