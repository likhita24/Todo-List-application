from django.db import models


class users(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __str__(self):
        return self.username

class todoitems(models.Model):
    Task_name = models.CharField(max_length = 100)
    user_id = models.ForeignKey(users, on_delete = models.CASCADE)





# Create your models here.
