from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    Contact_me, About,
    Skills, Portfolio,
    Experience, Education,
    References
)

admin.site.register(Contact_me)
# Register your models here.
@admin.register(About)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('title', 'description','address','email','phone',)