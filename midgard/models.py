from django.db import models


statut_choices = [
    ('disponible', 'DISPONIBLE'),
    ('En cours de traitement', 'EN COURS DE TRAITMENT'),
    ('Prévu','PREVU'),
]
capteurs_choices = [
    ('Thermique', 'THERMIQUE'),
    ('Optique', 'OPTIQUE'),
    ('Météo','METEO'),
]
# Create your models here.
class Vols(models.Model):
    date_du_vol = models.DateTimeField(auto_now_add=True)
    vol = models.ImageField( upload_to='midgard/static/img', height_field=None, width_field=None, max_length=None)
    nome = models.CharField(max_length=50, blank=True, default='')
    case = models.CharField(max_length=100, blank=True, default='')
    statut = models.CharField(choices=statut_choices, default='Prévu', max_length=100)
    capteurs = models.CharField(choices=capteurs_choices, default='Optique', max_length=100)

    class Meta:
        ordering = ('date_du_vol',)
