from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('formateur', 'Formateur'), ('etudiant', 'Etudiant')])
    adress = models.CharField(max_length=150)
    numero = models.CharField(max_length=150)
    gender_choice = (
        ("male", "Male"),
        ("female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10) 
    objects = CustomUserManager()
    def __str__(self):
        return self.first_name + self.last_name
    




class Centre(models.Model):
    nom = models.CharField(max_length=150,unique=True,)
    adress = models.CharField(max_length=150)
    number = models.IntegerField()
    email = models.EmailField(max_length=70,blank=True,unique=True)


    def __str__(self):
        return self.nom
    
class Salle(models.Model):
    nom = models.CharField(max_length=30,blank=True,unique=True,primary_key=True)
    capacite = models.IntegerField()
    centre=models.ForeignKey(Centre, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nom )+str(self.centre)
    


class Formateur(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True)
    salaire = models.FloatField()
    formateur_number = models.IntegerField( primary_key=True) 
    bio = models.TextField()
    def __str__(self):
        return self.user.first_name +' ' +self.user.last_name



    
class Formation(models.Model):
    nom = models.CharField(max_length=150, primary_key=True)
    prix = models.FloatField()
    category = models.CharField(max_length=100)
    date_debut = models.DateField( default=datetime.now())
    date_fin = models.DateField( default=datetime.now())
    Formateur = models.ForeignKey(Formateur, on_delete=models.DO_NOTHING)
    salle=models.ManyToManyField(Salle)
    canceled = models.BooleanField(default=False)                 

    def __str__(self):
        return self.nom



    
class Etudiant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True)
    academic_year = models.DateField( default=datetime.now())
    formation = models.ManyToManyField(Formation)
    student_number = models.IntegerField( primary_key=True)   
    isvalidated = models.BooleanField(default=False)


    def __str__(self):
        return self.user.last_name
    
    

class Review(models.Model):
    body = models.CharField(max_length=100)
    reviewer=models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    isvalidated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

class Registration(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    date_registration = models.DateField()
    payment = models.DecimalField(max_digits=5, decimal_places=2)
    payment_proof = models.FileField(upload_to='payments/')
    validated = models.BooleanField(default=False)

    def __str__(self):
        return self.etudiant.user.last_name + ' - ' + self.formation.nom
