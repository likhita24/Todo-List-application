from django.db import models


class users(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 1000)

class todoitems(models.Model):
    Task_name = models.CharField(max_length = 100)
    user_id = models.ForeignKey(users, on_delete = models.CASCADE)





# Create your models here.
