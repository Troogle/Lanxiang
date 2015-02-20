# coding=utf-8

from django.db import models


class Play(models.Model):
	player = models.ForeignKey('MatchUser')
	round = models.ForeignKey('Round', null=True)
	score = models.IntegerField()
	failed = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.round) + " " + str(self.player)

	@property
	def point(self):
		return float(self.score) / float(self.round.map.maxscore) \
			if not self.failed else float(self.score) / float(2 * self.round.map.maxscore)


class MatchUser(models.Model):
	osuid = models.IntegerField()
	username = models.CharField(max_length=30)
	checked = models.BooleanField(default=False)
	userType = models.IntegerField()

	def __unicode__(self):
		return self.username

	def getpoint(self, day):
		plays = Play.objects.filter(player=self,
									round__match__date__exact=day).order_by('round__match__time',
																			'round__order')
		point = 0.0
		uniquecheck=set([])
		for play in plays:
			if play.round.map.diffid in uniquecheck:
				continue
			uniquecheck.add(play.round.map.diffid)
			tpoint = float(play.score) / float(play.round.map.maxscore)
			if play.failed:
				tpoint /= 2
			point += tpoint
			if len(uniquecheck)==6:
				break
		return point

	@property
	def point1(self):
		return self.getpoint(1)

	@property
	def point2(self):
		return self.getpoint(2)

	@property
	def point3(self):
		return self.getpoint(3)

	@property
	def point(self):
		return self.point1 + self.point2 + self.point3


ModeChoice = (
	('None', 'None'),
	('HD', 'HD'),
	('HR', 'HR'),
	('DT', 'DT'),
	('Free Mod', 'Free Mod')
)


class Beatmap(models.Model):
	diffid = models.IntegerField()
	setid = models.IntegerField(default=0)
	maxscore = models.IntegerField()
	mapname = models.CharField(max_length=255, default='')
	diffname = models.CharField(max_length=255, default='')
	mode = models.CharField(choices=ModeChoice, max_length=10, default='None')
	date = models.IntegerField(default=0)

	def __unicode__(self):
		return '[Day:' + str(self.date) + ']' + self.mapname + '[' + self.diffname + ']'


class Match(models.Model):
	mpid = models.IntegerField()
	date = models.IntegerField()  # 人工输入，1-3，统计时取相同号的前6个
	time = models.IntegerField()  # 人工输入，1-4

	def __unicode__(self):
		return '[Day:' + str(self.date) + '/Time:' + str(self.time) + ']'

	class Meta:
		ordering = ['-date', '-time']


class Round(models.Model):
	match = models.ForeignKey('Match')
	map = models.ForeignKey('Beatmap')
	order = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.match) + '#' + str(self.order)

	class Meta:
		ordering = ['order']