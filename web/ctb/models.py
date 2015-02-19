# coding=utf-8
from django.db import models


class MatchUser(models.Model):
	osuid = models.IntegerField()
	username = models.CharField(max_length=30)
	checked = models.BooleanField(default=False)
	point = models.DecimalField(max_digits=10, decimal_places=7, default=0)
	userType = models.IntegerField()

	def __unicode__(self):
		return self.username


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


class Play(models.Model):
	player = models.ForeignKey(MatchUser)
	match = models.ForeignKey(Match)
	score = models.IntegerField()
	map = models.ForeignKey(Beatmap)
	order = models.IntegerField(default=0)

	def __unicode__(self):
		return '[' + str(self.match) + ']' + str(self.player)
