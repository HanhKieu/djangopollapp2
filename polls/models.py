import datetime
from django.db import models
from django.utils import timezone
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()- datetime.timedelta(days = 1)

class Choice(models.Model):
    question = models.ForeignKey(Question) #says there is a relationship between choice and queotion
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text #defines what the class prints when print statement is called on it
# Create your models here.
