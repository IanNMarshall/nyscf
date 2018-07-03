from django.contrib import admin

from .models import Df1

class Df1Admin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['filer_id']})
	]
	list_display = ('filer_id', 'filer_name', 'filer_type', 'status')

"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

"""

admin.site.register(Df1, Df1Admin)
# Register your models here.
