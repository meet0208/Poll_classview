from django.contrib import admin
from . import models

admin.site.site_header="Polls App"

# Register your models here.
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text","pub_date")
    list_filter = ("pub_date", )

    
@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin): 
    list_display = ("choice_text","question")
    search_fields = ("choice_text", )
    fields=("choice_text","votes")
# Register your models here.
