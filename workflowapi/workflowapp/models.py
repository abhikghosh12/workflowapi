from django.db import models

# Create your models here.
class workflow(models.Model):
    name = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=60)
    #steps = models.CharField(max_length=60)
    steps = models.ManyToManyField('step', blank=True)

class comment(models.Model):
    name = models.CharField(blank=True, max_length=200)
    text = models.CharField(blank=True, max_length=60)

class step(models.Model):
    name = models.CharField(blank=True, max_length=50)
    description = models.CharField(blank=True, max_length=60)

    def __str__(self):
        return 'Step_name: {} Description {}'.format(self.name, self.description)
    #def __str__(self):
        #return '%s ' % (self.name)
