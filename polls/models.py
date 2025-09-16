from django.db import models
import datetime
from django.utils import timezone


# Poll Model
class Poll(models.Model):

    questions = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    expiry_date = models.DateTimeField('expiry date', null=True, blank=True)

    def __str__(self):
        return self.questions


# Choice Model.
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text