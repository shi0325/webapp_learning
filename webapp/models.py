from django.db import models

# Create your models here.
class Player(models.Model):
    # TODO: Define fields here
    pos = models.CharField('Position', blank=True, null=True, max_length=2)
    num = models.IntegerField('Back Number', blank=True, null=True)
    age = models.IntegerField('Age', blank=True, null=True)
    barth = models.CharField('Barth', blank=True, max_length=100)
    name = models.CharField('Name', blank=True, max_length=100)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Player Directory'

    def __unicode__(self):
        return(self.name)
