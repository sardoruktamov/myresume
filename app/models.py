from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse


class Contact_me(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Ism familya'))
    techno = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='contactme', null=True)
    resume = models.FileField(upload_to='files',null=True)
    email = models.EmailField(null=True)
    telegram = models.URLField(null=True)
    instagram = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return self.full_name


class About(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_('Title')),
        description=models.TextField(verbose_name=_('Description')),
        address=models.CharField(max_length=250)
    )
    age = models.PositiveIntegerField(max_length=2)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    language = models.CharField(max_length=156, null=True)

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

    def url_text(self):
        parsed_url = urlparse(self.url)
        return parsed_url.hostname.replace("www.", "") + "/..."


class Experience(TranslatableModel):
    translations = TranslatedFields(
        description=models.TextField(verbose_name=_('Tavsif')),
        dagree=models.CharField(max_length=100, null=True)
    )
    techno = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()

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