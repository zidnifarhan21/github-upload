from django.core.validators import MaxValueValidator
import os
import random
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

# Create your models here.


# ini buat random image name pas upload biar ga ribet
def get_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_path(instance, filename):
    new_filename = random.randint(1,25294281123)
    name, ext = get_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{final_filename}".format(final_filename=final_filename)


# ini custom model manager
# class ProductManager(models.Manager):
#     def featured(self):
#         return self.get_queryset().filter(featured=True)


class Product(models.Model):
    kategori = [
        ('NW', 'Network'),
        ('DB', 'Database'),
        ('PM', 'Programming'),
        ('ML', 'Machine Learning'),
    ]
        
    judul = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True, unique=True)
    pengarang = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    tahun = models.IntegerField(validators=[MaxValueValidator(9999)], blank=True, null=True)
    isbn = models.IntegerField(validators=[MaxValueValidator(9999999999999)], blank=True, null=True) #13 digit
    stok = models.IntegerField(validators=[MaxValueValidator(999999)])
    harga = models.IntegerField(validators=[MaxValueValidator(99999999)])
    kategori = models.CharField(max_length=2, choices=kategori ,default="Network")
    image = models.ImageField(upload_to=upload_path)
    active = models.BooleanField(default=True, null=True)
    featured = models.BooleanField(default=False, null=True)

    def get_absolute_url(self):
        return "product/{slug}/".format(slug=self.slug)
    

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)

    def __unicode__(self):
        return "{}. {}".format(self.id, self.judul)

def product_pre_save_receiver(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=Product)