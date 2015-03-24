from django.contrib import admin
from polls.models import Question
from polls.models import Choice
# admin.site.register(Question)

class ChoiceInline(admin.TabularInline): #choices is on questions page
    model = Choice
    extra = 3 #provides enough fields for 3 choices

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questions',           {'fields':['question_text']}),
        ('Date information',    {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin) #optional argument
# Register your models here.
