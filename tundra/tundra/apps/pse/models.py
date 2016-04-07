from __future__ import unicode_literals

from django.db import models

optional = {
    'null': True,
    'blank': True
}


class Sector(models.Model):
    name           = models.CharField(max_length=20, unique=True)
    created_at     = models.DateTimeField(auto_now_add=True, **optional)
    updated_at     = models.DateTimeField(auto_now=True, **optional)

    def __unicode__(self):
        return u'%s' % (self.name,)


class Index(models.Model):
    sector         = models.ForeignKey('pse.Sector')
    value          = models.DecimalField(max_digits=10, decimal_places=2)
    change         = models.CharField(max_length=10)
    percent_change = models.CharField(max_length=20)
    created_at     = models.DateTimeField(auto_now_add=True, **optional)

    class Meta:
        verbose_name_plural = 'indices'

    def __unicode__(self):
        return u'%s - %s' % (self.sector, self.value,)
