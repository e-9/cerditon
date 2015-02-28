from django.db import models

# Create your models here.
class PigData(models.Model):
    Name = models.CharField('Nombre', max_length=100)
    Age = models.IntegerField('Edad', default=0)
    Height = models.IntegerField('Altura', default=0)
    def __str__(self):
        return self.Name

class PigStatus(models.Model):
    pig_data = models.ForeignKey(PigData)
    weight = models.FloatField('Peso', default=0.0)
    fat_percentage = models.FloatField('Porcentage de grasa', default=0.0)
    total_body_water = models.FloatField('Porcentage de liquidos', default=0.0)
    body_mass_index = models.FloatField('Porcentage de masa muscular', default=0.0)
    bone_percentage = models.FloatField('Porcentage de masa osea', default=0.0)
    muscle_percentage = models.FloatField('Porcentage de masa corporal', default=0.0)
    kilocalories = models.FloatField('Kilocalorias', default=0.0)
    ideal_weight = models.FloatField('Peso ideal', default=0.0)
    week = models.IntegerField('Semana', default=0)
    def __str__(self):
        return str(self.weight)

class MasterPig():
    name = ''
    age = 0
    height = 0.0
    weight = 0.0
    weight_diff = 0.0
    fat_percentage = 0.0
    fat_percentage_diff = 0.0
    total_body_water = 0.0
    total_body_water_diff = 0.0
    body_mass_index = 0.0
    body_mass_index_diff = 0.0
    bone_percentage = 0.0
    bone_percentage_diff = 0.0
    muscle_percentage = 0.0
    muscle_percentage_diff = 0.0
    kilocalories = 0.0
    kilocalories_diff = 0.0
    thumbs_up = 0
    thumbs_down = 0
    week = 0

    def __init__(self):
        self.data = []
