from django.db import models


class MatchUser(models.Model):
	osuid = models.IntegerField()
	username = models.CharField(max_length=30)
	checked = models.BooleanField(default=False)
	point = models.FloatField(max_digits=10, decimal_places=7)


class Beatmap(models.Model):
	diffid = models.IntegerField()
	maxscore = models.IntegerField()


class Play(models.Model):
	player = models.ForeignKey(MatchUser)
	match = models.ForeignKey(Match)
	score = models.IntegerField()
	map = models.ForeignKey(Beatmap)


class Match(models.Model):
	mpid = models.IntegerField()
	date = models.IntegerField() #人工输入，1-3，统计时取相同号的前6个