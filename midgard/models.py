from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    date_du_vol = models.DateTimeField(auto_now=True)
    image = models.ImageField( upload_to='midgard/static/img')
    nome = models.CharField(max_length=50, blank=True, default='')
    case = models.CharField(max_length=100, blank=True, default='')
    statut = models.CharField(choices=statut_choices, default='Prévu', max_length=100)
    capteurs = models.CharField(choices=capteurs_choices, default='Optique', max_length=100)
    owner = models.ForeignKey('Profiles', related_name='vols', on_delete=models.CASCADE)
    # highlighted = models.TextField()
    class Meta:
        ordering = ('date_du_vol',)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have a valid email address.')
        
        account = self.model(
            email=self.normalize_email(email),
        )
        account.set_password(password)
        account.save(using=self._db)
        return account
    
    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_admin = True
        account.save(using=self._db)
        return account


class Profiles(AbstractBaseUser):
    # username = None
    username = models.CharField(max_length=50,unique=True,null=True)
    full_name = models.CharField(max_length=100, default='')
    email = models.EmailField(('email address'), unique=True)
    image = models.ImageField(upload_to='midgard/static/img/profiles')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return self.full_name
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    def get_short_name(self):
        return self.username
    @property
    def is_staff(self):
        return self.is_admin

class Messages(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, default='', blank=True)
    message_body = models.TextField(default='')
    owner = models.ForeignKey('Profiles', related_name='messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)