from django.db import models

# Create your models here.
class data(models.Model):
    username = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100 ,blank=False)
    password = models.CharField(max_length=100,blank=False)
    confirm_password = models.CharField(max_length=100,default=False,)
    
    def __str__(self):
        return self.email

    class Meta:
        db_table =''
        managed=True
        verbose_name = 'data'
        verbose_name_plural = 'datas'

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'
    
    class Meta:
        db_table =''
        managed=True
        verbose_name = 'ContactMessage'
        verbose_name_plural = 'ContactMessages'
 

