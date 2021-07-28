from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    chat_id=models.IntegerField(unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    time_create=models.DateTimeField(auto_now_add=True)
    last_message= models.DateTimeField()

    def __str__(self):
        return f'{self.id} {self.last_name} {self.first_name}'
