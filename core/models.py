from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Skill(Base):
    habilidade = models.CharField('Habilidade', max_length=100)
    nivel = models.DecimalField('Nivel', max_digits=2, decimal_places=0)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.habilidade


class Profile(Base):
    ICONE_CHOICES = (
        ('flaticon-themeforest', 'themeforest'),
        ('flaticon-dribbble', 'dribbble'),
        ('flaticon-behance-logo', 'behance'),
        ('flaticon-github-logo', 'github'),
        ('flaticon-flickr-website-logo-silhouette', 'flickr'),
        ('flaticon-smug', 'smug'),
        ('flaticon-squarespace-logo', 'squarespace'),
        ('flaticon-bitbucket-logotype-camera-lens-in-perspective', 'bitbucket'),

    )
    descricao = models.CharField('Descrição', max_length=100)
    icone = models.CharField('Icone', max_length=55, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        return self.descricao


