from django.db import models

# Create your models here.
class workflow(models.Model):
    name = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return 'workflow_name: {} '.format(self.name)

class comment(models.Model):
    name = models.CharField(blank=True, max_length=200)
    text = models.CharField(blank=True, max_length=200)

class step(models.Model):
    workflow = models.ForeignKey(workflow, on_delete=models.CASCADE, related_name='steps', null=True, blank=True)
    name = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return 'Step_name: {} Description {}'.format(self.name, self.description)
