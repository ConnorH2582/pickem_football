from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class League(models.Model):
    name = models.CharField(max_length=200,unique=True)
    buy_in = models.DecimalField(max_digits = 20, decimal_places = 8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    commissioner = models.ForeignKey(User)
    nfl_year = models.IntegerField()
    marquee = models.ImageField(blank=True, upload_to = 'game/static/league')
    slug = models.SlugField()

    def to_json(self):
        return {'name':self.name,'buy_in':self.buy_in, 'created_at':self.created_at, 'updated_at':self.updated_at, 'commissioner':self.commissioner.name, 'nfl_year':self.nfl_year,'slug':self.slug,'marquee':self.marquee.name}


class Team(models.Model):
    name = models.CharField(max_length=100,default=None,unique=True)
    mascot = models.ImageField(blank=True, upload_to = 'game/static/team')
    manager = models.ForeignKey(User)
    league = models.ForeignKey(League)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    champion = models.BooleanField(default=False)
    slug = models.SlugField()

    def get_season_record(self):
        return str(self.wins, '-', self.losses)

    def to_json(self):
        return {'name':self.name,'manager':self.manager.username,'mascot':self.mascot.name,
        'slug':self.slug,'wins':self.wins,'losses':self.losses,'league':self.league.name}


class TeamPick(models.Model):
    nfl_week = models.IntegerField()
    choice = models.CharField(max_length=70)
    correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    was_counted = models.BooleanField(default=False)
    team = models.ForeignKey(Team)

    def to_json(self):
        return {'nfl_week':self.nfl_week,'choice':self.choice,'correct':self.correct,'team':self.team.name,
        'created_at':self.created_at,'updated_at':self.updated_at}
