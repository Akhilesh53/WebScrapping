from django.db import models

# Create your models here.

class BsModel(models.Model):
    
    id = models.IntegerField(primary_key=True)
    DateLicensed = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Island = models.CharField(max_length=50)
    Contact = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Name

class SeleniumModel(models.Model):

    LegalName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    MailingAddress = models.CharField(max_length=50)
    OffsiteCultivationAddress = models.CharField(max_length=100)
    ManufactureAddress = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    License = models.CharField(max_length=50)
    LicenseEffective = models.CharField(max_length=50)
    OwnerLicense = models.CharField(max_length=50)
    Services = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.LegalName

class ScrapModel(models.Model):
    
    id = models.IntegerField(primary_key=True)
    link = models.TextField()
    filename = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.filename