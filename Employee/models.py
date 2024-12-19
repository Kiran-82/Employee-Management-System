from django.db import models
import os
class Admin(models.Model):
    sno = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100, unique=True)
    Pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.userName

class Employee(models.Model):
    Image = models.ImageField(upload_to='employee_images/')
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Mobile = models.CharField(max_length=15)
    Designation = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    Course = models.CharField(max_length=100)
    Createdate = models.DateField(auto_now_add=True)
    def delete(self, *args, **kwargs):
        # Delete the image file when the employee is deleted
        if self.Image:
            try:
                os.remove(self.Image.path)
            except FileNotFoundError:
                pass  # Ignore if the file was not found (e.g., if it's already deleted)

        super().delete(*args, **kwargs)
    def __str__(self):
        return self.Name
