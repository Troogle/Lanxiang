# coding=utf-8

from django.db import models


class Play(models.Model):
	player = models.ForeignKey('MatchUser')
	round = models.ForeignKey('Round', null=True)
	score = models.IntegerField()
	failed = models.BooleanField(default=False)
	useful = models.BooleanField(default=False)
	team = models.IntegerField(default=0)

	def __unicode__(self):
		return str(self.round) + " " + str(self.player)

	def useit(self):
		self.useful = True
		self.save()

	@property
	def point(self):
		if self.team:
			return 1 if self.useful else 0
		return float(self.score) / float(self.round.map.maxscore) \
			if not self.failed else float(self.score) / float(2 * self.round.map.maxscore)

	class Meta:
		ordering = ['-score']


class MatchUser(models.Model):
	osuid = models.IntegerField()
	username = models.CharField(max_length=30)
	checked = models.BooleanField(default=False)
	userType = models.IntegerField()
	team = models.IntegerField(default=-1)

	def __unicode__(self):
		return self.username

	def calculatepoint(self, day):
		plays = Play.objects.filter(player=self,
									round__match__date__exact=day).order_by('round__match__time',
																			'round__order')
		plays.update(useful=False)
		uniquecheck = set([])
		for play in plays:
			if play.round.map.diffid in uniquecheck:
				continue
			uniquecheck.add(play.round.map.diffid)
			play.useit()
			if len(uniquecheck) == 6:
				break

	def getpoint(self, day):
		plays = Play.objects.filter(player=self,
									round__match__date__exact=day,
									useful=True)
		point = 0.0
		for play in plays:
			point += play.point
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

	@property
	def pointT(self):
		return self.getpoint('淘汰赛')

	@property
	def pointF(self):
		return self.getpoint('决赛')

	@property
	def pointFinal(self):
		plays = Play.objects.filter(player=self,useful=True)
		point = 0.0
		for play in plays:
			point += play.point
		return point


ModeChoice = (
('None', 'None'),
('HD', 'HD'),
('HR', 'HR'),
('DT', 'DT'),
('Free Mod', 'Free Mod'),
('Tie Breaker', 'Tie Breaker')
)


class Beatmap(models.Model):
	diffid = models.IntegerField()
	setid = models.IntegerField(default=0)
	maxscore = models.IntegerField()
	mapname = models.CharField(max_length=255, default='')
	diffname = models.CharField(max_length=255, default='')
	mode = models.CharField(choices=ModeChoice, max_length=10, default='None')
	date = models.CharField(max_length=20, default=0)

	def __unicode__(self):
		return '[Day:' + unicode(self.date) + ']' + self.mapname + '[' + self.diffname + ']'


class Match(models.Model):
	mpid = models.IntegerField()
	date = models.CharField(max_length=20)  # 人工输入，1-3，统计时取相同号的前6个
	time = models.IntegerField()  # 人工输入，1-4

	def __unicode__(self):
		return '[Day:' + unicode(self.date) + '/Time:' + str(self.time) + ']'

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