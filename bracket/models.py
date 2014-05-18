from django.db import models

max_opp_len = 200

class Tournament(models.Model):
    
    def __unicode__(self):
        return str(self.id)

class Match(models.Model):

    # Opponent names and their votes
    opp1 = models.CharField(max_length=max_opp_len)
    opp2 = models.CharField(max_length=max_opp_len)
    opp1votes = models.IntegerField(default=0)
    opp2votes = models.IntegerField(default=0)

    # generation is similar to what an index of a heap would be
    #               [ gen = 0 ]
    #   [ gen = 1 ]             [ gen = 2 ]
    generation = models.IntegerField()
    winner = models.CharField(max_length=max_opp_len)
    tournament = models.ForeignKey('Tournament')

    def __unicode__(self):
        return self.opp1 + " VS " + self.opp2
