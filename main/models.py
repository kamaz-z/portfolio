from django.db import models

class Skills(models.Model):
    skill = models.CharField(max_length=100)
    def __str__(self):
            return self.skill

    class Meta:
        verbose_name = 'Навички'

class Progets(models.Model):
    name = models.CharField(max_length=100)
    deskrp = models.CharField(max_length=300)
    skills = models.ManyToManyField(Skills)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проекти'