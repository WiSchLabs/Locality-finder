from django.db import models
from django.template.defaultfilters import slugify

from main.models import EventSeries, Participant, Venue


class League(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    name = models.CharField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(League, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Season(EventSeries):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    is_current = models.BooleanField(default=False)


class Stadium(Venue):
    pass


class Team(Participant):
    address = models.OneToOneField(Stadium, on_delete=models.CASCADE)
