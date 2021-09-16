from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    Contact_me, About,
    Skills, Portfolio,
    Experience, Education,
    References, Contact
)

admin.site.register(Contact_me)
admin.site.register(Skills)


# admin.site.register(Portfolio)
# Register your models here.
@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    list_display = ('title', 'description', 'address', 'email', 'phone', 'language',)


@admin.register(Portfolio)
class PortfolioAdmin(TranslatableAdmin):
    list_display = ('title',)


@admin.register(Experience)
class ExperienceAdmin(TranslatableAdmin):
    list_display = ('description', 'techno', 'from_date', 'to_date', 'dagree',)

@admin.register(Education)
class EducationAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'from_date', 'to_date', 'dagree',)

@admin.register(References)
class ReferencesAdmin(TranslatableAdmin):
    list_display = ('full_name', 'description', 'techno', 'image',)

admin.site.register(Contact)