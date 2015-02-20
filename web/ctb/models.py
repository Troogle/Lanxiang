# coding=utf-8
from decimal import Decimal as D

from django.db import models


class Play(models.Model):
	player = models.ForeignKey('MatchUser')
	round = models.ForeignKey('Round',null=True)
	score = models.IntegerField()
	failed = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.round) + str(self.player)


class MatchUser(models.Model):
	osuid = models.IntegerField()
	username = models.CharField(max_length=30)
	checked = models.BooleanField(default=False)
	userType = models.IntegerField()

	def __unicode__(self):
		return self.username

	def getpoint(self, day):
		plays = Play.objects.filter(round__match__date__exact=day).order_by('round__match__time', 'round__order')[:6]
		point = D(0)
		for play in plays:
			tpoint = D(play.score / play.round.map.maxscore)
			if play.failed:
				tpoint /= 2
			point += tpoint
		return point

	@property
	def point(self):
		return self.getpoint(1) + self.getpoint(2) + self.getpoint(3)


ModeChoice = (
	('None', 'None'),
	('HD', 'HD'),
	('HR', 'HR'),
	('DT', 'DT'),
	('Free Mod', 'Free Mod')
)


class Beatmap(models.Model):
	diffid = models.IntegerField()
	maxscore = models.IntegerField()
	mapname = models.CharField(max_length=255, default='')
	diffname = models.CharField(max_length=255, default='')
	mode = models.CharField(choices=ModeChoice, max_length=10, default='None')
	date = models.IntegerField(default=0)

	def __unicode__(self):
		return '(' + str(self.date) + ')' + self.mapname + '[' + self.diffname + ']'


class Match(models.Model):
	mpid = models.IntegerField()
	date = models.IntegerField()  # 人工输入，1-3，统计时取相同号的前6个
	time = models.IntegerField()  # 人工输入，1-4

	def __unicode__(self):
		return '(' + str(self.date) + ')' + str(self.time)


class Round(models.Model):
	match = models.ForeignKey('Match')
	map = models.ForeignKey('Beatmap')
	order = models.IntegerField(default=0)

	def __unicode__(self):
		return '[' + str(self.match) + ']' + str(self.order)