from django.db import models
from datetime import datetime


class Directory(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=200)
    start_date = models.DateTimeField(default=datetime.now, blank=True, null=True)

    class Meta:
        unique_together = ('name', 'version',)

    def __str__(self):
        return self.name + ' ' + self.version


class DirectoryItem(models.Model):
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        if self.parent:
            return self.value + ' (' + self.parent.value + ')'
        return self.value
