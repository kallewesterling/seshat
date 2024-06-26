from django.db import models


class Album(models.Model):
    """
    :private:
    :noindex:

    Note:
        TODO

        This model is used to store information about an album.

        It does not seem to belong to the codebase. Remove it?
    """
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)


class Track(models.Model):
    """
    :private:
    :noindex:

    Note:
        TODO

        This model is used to store information about tracks in an album.

        It does not seem to belong to the codebase. Remove it?
    """
    album = models.ForeignKey(
        Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        """
        :noindex:
        """
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
