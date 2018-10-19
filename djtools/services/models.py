from django.db import models


class AbstractService(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services')
    active = models.BooleanField(default=True, db_index=True)
    featured = models.BooleanField(default=False, db_index=True)
    order = models.IntegerField(default=0, db_index=True)

    class Meta:
        abstract = True
        ordering = ('-featured', 'order')
        index_together = [
            ['featured', 'order'],
            ['active', 'featured', 'order'],
        ]

    def __str__(self):
        return self.title


class Service(AbstractService):
    pass
