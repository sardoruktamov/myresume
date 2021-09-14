from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _


class Contact_me(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Ism familya'))

    def __str__(self):
        return self.name


class About(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_('Title')),
        description=models.TextField(verbose_name=_('Description')),
        address=models.CharField(max_length=250)
    )
    age = models.PositiveIntegerField(max_length=2)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.safe_translation_getter('title') or ''

    def get_absolute_url(self):
        return f'blog/{self.slug}'


class Skills(models.Model):
    name = models.CharField(max_length=200)
    perceive = models.PositiveIntegerField(max_length=3)

    def __str__(self):
        return self.name


class Portfolio(TranslatableModel):
    translation = TranslatedFields(
        title=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Title'))
    )
    image = models.ImageField(upload_to="portfolio")
    url = models.URLField()

    def __str__(self):
        return self.safe_translation_getter('title') or ''


class Experience(TranslatableModel):
    translations = TranslatedFields(
        description=models.TextField(verbose_name=_('Tavsif')),
    )
    techno = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    dagree = models.CharField(max_length=100)

    def __str__(self):
        return self.techno


class Education(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Nomi')),
        description=models.TextField(verbose_name=_('Tavsif')),
        dagree=models.CharField(max_length=100)
    )
    from_date = models.DateField()
    to_date = models.DateField()

class References(TranslatableModel):
    translations = TranslatedFields(
        full_name=models.CharField(max_length=255, verbose_name=_('Nomi')),
        description=models.TextField(verbose_name=_('Tavsif')),
        techno=models.CharField(max_length=100)
    )
    image = models.ImageField(upload_to="references")