from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    Contact_me, About,
    Skills, Portfolio,
    Experience, Education,
    References
)

admin.site.register(Contact_me)
admin.site.register(Skills)
# admin.site.register(Portfolio)
# Register your models here.
@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    list_display = ('title', 'description','address','email','phone', 'language',)

@admin.register(Portfolio)
class PortfolioAdmin(TranslatableAdmin):
    list_display = ('title',)