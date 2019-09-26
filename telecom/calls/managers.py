from django.db import models


class StartManager(models.Manager):
    def get_queryset(self):
        return super(StartManager, self).get_queryset().filter(type="start")


class EndManager(models.Manager):
    def get_queryset(self):
        return super(EndManager, self).get_queryset().filter(type="end")
