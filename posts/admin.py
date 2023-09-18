from django.contrib import admin

# Register your models here.
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Post, SomeModelAdmin)
admin.site.register(Comment)