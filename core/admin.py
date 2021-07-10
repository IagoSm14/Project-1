from django.contrib import admin

from .models import Skill, Profile


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('habilidade',  'nivel', 'modificado')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'icone', 'modificado')
