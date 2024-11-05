from django.db import models

# Create your models here.
class Fahim (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_added = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Mumina (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_added = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Nickson (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_added = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Ahlam (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_added = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Ashley (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_added = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Patel (models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    date_added = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"