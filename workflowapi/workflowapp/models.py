from django.db import models

# Create your models here.
class workflow(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=60)
    steps = models.CharField(max_length=60)

class comment(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=60)

"""
API endpoint that allows users to be viewed or edited.



class Step(models.Model):
    name = models.CharField(unique=True, max_length=50)
    documents = models.ManyToManyField('Document', blank=True, related_name="documents")

    def __str__(self):
        return 'Group name: {} Doc {}  '.format(self.name, self.documents)



class Acknowledgement(models.Model):
    date = models.DateField(default=datetime.now)
    documents = models.ForeignKey('Document', blank=True, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', blank=True, on_delete=models.CASCADE)
    token = models.CharField(unique=True, null=True, max_length=50)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return 'Ack token: {} '.format(self.token)

"""  
