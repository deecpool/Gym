from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CardAbout)
# admin.site.register(Trainer)
admin.site.register(Membership)
admin.site.register(Members)
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("last_name" , "first_name")}
    list_display = ['last_name','first_name','is_active','phone','email','classes_type']
    list_display_links = ['last_name','first_name','phone','email']
    ordering = ['last_name','first_name','is_active','phone','email']
    list_editable = ['is_active','classes_type']
    list_per_page = 10