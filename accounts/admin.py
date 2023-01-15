from django.contrib import admin
from django.contrib.auth.admin import UserAdmin





# Register your models here.
from .models import CustomUser, Etudiant, Formateur, Review, Formation, Salle, Centre
admin.site.register(CustomUser)
admin.site.register(Etudiant)
admin.site.register(Formateur)
admin.site.register(Review)
admin.site.register(Formation)
admin.site.register(Salle)
admin.site.register(Centre)