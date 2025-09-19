from django.conf import settings
from django.db import models
from django.utils import timezone


class Petition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='petitions')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def yes_count(self) -> int:
        return self.votes.count()


class PetitionVote(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='petition_votes')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('petition', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user} -> {self.petition}"
