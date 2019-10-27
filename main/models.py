from django.contrib.gis.db import models
from django.utils.text import slugify


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    worldborder_slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.worldborder_slug = slugify(self.name)
        super(WorldBorder, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=20)

    # def __str__(self):
    #     return ', '.join([self.address, self.postal_code, self.city, self.country])


class Venue(models.Model):
    name = models.CharField(max_length=80, unique=True)

    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    lat = models.FloatField()
    lon = models.FloatField()

    area_polygon = models.MultiPolygonField(blank=True)

    def __str__(self):
        return self.name


class EventSeries(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    name: models.CharField(max_length=100, unique=True)
    start_date = models.DateField
    end_date = models.DateField

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(EventSeries, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Round(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    name: models.CharField(max_length=100, unique=True)
    series = models.ForeignKey(EventSeries, on_delete=models.CASCADE, related_name='rounds')


class Event(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    name = models.CharField(max_length=80)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    # just for testing what this looks like in forms
    date_time = models.DateTimeField()

    series = models.ForeignKey(EventSeries, on_delete=models.CASCADE, related_name='events')
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, related_name='events')
    round = models.ForeignKey(Round, on_delete=models.SET_NULL, null=True, related_name='events')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.venue.name + ": " + self.name


class Participant(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Participant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
