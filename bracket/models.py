from django.db import models

class Tournament(models.Model):
    winner = models.ForeignKey('Competitor')

class Match(models.Model):
    tournament = models.ForeignKey('Tournament')
    winner = models.ForeignKey('Competitor')
    leftMatch = models.ForeignKey('self')
    rightMatch = models.ForeignKey('self')
    nextMatch = models.ForeignKey('self')

    def __unicode__(self):
        return leftMatch.text + " VS " + rightMatch.text

class Competitor(models.Model):
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.text;
