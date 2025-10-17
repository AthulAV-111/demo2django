from django.db import models

# Create your models here.


class employee(models.Model):
    emp_id=models.IntegerField()
    Name=models.CharField(max_length=100)
    email=models.EmailField()
    phon_number=models.IntegerField()
    designation=models.CharField(max_length=100)
    salary=models.IntegerField()
    image=models.ImageField(upload_to="images")