from django.contrib import admin
from .models import workflow, comment, step

# Register your models here.
admin.site.register(workflow)
admin.site.register(comment)
admin.site.register(step)
