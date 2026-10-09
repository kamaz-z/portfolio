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
    all_deskrp = models.TextField(max_length=900, blank=True)
    photo = models.ImageField(upload_to='projects/', blank=True)
    url = models.URLField(blank=True,null=True)
    skills = models.ManyToManyField(Skills)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проекти'


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Progets,on_delete=models.CASCADE,related_name='photos',)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or f'Фото для {self.project.name}'