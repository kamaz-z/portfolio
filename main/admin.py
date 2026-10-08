from django.contrib import admin
from .models import ProjectPhoto, Progets, Skills

admin.site.register(Skills)


class ProjectPhotoInline(admin.StackedInline):
    model = ProjectPhoto
    extra = 3


@admin.register(Progets)
class ProgetsAdmin(admin.ModelAdmin):
    inlines = [ProjectPhotoInline]